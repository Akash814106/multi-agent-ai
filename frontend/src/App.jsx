import { useState } from "react";
import axios from "axios";

function App() {

  const [query, setQuery] = useState("");
  const [result, setResult] = useState(null);

  async function sendQuery() {

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/chat",
        {
          query: query,
        }
      );
      
      setResult(response.data);

    } catch (error) {

      console.error(error);

    }
  }

  return (

    <div className="min-h-screen bg-slate-900 text-white">

      <div className="max-w-5xl mx-auto p-10">

        <h1 className="text-5xl font-bold text-center">
          🤖 Multi-Agent AI Assistant
        </h1>

        <p className="text-center text-gray-400 mt-3">
          Planner • Research • Critic • Revision • Memory
        </p>

        <div className="mt-10 flex gap-4">

          <input
            className="flex-1 p-4 rounded-xl bg-slate-800 border border-slate-700"
            type="text"
            placeholder="Ask anything..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />

          <button
            onClick={sendQuery}
            className="bg-blue-600 hover:bg-blue-700 px-8 rounded-xl font-semibold"
          >
            Send
          </button>

        </div>

        
          {
            result && (
              <div className="mt-10 bg-slate-800 rounded-xl p-6">
              
                <h2 className="text-2xl font-semibold mb-4">
                  🧠 Goal
                </h2>
            
                <p className="whitespace-pre-wrap">
                  {result.goal}
                </p>
            
              </div>
            )
          }

          {
            result && (
              <div className="mt-10 bg-slate-800 rounded-xl p-6">
              
                <h2 className="text-2xl font-semibold mb-4">
                  📋 Tasks
                </h2>
            
                <ul className="space-y-3">
            
                  {result.tasks.map((task, index) => (
                  
                    <li key={index}>
                      ✅ {task}
                    </li>

                  ))}

                </ul>
                
              </div>
            )
          }


          {
            result && (
              <div className="mt-10 bg-slate-800 rounded-xl p-6">
              
                <h2 className="text-2xl font-semibold mb-4">
                  🤖 Final Summary
                </h2>
            
                <p className="whitespace-pre-wrap">
                  {result.final_summary}
                </p>
            
              </div>
            )
          }


        {
          result && (
            <div className="mt-10 bg-slate-800 rounded-xl p-6">

              <h2 className="text-2xl font-semibold mb-6">
              📊 Workflow Metrics
              </h2>

              <div className="grid grid-cols-2 gap-4">

                <div>⚡ Execution Time: {result.metrics.execution_time} sec</div>

                <div>🧠 Memory Used: {result.metrics.memory_used ? "Yes" : "No"}</div>

                <div>📋 Tasks: {result.metrics.task_count}</div>

                <div>🔄 Revisions: {result.metrics.revision_executed}</div>

                <div>⏭️ Revisions Skipped: {result.metrics.revision_skipped}</div>

                <div>❌ Failed Tasks: {result.metrics.failed_tasks}</div>

              </div>

            </div>
          )
        }

      </div>

    </div>

  );
}

export default App;