import { useState } from "react";

function Register({ onRegister, goToLogin }) {

    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleRegister = (e) => {
        e.preventDefault();

        onRegister(
            username,
            email,
            password
        );
    };

    return (

        <div className="min-h-screen bg-slate-900 flex items-center justify-center px-6">

            <div className="w-full max-w-md">

                <div className="text-center mb-10">

                    <h1 className="text-5xl font-bold text-white">
                        AgentFlow
                    </h1>

                    <p className="text-blue-400 mt-4 text-lg">
                        Multi-Agent AI Workspace
                    </p>

                    <p className="text-slate-400 mt-2">
                        Research • Build • Learn
                    </p>

                </div>

                <form
                    onSubmit={handleRegister}
                    className="bg-[#1B2435] border border-slate-700 rounded-3xl shadow-2xl p-8"
                >

                    <h2 className="text-2xl font-semibold text-white mb-8">
                        Create Account
                    </h2>

                    <div className="space-y-5">

                        <input
                            type="text"
                            placeholder="Username"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            className="w-full bg-slate-800 border border-slate-700 rounded-xl px-5 py-4 text-white placeholder:text-slate-500 focus:outline-none focus:border-blue-500 transition"
                        />

                        <input
                            type="email"
                            placeholder="Email Address"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            className="w-full bg-slate-800 border border-slate-700 rounded-xl px-5 py-4 text-white placeholder:text-slate-500 focus:outline-none focus:border-blue-500 transition"
                        />

                        <input
                            type="password"
                            placeholder="Password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            className="w-full bg-slate-800 border border-slate-700 rounded-xl px-5 py-4 text-white placeholder:text-slate-500 focus:outline-none focus:border-blue-500 transition"
                        />

                    </div>

                    <button
                        type="submit"
                        className="w-full mt-8 bg-blue-600 hover:bg-blue-700 transition rounded-xl py-4 font-semibold"
                    >
                        Create Account
                    </button>

                    <div className="mt-8 text-center">

                        <p className="text-slate-400">
                            Already have an account?
                        </p>

                        <button
                            type="button"
                            onClick={goToLogin}
                            className="mt-2 text-blue-400 hover:text-blue-300 transition font-medium"
                        >
                            Sign In
                        </button>

                    </div>

                </form>

            </div>

        </div>

    );

}

export default Register;