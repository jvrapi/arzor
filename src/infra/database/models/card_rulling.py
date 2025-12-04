from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid_utils import uuid7

from infra.database.base import Base


class CardRullingModel(Base):
    __tablename__ = "card_rullings"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid7()),
    )
    text: Mapped[str] = mapped_column(Text, nullable=False)

    card_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("cards.id", ondelete="CASCADE"),
        nullable=False,
    )
    card = relationship("CardModel", back_populates="rullings")
