from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_table import Base


class ActorTable(Base):
    __tablename__ = "actor"

    actor_id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(45), nullable=False)
    last_name: Mapped[str] = mapped_column(String(45), nullable=False)
