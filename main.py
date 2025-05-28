import argparse

from converters.json_conventer import save_report_file_by_json
from core.arg_validation import validation_path, validation_report
from reports.average_hourly_rate_report import get_average_hourly_rate_per_department
from reports.average_salary_by_department_report import get_average_salary_by_department
from reports.payout_report import get_payout_data

parser = argparse.ArgumentParser(description='аргументы запуска скрипта')

parser.add_argument("paths",
                    type=validation_path,
                    nargs="+",
                    help="Список входных файлов"
                    )

parser.add_argument('--report',
                    type=validation_report
                    )

parser.add_argument(
    "--format",
    type=str,
    choices=["json", "pdf", "docx"],  # Примеры выходных форматов
    default="json",
    help="Формат выходного файла (json, pdf, csv). По умолчанию: json"
)

reports_list = {'payout_report': get_payout_data,  # метод для отчета по зарплатам
                'average_salary_by_department_report': get_average_salary_by_department,  # средняя зарплата по отделам
                'average_hourly_rate_report': get_average_hourly_rate_per_department
                # средняя часовая ставка по отделам
                # Можно добавить методы
                }  # Список всех отчетов , при желании можно легко добавить

converters_method_list = {
    'json': save_report_file_by_json,
    # Можно добавить еще выходные форматы
}

args = parser.parse_args()

report_type = args.report  # Тип отсчета например payout_report
report_format = args.format  # формат выходных данных
path_object = args.paths  # список объектов Path

files = []
for path in path_object:
    try:
        content = path.read_text(encoding="utf-8")
        lines = content.splitlines()
        # Преобразуем строки в списки полей
        rows = [line.split(',') for line in lines]
        files.append(rows)
    except Exception as e:
        print(f"Ошибка при чтении файла {path}: {e}")
print(files)

report_method = reports_list[report_type]

for i in range(len(files)):
    report_data, report_name = report_method(files[i])
    converters_method_list[report_format](report_data, report_name)
print('УРАА')