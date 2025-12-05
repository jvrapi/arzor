from dataclasses import dataclass

from .base import BaseEntity


@dataclass(frozen=True)
class SetType(BaseEntity):
    name: str
    description: str
