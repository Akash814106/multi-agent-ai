import { useState } from "react";

function Section({ title, color, children }) {
    return (
        <div className="space-y-2">
            <h4 className={`font-semibold ${color}`}>
                {title}
            </h4>

            <div className="bg-slate-900 rounded-lg border border-slate-700 p-4 text-slate-300 whitespace-pre-wrap leading-7">
                {children}
            </div>
        </div>
    );
}

export default function TaskCard({ taskData, index }) {

    const [expanded, setExpanded] = useState(false);

    return (

        <div className="bg-[#273247] rounded-2xl border border-slate-700 overflow-hidden transition-all">

            <button
                onClick={() => setExpanded(!expanded)}
                className="w-full px-6 py-5 flex justify-between items-start hover:bg-[#313d55] transition"
            >

                <div className="text-left flex-1">

                    <h3 className="text-2xl font-semibold text-white">

                        📋 Task {index + 1}

                    </h3>

                    <p className="text-slate-400 mt-2 leading-7">

                        {taskData.task}

                    </p>

                </div>

                <div className="flex items-center gap-4 ml-6">

                    <span
                        className={`px-4 py-1 rounded-full text-sm font-semibold ${
                            taskData.status === "SUCCESS"
                                ? "bg-green-600 text-white"
                                : "bg-red-600 text-white"
                        }`}
                    >
                        {taskData.status}
                    </span>

                    <span className="text-2xl text-white">

                        {expanded ? "▴" : "▾"}

                    </span>

                </div>

            </button>

            {

                expanded && (

                    <div className="border-t border-slate-700 bg-[#202a3b] p-6 space-y-8">

                        <Section
                            title="Research Output"
                            color="text-blue-400"
                        >
                            {taskData.research}
                        </Section>

                        <Section
                            title="Critic Feedback"
                            color="text-yellow-400"
                        >

                            <div className="mb-4">

                                <span className="bg-yellow-600 text-white px-3 py-1 rounded-full text-sm">

                                    Score : {taskData.best_score}/10

                                </span>

                            </div>

                            {taskData.critic?.feedback}

                        </Section>

                        <Section
                            title="Revision Output"
                            color="text-green-400"
                        >
                            {taskData.revision}
                        </Section>

                        <Section
                            title="Summary"
                            color="text-purple-400"
                        >
                            {taskData.summary}
                        </Section>

                        <div className="grid grid-cols-2 gap-4">

                            <div className="bg-slate-900 border border-slate-700 rounded-xl p-4">

                                <div className="text-slate-400">

                                    Revisions Executed

                                </div>

                                <div className="text-3xl font-bold text-white mt-2">

                                    {taskData.revision_executed}

                                </div>

                            </div>

                            <div className="bg-slate-900 border border-slate-700 rounded-xl p-4">

                                <div className="text-slate-400">

                                    Revisions Skipped

                                </div>

                                <div className="text-3xl font-bold text-white mt-2">

                                    {taskData.revision_skipped}

                                </div>

                            </div>

                        </div>

                    </div>

                )

            }

        </div>

    );

}