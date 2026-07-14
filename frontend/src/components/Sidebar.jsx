import { useState } from "react";
import { Plus, Trash2} from "lucide-react";

function Sidebar({
    user,
    conversations,
    activeConversation,
    setActiveConversation,
    createConversation,
    renameConversation,
    deleteConversation,
}) {

    const [editingId, setEditingId] = useState(null);
    const [editedTitle, setEditedTitle] = useState("");

    return (
        <aside className="w-80 min-w-80 bg-[#0b1120] border-r border-slate-800 flex flex-col overflow-hidden">

            {/* Header */}

            <div className="p-7 border-b border-slate-800">

                <h1 className="text-4xl font-bold tracking-tight">
                    AgentFlow
                </h1>

                <p className="text-blue-400 mt-4 text-lg">
                    Welcome, {user} 👋
                </p>

                <p className="text-slate-400 text-sm">
                    AI Workspace
                </p>

            </div>

            {/* New Conversation */}

            <div className="p-5">

                <button
                    onClick={createConversation}
                    className="w-full flex items-center justify-center gap-3 bg-blue-600 hover:bg-blue-700 transition rounded-2xl py-4 text-lg font-medium shadow-lg"
                >

                    <Plus size={22} />

                    New Conversation

                </button>

            </div>

            {/* Conversation List */}

            <div className="flex-1 overflow-y-auto px-4 space-y-3">

                {conversations.map((conversation) => (

                    <div
                        key={conversation.id}
                        onClick={() => setActiveConversation(conversation.id)}
                        onDoubleClick={() => {
                            setEditingId(conversation.id);
                            setEditedTitle(conversation.title);
                        }}
                        className={`

                            rounded-2xl
                            cursor-pointer
                            transition-all
                            duration-200
                            p-5

                            ${
                                activeConversation === conversation.id
                                    ? "bg-[#1e293b] border border-blue-500 shadow-lg"
                                    : "hover:bg-[#151d2d] border border-transparent"
                            }

                        `}
                    >

                        {editingId === conversation.id ? (

                            <input
                                autoFocus
                                value={editedTitle}
                                onChange={(e) => setEditedTitle(e.target.value)}
                                onBlur={() => {
                                    renameConversation(
                                        conversation.id,
                                        editedTitle
                                    );
                                    setEditingId(null);
                                }}
                                onKeyDown={(e) => {
                                    if (e.key === "Enter") {
                                        renameConversation(
                                            conversation.id,
                                            editedTitle
                                        );
                                        setEditingId(null);
                                    }
                                }}
                                className="w-full bg-slate-700 rounded-lg px-3 py-2 outline-none"
                            />

                        ) : (

                            <>
                                <div className="flex items-start gap-3">

                                    <div className="flex-1 min-w-0">
                                                        
                                        <p
                                            className="font-semibold text-white truncate"
                                            title={conversation.title}
                                        >
                                            {conversation.title}
                                        </p>
                                                        
                                        <p className="text-sm text-slate-400 mt-2">
                                                        
                                            {conversation.messages.length} message
                                            {conversation.messages.length !== 1 && "s"}
                                                        
                                        </p>
                                                        
                                    </div>
                                                        
                                    <button
                                        onClick={(e) => {
                                            e.stopPropagation();
                                            deleteConversation(conversation.id);
                                        }}
                                        className="
                                            flex-shrink-0
                                            p-1
                                            rounded-md
                                            text-slate-500
                                            hover:text-red-400
                                            hover:bg-slate-700/50
                                            transition
                                        "
                                    >
                                        <Trash2 size={18} />
                                    </button>
                                    
                                </div>

                            </>

                        )}

                    </div>

                ))}

            </div>

        </aside>
    );
}

export default Sidebar;