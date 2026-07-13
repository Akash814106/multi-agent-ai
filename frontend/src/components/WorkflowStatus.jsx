import WorkflowItem from "./WorkflowItem";

function WorkflowStatus({

    isDirectResponse,
    statusList,

}) {

    const currentTime = new Date().toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit",
    });

    const steps = isDirectResponse
        ? [
              "Query Received",
              "Memory Retrieved",
              "Final Response",
          ]
        : [
              "Query Received",
              "Memory Retrieved",
              "Planning",
              "Research",
              "Analysis",
              "Final Response",
          ];

    return (

        <div className="bg-[#1B2435] border border-slate-700 rounded-2xl p-5 h-full w-full shadow-lg">

            <div className="flex items-center justify-between mb-5">

                <div>

                    <h2 className="text-xl font-semibold text-white">

                        Workflow Status

                    </h2>

                    <p className="text-sm text-slate-400 mt-1">

                        Live execution progress

                    </p>

                </div>

                <div className="w-3 h-3 rounded-full bg-green-400 animate-pulse"></div>

            </div>

            <div className="space-y-1">

                {steps.map((step, index) => (

                    <WorkflowItem

                        key={index}

                        label={step}

                        index={index}

                        activeIndex={statusList.length - 1}

                        time={currentTime}

                    />

                ))}

            </div>

        </div>

    );

}

export default WorkflowStatus;