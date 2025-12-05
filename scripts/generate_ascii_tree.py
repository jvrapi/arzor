import os

IGNORAR_PASTAS = {"__pycache__", ".venv", ".git"}
IGNORAR_EXTENSOES = {".pyc"}

def ascii_tree(root_path: str, prefix: str = ""):
    items = sorted(
        [
            item for item in os.listdir(root_path)
            if item not in IGNORAR_PASTAS and not item.endswith(tuple(IGNORAR_EXTENSOES))
        ]
    )

    count = len(items)

    for i, name in enumerate(items):
        full_path = os.path.join(root_path, name)
        connector = "└── " if i == count - 1 else "├── "

        print(prefix + connector + name)

        if os.path.isdir(full_path):
            extension = "    " if i == count - 1 else "│   "
            ascii_tree(full_path, prefix + extension)


def gerar_ascii(root_path: str = ".", output_file: str | None = None):
    lines = []
    original_print = print

    # Captura o print para salvar se precisar
    def capture_print(*args, **kwargs):
        text = " ".join(str(a) for a in args)
        lines.append(text)
        original_print(*args, **kwargs)

    # Temporariamente substitui print
    globals()["print"] = capture_print

    # Imprime nome da raiz
    print(os.path.basename(os.path.abspath(root_path)) or ".")
    ascii_tree(root_path)

    # Restaura print original
    globals()["print"] = original_print

    # Salva em arquivo, se quiser
    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"\n📄 ASCII tree salva em: {output_file}")


if __name__ == "__main__":
    gerar_ascii(".", "estrutura_ascii.txt")
