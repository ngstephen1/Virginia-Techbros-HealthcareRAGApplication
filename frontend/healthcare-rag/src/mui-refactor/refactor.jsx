import React, { useState, useEffect, useRef, useCallback } from "react";
import { 
  createTheme, 
  ThemeProvider, 
  CssBaseline,
  Box, 
  AppBar, 
  Toolbar, 
  Typography, 
  Button, 
  Container, 
  TextField, 
  Paper, 
  List, 
  ListItem, 
  ListItemText, 
  IconButton,
  Tabs,
  Tab,
  CircularProgress,
  Divider,
} from '@mui/material';
import DeleteIcon from '@mui/icons-material/Delete';
import FilePresentIcon from '@mui/icons-material/FilePresent';
import ChatBubbleOutlineIcon from '@mui/icons-material/ChatBubbleOutline';
import HistoryIcon from '@mui/icons-material/History';
import SendIcon from '@mui/icons-material/Send';
import AddIcon from '@mui/icons-material/Add';
import ChatIcon from '@mui/icons-material/Chat';

// --- I. Constants and Theme Setup ---

const MAX_DOCUMENTS = 10;
const ACCENT_COLOR = "#0f62fe"; // IBM Blue
const TEXT_COLOR = "#242424"; 
const GRAY_TEXT = "#525252";

// Define the custom MUI theme to use the IBM blue accent color
const theme = createTheme({
  palette: {
    primary: {
      main: ACCENT_COLOR,
    },
    secondary: {
      main: GRAY_TEXT,
    },
    background: {
      default: "#f5f7fa",
      paper: "#ffffff",
    },
    text: {
      primary: TEXT_COLOR,
      secondary: GRAY_TEXT,
    },
  },
  typography: {
    fontFamily: "'IBM Plex Sans', sans-serif",
  },
  components: {
    MuiButton: {
      defaultProps: {
        disableElevation: true,
      },
      styleOverrides: {
        root: {
          borderRadius: 8,
          textTransform: 'none',
        },
      },
    },
    MuiPaper: {
      styleOverrides: {
        root: {
          borderRadius: 12,
        },
      },
    },
  },
});

// --- II. API Service Layer (Simulated Flask Backend) ---
// This section simulates interaction with the Flask API (Tia/Stephen/Raf/Alex roles)

const API_BASE_URL = 'http://localhost:5000/api';

async function mockFetch(url, options = {}) {
    // Basic mock data generation. In a real app, this would be a direct fetch.
    const path = url.replace(API_BASE_URL, '');
    let mockData = [];

    if (path.startsWith('/documents')) {
        mockData = [
            { id: 'doc-1', name: 'Microbiome Study 2024.pdf', uploadedAt: Date.now() - 86400000 },
            { id: 'doc-2', name: 'Oncology_Review.txt', uploadedAt: Date.now() - 3600000 },
        ];
    } else if (path.startsWith('/conversations')) {
        mockData = [
            { conversationId: 'conv-1', title: 'RNA Synthesis Pathway Analysis', createdAt: Date.now() - 100000 },
            { conversationId: 'conv-2', title: 'Neuroplasticity mechanisms...', createdAt: Date.now() - 50000 },
        ];
    } else if (path.includes('/messages')) {
        const convId = path.split('/')[2];
        mockData = [
            { id: 'msg-1', conversationId: convId, role: 'user', content: 'What are the main findings on RNA synthesis?', timestamp: Date.now() - 40000 },
            { id: 'msg-2', conversationId: convId, role: 'assistant', content: 'The primary findings indicate a reliance on a novel complex [Document 1: Microbiome Study 2024.pdf].', timestamp: Date.now() - 30000 },
        ];
    }

    if (options.method === 'POST') {
        const data = JSON.parse(options.body);
        if (path === '/query') {
            const docNames = data.documents.length > 0 ? data.documents.join(', ') : 'no documents';
            return { response: `I have synthesized the answer to your query: "${data.query}" using the IBM Granite model, grounded by the context from ${docNames}.` };
        }
        return { ...data, id: `new-${Date.now()}` };
    }
    if (options.method === 'DELETE') {
        return {};
    }

    // Sort messages and conversations by timestamp/date for display order
    if (path.startsWith('/conversations')) {
        mockData.sort((a, b) => b.createdAt - a.createdAt);
    } else if (path.includes('/messages')) {
        mockData.sort((a, b) => a.timestamp - b.timestamp);
    }

    return mockData;
}

