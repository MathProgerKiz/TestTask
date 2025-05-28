import pytest
from reports.average_salary_by_department_report import get_average_salary_by_department

def test_get_average_salary_by_department():
    """Тест на проверку валидности данных отчета по средней зарплате по отделам"""
    test_data = [
        ['id', 'email', 'name', 'department', 'hours_worked', 'hourly_rate'],
        ['1', 'alice@example.com', 'Alice Johnson', 'Marketing', '160', '50'],
        ['2', 'bob@example.com', 'Bob Smith', 'Design', '150', '40'],
        ['3', 'carol@example.com', 'Carol Williams', 'Design', '170', '60']
    ]
    
    result, report_name = get_average_salary_by_department(test_data) # Вызов тестируемой функции
    
    # Проверка базовой структуры
    assert report_name == 'average_salary_by_department'
    assert len(result) == 2  # Два отдела: Marketing и Design
    assert isinstance(result, dict)
    
    # Проверка Marketing
    assert 'Marketing' in result
    assert result['Marketing'] == 8000.0  # (160 * 50) / 1
    
    # Проверка Design
    assert 'Design' in result
    assert result['Design'] == 8100.0  # ((150 * 40) + (170 * 60)) / 2
    
    # Проверка типов данных и значений
    for dept, avg_salary in result.items():
        assert isinstance(dept, str)
        assert isinstance(avg_salary, float)
        assert avg_salary > 0
