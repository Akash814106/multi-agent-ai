import { useState } from "react";

function Sidebar({

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

        <aside className="w-72 bg-slate-950 border-r border-slate-800 flex flex-col">

            <div className="p-6 border-b border-slate-800">

                <h2 className="text-2xl font-bold">

                    AgentFlow

                </h2>

                <p className="text-sm text-gray-400 mt-1">

                    AI Workspace

                </p>

            </div>

            <div className="p-4">

                <button

                    onClick={createConversation}

                    className="w-full bg-blue-600 hover:bg-blue-700 rounded-xl py-3 transition"

                >

                    New Conversation

                </button>

            </div>

            <div className="flex-1 overflow-y-auto px-3 pb-3">

                {

                    conversations.map((conversation) => (

                        <div

                            key={conversation.id}

                            className={`

                                rounded-xl
                                mb-3
                                transition
                                p-4
                                cursor-pointer

                                ${

                                    activeConversation === conversation.id

                                        ? "bg-slate-800 border border-blue-500"

                                        : "hover:bg-slate-900"

                                }

                            `}

                            onClick={() =>

                                setActiveConversation(conversation.id)

                            }

                            onDoubleClick={() => {

                                setEditingId(conversation.id);

                                setEditedTitle(conversation.title);

                            }}

                        >

                            {

                                editingId === conversation.id ? (

                                    <input

                                        autoFocus

                                        value={editedTitle}

                                        onChange={(e) =>

                                            setEditedTitle(e.target.value)

                                        }

                                        onBlur={() => {

                                            renameConversation(

                                                conversation.id,

                                                editedTitle

                                            );

                                            setEditingId(null);

                                        }}

                                        onKeyDown={(e) => {

                                            if (e.key === "Enter") {
                                            
                                                e.preventDefault();
                                            
                                                renameConversation(
                                                
                                                    conversation.id,
                                                
                                                    editedTitle
                                                
                                                );
                                            
                                                setEditingId(null);
                                            
                                            }
                                        
                                        }}


                                        className="w-full bg-slate-700 rounded-lg p-2 outline-none"

                                    />

                                ) : (

                                   <>
                                        <div className="flex justify-between items-center">
                                                                    
                                            <p className="truncate font-medium">
                                                {conversation.title}
                                            </p>
                                                                    
                                            <button
                                                onClick={(e) => {
                                                    e.stopPropagation();
                                                    deleteConversation(conversation.id);
                                                }}
                                                className="text-red-400 hover:text-red-600 text-lg"
                                            >
                                                🗑️
                                            </button>
                                            
                                        </div>
                                            
                                        <p className="text-xs text-gray-400 mt-1">
                                            {conversation.messages.length} message(s)
                                        </p>
                                    </>

                                )

                            }

                        </div>

                    ))

                }

            </div>

        </aside>

    );

}

export default Sidebar;