const api = {
    getDocuments: async () => mockFetch(`${API_BASE_URL}/documents`),
    uploadDocument: async (fileData) => mockFetch(`${API_BASE_URL}/documents`, { method: 'POST', body: JSON.stringify(fileData) }),
    deleteDocumentApi: async (docId) => mockFetch(`${API_BASE_URL}/documents/${docId}`, { method: 'DELETE' }),
    getConversations: async () => mockFetch(`${API_BASE_URL}/conversations`),
    startNewConversationApi: async (title) => mockFetch(`${API_BASE_URL}/conversations`, { method: 'POST', body: JSON.stringify({ title, conversationId: `conv-${Date.now()}` }) }),
    deleteConversationApi: async (conversationId) => mockFetch(`${API_BASE_URL}/conversations/${conversationId}`, { method: 'DELETE' }),
    getMessages: async (conversationId) => mockFetch(`${API_BASE_URL}/conversations/${conversationId}/messages`),
    postUserMessage: async (conversationId, content) => mockFetch(`${API_BASE_URL}/conversations/${conversationId}/messages`, { method: 'POST', body: JSON.stringify({ role: 'user', content, timestamp: Date.now() }) }),
    sendRAGQuery: async (conversationId, userQuery, documentNames) => {
        const response = await mockFetch(`${API_BASE_URL}/query`, {
            method: 'POST',
            body: JSON.stringify({ conversationId, query: userQuery, documents: documentNames }),
        });
        // Simulate saving the assistant response on the backend side
        const assistantResponse = { 
            id: `msg-${Date.now() + 1}`, 
            conversationId, 
            role: 'assistant', 
            content: response.response, 
            timestamp: Date.now() + 1 
        };
        return assistantResponse;
    },
};


// --- III. Custom Hooks and Data Fetcher ---

const useDataFetcher = (activeConversationId) => {
    const [uploadedDocs, setUploadedDocs] = useState([]);
    const [conversations, setConversations] = useState([]);
    const [messages, setMessages] = useState([]);
    const [isLoading, setIsLoading] = useState(false);

    const fetchData = useCallback(async () => {
        setIsLoading(true);
        try {
            const [docs, convs] = await Promise.all([
                api.getDocuments(),
                api.getConversations(),
            ]);
            setUploadedDocs(docs || []);
            setConversations(convs || []);
            
            if (activeConversationId) {
                const msgs = await api.getMessages(activeConversationId);
                setMessages(msgs || []);
            } else {
                setMessages([]);
            }
        } catch (error) {
            console.error("Error fetching initial data:", error);
        } finally {
            setIsLoading(false);
        }
    }, [activeConversationId]);

    useEffect(() => {
        fetchData();
        // NOTE: In a real environment, polling or WebSockets would replace this manual interval/fetchData() calls.
    }, [fetchData]);

    return { uploadedDocs, conversations, messages, fetchData, isLoading };
};


// --- IV. Refactored MUI Components ---

// Component 1: Header
const Header = React.memo(({ uploadedCount, startNewConversation }) => (
  <AppBar position="static" color="default" sx={{ bgcolor: 'white', borderBottom: 1, borderColor: 'grey.300', boxShadow: 'none' }}>
    <Container maxWidth="md">
      <Toolbar disableGutters sx={{ justifyContent: 'space-between' }}>
        <Box>
          <Typography variant="h5" component="div" color="primary.main" fontWeight={600}>
            ResearchBot
          </Typography>
          <Typography variant="caption" color="text.secondary">
            AI Literature Analysis Assistant
          </Typography>
        </Box>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
          <Typography variant="body2" color="text.secondary">
            <Typography component="span" fontWeight={600}>{uploadedCount}</Typography>/{MAX_DOCUMENTS} documents
          </Typography>
          <Button
            variant="contained"
            color="primary"
            onClick={startNewConversation}
            startIcon={<AddIcon />}
            sx={{ px: 2, py: 1, textTransform: 'none' }}
          >
            New Chat
          </Button>
        </Box>
      </Toolbar>
    </Container>
  </AppBar>
));

