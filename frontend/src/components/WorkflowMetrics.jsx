import {
    Clock3,
    Brain,
    ListTodo,
    RefreshCcw,
    CheckCircle2,
    XCircle,
} from "lucide-react";

function MetricCard({

    icon,
    title,
    value,
    subtitle,

}) {

    return (

        <div className="bg-slate-900 border border-slate-700 rounded-xl p-4 hover:border-blue-500 transition-all">

            <div className="flex items-center gap-2 text-slate-400 mb-3">

                {icon}

                <span className="text-sm">

                    {title}

                </span>

            </div>

            <div className="text-3xl font-bold text-white">

                {value}

            </div>

            <div className="text-xs text-slate-500 mt-2">

                {subtitle}

            </div>

        </div>

    );

}

function WorkflowMetrics({ metrics }) {

    const completedTasks =
        metrics.task_count - metrics.failed_tasks;

    return (

        <div className="bg-[#1B2435] border border-slate-700 rounded-2xl p-5 h-full w-full shadow-lg">

            <div className="mb-5">

                <h2 className="text-xl font-semibold">

                    Workflow Metrics

                </h2>

                <p className="text-sm text-slate-400 mt-1">

                    Execution statistics

                </p>

            </div>

            <div className="grid grid-cols-2 gap-4">

                <MetricCard
                    icon={<Clock3 size={18} className="text-blue-400" />}
                    title="Execution Time"
                    value={`${metrics.execution_time}s`}
                    subtitle="Total runtime"
                />

                <MetricCard
                    icon={<Brain size={18} className="text-violet-400" />}
                    title="Memory Used"
                    value={metrics.memory_used ? "Yes" : "No"}
                    subtitle="Context retrieved"
                />

                <MetricCard
                    icon={<ListTodo size={18} className="text-cyan-400" />}
                    title="Work Items"
                    value={metrics.task_count}
                    subtitle="Tasks planned"
                />

                <MetricCard
                    icon={<RefreshCcw size={18} className="text-yellow-400" />}
                    title="Revisions"
                    value={metrics.revision_executed}
                    subtitle="Quality improvements"
                />

                <MetricCard
                    icon={<CheckCircle2 size={18} className="text-green-400" />}
                    title="Tasks Completed"
                    value={completedTasks}
                    subtitle="Successful tasks"
                />

                <MetricCard
                    icon={<XCircle size={18} className="text-red-400" />}
                    title="Failed Tasks"
                    value={metrics.failed_tasks}
                    subtitle="Needs attention"
                />

            </div>

        </div>

    );

}

export default WorkflowMetrics;