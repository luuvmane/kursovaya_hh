import json

def display_vacancies(vacancies):
    for vacancy in vacancies:
        print("Название вакансии:", vacancy["name"])
        if vacancy.get("salary"):
            print("Зарплата от:", vacancy["salary"]["from"])
            if vacancy["salary"].get("to"):
                print("Зарплата до:", vacancy["salary"]["to"])
            print("Валюта:", vacancy["salary"]["currency"])
        else:
            print("Зарплата: не указана")
        print("Ссылка на вакансию:", vacancy["url"])
        print("Работодатель:", vacancy["employer"])
        print("-" * 20)

def user_interface(vacancies):
    while True:
        print("1. Показать все вакансии")
        print("2. Показать вакансии с зарплатой от...")
        print("3. Показать вакансии с зарплатой до...")
        print("4. Показать вакансии в указанной валюте")
        print("5. Показать вакансии с ключевым словом в названии или описании")
        print("6. Сортировать вакансии")
        print("7. Выйти")

        choice = input("Выберите действие (1-7): ")

        if choice == "1":
            display_vacancies(vacancies)
        elif choice == "2":
            min_salary = int(input("Введите минимальную зарплату: "))
            filtered_vacancies = [vacancy for vacancy in vacancies if
                                  vacancy.get("salary") and vacancy["salary"].get("from") and vacancy["salary"][
                                      "from"] >= min_salary]
            display_vacancies(filtered_vacancies)
        elif choice == "3":
            max_salary = int(input("Введите максимальную зарплату: "))
            filtered_vacancies = [vacancy for vacancy in vacancies if
                                  vacancy.get("salary") and vacancy["salary"].get("to") and vacancy["salary"][
                                      "to"] <= max_salary]
            display_vacancies(filtered_vacancies)
        elif choice == "4":
            currency = input("Введите валюту (USD, RUR, EUR и т.д.): ").upper()
            filtered_vacancies = [vacancy for vacancy in vacancies if
                                  vacancy.get("salary") and vacancy["salary"].get("currency") == currency]
            display_vacancies(filtered_vacancies)
        elif choice == "5":
            keyword = input("Введите ключевое слово для поиска: ")
            keyword = keyword.lower()
            filtered_vacancies = [vacancy for vacancy in vacancies if keyword in vacancy["name"].lower() or (
                        vacancy.get("description") and keyword in vacancy["description"].lower())]
            display_vacancies(filtered_vacancies)
        elif choice == "6":
            sort_key = input("Выберите критерий сортировки (name, salary_from, salary_to): ")
            sorted_vacancies = sorted(vacancies, key=lambda x: x.get(sort_key) or float('inf'))
            display_vacancies(sorted_vacancies)
        elif choice == "7":
            print("До свидания!")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

filename = "../data/vacancies.json"
with open(filename, "r", encoding="utf-8") as f:
    vacancies_data = json.load(f)
user_interface(vacancies_data)

