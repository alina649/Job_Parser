import json
import os

import requests
from abc import ABC
from pprint import pprint

from src.abstract_class_vacancy import AbstractVacancy


class SuperJob(AbstractVacancy):

    def __init__(self, keyword=str, town_person=str):
        self.list_json = []

        self.town_person = town_person
        self.keyword = keyword
        self.count = 0
        self.api_key = None

        self.description = None
        self.salary_max = None
        self.salary_min = None
        self.link = None
        self.id = None
        self.title = None
        self.town = None

    def __repr__(self):
        return f"{self.__class__.__name__}({self.keyword}, {self.town_person})"

    def atribute(self):
        """Создание атрибутыов для дальнейшей работы со значениями"""
        if self.site_connecting().status_code == 200:
            data = self.site_connecting().json()
            for item in data['objects']:
                self.title = item['profession']
                self.id = item['id']
                self.link = item['link']

                if item['payment_from']:
                    self.salary_min = item['payment_from']
                    self.salary_max = item['payment_to']

                self.description = item['candidat']
                self.town = item['town']['title']

                list_job = {'id': self.id, 'title': self.title, 'link': self.link, 'salary_min': self.salary_min,
                            'salary_max': self.salary_max, 'description': self.description, 'town': self.town}

                self.list_json.append(list_job)
                self.to_json(self.list_json)
            return self.list_json

        else:
            return None

    def site_connecting(self):
        """Подключаемся к API super_job_ry"""
        api_key: str = os.getenv('SJ_API_KEY')
        params = {"town": self.town_person,  # количество вакансий
                  "page": None,
                  "keyword": self.keyword, "archive": False, }
        headers = {
            'Host': 'api.superjob.ru',
            'X-Api-App-Id': api_key,
            'Authorization': 'Bearer r.000000010000001.example.access_token',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=headers, params=params)
        return response

    def to_json(self, list_job):
        """Создание JSON файла с вакансиями"""
        with open('sj_python.json', 'w', encoding='utf-8') as file:
            json.dump(list_job, file, sort_keys=False, indent=4, ensure_ascii=False)

    def conclusion_in_humans(self):
        """Функция выводит на экран пользователя вакансии"""
        self.atribute()
        a = 0
        for i in self.atribute():
            if str(self.town_person) == str(i['town']):
                a += 1
                print(f"{a}. Город:{i['town']} \n"
                      f"Название:{i['title']} \n"
                      f"Ссылка:{i['link']} "
                      f"Зарплата: от {i['salary_min']} до {i['salary_max']} руб.\n"
                      f"Описание: {i['description']} \n")
        if a == 0:
            print('По ващему запросу ничего не найдено')
