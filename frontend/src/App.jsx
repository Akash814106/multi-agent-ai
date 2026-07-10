import { useState } from "react";
import axios from "axios";

import TaskCard from "./components/TaskCard";

function App() {

  const [query, setQuery] = useState("");
  const [result, setResult] = useState(null);

  const [loading, setLoading] = useState(false);
  const [statusList, setStatusList] = useState([]);

  async function sendQuery() {

    if (!query.trim()) {
      return;
    }

    setLoading(true);

    setStatusList([
      "✔ Query Received",
      "🟡 Sending to Backend..."
    ]);

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/chat",
        {
          query: query,
        }
      );

      setResult(response.data);
      setQuery("");
      setStatusList([]);

    } catch (error) {

      console.error(error);

      setStatusList([
        "❌ Backend Error"
      ]);

    } finally {

      setLoading(false);

    }

  }

  const isDirectResponse = result?.goal === "Direct Response";

  return (

    <div className="min-h-screen bg-slate-900 text-white">

      <div className="max-w-6xl mx-auto p-10">

        <h1 className="text-5xl font-bold text-center">
          🤖 Multi-Agent AI Assistant
        </h1>

        <p className="text-center text-gray-400 mt-3">
          Planner • Research • Critic • Revision • Memory
        </p>

        <div className="mt-10 flex gap-4">

          <input
            disabled={loading}
            className="flex-1 p-4 rounded-xl bg-slate-800 border border-slate-700"
            type="text"
            placeholder="Ask anything..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />

          <button
            onClick={sendQuery}
            disabled={loading}
            className="bg-blue-600 hover:bg-blue-700 disabled:bg-gray-600 px-8 rounded-xl font-semibold"
          >
            {loading ? "⏳ Processing..." : "Send"}
          </button>

        </div>

        {

          loading && (

            <div className="mt-6 bg-slate-800 rounded-xl p-5 border border-slate-700">

              <h2 className="text-xl font-semibold mb-4">
                🤖 Workflow Progress
              </h2>

              <ul className="space-y-2">

                {

                  statusList.map((item, index) => (

                    <li
                      key={index}
                      className="bg-slate-700 rounded-lg p-3"
                    >

                      {item}

                    </li>

                  ))

                }

              </ul>

            </div>

          )

        }

        {

          result && !isDirectResponse && (

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

          result && !isDirectResponse && (

            <div className="mt-10">

              <h2 className="text-3xl font-bold mb-6">
                📋 Multi-Agent Execution
              </h2>

              {

                result.results.map((task, index) => (

                  <TaskCard
                    key={index}
                    taskData={task}
                    index={index}
                  />

                ))

              }

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

                <div>
                  ⚡ Execution Time: {result.metrics.execution_time} sec
                </div>

                <div>
                  🧠 Memory Used: {result.metrics.memory_used ? "Yes" : "No"}
                </div>

                <div>
                  📋 Tasks: {result.metrics.task_count}
                </div>

                <div>
                  🔄 Revisions: {result.metrics.revision_executed}
                </div>

                <div>
                  ⏭️ Revisions Skipped: {result.metrics.revision_skipped}
                </div>

                <div>
                  ❌ Failed Tasks: {result.metrics.failed_tasks}
                </div>

              </div>

            </div>

          )

        }

      </div>

    </div>

  );

}

export default App;