// src/utils/api.js
// This module encapsulates all interactions with the Flask Backend API.
import { API_BASE_URL } from './constants.jsx';

// --- Document Handlers ---

export async function getDocuments() {
    try {
        const response = await fetch(`${API_BASE_URL}/documents`);
        if (!response.ok) throw new Error('Failed to fetch documents');
        return response.json();
    } catch (err) {
        console.warn("Documents endpoint unavailable, returning empty list.", err);
        return [];
    }
}

export async function uploadDocument(file) {
    const formData = new FormData();
    formData.append("file", file);
    const response = await fetch(`${API_BASE_URL}/ingest_document`, {
        method: 'POST',
        body: formData,
    });
    if (!response.ok) throw new Error('Failed to upload document');
    return response.json();
}

export async function deleteDocumentApi(docId) {
    // Backend does not yet expose deletion; return noop to keep UI consistent.
    console.warn(`Delete document ${docId} not supported on backend yet.`);
    return { ok: true };
}

// --- Conversation Handlers ---

export async function getConversations() {
    try {
        const response = await fetch(`${API_BASE_URL}/conversations`);
        if (!response.ok) throw new Error('Failed to fetch conversations');
        return response.json();
    } catch (err) {
        console.warn("Conversations endpoint unavailable, returning empty list.", err);
        return [];
    }
}

export async function startNewConversationApi(title) {
    const response = await fetch(`${API_BASE_URL}/conversations`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title }),
    });
    if (!response.ok) throw new Error('Failed to start new conversation');
    return response.json(); // Expected to return { conversationId, title, createdAt }
}

export async function deleteConversationApi(conversationId) {
    const response = await fetch(`${API_BASE_URL}/conversations/${conversationId}`, {
        method: 'DELETE',
    });
    if (!response.ok) throw new Error('Failed to delete conversation');
    return response.json();
}

// --- Message Handlers ---

export async function getMessages(conversationId) {
    // Fetches all messages for the active conversation.
    const response = await fetch(`${API_BASE_URL}/conversations/${conversationId}/messages`);
    if (!response.ok) throw new Error('Failed to fetch messages');
    return response.json();
}

export async function postUserMessage(conversationId, content) {
    // Sends and saves the user's message.
    const response = await fetch(`${API_BASE_URL}/conversations/${conversationId}/messages`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ role: 'user', content }),
    });
    if (!response.ok) throw new Error('Failed to post user message');
    return response.json(); // Expected to return the saved message object
}

// --- CORE AI/RAG QUERY HANDLER ---

export async function sendRAGQuery(conversationId, userQuery, documentNames) {
    const response = await fetch(`${API_BASE_URL}/ingest_user_query`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt: userQuery, top_k: 5 }),
    });

    if (!response.ok) {
        throw new Error(`AI Request Failed: ${response.status} ${response.statusText}`);
    }

    const data = await response.json();
    return data;
}
