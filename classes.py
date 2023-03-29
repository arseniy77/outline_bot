from dataclasses import dataclass


@dataclass
class OutlineUser:
    id: int = None
    name: str = None
    password: str = None
    port: int = None
    method: str = None
    accessUrl: str = None
    data_usage: int = None
