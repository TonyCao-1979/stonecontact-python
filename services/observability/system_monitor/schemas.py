from pydantic import BaseModel


class MonitorListRequest(BaseModel):
    system_name: str | None = None
    page: int = 1
    page_size: int = 20


class MonitorSaveRequest(BaseModel):
    id: str | None = None
    system_name: str
    monitor_type: str
    is_enabled: bool = True


class MonitorItem(BaseModel):
    id: str
    system_name: str
    monitor_type: str
    is_enabled: bool = True


class MonitorPage(BaseModel):
    items: list[MonitorItem]
    total: int

