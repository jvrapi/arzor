from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid_utils import uuid7

from infra.database.base import Base


class SetModel(Base):
    __tablename__ = "sets"

    set_type = relationship("SetTypeModel")

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid7())
    )
    external_id: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    set_type_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("set_types.id"), unique=True, nullable=False
    )
    code: Mapped[str] = mapped_column(String(5), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    card_count: Mapped[int] = mapped_column(nullable=False)
    release_date: Mapped[str] = mapped_column(String(10), nullable=True)
    is_digital: Mapped[bool] = mapped_column(nullable=False, default=False)
    is_foil_only: Mapped[bool] = mapped_column(nullable=False, default=False)
    is_nonfoil_only: Mapped[bool] = mapped_column(nullable=False, default=False)
