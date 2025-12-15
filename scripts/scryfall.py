import json
from collections import defaultdict

import requests

SCRYFALL_BULK_CARDS = "https://api.scryfall.com/bulk-data/default-cards"


# --------------------------------------------
# 1. Download bulk data URL
# --------------------------------------------
def download_bulk_cards():
    print("Baixando URL do bulk Scryfall...")
    meta = requests.get(SCRYFALL_BULK_CARDS).json()
    download_uri = meta["download_uri"]

    print("Baixando arquivo completo (~200MB)... isso demora.")
    data = requests.get(download_uri).json()
    return data


# --------------------------------------------
# 2. Mapper: Scryfall → CreateCardInput
#    Ajuste conforme seu schema atualizado
# --------------------------------------------
def map_to_create_card_input(card):
    """
    Mapper ajustado para incluir oracle_id e external_id
    """
    legalities = card.get("legalities") or {}

    # Faces (para layouts que possuem)
    faces = []
    if "card_faces" in card and isinstance(card["card_faces"], list):
        for f in card["card_faces"]:
            faces.append(
                {
                    "name": f.get("name"),
                    "type_line": f.get("type_line"),
                    "oracle_text": f.get("oracle_text"),
                    "mana_cost": f.get("mana_cost"),
                    "power": f.get("power"),
                    "toughness": f.get("toughness"),
                    "loyalty": f.get("loyalty"),
                    "colors": f.get("colors"),
                    "color_identity": f.get("color_indicator") or f.get("colors"),
                    "image_uris": f.get("image_uris"),
                    "cmc": f.get("cmc"),
                }
            )

    return {
        "name": card.get("name"),
        "layout": card.get("layout"),
        "cmc": card.get("cmc"),
        # "set_id": card.get("set"),
        "set_id": "019b08b9-9fe4-7572-8c87-fc462d54510e",
        "collector_number": card.get("collector_number"),
        "lang": card.get("lang"),
        "type_line": card.get("type_line"),
        "rarity": card.get("rarity"),
        "mana_cost": card.get("mana_cost"),
        "oracle_text": card.get("oracle_text"),
        "power": card.get("power"),
        "toughness": card.get("toughness"),
        "loyalty": card.get("loyalty"),
        "colors": card.get("colors"),
        "color_identity": card.get("color_identity"),
        "image_uris": card.get("image_uris"),
        "legalities": {k: v for k, v in legalities.items()},
        "faces": faces if faces else None,
        "oracle_id": card.get("oracle_id"),
        "external_id": card.get("id"),
        "released_at": card.get("released_at"),
        "border_color": card.get("border_color"),
        "finishes": card.get("finishes"),
        "is_reserved": card.get("reserved"),
        "is_game_changer": card.get("game_changer"),
        "is_foil": card.get("foil"),
        "is_found_on_booster": card.get("booster"),
        "is_oversized": card.get("oversized"),
        "is_promo": card.get("promo"),
        "is_reprint": card.get("reprint"),
        "is_textless": card.get("textless"),
        "is_variation": card.get("variation"),
        "is_full_art": card.get("full_art"),
        "keywords": card.get("keywords"),
    }


# --------------------------------------------
# 3. Selecionar 1 carta por layout
# --------------------------------------------
def collect_one_card_per_layout(cards):
    layouts = defaultdict(list)

    for c in cards:
        layout = c.get("layout")
        if layout:
            layouts[layout].append(c)

    print(f"Layouts encontrados: {len(layouts)}")
    for layout, arr in layouts.items():
        print(f" - {layout}: {len(arr)} cards")

    # Apenas um de cada
    selected = []
    for layout, arr in layouts.items():
        selected.append(arr[0])  # 1º card do layout

    return selected


# --------------------------------------------
# 4. MAIN
# --------------------------------------------
def main():
    cards = download_bulk_cards()
    print("Total de cards carregados:", len(cards))

    selected = collect_one_card_per_layout(cards)
    print("Selecionados:", len(selected), "layouts distintos.")

    # Mapear para CreateCardInput
    mapped_cards = [map_to_create_card_input(c) for c in selected]

    # Salvar JSON
    with open("cards_seed.json", "w", encoding="utf-8") as f:
        json.dump(mapped_cards, f, indent=2, ensure_ascii=False)

    print("\nArquivo gerado: cards_seed.json")


if __name__ == "__main__":
    main()
