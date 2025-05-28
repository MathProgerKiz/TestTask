import argparse
from pathlib import Path

def validation_path(path_str):
    """Валидация путей"""
    path = Path(path_str)
    if path.exists():
        return path
    raise argparse.ArgumentTypeError(f"Путь {path_str} не существует")

def validation_report(report_str):
    """
    Валидация для отчетов, проверяем есть ли такой тип отчета

    :param report_str:
    :return:
    """
    current_dir = Path(__file__).parent.parent
    print(current_dir)
    reports_directory = current_dir / 'reports'
    expected_file = report_str if report_str.endswith('.py') else report_str + '.py'
    reports_name = [f.name for f in reports_directory.iterdir() if f.is_file()]

    if expected_file in reports_name:
        # Возвращаем имя без расширения
        return expected_file[:-3]  # отрезаем '.py'
    raise argparse.ArgumentTypeError(f"Отчёт '{report_str}' не найден в папке reports")