// Component 2: Message Bubbles (Chat)
const MessageBubble = React.memo(({ msg }) => {
  const isUser = msg.role === "user";
  const time = new Date(msg.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  
  return (
    <Box sx={{ display: 'flex', justifyContent: isUser ? 'flex-end' : 'flex-start' }}>
      <Paper
        elevation={1}
        sx={{
          maxWidth: '80%',
          minWidth: '200px',
          p: 2,
          borderRadius: '16px',
          borderTopRightRadius: isUser ? 0 : '16px',
          borderTopLeftRadius: isUser ? '16px' : 0,
          bgcolor: isUser ? 'primary.main' : 'background.paper',
          color: isUser ? 'white' : 'text.primary',
          boxShadow: isUser ? '0 3px 6px rgba(0, 0, 0, 0.2)' : '0 1px 3px rgba(0, 0, 0, 0.1)',
        }}
      >
        <Typography variant="caption" sx={{ opacity: 0.8, fontWeight: 'medium', mb: 0.5, display: 'block' }}>
          {isUser ? "You" : "ResearchBot"}
        </Typography>
        <Typography variant="body1" sx={{ whiteSpace: 'pre-wrap', lineHeight: 1.5 }}>
          {msg.content}
        </Typography>
        <Typography variant="caption" sx={{ display: 'block', mt: 1, opacity: 0.7 }}>
          {time}
        </Typography>
      </Paper>
    </Box>
  );
});

// Component 3: Chat Interface (Messages + Welcome Screen)
const ChatInterface = React.memo(({ messages, uploadedDocs, responseEndRef, isProcessing }) => {
  if (messages.length === 0 && !isProcessing) {
    return (
      <Box sx={{ textAlign: 'center', py: 8 }}>
        <Box sx={{ display: 'inline-flex', alignItems: 'center', justifyContent: 'center', width: 64, height: 64, borderRadius: '50%', bgcolor: 'primary.main', opacity: 0.1, mb: 2 }}>
          <ChatIcon color="primary" sx={{ fontSize: 36, opacity: 1 }} />
        </Box>
        <Typography variant="h6" component="h3" fontWeight={500} sx={{ mb: 1 }}>
          Ready to help with your research
        </Typography>
        <Typography color="text.secondary" sx={{ maxWidth: 400, mx: 'auto' }}>
          {uploadedDocs.length === 0 
            ? "Ask me anything! Upload documents for citation-backed analysis, or ask general research questions."
            : "Ask questions about your uploaded documents to receive synthesized answers with accurate citations."}
        </Typography>
      </Box>
    );
  }

  return (
    <Box sx={{ maxWidth: 'md', mx: 'auto', display: 'flex', flexDirection: 'column', gap: 2 }}>
      {messages.map((msg) => (
        <MessageBubble key={msg.id || msg.timestamp} msg={msg} />
      ))}
      {isProcessing && (
        <Box sx={{ display: 'flex', justifyContent: 'flex-start' }}>
            <CircularProgress size={20} sx={{ ml: 2, mt: 1 }} />
        </Box>
      )}
      <div ref={responseEndRef} />
    </Box>
  );
});

// Component 4: Document Item
const DocumentItem = React.memo(({ doc, deleteDocument }) => (
  <Paper elevation={1} sx={{ p: 2, display: 'flex', alignItems: 'center', justifyContent: 'space-between', mb: 1 }}>
    <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
      <FilePresentIcon color="primary" sx={{ fontSize: 30 }} />
      <Box>
        <Typography fontWeight={500} noWrap sx={{ maxWidth: 300 }}>{doc.name}</Typography>
        <Typography variant="body2" color="text.secondary">
          {new Date(doc.uploadedAt).toLocaleDateString()}
        </Typography>
      </Box>
    </Box>
    <IconButton onClick={() => deleteDocument(doc.id)} color="error" aria-label="delete document">
      <DeleteIcon />
    </IconButton>
  </Paper>
));

// Component 5: Document Manager (Upload + List)
const DocumentManager = React.memo(({ uploadedDocs, handleFileUpload, deleteDocument }) => (
  <Container maxWidth="sm" sx={{ pt: 2, pb: 4 }}>
    <Paper elevation={2} sx={{ p: 3, mb: 4 }}>
      <Typography variant="h6" fontWeight={600} gutterBottom>Upload Documents</Typography>
      <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
        Upload research papers, articles, or literature. Maximum {MAX_DOCUMENTS} documents. Documents enable citation-backed RAG analysis.
      </Typography>
      <Button
        variant="contained"
        component="label"
        startIcon={<AddIcon />}
        disabled={uploadedDocs.length >= MAX_DOCUMENTS}
        sx={{ width: '100%', py: 1.5, textTransform: 'none' }}
      >
        {uploadedDocs.length >= MAX_DOCUMENTS ? "Maximum documents reached" : "Choose Files"}
        <input type="file" multiple accept=".txt,.pdf" onChange={handleFileUpload} hidden />
      </Button>
    </Paper>

    <Box>
      <Typography variant="subtitle1" fontWeight={600} sx={{ mb: 2 }}>
          Uploaded Files ({uploadedDocs.length})
      </Typography>
      {uploadedDocs.length === 0 && (
        <Typography color="text.secondary" textAlign="center" sx={{ py: 4 }}>
          No documents uploaded yet.
        </Typography>
      )}
      <List disablePadding>
        {uploadedDocs.map(doc => (
          <DocumentItem key={doc.id} doc={doc} deleteDocument={deleteDocument} />
        ))}
      </List>
    </Box>
  </Container>
));

// Component 6: History Item
const HistoryItem = React.memo(({ conv, activeConversationId, loadConversation, deleteConversation }) => (
  <Paper 
    elevation={1} 
    onClick={() => loadConversation(conv.conversationId)}
    sx={{ 
      p: 2, 
      mb: 1, 
      cursor: 'pointer', 
      border: activeConversationId === conv.conversationId ? `2px solid ${ACCENT_COLOR}` : '1px solid transparent',
      transition: 'all 0.2s',
      '&:hover': {
          boxShadow: 3,
      }
    }}
  >
    <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
      <Box sx={{ flexGrow: 1, minWidth: 0 }}>
        <Typography fontWeight={500} noWrap>{conv.title}</Typography>
        <Typography variant="caption" color="text.secondary">
          {new Date(conv.createdAt).toLocaleDateString()} • {new Date(conv.createdAt).toLocaleTimeString()}
        </Typography>
      </Box>
      <IconButton 
        onClick={(e) => {
          e.stopPropagation();
          deleteConversation(conv);
        }} 
        color="error" 
        aria-label="delete conversation"
      >
        <DeleteIcon fontSize="small" />
      </IconButton>
    </Box>
  </Paper>
));

// Component 7: History Sidebar
const HistorySidebar = React.memo(({ conversations, activeConversationId, loadConversation, deleteConversation }) => (
  <Container maxWidth="sm" sx={{ pt: 2, pb: 4 }}>
    <Typography variant="h6" fontWeight={600} gutterBottom>
        Conversation History ({conversations.length})
    </Typography>
    <Divider sx={{ mb: 2 }}/>
    <List disablePadding>
      {conversations.length === 0 ? (
        <Typography color="text.secondary" textAlign="center" sx={{ py: 4 }}>
          No conversations yet.
        </Typography>
      ) : (
        conversations.map(conv => (
          <HistoryItem 
            key={conv.conversationId}
            conv={conv}
            activeConversationId={activeConversationId}
            loadConversation={loadConversation}
            deleteConversation={deleteConversation}
          />
        ))
      )}
    </List>
  </Container>
));


// Component 8: Tab Navigation
const TabNavigation = React.memo(({ activeTab, setActiveTab, uploadedCount, conversationCount }) => {
  const tabs = [
    { id: "chat", label: "Chat", icon: <ChatBubbleOutlineIcon />, count: null },
    { id: "documents", label: `Documents (${uploadedCount})`, icon: <FilePresentIcon />, count: uploadedCount },
    { id: "conversations", label: `History (${conversationCount})`, icon: <HistoryIcon />, count: conversationCount },
  ];

  const handleChange = (event, newValue) => {
    setActiveTab(newValue);
  };

  return (
    <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
      <Tabs 
        value={activeTab} 
        onChange={handleChange} 
        centered
        variant="fullWidth"
      >
        {tabs.map(tab => (
          <Tab 
            key={tab.id} 
            value={tab.id} 
            label={tab.label} 
            icon={tab.icon} 
            iconPosition="start"
            sx={{ textTransform: 'none', fontWeight: 600 }}
          />
        ))}
      </Tabs>
    </Box>
  );
});

// Component 9: Query Input Form
const QueryInput = React.memo(({ promptDoc, mergePrompt, isProcessing, uploadedDocs, handleSubmitQuery }) => {
  const placeholderText = uploadedDocs.length > 0 
    ? "Ask a question about your research documents..." 
    : "Ask me anything about research or general topics...";
    
  return (
    <Box component="form" onSubmit={handleSubmitQuery} sx={{ p: 2, maxWidth: 'md', mx: 'auto' }}>
      <Box sx={{ display: 'flex', gap: 2, alignItems: 'center' }}>
        <TextField
          fullWidth
          multiline
          minRows={2}
          maxRows={4}
          value={promptDoc.prompt}
          onChange={(e) => mergePrompt({ prompt: e.target.value })}
          placeholder={placeholderText}
          variant="outlined"
          disabled={isProcessing}
          onKeyDown={(e) => {
            if (e.key === "Enter" && !e.shiftKey) {
              e.preventDefault();
              handleSubmitQuery(e);
            }
          }}
          sx={{
            bgcolor: '#f4f4f4',
            borderRadius: 2,
            '& fieldset': { border: 'none' }, // Remove default border
            '& .MuiOutlinedInput-root': { padding: '8px 14px' }
          }}
        />
        <Button
          type="submit"
          variant="contained"
          color="primary"
          disabled={isProcessing || !promptDoc.prompt.trim()}
          startIcon={isProcessing ? <CircularProgress color="inherit" size={20} /> : <SendIcon />}
          sx={{ height: 56, width: 120, textTransform: 'none', fontWeight: 600, py: 1 }}
        >
          {isProcessing ? "Thinking" : "Send"}
        </Button>
      </Box>
      {uploadedDocs.length === 0 && (
        <Typography variant="caption" color="text.secondary" sx={{ mt: 1, display: 'block', fontStyle: 'italic' }}>
          💡 Upload documents for citation-backed analysis, or ask general questions now.
        </Typography>
      )}
    </Box>
  );
});


// --- V. Main App Component ---

export default function App() {
  const [isProcessing, setIsProcessing] = useState(false);
  const [activeConversationId, setActiveConversationId] = useState(null);
  const [activeTab, setActiveTab] = useState("chat");
  const [promptInput, setPromptInput] = useState("");
  const responseEndRef = useRef(null);
  
  const { uploadedDocs, conversations, messages, fetchData } = useDataFetcher(activeConversationId);

  // Handles initial conversation creation/loading
  useEffect(() => {
    if (conversations.length > 0 && !activeConversationId) {
      setActiveConversationId(conversations[0].conversationId);
    } else if (conversations.length === 0 && !activeConversationId) {
        // Only start a new conversation if there are none and we haven't tried to load one
      startNewConversation();
    }
  }, [conversations, activeConversationId]);

  // Scrolls to bottom on new message
  useEffect(() => {
    responseEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);


  // --- Database/API Handlers ---

  const startNewConversation = async () => {
    try {
        const newConv = await api.startNewConversationApi("New Conversation");
        setActiveConversationId(newConv.conversationId);
        setActiveTab("chat");
        fetchData();
    } catch (error) {
        console.error("Failed to start new conversation:", error);
    }
  }

  const loadConversation = (conversationId) => {
    setActiveConversationId(conversationId);
    setActiveTab("chat");
  }

  const deleteConversation = async (conv) => {
    try {
        await api.deleteConversationApi(conv.conversationId);
        
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
    // Note: FileReader and async state updates are challenging. 
    // We process sequentially to ensure all files are handled before refetching.
    for (const file of files) {
      const reader = new FileReader();
      reader.onload = async (event) => {
        if (event.target.result.length > 0) {
           await api.uploadDocument({
            name: file.name,
            content: event.target.result, 
            uploadedAt: Date.now()
          });
        }
      };
      reader.readAsText(file);
    }
    
    // Allow a slight delay for all asynchronous uploads to finish before fetching fresh data
    setTimeout(fetchData, 1000); 
    e.target.value = "";
    setActiveTab("documents"); // Stay on documents to see upload confirmation
    setIsProcessing(false);
  }

  const deleteDocument = async (docId) => {
    try {
        await api.deleteDocumentApi(docId);
        fetchData(); 
    } catch (error) {
        console.error("Failed to delete document:", error);
    }
  }

  const handleSubmitQuery = async (e) => {
    e.preventDefault();
    
    if (!promptInput.trim() || isProcessing) return;
    
    if (!activeConversationId) {
      await startNewConversation(); 
      setTimeout(() => handleSubmitQuery(e), 100); 
      return;
    }

    setIsProcessing(true);
    setActiveTab("chat");

    const userMessage = promptInput;
    setPromptInput("");

    // 1. Post user message (optimistic update via API call)
    const userMsg = await api.postUserMessage(activeConversationId, userMessage);
    // Add temporary message locally for faster UI
    const tempMsg = { ...userMsg, id: userMsg.id || `temp-${Date.now()}` };
    setMessages(prev => [...prev, tempMsg].sort((a, b) => a.timestamp - b.timestamp));
    
    // Simulate assistant thinking message immediately after user posts
    const thinkingMsg = { id: `thinking-${Date.now()}`, role: 'assistant', content: 'Processing query with IBM Granite RAG agent...', timestamp: Date.now() + 1 };
    setMessages(prev => [...prev, thinkingMsg].sort((a, b) => a.timestamp - b.timestamp));


    try {
        // 2. Call the RAG endpoint on the Flask API (backend heavy lifting)
        const documentNames = uploadedDocs.map(doc => doc.name);
        await api.sendRAGQuery(activeConversationId, userMessage, documentNames);
        
        // 3. Refetch ALL data to get the final, saved assistant message and updated convo title
        await fetchData(); 

    } catch (error) {
        console.error("Error processing RAG query:", error);
        // Fallback: Manually insert an error message
        const errorMsg = {
            id: `error-${Date.now()}`,
            role: "assistant",
            content: `Sorry, there was an error processing your request: ${error.message || 'Unknown error'}. Please check the Flask server is running and try again.`,
            conversationId: activeConversationId,
            timestamp: Date.now() + 100000, 
        };
        setMessages(prev => {
            // Remove thinking message and add the error message
            const filtered = prev.filter(m => m.id !== thinkingMsg.id);
            return [...filtered, errorMsg].sort((a, b) => a.timestamp - b.timestamp);
        });
    } finally {
        setIsProcessing(false);
        // Remove the "thinking" message when done, if it wasn't removed by a successful fetch
        setMessages(prev => prev.filter(m => m.id !== thinkingMsg.id));
    }
  }


  // --- Render based on activeTab state ---
  let content = null;
  if (activeTab === "chat") {
    content = <ChatInterface messages={messages} uploadedDocs={uploadedDocs} responseEndRef={responseEndRef} isProcessing={isProcessing} />;
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
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Box sx={{ minHeight: '100vh', display: 'flex', flexDirection: 'column', bgcolor: 'background.default' }}>
        
        {/* Header */}
        <Header uploadedCount={uploadedDocs.length} startNewConversation={startNewConversation} />

        {/* Main Content Area */}
        <Container maxWidth="md" sx={{ flexGrow: 1, display: 'flex', flexDirection: 'column', overflow: 'hidden' }}>
          <Box sx={{ flexGrow: 1, overflowY: 'auto', py: 3 }} className="custom-scrollbar">
            {content}
          </Box>
        </Container>

        {/* Bottom Input Area with Tabs and Query Input */}
        <Paper elevation={8} sx={{ borderTop: 1, borderColor: 'grey.200', position: 'sticky', bottom: 0, zIndex: 10 }}>
          <Container maxWidth="md">
            
            <TabNavigation 
              activeTab={activeTab} 
              setActiveTab={setActiveTab} 
              uploadedCount={uploadedDocs.length}
              conversationCount={conversations.length}
            />

            <QueryInput 
              promptDoc={{ prompt: promptInput }}
              mergePrompt={(update) => setPromptInput(update.prompt)} 
              isProcessing={isProcessing} 
              uploadedDocs={uploadedDocs} 
              handleSubmitQuery={handleSubmitQuery} 
            />
          </Container>
        </Paper>
      </Box>
    </ThemeProvider>
  );
}
