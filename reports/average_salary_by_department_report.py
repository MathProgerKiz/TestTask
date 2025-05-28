from core.field_mapping import get_formatted_file

from collections import defaultdict

def get_average_salary_by_department(file):
    """Средняя зарплата по отделам"""
    list_workers = get_formatted_file(file)

    department_dict = defaultdict(list)  # ключ — департамент, значение — список сотрудников

    for worker in list_workers:
        department = worker['department']
        # Преобразование в числовой формат
        hours = float(worker['hours_worked'])
        rate = float(worker['hourly_rate'])
        salary = hours * rate
        worker['salary'] = salary
        department_dict[department].append(worker)

    result = {}
    for dep, workers in department_dict.items():  # dep — это имя департамента (например, "Sales")
        total_salary = sum(w['salary'] for w in workers)
        avg_salary = total_salary / len(workers)
        result[dep] = avg_salary

    return (result, 'average_salary_by_department')
