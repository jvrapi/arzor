from sqlalchemy import inspect

from domain.entities import Set, SetType
from infra.database.models import SetModel


class SetMapper:
    @staticmethod
    def to_entity(model: SetModel) -> Set:
        state = inspect(model)

        set_type = None
        if "set_type" not in state.unloaded:
            if model.set_type is not None:
                set_type = SetType(
                    id=model.set_type.id,
                    name=model.set_type.name,
                    description=model.set_type.description,
                )

        return Set(
            id=model.id,
            name=model.name,
            code=model.code,
            external_id=model.external_id,
            set_type_id=model.set_type_id,
            card_count=model.card_count,
            release_date=model.release_date,
            is_digital=model.is_digital,
            is_foil_only=model.is_foil_only,
            is_nonfoil_only=model.is_nonfoil_only,
            icon_uri=model.icon_uri,
            set_type=set_type,
        )
