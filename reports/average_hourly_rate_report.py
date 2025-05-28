from collections import defaultdict

from core.field_mapping import get_formatted_file


def get_average_hourly_rate_per_department(file):
    list_workers = get_formatted_file(file)

    department_dict = defaultdict(list)  # ключ — департамент, значение — список почасовых ставок

    for worker in list_workers:
        department = worker['department']
        rate = float(worker['hourly_rate'])
        department_dict[department].append(rate)

    result = {}
    for dep, rates in department_dict.items():
        avg_rate = sum(rates) / len(rates)
        result[dep] = avg_rate

    return (result, 'average_rate_report')
