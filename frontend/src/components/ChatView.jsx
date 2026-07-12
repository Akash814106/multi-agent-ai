import TaskCard from "./TaskCard";

function ChatView({

    loading,
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

            {

                loading && (

                    <div className="mt-8 bg-slate-800 rounded-xl p-6 border border-slate-700">

                        <h2 className="text-xl font-semibold mb-4">

                            Activity

                        </h2>

                        <ul className="space-y-3">

                            {

                                statusList.map((item, index) => (

                                    <li

                                        key={index}

                                        className="bg-slate-700 rounded-lg p-3"

                                    >

                                        {item}

                                    </li>

                                ))

                            }

                        </ul>

                    </div>

                )

            }

            {

                conversation.messages.length === 0 && !loading && (

                    <div className="mt-16 text-center text-gray-400">

                        <h2 className="text-3xl font-semibold">

                            Welcome to AgentFlow

                        </h2>

                        <p className="mt-3">

                            Research, build and learn using multiple AI agents.

                        </p>

                    </div>

                )

            }

            {

                conversation.messages.map((message) => {

                   const result = message.result.response;

                    const isDirectResponse =
                        result.goal === "Direct Response";

                    return (

                        <div

                            key={message.id}

                            className="mt-12"

                        >

                            <div className="bg-blue-600 rounded-xl p-5">

                                <h2 className="font-semibold mb-2">

                                    You

                                </h2>

                                <p>

                                    {message.query}

                                </p>

                            </div>

                            {

                                !isDirectResponse && (

                                    <div className="mt-8 bg-slate-800 rounded-xl p-6">

                                        <h2 className="text-2xl font-semibold mb-4">

                                            Goal

                                        </h2>

                                        <p className="whitespace-pre-wrap">

                                            {result.goal}

                                        </p>

                                    </div>

                                )

                            }

                            {

                                !isDirectResponse && (

                                    <div className="mt-10">

                                        <h2 className="text-3xl font-bold mb-6">

                                            Work Items

                                        </h2>

                                        {

                                            result.results.map(

                                                (task, index) => (

                                                    <TaskCard

                                                        key={index}

                                                        taskData={task}

                                                        index={index}

                                                    />

                                                )

                                            )

                                        }

                                    </div>

                                )

                            }

                            <div className="mt-10 bg-slate-800 rounded-xl p-6">

                                <h2 className="text-2xl font-semibold mb-4">

                                    Final Report

                                </h2>

                                <p className="whitespace-pre-wrap">

                                    {result.final_summary}

                                </p>

                            </div>

                            <div className="mt-10 bg-slate-800 rounded-xl p-6">

                                <h2 className="text-2xl font-semibold mb-6">

                                    Workflow Metrics

                                </h2>

                                <div className="grid grid-cols-2 gap-4">

                                    <div>

                                        Execution Time: {result.metrics.execution_time} sec

                                    </div>

                                    <div>

                                        Memory Used: {result.metrics.memory_used ? "Yes" : "No"}

                                    </div>

                                    <div>

                                        Work Items: {result.metrics.task_count}

                                    </div>

                                    <div>

                                        Revisions: {result.metrics.revision_executed}

                                    </div>

                                    <div>

                                        Revisions Skipped: {result.metrics.revision_skipped}

                                    </div>

                                    <div>

                                        Failed Tasks: {result.metrics.failed_tasks}

                                    </div>

                                </div>

                            </div>

                        </div>

                    );

                })

            }

        </>

    );

}

export default ChatView;