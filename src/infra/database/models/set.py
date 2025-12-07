from datetime import UTC, datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid_utils import uuid7

from infra.database.base import Base


class SetModel(Base):
    __tablename__ = "sets"

    set_type = relationship("SetTypeModel")

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid7()),
        comment="Primary key UUID for the set",
    )
    external_id: Mapped[str] = mapped_column(
        String(100), unique=True, nullable=False, comment="Original ID from Scryfall"
    )
    set_type_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("set_types.id"),
        unique=False,
        nullable=False,
        comment="Foreign key to the set type",
    )
    code: Mapped[str] = mapped_column(
        String(5), unique=True, nullable=False, comment="Set code"
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False, comment="Set name")
    card_count: Mapped[int] = mapped_column(
        nullable=False, comment="Number of cards in the set"
    )
    release_date: Mapped[str] = mapped_column(
        String(10), nullable=True, comment="Release date of the set (YYYY-MM-DD)"
    )
    is_digital: Mapped[bool] = mapped_column(
        nullable=False, default=False, comment="Indicates if the set is digital-only"
    )
    is_foil_only: Mapped[bool] = mapped_column(
        nullable=False,
        default=False,
        comment="Indicates if the set contains only foil cards",
    )
    is_non_foil_only: Mapped[bool] = mapped_column(
        nullable=False,
        default=False,
        comment="Indicates if the set contains only non-foil cards",
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
