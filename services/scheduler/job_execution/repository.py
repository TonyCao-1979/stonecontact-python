from services.scheduler.job_execution.models import JobExecutionLog


class JobExecutionRepository:
    def list_logs(self, _: str) -> list[JobExecutionLog]:
        return []
