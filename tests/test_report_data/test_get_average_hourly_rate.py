import pytest
from reports.average_hourly_rate_report import get_average_hourly_rate_per_department

def test_get_average_hourly_rate_per_department():
    """Тест на проверку валидности данных отчета по средней часовой ставке по отделам"""
    test_data = [
        ['id', 'email', 'name', 'department', 'hours_worked', 'hourly_rate'],
        ['1', 'alice@example.com', 'Alice Johnson', 'Marketing', '160', '50'],
        ['2', 'bob@example.com', 'Bob Smith', 'Design', '150', '40'],
        ['3', 'carol@example.com', 'Carol Williams', 'Design', '170', '60']
    ]
    
    result, report_name = get_average_hourly_rate_per_department(test_data) # Вызов тестируемой функции
    
    # Проверка базовой структуры
    assert report_name == 'average_rate_report'
    assert len(result) == 2  # Два отдела: Marketing и Design
    assert isinstance(result, dict)
    
    # Проверка Marketing
    assert 'Marketing' in result
    assert result['Marketing'] == 50.0  # 50 / 1
    
    # Проверка Design
    assert 'Design' in result
    assert result['Design'] == 50.0  # (40 + 60) / 2
    
    # Проверка типов данных и значений
    for dept, avg_rate in result.items():
        assert isinstance(dept, str)
        assert isinstance(avg_rate, float)
        assert avg_rate > 0 