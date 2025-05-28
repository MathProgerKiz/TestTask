import pytest
import json
import os
from converters.json_conventer import save_report_file_by_json

def test_save_report_file_by_json():
    """Тест на проверку валидности конвертации данных в JSON"""
  
    test_data = {
        'Marketing': [
            {
                'name': 'Alice Johnson',
                'email': 'alice@example.com',
                'hours_worked': 160,
                'hourly_rate': 50,
                'salary': 8000
            }
        ],
        'Design': [
            {
                'name': 'Bob Smith',
                'email': 'bob@example.com',
                'hours_worked': 150,
                'hourly_rate': 40,
                'salary': 6000
            },
            {
                'name': 'Carol Williams',
                'email': 'carol@example.com',
                'hours_worked': 170,
                'hourly_rate': 60,
                'salary': 10200
            }
        ]
    }
    
    # Вызов тестируемой функции
    filename = save_report_file_by_json(test_data, 'test_report')
    
    
    assert os.path.exists(filename)  # Создан ли файл ?
    assert filename.endswith('.json')  
    
    # Читаем файл
    f = open(filename, 'r', encoding='utf-8')
    loaded_data = json.load(f)
    f.close()
        
    
    assert isinstance(loaded_data, dict)
    assert len(loaded_data) == 2  # Два отдела
    
    
    assert 'Marketing' in loaded_data
    marketing_data = loaded_data['Marketing']
    assert len(marketing_data) == 1
    assert marketing_data[0]['name'] == 'Alice Johnson'
    assert marketing_data[0]['salary'] == 8000
    
    
    assert 'Design' in loaded_data
    design_data = loaded_data['Design']
    assert len(design_data) == 2
    assert design_data[0]['name'] == 'Bob Smith'
    assert design_data[0]['salary'] == 6000
    assert design_data[1]['name'] == 'Carol Williams'
    assert design_data[1]['salary'] == 10200
    
    
    os.remove(filename) 