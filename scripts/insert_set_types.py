import asyncio
import os
import sys

# Adiciona a pasta 'src' ao sys.path para encontrar 'infra'
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)


from infra.database.base import get_db
from infra.database.models.set_type import (
    SetTypeModel,  # ajuste se estiver em outro path
)

# Lista de sets a serem inseridos
set_types = [
    ("core", "A yearly Magic core set (Tenth Edition, etc)"),
    ("expansion", "A rotational expansion set in a block (Zendikar, etc)"),
    ("masters", "A reprint set that contains no new cards (Modern Masters, etc)"),
    ("eternal", "A set of new cards that only get added to high-power formats"),
    ("alchemy", "An Arena set designed for Alchemy"),
    ("masterpiece", "Masterpiece Series premium foil cards"),
    ("arsenal", "A Commander-oriented gift set"),
    ("from_the_vault", "From the Vault gift sets"),
    ("spellbook", "Spellbook series gift sets"),
    ("premium_deck", "Premium Deck Series decks"),
    ("duel_deck", "Duel Decks"),
    ("draft_innovation", "Special draft sets, like Conspiracy and Battlebond"),
    ("treasure_chest", "Magic Online treasure chest prize sets"),
    ("commander", "Commander preconstructed decks"),
    ("planechase", "Planechase sets"),
    ("archenemy", "Archenemy sets"),
    ("vanguard", "Vanguard card sets"),
    ("funny", "A funny un-set or set with funny promos (Unglued, Happy Holidays, etc)"),
    ("starter", "A starter/introductory set (Portal, etc)"),
    ("box", "A gift box set"),
    ("promo", "A set that contains purely promotional cards"),
    ("token", "A set made up of tokens and emblems."),
    (
        "memorabilia",
        "A set made up of gold-bordered, oversize, or trophy cards that are not legal",
    ),
    ("minigame", "A set that contains minigame card inserts from booster packs"),
]


async def insert_set_types():
    async for session in get_db():
        try:
            for name, description in set_types:
                set_type = SetTypeModel(name=name, description=description)
                session.add(set_type)
            await session.commit()
            print("Todos os set_types foram inseridos com sucesso!")
        except Exception as e:
            await session.rollback()
            print("Erro ao inserir set_types:", e)


if __name__ == "__main__":
    asyncio.run(insert_set_types())
