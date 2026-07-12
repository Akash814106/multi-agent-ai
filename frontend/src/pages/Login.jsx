import { useState } from "react";

function Login({ onLogin, goToRegister }) {

    const [email, setEmail] = useState("");

    const [password, setPassword] = useState("");

    return (

        <div className="min-h-screen bg-slate-900 flex items-center justify-center">

            <div className="w-full max-w-md bg-slate-800 p-8 rounded-2xl">

                <h1 className="text-3xl font-bold text-white mb-8">

                    Login

                </h1>

                <input
                    type="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    className="w-full p-3 mb-4 rounded-lg bg-slate-700 text-white"
                />

                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    className="w-full p-3 mb-6 rounded-lg bg-slate-700 text-white"
                />

                <button
                    onClick={() =>
                        onLogin(email, password)
                    }
                    className="w-full bg-blue-600 hover:bg-blue-700 py-3 rounded-lg"
                >
                    Login
                </button>

                <button
                    onClick={goToRegister}
                    className="w-full mt-4 text-gray-400"
                >
                    Create Account
                </button>

            </div>

        </div>

    );

}

export default Login;