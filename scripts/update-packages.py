#!/usr/bin/env python3
import re
import subprocess
import urllib.parse
from pathlib import Path

import requests

PYPROJECT = Path("pyproject.toml")


def get_latest_lts(package_name: str) -> str:
    """
    Consulta PyPI e retorna a última versão estável (sem pre-releases).
    """
    safe_name = urllib.parse.quote(package_name, safe="")
    url = f"https://pypi.org/pypi/{safe_name}/json"
    resp = requests.get(url, timeout=10)
    if resp.status_code != 200:
        raise RuntimeError(f"Erro ao buscar {package_name} no PyPI: {resp.status_code}")
    data = resp.json()
    releases = data.get("releases", {})
    stable_versions = [
        v
        for v in releases.keys()
        if not any(c in v for c in ["a", "b", "rc", "dev", "post"])
    ]
    if not stable_versions:
        raise RuntimeError(f"Nenhuma versão estável encontrada para {package_name}")
    stable_versions.sort(
        key=lambda v: tuple(int(x) if x.isdigit() else x for x in re.split(r"[.-]", v))
    )
    return stable_versions[-1]


def update_dependency_line(line: str) -> str:
    """
    Atualiza apenas a versão de uma dependência na linha.
    Preserva prefixo, sufixo, extras e indentação.
    """
    match = re.match(r'(\s*")([^"]+)(".*)', line)
    if not match:
        return line
    prefix, pkg_spec, suffix = match.groups()

    # Extrai nome do pacote e extras
    if "==" in pkg_spec:
        base, _ = pkg_spec.split("==", 1)
    elif ">=" in pkg_spec:
        base, _ = pkg_spec.split(">=", 1)
    elif ">" in pkg_spec:
        base, _ = pkg_spec.split(">", 1)
    else:
        base = pkg_spec

    # Preserve extras originais, mas busque somente o pacote base
    base_name = base.split("[")[0]
    extras = ""
    if "[" in base and "]" in base:
        extras = base.split("[", 1)[1].split("]")[0]

    try:
        latest = get_latest_lts(base_name)
        new_pkg = base_name
        if extras:
            new_pkg += f"[{extras}]"
        new_pkg += f"=={latest}"
        return f"{prefix}{new_pkg}{suffix}"
    except Exception as e:
        print(f"⚠️ Não foi possível atualizar {pkg_spec}: {e}")
        return line


def main():
    lines = PYPROJECT.read_text().splitlines()
    new_lines = []
    inside_array = False

    for line in lines:
        stripped = line.strip()

        # Detecta início de arrays de dependência
        if stripped.endswith("[") and (
            "dependencies" in stripped or "dependency-groups" in stripped
        ):
            inside_array = True
            new_lines.append(line)
            continue

        # Detecta fim de array
        if inside_array and stripped.startswith("]"):
            inside_array = False
            new_lines.append(line)
            continue

        if inside_array:
            dep_line = line.strip()
            if dep_line.startswith('"') and dep_line.endswith(('"', '",')):
                line = update_dependency_line(line)

        new_lines.append(line)

    # Escreve de volta mantendo formatação original
    PYPROJECT.write_text("\n".join(new_lines) + "\n")
    print(f"{PYPROJECT} atualizado com versões LTS.")

    # Rodar uv sync
    try:
        print("Rodando uv sync --all-groups ...")
        subprocess.run(["uv", "sync", "--all-groups"], check=True)
        print("Sincronização concluída!")
    except subprocess.CalledProcessError as e:
        print(
            f"⚠️ uv sync falhou: {e}. Verifique conflitos de versões no pyproject.toml."
        )


if __name__ == "__main__":
    main()
