from enum import Enum

from pydantic import BaseModel, Field


class LegalitiesType(str, Enum):
    legal = "legal"
    not_legal = "not_legal"
    restricted = "restricted"
    banned = "banned"


class Rarity(str, Enum):
    common = "common"
    uncommon = "uncommon"
    rare = "rare"
    mythic = "mythic"
    special = "special"
    bonus = "bonus"


class SecurityStamp(str, Enum):
    oval = "oval"
    triangle = "triangle"
    acorn = "acorn"
    circle = "circle"
    arena = "arena"
    heart = "heart"


class BorderColor(str, Enum):
    black = "black"
    white = "white"
    borderless = "borderless"
    yellow = "yellow"
    silver = "silver"
    gold = "gold"


class Finish(str, Enum):
    foil = "foil"
    nonfoil = "nonfoil"
    etched = "etched"


class Color(str, Enum):
    W = "W"
    U = "U"
    B = "B"
    R = "R"
    G = "G"


class Legalities(BaseModel):
    standard: LegalitiesType = Field(description="Legality in the Standard format.")
    future: LegalitiesType = Field(
        description="Legality in the Future (future standard) format."
    )
    historic: LegalitiesType = Field(description="Legality in the Historic format.")
    timeless: LegalitiesType = Field(description="Legality in the Timeless format.")
    gladiator: LegalitiesType = Field(description="Legality in the Gladiator format.")
    pioneer: LegalitiesType = Field(description="Legality in the Pioneer format.")
    modern: LegalitiesType = Field(description="Legality in the Modern format.")
    legacy: LegalitiesType = Field(description="Legality in the Legacy format.")
    pauper: LegalitiesType = Field(description="Legality in the Pauper format.")
    vintage: LegalitiesType = Field(description="Legality in the Vintage format.")
    penny: LegalitiesType = Field(description="Legality in the Penny Dreadful format.")
    commander: LegalitiesType = Field(description="Legality in the Commander format.")
    oathbreaker: LegalitiesType = Field(
        description="Legality in the Oathbreaker format."
    )
    standardbrawl: LegalitiesType = Field(
        description="Legality in the Standard Brawl format."
    )
    brawl: LegalitiesType = Field(description="Legality in the Brawl format.")
    alchemy: LegalitiesType = Field(description="Legality in the Alchemy format.")
    paupercommander: LegalitiesType = Field(
        description="Legality in the Pauper Commander format."
    )
    duel: LegalitiesType = Field(description="Legality in the Duel format.")
    oldschool: LegalitiesType = Field(description="Legality in the Old School format.")
    premodern: LegalitiesType = Field(description="Legality in the Premodern format.")
    predh: LegalitiesType = Field(description="Legality in the PreDH format.")


class ImageUris(BaseModel):
    small: str = Field(
        description="A small version of the card image. (Scryfall 'small' image URI)"
    )
    normal: str = Field(
        description="A normal-resolution card image. (Scryfall 'normal' image URI)"
    )
    large: str = Field(
        description="A large-resolution card image. (Scryfall 'large' image URI)"
    )
    png: str = Field(
        description="A PNG version of the card image. (Scryfall 'png' image URI)"
    )
    art_crop: str = Field(
        description="Cropped image containing only the card art. (Scryfall 'art_crop' image URI)"
    )
    border_crop: str = Field(
        description="Cropped image including border; useful for thumbnails. (Scryfall 'border_crop' image URI)"
    )
