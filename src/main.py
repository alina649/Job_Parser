from hh_ru import HHruJob
from super_job import SuperJob


def main():
    """Основная функция программы"""

    print("Добро пожаловать. Ддя поиска работы вам предооставленоы две платформы. Выберите одну из них\n")

    while True:
        while True:  # Проверка ответа пользователя
            choosing_platform = input("Введите 'H' или 'J' в зависимости от вашего выбора: \n"
                                      "'H' - hh.ru\n"
                                      "'J' - super_job\n")
            if choosing_platform == 'H' or choosing_platform == 'J':
                break
            else:
                print('Неверно введен символ выбора сайта')
                continue

        keyword = input('Введите название проффессии:  \n')
        city = input('Введите наименование вашего города: \n')
        count_vacancy = input('Введите количество ваканий: \n')

        if choosing_platform.lower() == 'h':
            keyword_and_city = str(keyword) + str(f' {city}')
            print("Ваши вакансии:")
            vacancy = HHruJob(keyword_and_city, count_vacancy)  # вызываем функцию для поиска с параметрами
            # пользователя (сайт HH_ru)
            print(vacancy.conclusion_in_humans())

        if choosing_platform.lower() == 'j':
            vacancy = SuperJob(keyword, city, count_vacancy)  # вызываем функцию для поиска с параметрами пользователя
            # (сайт super job)
            print("Ваши вакансии:")
            print(vacancy.conclusion_in_humans())

        while True:  # Цикл для проверки ответа
            end_search = input('Продолжить поиск? Да/нет.\n')
            if end_search.lower() == 'да':
                break
            elif end_search.lower() == 'нет':
                print('Поиск завершен.')
                exit()
            else:
                print('Ответ не верен.')
                continue


if __name__ == '__main__':
    main()
