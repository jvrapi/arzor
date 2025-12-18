from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from domain.entities import Set
from domain.ports.repositories import FindSetProps, ISetRepository
from domain.value_objects import OrderType, PaginatedResult
from infra.database.mappers import SetMapper
from infra.database.models import SetModel


class SetRepository(ISetRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def list(
        self,
        limit: int = 5,
        cursor: Optional[str] = None,
        order: OrderType = "asc",
    ) -> PaginatedResult[Set]:
        """
        Lista todos os Sets no banco de dados.

        Returns:
            list[Set]: Uma lista de entidades Set.
        """

        query = select(SetModel).options(selectinload(SetModel.set_type))

        if order == "asc":
            query = query.order_by(SetModel.id.asc())
        else:
            query = query.order_by(SetModel.id.desc())

        if cursor:
            if order == "asc":
                query = query.where(SetModel.id > cursor)
            else:
                query = query.where(SetModel.id < cursor)

        query = query.limit(limit + 1)

        result = await self._session.execute(query)

        rows = result.scalars().all()

        if len(rows) > limit:
            next_cursor = rows[-1].id
            rows = rows[:-1]
        else:
            next_cursor = None

        items = [SetMapper.to_entity(r) for r in rows]

        return PaginatedResult(
            items=items,
            next_cursor=next_cursor,
        )

    async def create(self, set: Set) -> str:
        """
        Cria um novo Set no banco de dados.

        Args:
            set_entity (Set): A entidade Set a ser criada.

        Returns:
            Set: A entidade Set criada com o ID atribuído.
        """
        # 1. Cria uma instância do modelo SQLAlchemy a partir da entidade de domínio.
        model = SetModel(
            name=set.name,
            code=set.code,
            external_id=set.external_id,
            set_type_id=set.set_type_id,
            card_count=set.card_count,
            release_date=set.release_date,
            is_digital=set.is_digital,
            is_foil_only=set.is_foil_only,
            is_nonfoil_only=set.is_nonfoil_only,
            icon_uri=set.icon_uri,
        )

        # 2. Adiciona o modelo à sessão.
        self._session.add(model)

        # 3. Comita a transação para persistir os dados no banco.
        await self._session.commit()

        return model.id

    async def get_by(self, find_props: FindSetProps) -> Set | None:
        """
        Recupera um Set do banco de dados com base nos parâmetros fornecidos.
        Args:
            find_props (FindSetProps): Os parâmetros para encontrar o Set.
        Returns:
            Set | None: A entidade Set encontrada ou None se não existir.
        """

        query = select(SetModel)

        if find_props.id is not None:
            query = query.where(SetModel.id == str(find_props.id))
        if find_props.code is not None:
            query = query.where(SetModel.code == find_props.code)
        if find_props.external_id is not None:
            query = query.where(SetModel.external_id == find_props.external_id)

        result = await self._session.execute(query)
        model = result.scalars().first()

        if model is None:
            return None

        return SetMapper.to_entity(model)
