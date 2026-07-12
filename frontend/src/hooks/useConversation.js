import { useState, useEffect } from "react";
import axios from "axios";

export default function useConversation(user) {

    const conversationKey = user
        ? `conversations_${user}`
        : "conversations";

    const activeConversationKey = user
        ? `activeConversation_${user}`
        : "activeConversation";

    const [conversations, setConversations] = useState(() => {

        const saved = localStorage.getItem(conversationKey);

        if (saved) {

            return JSON.parse(saved);

        }

        return [
            {
                id: 1,
                title: "New Conversation",
                messages: [],
            },
        ];

    });

    const [activeConversation, setActiveConversation] = useState(() => {

        const saved = localStorage.getItem(activeConversationKey);

        return saved ? Number(saved) : 1;

    });

    const [query, setQuery] = useState("");

    const [loading, setLoading] = useState(false);

    const [statusList, setStatusList] = useState([]);

    useEffect(() => {

        localStorage.setItem(
            conversationKey,
            JSON.stringify(conversations)
        );

        localStorage.setItem(
            activeConversationKey,
            activeConversation
        );

    }, [conversations, activeConversation]);



    useEffect(() => {
        
        const savedConversations = localStorage.getItem(conversationKey);
        
        if (savedConversations) {
        
            setConversations(
                JSON.parse(savedConversations)
            );
        
        } else {
        
            setConversations([
                {
                    id: 1,
                    title: "New Conversation",
                    messages: [],
                },
            ]);
        
        }
    
        const savedActive = localStorage.getItem(
            activeConversationKey
        );
    
        setActiveConversation(
            savedActive ? Number(savedActive) : 1
        );
    
    }, [conversationKey, activeConversationKey]);

    

    function createConversation() {

        const newConversation = {

            id: Date.now(),

            title: "New Conversation",

            messages: [],

        };

        setConversations((prev) => [

            ...prev,

            newConversation,

        ]);

        setActiveConversation(newConversation.id);

        setQuery("");

    }

    function renameConversation(id, newTitle) {

        if (!newTitle.trim()) return;

        setConversations((prev) =>

            prev.map((conversation) =>

                conversation.id === id

                    ? {

                        ...conversation,

                        title: newTitle,

                    }

                    : conversation

            )

        );

    }

    function deleteConversation(id) {

        const updatedConversations = conversations.filter(
            (conversation) => conversation.id !== id
        );

        setConversations(updatedConversations);

        if (activeConversation === id) {

            if (updatedConversations.length > 0) {

                setActiveConversation(updatedConversations[0].id);

            } else {

                const newConversation = {
                    id: Date.now(),
                    title: "New Conversation",
                    messages: [],
                };

                setConversations([newConversation]);
                setActiveConversation(newConversation.id);

            }

        }

    }

    async function sendQuery() {

        if (!query.trim()) return;

        setLoading(true);

        setStatusList([
            "Query Received",
            "Sending to Backend..."
        ]);

        try {

            const token = localStorage.getItem("token");

            const response = await axios.post(
            
                "http://127.0.0.1:8000/chat",
            
                {
                
                    query,
                
                },
            
                {
                
                    headers: {
                    
                        Authorization: `Bearer ${token}`,
                    
                    },
                
                }
            
            );

            const newMessage = {

                id: Date.now(),

                query,

                result: response.data,

            };

            setConversations((prev) =>

                prev.map((conversation) =>

                    conversation.id === activeConversation

                        ? {

                            ...conversation,

                            title:

                                conversation.messages.length === 0

                                    ? query

                                    : conversation.title,

                            messages: [

                                ...conversation.messages,

                                newMessage,

                            ],

                        }

                        : conversation

                )

            );

            setQuery("");

            setStatusList([]);

        }

        catch (error) {

            console.error(error);

            setStatusList([

                "Backend Error"

            ]);

        }

        finally {

            setLoading(false);

        }

    }

    const currentConversation = conversations.find(

        (conversation) =>

            conversation.id === activeConversation

    );

    return {

        conversations,

        activeConversation,

        currentConversation,

        loading,

        statusList,

        query,

        setQuery,

        setActiveConversation,

        createConversation,

        sendQuery,

        renameConversation,

         deleteConversation,

    };

}