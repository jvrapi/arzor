from datetime import UTC, datetime

from sqlalchemy import DateTime, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid_utils import uuid7

from domain.value_objects import Color
from infra.database.base import Base


class CardFaceModel(Base):
    __tablename__ = "card_faces"

    card = relationship("CardModel", back_populates="faces")

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid7()),
        comment="Primary key UUID for the card face",
    )

    card_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("cards.id", ondelete="CASCADE"),
        nullable=False,
        comment="Foreign key to the card this face belongs to",
    )

    oracle_id: Mapped[str | None] = mapped_column(
        String(36), nullable=True, comment="Scryfall oracle_id"
    )

    name: Mapped[str] = mapped_column(String(200), nullable=False, comment="Face name")

    mana_cost: Mapped[str | None] = mapped_column(
        String(100), nullable=True, comment="Mana cost of the face"
    )

    type_line: Mapped[str | None] = mapped_column(
        String(200), nullable=True, comment="Type line of the face"
    )

    oracle_text: Mapped[str | None] = mapped_column(
        Text, nullable=True, comment="Oracle text of the face (long text)"
    )

    power: Mapped[str | None] = mapped_column(
        String(10), nullable=True, comment="Power value (for creatures)"
    )

    toughness: Mapped[str | None] = mapped_column(
        String(10), nullable=True, comment="Toughness value (for creatures)"
    )

    loyalty: Mapped[str | None] = mapped_column(
        String(10), nullable=True, comment="Loyalty (for planeswalkers)"
    )

    image_uris: Mapped[dict[str, str] | None] = mapped_column(
        JSONB, nullable=True, comment="Image URIs from Scryfall"
    )

    cmc: Mapped[int | None] = mapped_column(
        Integer, nullable=True, comment="Converted mana cost"
    )

    colors: Mapped[list[Color] | None] = mapped_column(
        ARRAY(Enum(Color, name="color_enum", native_enum=False)), nullable=True
    )

    color_identity: Mapped[list[Color] | None] = mapped_column(
        ARRAY(Enum(Color, name="color_enum", native_enum=False)), nullable=True
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
