from typing import TypedDict, List, Dict, Any, NotRequired


class AgentState(TypedDict):

    current_user: str
    user_query: str

    enhanced_user_query: NotRequired[str]
    enhanced_query: NotRequired[str]

    router_decision: NotRequired[str]
    memory_decision: NotRequired[str]

    memory_context: NotRequired[str]

    goal: NotRequired[str]
    plan: NotRequired[str]

    tasks: NotRequired[List[str]]

    results: NotRequired[List[Dict[str, Any]]]

    summary_list: NotRequired[List[str]]

    final_summary: NotRequired[str]

    metrics: NotRequired[Dict[str, Any]]