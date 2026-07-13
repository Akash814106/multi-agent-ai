export default function ThinkingBar() {

    return (

        <div className="mt-6 bg-[#1B2435] border border-slate-700 rounded-2xl px-6 py-5 shadow-lg">

            <div className="flex items-center gap-3">

                <div className="flex gap-2">

                    <span className="w-3 h-3 rounded-full bg-green-400 animate-pulse"></span>

                    <span
                        className="w-3 h-3 rounded-full bg-green-400 animate-pulse"
                        style={{ animationDelay: "0.2s" }}
                    ></span>

                    <span
                        className="w-3 h-3 rounded-full bg-green-400 animate-pulse"
                        style={{ animationDelay: "0.4s" }}
                    ></span>

                </div>

                <div>

                    <h3 className="text-lg font-semibold text-white">

                        AgentFlow is thinking...

                    </h3>

                    <p className="text-sm text-slate-400 mt-1">

                        Please wait while the agents collaborate.

                    </p>

                </div>

            </div>

        </div>

    );

}