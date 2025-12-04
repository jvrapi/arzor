from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from uuid_utils import uuid7

from infra.database.base import Base


class SetTypeModel(Base):
    __tablename__ = "set_types"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid7())
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
