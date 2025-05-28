FIELD_ALIASES = {
    "id": ["id", "ID", "employee_id"],
    "email": ["email", "email_address"],
    "name": ["name", "full_name", "employee_name"],
    "department": ["department", "dept"],
    "hours_worked": ["hours_worked", "worked_hours"],
    "hourly_rate": ["hourly_rate", "rate", "salary"]
}



def normalize_data(fields: list[str]) -> list[str]:
    """
    Приводит список названий полей к единому формату,
    используя словарь алиасов FIELD_ALIASES.
    """
    normalized = []

    for field in fields:
        field_lower = field.strip().lower()
        matched = False

        for standard, aliases in FIELD_ALIASES.items():
            if field_lower in [alias.lower() for alias in aliases]:
                normalized.append(standard)
                matched = True
                break

        if not matched:

            raise ValueError(f"Неизвестное поле: {field}")

    return normalized

def get_formatted_file(file_lines):
    result = []
    print(file_lines)

    rows = file_lines  # уже список списков

    # Нормализуем заголовки
    headers = normalize_data(rows[0])

    # Преобразуем каждую строку в словарь
    for row in rows[1:]:
        record = dict(zip(headers, row))
        result.append(record)

    return result
