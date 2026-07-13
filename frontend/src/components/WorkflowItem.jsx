import {
    CheckCircle2,
    Circle,
    Loader2,
} from "lucide-react";

export default function WorkflowItem({

    label,
    index,
    activeIndex,
    time,

}) {

    const completed = index < activeIndex;

    const running = index === activeIndex;

    return (

        <div className="flex items-center justify-between py-3 border-b border-slate-700 last:border-b-0">

            <div className="flex items-center gap-3">

                {completed ? (

                    <CheckCircle2
                        size={18}
                        className="text-green-400"
                    />

                ) : running ? (

                    <Loader2
                        size={18}
                        className="text-blue-400 animate-spin"
                    />

                ) : (

                    <Circle
                        size={16}
                        className="text-slate-500"
                    />

                )}

                <div>

                    <p className="text-sm font-medium text-white">

                        {label}

                    </p>

                    <p className="text-xs text-slate-400">

                        {completed
                            ? time
                            : running
                            ? "In Progress"
                            : "Pending"}

                    </p>

                </div>

            </div>

            {completed && (

                <span className="text-xs text-green-400 font-medium">

                    Done

                </span>

            )}

        </div>

    );

}