from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from domain.entities import SetType
from domain.ports.repositories import ISetTypeRepository
from infra.database.models import SetTypeModel


class SetTypeRepository(ISetTypeRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def list(self) -> list[SetType]:
        """
        Lista todos os SetTypes no banco de dados.

        Returns:
            list[SetType]: Uma lista de entidades SetType.
        """
        # 1. Cria a query que seleciona todos os dados da tabela SetTypeModel.
        # Utilizamos selectinload() se houver relacionamentos que precisam ser carregados,
        # mas aqui vamos manter simples, selecionando apenas o modelo principal.
        query = select(SetTypeModel)

        # 2. Executa a query no banco de dados.
        result = await self._session.execute(query)

        # 3. Mapeia os resultados.
        # O .scalars() retorna os elementos de SetTypeModel de forma plana,
        # evitando tuplas (SetTypeModel,).
        models = result.scalars().all()

        # 4. Converte cada modelo SQLAlchemy para a entidade de domínio.
        # Assumimos aqui que SetType tem um método de fábrica `from_model`.
        # Se você não tiver esse método, você precisará criá-lo.
        entities = [
            SetType(
                id=model.id,
                name=model.name,
                description=model.description,
                created_at=model.created_at,
                updated_at=model.updated_at,
            )
            for model in models
        ]

        return entities
