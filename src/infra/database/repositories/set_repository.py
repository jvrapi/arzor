from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from domain.entities import Set
from domain.ports.repositories import FindSetProps, ISetRepository
from infra.database.models import SetModel


class SetRepository(ISetRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def list(self) -> list[Set]:
        """
        Lista todos os Sets no banco de dados.

        Returns:
            list[Set]: Uma lista de entidades Set.
        """
        # 1. Cria a query que seleciona todos os dados da tabela SetModel.
        # Utilizamos selectinload() se houver relacionamentos que precisam ser carregados,
        # mas aqui vamos manter simples, selecionando apenas o modelo principal.
        query = select(SetModel)

        # 2. Executa a query no banco de dados.
        result = await self._session.execute(query)

        # 3. Mapeia os resultados.
        # O .scalars() retorna os elementos de SetModel de forma plana,
        # evitando tuplas (SetModel,).
        models = result.scalars().all()

        # 4. Converte cada modelo SQLAlchemy para a entidade de domínio.
        # Assumimos aqui que Set tem um método de fábrica `from_model`.
        # Se você não tiver esse método, você precisará criá-lo.
        entities = [
            Set(
                id=model.id,
                name=model.name,
                description=model.description,
                created_at=model.created_at,
                updated_at=model.updated_at,
            )
            for model in models
        ]

        return entities

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
            is_non_foil_only=set.is_non_foil_only,
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
            is_non_foil_only=model.is_non_foil_only,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )
