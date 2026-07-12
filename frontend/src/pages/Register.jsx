import { useState } from "react";

function Register({ onRegister, goToLogin }) {

    const [username, setUsername] = useState("");

    const [email, setEmail] = useState("");

    const [password, setPassword] = useState("");

    return (

        <div className="min-h-screen bg-slate-900 flex items-center justify-center">

            <div className="w-full max-w-md bg-slate-800 p-8 rounded-2xl">

                <h1 className="text-3xl font-bold text-white mb-8">

                    Register

                </h1>

                <input
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    className="w-full p-3 mb-4 rounded-lg bg-slate-700 text-white"
                />

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
                        onRegister(
                            username,
                            email,
                            password
                        )
                    }
                    className="w-full bg-green-600 hover:bg-green-700 py-3 rounded-lg"
                >
                    Register
                </button>

                <button
                    onClick={goToLogin}
                    className="w-full mt-4 text-gray-400"
                >
                    Already have an account?
                </button>

            </div>

        </div>

    );

}

export default Register;