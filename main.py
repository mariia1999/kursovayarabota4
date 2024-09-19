from src.hh_api import HHapi
from src.vacancy_saver import JSONSaver
from utils.utils import print_vacancies, filter_vacancies, sort_vacancies, get_top_vacancies


def user_interaction():
    """
    Функция взаимодействия с пользователем для поиска, фильтрации и вывода вакансий с сайта HH.ru.
    """
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()

    # Создание экземпляра API и получение вакансий по поисковому запросу
    hh_api = HHapi()
    hh_vacancies = hh_api.get_vacancies(search_query)
    saver = JSONSaver()
    saver.write_data(hh_vacancies)
    print("Ответ API:", hh_vacancies)

    if hh_vacancies:
        vacancies_list = []

        for vac in hh_vacancies:
            print(vac.__dict__)
            vacancies_list.append(vac.__dict__)
        # Фильтрация, сортировка и выбор топ N вакансий
        print(vacancies_list)
        filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
        sorted_vacancies = sort_vacancies(filtered_vacancies)
        top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
        print_vacancies(top_vacancies)
    else:
        print("Не удалось получить вакансии. Пожалуйста, проверьте запрос и попробуйте снова.")


if __name__ == "__main__":
    user_interaction()
    print("Программа завершила выполнение.")