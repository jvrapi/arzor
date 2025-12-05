from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional


@dataclass(kw_only=True, frozen=True)
class BaseEntity:
    """
    Classe base contendo campos comuns a todas as entidades,
    como identificadores e timestamps de auditoria.
    """

    id: Optional[str] = field(default=None)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
