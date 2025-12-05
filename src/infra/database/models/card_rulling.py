from datetime import UTC, datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from uuid_utils import uuid7

from infra.database.base import Base


class CardRullingModel(Base):
    __tablename__ = "card_rullings"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid7()),
        comment="Primary key UUID for the card rulling",
    )

    text: Mapped[str] = mapped_column(Text, nullable=False, comment="Rulling text")

    card_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("cards.id", ondelete="CASCADE"),
        nullable=False,
        comment="Foreign key to the card this rulling belongs to",
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
