from datetime import UTC, datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from uuid_utils import uuid7

from infra.database.base import Base


class CardFaceModel(Base):
    __tablename__ = "card_faces"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid7()),
        comment="Primary key UUID for the card face",
    )

    card_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("cards.id"),
        nullable=False,
        comment="Foreign key to the card this face belongs to",
    )

    name: Mapped[str] = mapped_column(String(200), nullable=False, comment="Face name")

    mana_cost: Mapped[str] = mapped_column(
        String(20), nullable=True, comment="Mana cost of the face"
    )

    type_line: Mapped[str] = mapped_column(
        String(200), nullable=True, comment="Type line of the face"
    )

    oracle_text: Mapped[str] = mapped_column(
        Text, nullable=True, comment="Oracle text of the face (long text)"
    )

    power: Mapped[str] = mapped_column(
        String(10), nullable=True, comment="Power value (for creatures)"
    )

    toughness: Mapped[str] = mapped_column(
        String(10), nullable=True, comment="Toughness value (for creatures)"
    )

    loyalty: Mapped[str] = mapped_column(
        String(10), nullable=True, comment="Loyalty (for planeswalkers)"
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
