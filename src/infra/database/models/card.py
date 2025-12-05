from datetime import UTC, datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid_utils import uuid7

from infra.database.base import Base


class CardModel(Base):
    __tablename__ = "cards"

    set = relationship("SetModel")
    faces = relationship("CardFaceModel")

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid7()),
        comment="Primary key UUID for the card",
    )

    external_id: Mapped[str] = mapped_column(
        String(100), unique=True, nullable=False, comment="Original ID from Scryfall"
    )

    set_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("sets.id"),
        nullable=False,
        comment="Foreign key to the set this card belongs to",
    )

    name: Mapped[str] = mapped_column(String(200), nullable=False, comment="Card name")

    lang: Mapped[str] = mapped_column(
        String(10), nullable=True, comment="Language code of the card"
    )

    layout: Mapped[str] = mapped_column(
        String(50),
        nullable=True,
        comment="Card layout (normal, transform, split, meld, etc.)",
    )

    rarity: Mapped[str] = mapped_column(
        String(20),
        nullable=True,
        comment="Card rarity (common, uncommon, rare, mythic)",
    )

    mana_cost: Mapped[str] = mapped_column(
        String(20), nullable=True, comment="Mana cost of the card"
    )

    cmc: Mapped[int] = mapped_column(
        Integer, nullable=True, comment="Converted mana cost"
    )

    type_line: Mapped[str] = mapped_column(
        String(200), nullable=True, comment="Type line of the card"
    )

    oracle_text: Mapped[str] = mapped_column(
        Text, nullable=True, comment="Oracle text of the card (long text)"
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

    collector_number: Mapped[str] = mapped_column(
        String(20), nullable=True, comment="Collector number of the card"
    )

    # Boolean fields
    is_reprint: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        comment="Indicates if the card is a reprint (from Scryfall)",
    )

    is_reserved: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        comment="Indicates if the card is on the reserved list (from Scryfall)",
    )

    is_full_art: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        comment="Indicates if the card is full art (from Scryfall)",
    )

    is_textless: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        comment="Indicates if the card has no text (from Scryfall)",
    )

    is_booster: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        comment="Indicates if the card can appear in boosters (from Scryfall)",
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
