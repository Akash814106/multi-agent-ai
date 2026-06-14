class WorkflowMetrics:

    def __init__(self):

        self.task_count = 0

        self.revision_executed = 0
        self.revision_skipped = 0
        self.revision_rate = 0

        self.memory_used = False

        self.execution_time = 0
        self.avg_time_per_task = 0


        self.query_type = ""

        self.timestamp = ""