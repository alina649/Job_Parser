import json

import requests
from abc import ABC
from pprint import pprint

from src.abstract_class_vacancy import AbstractVacancy


class HHruJob(AbstractVacancy):
    def __init__(self, keyword, count_vacancy):

        self.keyword = keyword
        self.count_vacancy = count_vacancy

        self.description = None
        self.salary_max = None
        self.salary_min = None
        self.link = None
        self.id = None
        self.title = None

    def __repr__(self):
        return f"{self.__class__.__name__}({self.keyword},{self.count_vacancy})"

    def atribute(self):
        """Создание атрибутыов для дальнейшей работы со значениями"""
        if self.site_connecting().status_code == 200:
            list_json = []
            data = self.site_connecting().json()
            for item in data['items']:
                self.title = item['name']
                self.id = item['id']
                self.link = item['alternate_url']

                if item['salary']:
                    self.salary_min = item['salary']['from']
                    self.salary_max = item['salary']['to']

                self.description = item['snippet']['requirement'] if item['snippet'] and 'requirement' in item[
                    'snippet'] else None

                list_job = {'id': self.id, 'title': self.title, 'link': self.link, 'salary_min': self.salary_min,
                            'salary_max': self.salary_max, 'description': self.description}

                list_json.append(list_job)
                self.to_json(list_json)
            return list_json

        else:
            return None

    def site_connecting(self):
        """Подключаемся к API hh_ry"""
        url = 'https://api.hh.ru/vacancies'
        params = {'text': self.keyword,  # Ключевое слово для поиска ваканчий
                  # 'area': 1,  # Индекс города для поиска 1(Москва)
                  'per_page': self.count_vacancy  # Кол-во вакансий на странице
                  }
        headers = {
            "User-Agent": "50355527",  # Replace with your User-Agent header
        }

        response = requests.get(url, params=params, headers=headers)
        return response

    def to_json(self, list_job):
        """Создание JSON файла с вакансиями"""
        with open('../data/hh_ry_python.json', 'w', encoding='utf-8') as file:
            json.dump(list_job, file, sort_keys=False, indent=4, ensure_ascii=False)

    def conclusion_in_humans(self):
        """Функция выводит на экран пользователя вакансии"""
        try:
            self.atribute()
            for i in self.atribute():
                print(f"Название:{i['title']} \n"
                      f"Ссылка:{i['link']} \n"
                      f"Зарплата: от {i['salary_min']} до {i['salary_max']} руб.\n"
                      f"Описание: {i['description']} \n")
        except TypeError:
            print('Ошибка в ответах')
