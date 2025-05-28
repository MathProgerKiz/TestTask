
from core.field_mapping import get_formatted_file


def get_payout_data(file):

    list_workers = get_formatted_file(file)

    department_dict = {}

    for worker in list_workers:
        department = worker['department']
        if department not in department_dict:
            department_dict[department] = []
        # Преобразование в числовой формат
        hours = float(worker['hours_worked'])
        rate = float(worker['hourly_rate'])
        salary = hours * rate
        # Добавляем поле зарплаты
        worker['salary'] = salary

        worker_data = {
            'name': worker['name'],
            'email': worker['email'],
            'hours_worked': hours,
            'hourly_rate': rate,
            'salary': salary
        }
        department_dict[department].append(worker_data)

    return (department_dict, 'payout')