import { useState } from "react";

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

          <div className="mt-10 flex gap-4">

            <input

              value={query}

              disabled={loading}

              onChange={(e) => setQuery(e.target.value)}

              className="flex-1 p-4 rounded-xl bg-slate-800 border border-slate-700"

              placeholder="Ask anything..."

            />

            <button

              onClick={sendQuery}

              disabled={loading}

              className="bg-blue-600 hover:bg-blue-700 disabled:bg-gray-600 px-8 rounded-xl"

            >

              {loading ? "Running..." : "Run"}

            </button>

          </div>

          <ChatView
            loading={loading}
            statusList={statusList}
            conversation={currentConversation}
          />

        </div>

      </main>

    </div>

  );

}

export default App;