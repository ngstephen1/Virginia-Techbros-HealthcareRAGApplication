// --- API Service Layer (Simulated Flask Backend) ---

const API_BASE_URL = 'http://localhost:5000/api';

async function mockFetch(url, options = {}) {
    const path = url.replace(API_BASE_URL, '');
    let mockData = [];

    // Simulate different GET requests
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

    // Simulate POST and DELETE operations
    if (options.method === 'POST') {
        const data = JSON.parse(options.body);
        if (path === '/query') {
            const docNames = data.documents.length > 0 ? data.documents.join(', ') : 'no documents';
            return { response: `I have synthesized the answer to your query: "${data.query}" using the IBM Granite model, grounded by the context from ${docNames}.` };
        }
        // General POST returns the object with a new ID
        return { ...data, id: `new-${Date.now()}` };
    }
    if (options.method === 'DELETE') {
        return {};
    }

    // Sorting logic remains
    if (path.startsWith('/conversations')) {
        mockData.sort((a, b) => b.createdAt - a.createdAt);
    } else if (path.includes('/messages')) {
        mockData.sort((a, b) => a.timestamp - b.timestamp);
    }

    return mockData;
}

export const api = {
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