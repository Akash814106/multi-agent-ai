import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

export default function AgentMessage({ message }) {

    const time = new Date().toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit",
    });

    return (

        <div className="mt-6 bg-[#222B3D] border border-slate-700 rounded-2xl p-6 shadow-lg">

            <div className="flex justify-between items-start">

                <div className="flex items-center gap-4">
                
                    <div className="w-12 h-12 rounded-full bg-gradient-to-br from-violet-600 to-blue-600 flex items-center justify-center shadow-lg">
                
                        <span className="text-white text-lg font-bold">
                
                            ✦
                
                        </span>
                
                    </div>
                
                    <div>
                
                        <h3 className="text-lg font-semibold text-white">
                
                            AgentFlow AI
                
                        </h3>
                
                        <p className="text-sm text-slate-400">
                
                            Multi-Agent Assistant
                
                        </p>
                
                    </div>
                
                </div>
                
                <span className="text-sm text-slate-400">
                
                    {time}
                
                </span>
                
            </div>

            <div className="mt-6">

                <ReactMarkdown
                    remarkPlugins={[remarkGfm]}
                    components={{
                        h1: ({ children }) => (
                            <h1 className="text-3xl font-bold text-white mb-5">
                                {children}
                            </h1>
                        ),

                        h2: ({ children }) => (
                            <h2 className="text-2xl font-semibold text-white mt-8 mb-4">
                                {children}
                            </h2>
                        ),

                        h3: ({ children }) => (
                            <h3 className="text-xl font-semibold text-white mt-6 mb-3">
                                {children}
                            </h3>
                        ),

                        p: ({ children }) => (
                            <p className="text-slate-200 leading-8 mb-4">
                                {children}
                            </p>
                        ),

                        ul: ({ children }) => (
                            <ul className="list-disc pl-6 space-y-2 text-slate-200 mb-5">
                                {children}
                            </ul>
                        ),

                        ol: ({ children }) => (
                            <ol className="list-decimal pl-6 space-y-2 text-slate-200 mb-5">
                                {children}
                            </ol>
                        ),

                        li: ({ children }) => (
                            <li>{children}</li>
                        ),

                        strong: ({ children }) => (
                            <strong className="font-bold text-white">
                                {children}
                            </strong>
                        ),

                        em: ({ children }) => (
                            <em className="italic text-slate-100">
                                {children}
                            </em>
                        ),

                        blockquote: ({ children }) => (
                            <blockquote className="border-l-4 border-violet-500 pl-4 italic text-slate-300 my-5">
                                {children}
                            </blockquote>
                        ),

                        table: ({ children }) => (
                            <div className="overflow-x-auto my-6">

                                <table className="min-w-full border border-slate-700 rounded-lg">

                                    {children}

                                </table>

                            </div>
                        ),

                        thead: ({ children }) => (
                            <thead className="bg-slate-800">
                                {children}
                            </thead>
                        ),

                        tbody: ({ children }) => (
                            <tbody>
                                {children}
                            </tbody>
                        ),

                        tr: ({ children }) => (
                            <tr className="border-b border-slate-700">
                                {children}
                            </tr>
                        ),

                        th: ({ children }) => (
                            <th className="px-4 py-3 text-left font-semibold text-white">
                                {children}
                            </th>
                        ),

                        td: ({ children }) => (
                            <td className="px-4 py-3 text-slate-200">
                                {children}
                            </td>
                        ),

                        code({ inline, children }) {

                            if (inline) {

                                return (

                                    <code className="bg-slate-900 px-2 py-1 rounded text-green-400">

                                        {children}

                                    </code>

                                );

                            }

                            return (

                                <pre className="bg-[#0F172A] border border-slate-700 rounded-xl p-5 overflow-x-auto my-5">

                                    <code className="text-green-300">

                                        {children}

                                    </code>

                                </pre>

                            );

                        },

                    }}
                >

                    {message}

                </ReactMarkdown>

            </div>

        </div>

    );

}