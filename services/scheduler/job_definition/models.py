from dataclasses import dataclass


@dataclass(slots=True)
class JobDefinition:
    id: str
    job_code: str
    name: str
    cron_expression: str | None = None
    is_enabled: bool = True
