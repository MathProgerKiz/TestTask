import pytest
from reports.payout_report import get_payout_data

def test_get_payout_data():
    """Тест на проверку валидности данных отчета по выплатам"""
    test_data = [
        ['id', 'email', 'name', 'department', 'hours_worked', 'hourly_rate'],
        ['1', 'alice@example.com', 'Alice Johnson', 'Marketing', '160', '50'],
        ['2', 'bob@example.com', 'Bob Smith', 'Design', '150', '40'],
        ['3', 'carol@example.com', 'Carol Williams', 'Design', '170', '60']
    ]
    
    
    result, report_name = get_payout_data(test_data) # Вызов тестируемой функции
    
   
    assert report_name == 'payout'
    assert len(result) == 2  # Два отдела: Marketing и Design
    assert isinstance(result, dict)
    
   
    marketing_employees = result['Marketing']
    assert len(marketing_employees) == 1
    assert marketing_employees[0]['name'] == 'Alice Johnson'
    assert marketing_employees[0]['salary'] == 8000.0
    assert marketing_employees[0]['hours_worked'] == 160.0
    assert marketing_employees[0]['hourly_rate'] == 50.0
    assert marketing_employees[0]['email'] == 'alice@example.com'
    
   
    design_employees = result['Design']
    assert len(design_employees) == 2
    assert design_employees[0]['name'] == 'Bob Smith'
    assert design_employees[0]['salary'] == 6000.0
    assert design_employees[0]['hours_worked'] == 150.0
    assert design_employees[0]['hourly_rate'] == 40.0
    assert design_employees[0]['email'] == 'bob@example.com'
    
    assert design_employees[1]['name'] == 'Carol Williams'
    assert design_employees[1]['salary'] == 10200.0
    assert design_employees[1]['hours_worked'] == 170.0
    assert design_employees[1]['hourly_rate'] == 60.0
    assert design_employees[1]['email'] == 'carol@example.com'
    
    # Проверка типов данных
    for dept in result.values():
        for employee in dept:
            assert isinstance(employee['name'], str)
            assert isinstance(employee['email'], str)
            assert isinstance(employee['hours_worked'], float)
            assert isinstance(employee['hourly_rate'], float)
            assert isinstance(employee['salary'], float)
            assert employee['hours_worked'] > 0
            assert employee['hourly_rate'] > 0
            assert employee['salary'] > 0
            assert employee['salary'] == employee['hours_worked'] * employee['hourly_rate']
