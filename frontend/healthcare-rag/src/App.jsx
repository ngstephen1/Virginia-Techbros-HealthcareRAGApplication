import React, { useState, useEffect, useRef, useCallback } from "react"

// Import API Services
import { 
  getDocuments, getConversations, getMessages, 
  startNewConversationApi, deleteConversationApi, deleteDocumentApi,
  postUserMessage, sendRAGQuery, uploadDocument
} from './utils/api.js';

// Import Components and Constants
import Header from './components/Header.jsx';
import ChatInterface from './components/Chat/ChatInterface.jsx';
import DocumentManager from './components/Documents/DocumentManager.jsx';
import HistorySidebar from './components/History/HistorySidebar.jsx';
import TabNavigation from './components/Input/TabNavigation.jsx';
import QueryInput from './components/Input/QueryInput.jsx';
import { MAX_DOCUMENTS } from './utils/constants.jsx';

// --- Data Fetching Logic (Centralized) ---

// Custom hook to manage fetching and state for all primary data sources
const useDataFetcher = (activeConversationId) => {
    const [uploadedDocs, setUploadedDocs] = useState([]);
    const [conversations, setConversations] = useState([]);
    const [messages, setMessages] = useState([]);
    const [isLoading, setIsLoading] = useState(false);

    const fetchData = useCallback(async () => {
        setIsLoading(true);
        try {
            const [docs, convs] = await Promise.all([
                getDocuments(),
                getConversations(),
            ]);
            setUploadedDocs(docs || []);
            setConversations(convs || []);
            
            if (activeConversationId) {
                const msgs = await getMessages(activeConversationId);
                setMessages(msgs || []);
            } else {
                setMessages([]);
            }
        } catch (error) {
            console.error("Error fetching initial data:", error);
            // In a real app, show a notification to the user
        } finally {
            setIsLoading(false);
        }
    }, [activeConversationId]);

    useEffect(() => {
        fetchData();
        // Optional: Implement polling here for real-time updates if websockets aren't used
        // const interval = setInterval(fetchData, 5000); 
        // return () => clearInterval(interval);
    }, [fetchData]);

    return { uploadedDocs, conversations, messages, fetchData, setMessages, setConversations, setUploadedDocs, isLoading };
};


// --- Main App Component ---

