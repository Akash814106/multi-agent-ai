export default function UserMessage({ query }) {
    return (
        <div className="mt-8">

            <div className="bg-gradient-to-r from-blue-600 to-blue-500 rounded-2xl p-5 shadow-lg">

                <div className="flex justify-between items-center mb-3">

                    <div className="flex items-center gap-3">

                        <div className="w-10 h-10 rounded-full bg-blue-700 flex items-center justify-center text-white font-bold">
                            A
                        </div>

                        <div>

                            <h3 className="font-semibold text-white">
                                You
                            </h3>

                            <p className="text-xs text-blue-100">
                                User
                            </p>

                        </div>

                    </div>

                    <span className="text-sm text-blue-100">
                        {new Date().toLocaleTimeString([], {
                            hour: "2-digit",
                            minute: "2-digit",
                        })}
                    </span>

                </div>

                <p className="text-white text-lg leading-7">
                    {query}
                </p>

            </div>

        </div>
    );
}