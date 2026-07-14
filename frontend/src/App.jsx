import { useState } from "react";
import { Send, LoaderCircle } from "lucide-react";

import Login from "./pages/Login";
import Register from "./pages/Register";

import useAuth from "./hooks/useAuth";

import Sidebar from "./components/Sidebar";
import ChatView from "./components/ChatView";

import useConversation from "./hooks/useConversation";

function App() {

  const [showRegister, setShowRegister] = useState(false);

  const {
  
    user,
  
    token,
  
    login,
  
    register,
  
    logout,
  
  } = useAuth();

  const {

    conversations,

    activeConversation,

    currentConversation,

    loading,

    thinking,

    statusList,

    query,

    setQuery,

    setActiveConversation,

    createConversation,

    renameConversation,

    deleteConversation,

    sendQuery,

  } = useConversation(user);



  if (!token) {

    if (showRegister) {

      return (

        <Register

          onRegister={async (username, email, password) => {

            await register(

              username,

              email,

              password

            );

            setShowRegister(false);

          }}

          goToLogin={() =>

            setShowRegister(false)

          }

        />

      );

    }

    return (

      <Login

        onLogin={login}

        goToRegister={() =>

          setShowRegister(true)

        }

      />

    );

  }


  return (

    <div className="min-h-screen bg-slate-900 text-white flex">

      <Sidebar

        user = {user}

        conversations={conversations}

        activeConversation={activeConversation}

        setActiveConversation={setActiveConversation}

        createConversation={createConversation}

        renameConversation={renameConversation}

        deleteConversation={deleteConversation}

      />

      <main className="flex-1">

        <div className="max-w-6xl mx-auto p-10">

            <div className="flex justify-between items-center mb-8">

                <div>

                    <h1 className="text-5xl font-bold">
                        AgentFlow
                    </h1>

                    <p className="text-gray-400 mt-2">
                        Research • Build • Learn
                    </p>

                </div>

                <button
                    onClick={logout}
                    className="bg-red-600 hover:bg-red-700 px-5 py-2 rounded-lg"
                >
                    Logout
                </button>

            </div>

            <div className="mt-10">

                <div className="bg-[#1B2435] border border-slate-700 rounded-3xl shadow-xl overflow-hidden">

                    <div className="flex items-center px-6 py-5">

                        <input
                            value={query}
                            disabled={loading}
                            onChange={(e) => setQuery(e.target.value)}
                            onKeyDown={(e) => {
                                if (e.key === "Enter" && !loading) {
                                    sendQuery();
                                }
                            }}
                            placeholder="Ask AgentFlow to research, explain, or solve..."
                            className="flex-1 bg-transparent outline-none text-lg placeholder:text-slate-500"
                        />

                        <button
                          onClick={sendQuery}
                          disabled={loading}
                          className="ml-4 w-12 h-12 rounded-full bg-blue-600 hover:bg-blue-700 disabled:bg-slate-600 transition-all duration-300 flex items-center justify-center"
                      >

                          {loading ? (
                          
                              <LoaderCircle
                                  size={20}
                                  className="animate-spin"
                              />
                          
                          ) : (
                          
                              <Send size={20} />
                          
                          )}

                      </button>
                          
                    </div>
                          
                    <div className="flex justify-between items-center border-t border-slate-700 px-6 py-3 text-sm text-slate-400">
                          
                        <span>
                            <span className="font-semibold text-white">Press Enter to send</span>
                        </span>
                          
                        <span className="flex items-center gap-2">
                          
                            <span
                                className={`w-2 h-2 rounded-full ${
                                    loading
                                        ? "bg-yellow-400 animate-pulse"
                                        : "bg-green-400"
                                }`}
                            />

                            {loading ? "Agents Working..." : "Ready"}
                              
                        </span>
                              
                    </div>
                              
                </div>
                              
            </div>
                              
            <ChatView
                loading={loading}
                thinking={thinking}
                statusList={statusList}
                conversation={currentConversation}
            />

        </div>
                              
      </main>

    </div>

  );

}

export default App;