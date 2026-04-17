from dataclasses import dataclass


@dataclass(slots=True)
class MonitorDefinition:
    id: str
    system_name: str
    monitor_type: str
    is_enabled: bool = True

