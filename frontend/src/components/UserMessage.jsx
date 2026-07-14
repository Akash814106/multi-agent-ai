export default function UserMessage({ query }) {

    const username =
        localStorage.getItem("username") || "A";

    return (

        <div className="mt-8">

            <div className="bg-gradient-to-r from-blue-600 to-blue-500 rounded-2xl px-5 py-3 shadow-lg">

                <div className="flex items-center justify-between">

                    <div className="flex items-center gap-3 flex-1 min-w-0">

                        <div className="w-10 h-10 rounded-full bg-blue-700 flex items-center justify-center text-white font-semibold text-base shrink-0">

                            {username.charAt(0).toUpperCase()}

                        </div>

                        <p className="text-white text-lg font-medium truncate">

                            {query}

                        </p>

                    </div>

                    <span className="ml-5 text-xs text-blue-100 whitespace-nowrap">

                        {new Date().toLocaleTimeString([], {
                            hour: "2-digit",
                            minute: "2-digit",
                        })}

                    </span>

                </div>

            </div>

        </div>

    );

}
