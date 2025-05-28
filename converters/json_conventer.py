import json
from typing import Any

_counter = 0  # Глобальный счетчик


def save_report_file_by_json(data: Any, base_filename: str) -> str:
    '''Сохраняет словарь в JSON файл с инкрементным номером.'''
    global _counter
    _counter += 1
    unique_filename = f"{base_filename}_{_counter}.json"

    with open(unique_filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    return unique_filename