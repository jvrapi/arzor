from datetime import UTC, datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column
from uuid_utils import uuid7

from infra.database.base import Base


class SetTypeModel(Base):
    __tablename__ = "set_types"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid7())
    )
    name: Mapped[str] = mapped_column(
        String(100), nullable=False, comment="Name of the set type"
    )
    description: Mapped[str] = mapped_column(
        String(255), nullable=True, comment="Description of the set type"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        comment="Timestamp when the set was created",
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
        comment="Timestamp when the set was last updated",
    )
