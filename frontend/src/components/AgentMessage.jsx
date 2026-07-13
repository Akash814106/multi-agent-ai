export default function AgentMessage({ message }) {

    const time = new Date().toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit",
    });

    return (

        <div className="mt-6 bg-[#222B3D] border border-slate-700 rounded-2xl p-6 shadow-lg">

            <div className="flex justify-between items-start">

                <div className="flex gap-4">

                    <div className="w-12 h-12 rounded-full bg-slate-700 flex items-center justify-center text-xl">

                        🤖

                    </div>

                    <div>

                        <h3 className="text-xl font-semibold text-violet-300">

                            Agent

                        </h3>

                        <p className="text-sm text-slate-400">

                            AI Assistant

                        </p>

                    </div>

                </div>

                <span className="text-sm text-slate-400">

                    {time}

                </span>

            </div>

            <div className="mt-6 text-gray-100 whitespace-pre-wrap leading-8">

                {message}

            </div>

        </div>

    );

}