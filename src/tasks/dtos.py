from pydantic import BaseModel

class TaskDTO(BaseModel):
    title: str
    description: str
    deadline: str
    is_completed: bool = False