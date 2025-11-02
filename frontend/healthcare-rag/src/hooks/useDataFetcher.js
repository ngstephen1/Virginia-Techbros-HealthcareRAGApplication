import { useState, useEffect, useCallback } from "react";
import { api } from "../services/apiService";

export const useDataFetcher = (activeConversationId) => {
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
        // NOTE: Polling/WebSockets would replace this manual interval/fetchData() calls in a real app.
    }, [fetchData]);

    return { uploadedDocs, conversations, messages, fetchData, isLoading };
};