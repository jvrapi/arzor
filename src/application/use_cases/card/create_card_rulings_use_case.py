from domain.entities.card_ruling import CardRuling
from domain.ports.repositories.card_ruling_repository import ICardRulingRepository

from .dto import CreateCardRulingInput


class CreateCardRulingsUseCase:
    def __init__(self, card_ruling_repository: ICardRulingRepository):
        self.card_ruling_repository = card_ruling_repository

    def execute(self, rulings: list[CreateCardRulingInput]) -> list[str]:
        card_rulings = [CardRuling(**ruling.model_dump()) for ruling in rulings]

        return self.card_ruling_repository.create_many(card_rulings)
