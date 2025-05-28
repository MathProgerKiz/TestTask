import pytest
from pathlib import Path
from core.arg_validation import validation_path, validation_report
import argparse

def test_validation_path():
    """Тест валидации пути"""
    # Создаем тестовый файл
    test_file = Path('test_file.txt')
    test_file.touch()
    
    # Проверяем что путь существует и возвращается корректное значение
    result = validation_path(str(test_file))
    assert result == test_file
    
    # Очистка
    test_file.unlink()

def test_validation_path_invalid():
    """Тест невалидных путей"""
    # Проверка несуществующего файла
    with pytest.raises(argparse.ArgumentTypeError) as exc_info:
        validation_path("non_existent_file.txt")
    assert "не существует" in str(exc_info.value)

    # Проверка некорректного формата пути
    with pytest.raises(argparse.ArgumentTypeError) as exc_info:
        validation_path("invalid/path/*/file.txt")
    assert "не существует" in str(exc_info.value)

def test_validation_report_valid():
    """Валидный отчет"""
    report_name = 'payout_report'
    result = validation_report(report_name)

    assert result == report_name

def test_validation_report_invalid():
    """Невалидный отчет"""
    report_name = 'non_existent_report'
    with pytest.raises(argparse.ArgumentTypeError) as exc_info:
        validation_report(report_name)  