export default function App() {
  // Frontend State Management (no more useFireproof hooks)
  const [isProcessing, setIsProcessing] = useState(false);
  const [activeConversationId, setActiveConversationId] = useState(null);
  const [activeTab, setActiveTab] = useState("chat");
  const [promptInput, setPromptInput] = useState("");
  const responseEndRef = useRef(null);
  
  // Custom hook for all backend data access
  const { uploadedDocs, conversations, messages, fetchData, setMessages } = useDataFetcher(activeConversationId);

  const startNewConversation = useCallback(async () => {
    try {
        const newConv = await startNewConversationApi("New Conversation");
        setActiveConversationId(newConv.conversationId);
        setActiveTab("chat");
        fetchData(); // Refresh conversation list
    } catch (error) {
        console.error("Failed to start new conversation:", error);
    }
  }, [fetchData]);

  // Handles initial conversation creation/loading
  useEffect(() => {
    // Only run once data has loaded and conversations array is populated
    if (conversations.length > 0 && !activeConversationId) {
      setActiveConversationId(conversations[0].conversationId);
    } else if (conversations.length === 0) {
      // If no conversations exist, create the first one immediately
      startNewConversation();
    }
  }, [conversations, activeConversationId, startNewConversation]);

  // Scrolls to bottom on new message
  useEffect(() => {
    responseEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);


  // --- Database/API Handlers ---
  const loadConversation = (conversationId) => {
    setActiveConversationId(conversationId);
    setActiveTab("chat");
  }

  const deleteConversation = async (conv) => {
    try {
        await deleteConversationApi(conv.conversationId);
        
        // Update local state and refetch data
        if (activeConversationId === conv.conversationId) {
            const remaining = conversations.filter(c => c.conversationId !== conv.conversationId);
            setActiveConversationId(remaining.length > 0 ? remaining[0].conversationId : null);
        }
        fetchData(); 
    } catch (error) {
        console.error("Failed to delete conversation:", error);
    }
  }

  const handleFileUpload = async (e) => {
    const files = Array.from(e.target.files);
    
    if (uploadedDocs.length + files.length > MAX_DOCUMENTS) {
      alert(`Maximum ${MAX_DOCUMENTS} documents allowed. You currently have ${uploadedDocs.length} documents.`);
      return;
    }

    setIsProcessing(true);
    try {
      for (const file of files) {
        await uploadDocument(file);
      }
      await fetchData();
    } catch (error) {
      console.error("Failed to upload document:", error);
    } finally {
      e.target.value = "";
      setActiveTab("chat");
      setIsProcessing(false);
    }
  }

  const deleteDocument = async (docId) => {
    try {
        await deleteDocumentApi(docId);
        fetchData(); // Refresh document list
    } catch (error) {
        console.error("Failed to delete document:", error);
    }
  }


  // --- CORE RAG HANDLER ---

  const handleSubmitQuery = async (e) => {
    e.preventDefault();
    
    if (!promptInput.trim() || isProcessing) return;
    
    if (!activeConversationId) {
      // Should not happen if useEffect works, but a safety measure
      await startNewConversation(); 
      setTimeout(() => handleSubmitQuery(e), 100); 
      return;
    }

    setIsProcessing(true);
    setActiveTab("chat");

    const userMessage = promptInput;
    setPromptInput(""); // Clear input immediately

    // 1. Post user message to backend and update local state
    const userMsg = await postUserMessage(activeConversationId, userMessage);
    // Optimistic UI update: append user message to local state
    setMessages(prev => [...prev, userMsg].sort((a, b) => a.timestamp - b.timestamp));


    try {
        // 2. Call the RAG endpoint on the Flask API
        const documentNames = uploadedDocs.map(doc => doc.name);
        const fullResponse = await sendRAGQuery(activeConversationId, userMessage, documentNames);
        
        // 3. The backend is responsible for saving the assistant message. 
        // We trigger a full data refresh to get the new assistant message(s) and title updates.
        fetchData(); 

        // 4. Update conversation title if it's the first message
        const conv = conversations.find(c => c.conversationId === activeConversationId);
        const isFirstMessage = messages.length === 0; // Check local state before the current message
        
        if (conv && conv.title === "New Conversation" && isFirstMessage) {
            // Note: Title update is now a separate API call in a real scenario
            // For simplicity here, we assume fetchData might handle the update if the backend does it.
            // A safer, explicit update call would be needed here for production quality.
            // Example: updateConversationTitleApi(activeConversationId, newTitle);
        }

    } catch (error) {
        console.error("Error processing RAG query:", error);
        // Fallback: Manually insert an error message into the local state
        const errorMsg = {
            _id: `error-${Date.now()}`,
            type: "message",
            role: "assistant",
            content: `Sorry, there was an error processing your request: ${error.message || 'Unknown error'}. Please check the Flask server is running and try again.`,
            conversationId: activeConversationId,
            timestamp: Date.now() + 1,
        };
        setMessages(prev => [...prev, errorMsg].sort((a, b) => a.timestamp - b.timestamp));
    } finally {
        setIsProcessing(false);
    }
  }

  // --- Render based on activeTab state ---
  let content = null;
  if (activeTab === "chat") {
    content = <ChatInterface messages={messages} uploadedDocs={uploadedDocs} responseEndRef={responseEndRef} />;
  } else if (activeTab === "documents") {
    content = (
      <DocumentManager 
        uploadedDocs={uploadedDocs} 
        handleFileUpload={handleFileUpload} 
        deleteDocument={deleteDocument} 
      />
    );
  } else if (activeTab === "conversations") {
    content = (
      <HistorySidebar 
        conversations={conversations} 
        activeConversationId={activeConversationId} 
        loadConversation={loadConversation}
        deleteConversation={deleteConversation}
      />
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-[#f5f7fa] to-[#e8eef5] font-sans flex flex-col" style={{ fontFamily: "'IBM Plex Sans', -apple-system, BlinkMacSystemFont, sans-serif" }}>
      
      {/* Header */}
      <Header uploadedCount={uploadedDocs.length} startNewConversation={startNewConversation} />

      {/* Main Content Area */}
      <div className="flex-1 max-w-6xl w-full mx-auto flex flex-col overflow-hidden">
        {/* Messages or Tab Content */}
        <div className="flex-1 overflow-y-auto px-6 py-6 custom-scrollbar">
          {content}
        </div>
      </div>

      {/* Bottom Input Area with Tabs and Query Input */}
      <div className="bg-white border-t border-[#e0e0e0] shadow-lg">
        <div className="max-w-6xl mx-auto">
          
          <TabNavigation 
            activeTab={activeTab} 
            setActiveTab={setActiveTab} 
            uploadedCount={uploadedDocs.length}
            conversationCount={conversations.length}
          />

          <QueryInput 
            promptDoc={{ prompt: promptInput }} // Pass the local state as a mock document structure
            mergePrompt={(update) => setPromptInput(update.prompt)} 
            isProcessing={isProcessing} 
            uploadedDocs={uploadedDocs} 
            handleSubmitQuery={handleSubmitQuery} 
          />
        </div>
      </div>
    </div>
  );
}
