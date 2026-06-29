import json

from core.decorators import measure_time


@measure_time
def load_bonds(filepath: str = "data/bonds.json") -> list[dict]:
    """Читает json из файла."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise ValueError(f"Файл не найден")
    except json.JSONDecodeError:
        raise ValueError(f"Невалидный JSON")


@measure_time
def save_bonds(bonds: list[dict], filepath: str = "data/bonds.json") -> None:
    with open(filepath, "w",  encoding="utf-8") as f:
        json.dump(bonds, f, ensure_ascii=False, indent=4)
