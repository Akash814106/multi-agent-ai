import { useEffect, useRef, useState } from "react";

import TaskCard from "./TaskCard";
import ThinkingBar from "./ThinkingBar";
import UserMessage from "./UserMessage";
import AgentMessage from "./AgentMessage";
import WorkflowStatus from "./WorkflowStatus";
import WorkflowMetrics from "./WorkflowMetrics";

function ChatView({
    loading,
    thinking,
    statusList,
    conversation,
}) {

    const bottomRef = useRef(null);

    const [expandedMessages, setExpandedMessages] = useState({});

    useEffect(() => {
        bottomRef.current?.scrollIntoView({
            behavior: "smooth",
            block: "end",
        });
    }, [conversation?.messages.length, thinking]);

    if (!conversation) {
        return (
            <div className="mt-12 text-center text-gray-400">

                <h2 className="text-3xl font-bold">
                    AgentFlow
                </h2>

                <p className="mt-3">
                    Start a new conversation to begin.
                </p>

            </div>
        );
    }

    return (
        <>

            {conversation.messages.length === 0 && (

                thinking ? (
                
                    <div className="mt-12">
                    
                        <ThinkingBar />
                
                    </div>
            
                ) : (
                
                    <div className="mt-16 text-center text-gray-400">
                    
                        <h2 className="text-3xl font-semibold">
                            Welcome to AgentFlow
                        </h2>
                
                        <p className="mt-3">
                            Research, build and learn using multiple AI agents.
                        </p>
                
                    </div>
            
                )
            
            )}

            {conversation.messages.map((message, index) => {

                const result = message.result.response;

                const isDirectResponse =
                    result.goal === "Direct Response";

                const isLastMessage =
                    index === conversation.messages.length - 1;

                const isExpanded = expandedMessages[message.id] || false;

                return (

                    <div
                        key={message.id}
                        className="mt-12"
                    >

                        <UserMessage
                            query={message.query}
                        />

                        {thinking && isLastMessage && (

                            <ThinkingBar />

                        )}

                        {!thinking && (

                            <>
                                {/* Final Answer First */}

                                <AgentMessage
                                    message={result.final_summary}
                                />

                                {/* Expand Button */}

                                
                                <button
                                    onClick={() =>
                                        setExpandedMessages((prev) => ({
                                            ...prev,
                                            [message.id]: !prev[message.id],
                                        }))
                                    }
                                    className="
                                        mt-8
                                        w-full
                                        bg-[#1B2435]
                                        border
                                        border-slate-700
                                        rounded-2xl
                                        px-6
                                        py-5
                                        hover:border-blue-500
                                        hover:bg-[#232D42]
                                        transition-all
                                        duration-300
                                        text-left
                                        group
                                    "
                                >
                                
                                    <div className="flex justify-between items-center">
                                
                                        <div>
                                
                                            <h3 className="text-lg font-semibold text-white">
                                
                                                ⚙ AI Execution Details
                                
                                            </h3>
                                
                                            <p className="text-sm text-slate-400 mt-1">
                                
                                                {isExpanded
                                                    ? "Hide the execution pipeline"
                                                    : "See how AgentFlow solved this problem"}

                                            </p>
                                                
                                        </div>
                                                
                                        <div
                                            className={`text-2xl text-slate-400 transition-transform duration-300 ${
                                                isExpanded ? "rotate-180" : ""
                                            }`}
                                        >
                                        
                                            ⌄
                                        
                                        </div>
                                        
                                    </div>
                                        
                                </button>

                                
                                {/* Hidden Execution */}
                                
                                {isExpanded && (
                                    <>

                                        {!isDirectResponse && (
                                        
                                            <div className="mt-8 bg-slate-800 rounded-xl p-6">
                                            
                                                <h2 className="text-2xl font-semibold mb-4">
                                                    Agent Goal
                                                </h2>
                                        
                                                <p className="whitespace-pre-wrap">
                                                    {result.goal}
                                                </p>
                                        
                                            </div>

                                        )}

                                        {!isDirectResponse && (
                                        
                                            <div className="mt-10">
                                            
                                                <h2 className="text-3xl font-bold mb-6">
                                                    Execution Plan
                                                </h2>
                                        
                                                {result.results.map((task, taskIndex) => (
                                                
                                                    <TaskCard
                                                        key={taskIndex}
                                                        taskData={task}
                                                        index={taskIndex}
                                                    />
                                                
                                                ))}

                                            </div>

                                        )}

                                        <div className="mt-10 grid grid-cols-1 lg:grid-cols-10 gap-6 items-stretch">
                                    
                                            <div className="lg:col-span-3 flex">
                                    
                                                <WorkflowStatus
                                                    isDirectResponse={isDirectResponse}
                                                    statusList={statusList}
                                                />

                                            </div>
                                    
                                            <div className="lg:col-span-7 flex">
                                    
                                                <WorkflowMetrics
                                                    metrics={result.metrics}
                                                />

                                            </div>
                                    
                                        </div>
                                    
                                    </>
                                )}
                            </>

                        )}

                    </div>

                );

            })}

            <div ref={bottomRef} />

        </>
    );

}

export default ChatView;