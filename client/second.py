import json
import os.path

file_path = "settings.json"
user_settings = dict()

def userSetup(file_path):
    print("Первоначальная настройка системы. Пожалуйста введите все данные корректно!")
    user_settings['name'] = str(input("Введите ваше имя:"))
    user_settings['surname'] = str(input("Введите вашу фамилию:"))
    user_settings['form'] = str(input("Укажите класс в котором вы учитесь(Пример: 10Ж):"))
    with open(file_path, 'w') as f:
        json.dump(user_settings, f)
    print("Настройка завершена!")
