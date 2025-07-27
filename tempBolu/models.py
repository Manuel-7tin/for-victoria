from datetime import datetime


class Task:
    username: str
    title: str
    desc: str
    due_date: datetime
    priority: str
    status: str
    archived: bool