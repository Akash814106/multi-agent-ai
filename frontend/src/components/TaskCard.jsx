import { useState } from "react";

function TaskCard({ taskData, index }) {

    const [expanded, setExpanded] = useState(false);

    return (

        <div className="mt-6 bg-slate-800 rounded-xl border border-slate-700">

            <button
                onClick={() => setExpanded(!expanded)}
                className="w-full flex justify-between items-center p-5 text-left hover:bg-slate-700 rounded-xl transition"
            >

                <div>

                    <h3 className="text-xl font-semibold">
                        📋 Task {index + 1}
                    </h3>

                    <p className="text-gray-400 mt-1">
                        {taskData.task}
                    </p>

                </div>

                <div className="flex items-center gap-4">

                    <span
                        className={
                            taskData.status === "SUCCESS"
                                ? "bg-green-600 px-3 py-1 rounded-full text-sm"
                                : "bg-red-600 px-3 py-1 rounded-full text-sm"
                        }
                    >
                        {taskData.status}
                    </span>

                    <span className="text-2xl">
                        {expanded ? "▲" : "▼"}
                    </span>

                </div>

            </button>

            {

                expanded && (

                    <div className="p-6 border-t border-slate-700 space-y-8">

                        <div>

                            <h4 className="text-lg font-semibold text-blue-400 mb-3">
                                🔍 Research
                            </h4>

                            <p className="whitespace-pre-wrap text-gray-300">
                                {taskData.research}
                            </p>

                        </div>

                        <div>

                            <h4 className="text-lg font-semibold text-yellow-400 mb-3">
                                🧠 Critic
                            </h4>

                            <div className="mb-3">

                                <span className="bg-yellow-600 px-3 py-1 rounded-full">

                                    Score : {taskData.best_score}/10

                                </span>

                            </div>

                            <p className="whitespace-pre-wrap text-gray-300">

                                {taskData.critic?.feedback}

                            </p>

                        </div>

                        <div>

                            <h4 className="text-lg font-semibold text-green-400 mb-3">
                                🔄 Revision
                            </h4>

                            <p className="whitespace-pre-wrap text-gray-300">

                                {taskData.revision}

                            </p>

                        </div>

                        <div>

                            <h4 className="text-lg font-semibold text-purple-400 mb-3">
                                📝 Summary
                            </h4>

                            <p className="whitespace-pre-wrap text-gray-300">

                                {taskData.summary}

                            </p>

                        </div>

                        <div className="grid grid-cols-2 gap-4">

                            <div>

                                🔄 Revisions Executed :
                                {" "}
                                {taskData.revision_executed}

                            </div>

                            <div>

                                ⏭️ Revisions Skipped :
                                {" "}
                                {taskData.revision_skipped}

                            </div>

                        </div>

                    </div>

                )

            }

        </div>

    );

}

export default TaskCard;