from datetime import UTC, datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from uuid_utils import uuid7

from infra.database.base import Base


class CardRulingModel(Base):
    __tablename__ = "card_rullings"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid7()),
        comment="Primary key UUID for the card rulling",
    )

    card_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("cards.id", ondelete="CASCADE"),
        nullable=False,
        comment="Foreign key to the card this rulling belongs to",
    )

    comment: Mapped[str] = mapped_column(Text, nullable=False, comment="Rulling text")

    published_at: Mapped[str] = mapped_column(
        String(25), nullable=False, comment="Published date of the rulling"
    )

    source: Mapped[str] = mapped_column(
        String(255), nullable=False, comment="Source of the rulling"
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
