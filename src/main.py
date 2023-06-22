from hh_ru import HHruJob
from super_job import SuperJob


def main():
    print("Привет. Ддя поиска работы вам предооставленоы две платформы. Выберите одну из них\n")
    choosing_platform = input("Введите 'H' или 'J' в зависимости от вашего выбора: \n"
                              "'H' - hh.ru\n"
                              "'J' - super_job\n")
    keyword = input('Введите название проффессии:  \n')
    city = input('Введите наименование вашего города: \n')

    if choosing_platform == 'H':
        count_vacancy = input('Введите количество ваканий: \n')
        keyword_and_city = str(keyword) + str(f' {city}')
        print("Ваши вакансии")
        vacancy = HHruJob(keyword_and_city, count_vacancy)
        print(vacancy.conclusion_in_humans())

    if choosing_platform == 'J':
        count_vacancy = input('Введите количество ваканий: \n')
        vacancy = SuperJob(keyword, city, count_vacancy)
        print("Ваши вакансии")
        print(vacancy.conclusion_in_humans())

    else:
        print('Повторите запрос и правильно запишите Ваши ответы')


if __name__ == '__main__':
    main()
