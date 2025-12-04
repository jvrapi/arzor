#!/usr/bin/env python3
"""Script para aplicar migrations do banco de dados (Alembic)"""

import argparse
import asyncio
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))


def run_alembic_migrations(database_url: str = None):
    """Aplica migrations do Alembic"""
    try:
        print("🔄 Aplicando migrations do Alembic...")

        import os

        cmd = ["alembic", "upgrade", "head"]
        env = os.environ.copy()

        if database_url:
            env["DATABASE_URL"] = database_url
            print("📍 Usando database_url fornecida")
        else:
            print("📍 Usando DATABASE_URL do .env")

        result = subprocess.run(cmd, env=env, capture_output=True, text=True)

        if result.returncode == 0:
            print("✅ Migrations do Alembic aplicadas com sucesso!")
            if result.stdout:
                print(result.stdout)
        else:
            print("❌ Erro ao aplicar migrations do Alembic:")
            print(result.stderr)
            raise RuntimeError(f"Falha ao executar Alembic: {result.stderr}")

    except subprocess.SubprocessError as e:
        print(f"❌ Erro ao executar Alembic: {e}")
        raise
    except Exception as e:
        print(f"❌ Erro inesperado ao aplicar migrations do Alembic: {e}")
        raise


async def main(database_url: str = None):
    """Executa todas as migrations"""
    print("=" * 60)
    print("🚀 Iniciando setup do banco de dados")
    print("=" * 60)

    run_alembic_migrations(database_url)

    print("\n" + "=" * 60)
    print("✅ Setup do banco de dados concluído com sucesso!")
    print("=" * 60)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Aplica todas as migrations do banco de dados"
    )
    parser.add_argument(
        "--database-url",
        type=str,
        help="URL de conexão do PostgreSQL (ex: postgresql://user:pass@host:5432/db)",
    )
    args = parser.parse_args()

    asyncio.run(main(args.database_url))
