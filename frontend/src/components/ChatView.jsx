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

            {conversation.messages.length === 0 && !loading && (

                <div className="mt-16 text-center text-gray-400">

                    <h2 className="text-3xl font-semibold">
                        Welcome to AgentFlow
                    </h2>

                    <p className="mt-3">
                        Research, build and learn using multiple AI agents.
                    </p>

                </div>

            )}

            {conversation.messages.map((message, index) => {

                const result = message.result.response;

                const isDirectResponse =
                    result.goal === "Direct Response";

                const isLastMessage =
                    index === conversation.messages.length - 1;

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

                                {!isDirectResponse && (

                                    <div className="mt-8 bg-slate-800 rounded-xl p-6">

                                        <h2 className="text-2xl font-semibold mb-4">

                                            Goal

                                        </h2>

                                        <p className="whitespace-pre-wrap">

                                            {result.goal}

                                        </p>

                                    </div>

                                )}

                                {!isDirectResponse && (

                                    <div className="mt-10">

                                        <h2 className="text-3xl font-bold mb-6">

                                            Work Items

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

                                <AgentMessage
                                    message={result.final_summary}
                                />

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

                    </div>

                );

            })}

        </>
    );

}

export default ChatView;