from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.utils.db import Base

class TaskModel(Base):
    __tablename__ = "user_tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    is_completed: Mapped[bool] = mapped_column(Boolean)
    user_id:Mapped[int] = mapped_column(Integer, ForeignKey("Users.id", ondelete="CASCADE"), nullable=True)