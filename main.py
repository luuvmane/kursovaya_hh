from src.hh_api import Headhunter
from src.vacancy import Vacancy
from src.json_class import JSONSaver


hh = Headhunter()
vacancies = hh.get_filter_vacansies("python")


js = JSONSaver()
js.write_data(vacancies)
data = js.get_vacancies()
for elem in data:
    print(elem)
    print("-" * 20)