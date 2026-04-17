from services.scheduler.job_definition.models import JobDefinition


class JobDefinitionRepository:
    def list_jobs(self) -> list[JobDefinition]:
        return []

    def get_job(self, _: str) -> JobDefinition | None:
        return None
