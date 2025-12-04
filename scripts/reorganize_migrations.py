#!/usr/bin/env python3
import os
import sys
import time

# Caminho da pasta de migrations
MIGRATIONS_DIR = "migrations/versions"


def rename_migration(file_path: str, timestamp: str):
    """Renomeia um arquivo de migration e atualiza a variável 'revision'"""
    if not os.path.isfile(file_path):
        print(f"Arquivo não encontrado: {file_path}")
        return

    dir_name = os.path.dirname(file_path)
    base_name = os.path.basename(file_path)

    # Separar a parte após o hash
    parts = base_name.split("_", 1)
    if len(parts) != 2:
        print(f"Nome do arquivo não está no formato esperado: {base_name}")
        return

    new_file_name = f"{timestamp}_{parts[1]}"
    new_file_path = os.path.join(dir_name, new_file_name)

    # Renomear arquivo
    os.rename(file_path, new_file_path)
    print(f"Arquivo renomeado para: {new_file_name}")

    # Atualizar a variável 'revision' dentro do arquivo
    with open(new_file_path) as f:
        content = f.read()

    lines = content.splitlines()
    for i, line in enumerate(lines):
        if line.strip().startswith("revision ="):
            lines[i] = f'revision = "{timestamp}"'
            break

    with open(new_file_path, "w") as f:
        f.write("\n".join(lines) + "\n")

    print(f"Variável 'revision' atualizada para: {timestamp}")


def main():
    rename_all = "--all" in sys.argv

    if not os.path.isdir(MIGRATIONS_DIR):
        print(f"Pasta não encontrada: {MIGRATIONS_DIR}")
        return

    files = [f for f in os.listdir(MIGRATIONS_DIR) if f.endswith(".py")]
    if not files:
        print("Nenhuma migration encontrada na pasta.")
        return

    # Ordenar por data de criação
    files_paths = [os.path.join(MIGRATIONS_DIR, f) for f in files]
    files_paths.sort(key=os.path.getctime)

    if rename_all:
        # Renomear todas as migrations, adicionando 1 segundo incremental para cada timestamp
        timestamp_base = int(time.time())
        for idx, file_path in enumerate(files_paths):
            timestamp = str(timestamp_base + idx)
            rename_migration(file_path, timestamp)
    else:
        # Apenas a última migration
        latest_file = files_paths[-1]
        timestamp = str(int(time.time()))
        rename_migration(latest_file, timestamp)


if __name__ == "__main__":
    main()
