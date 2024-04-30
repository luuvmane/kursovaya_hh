from abc import ABC, abstractmethod
import requests


class AbstractAPI(ABC):
    @abstractmethod
    def get_response(self, text, per_page):
        pass

    @abstractmethod
    def get_vacancies(self, text, per_page):
        pass

    @abstractmethod
    def get_filter_vacansies(self, text, per_page):
        pass


class Headhunter(AbstractAPI):
    """Класс для работы с HH API"""
    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"

    def get_response(self, text: str, per_page: int):
        """Запрос на HH API"""
        params = {"text": text, "per_page": per_page}
        response = requests.get(self.__url, params=params)
        return response

    def get_vacancies(self, text: str, per_page: int = 20) -> list:
        """Получение вакансий"""
        vacancies = self.get_response(text, per_page).json()["items"]
        return vacancies

    def get_filter_vacansies(self, text: str, per_page: int = 20) -> list:
        """Фильтрация ключей для всех вакансий"""
        filter_vacancies = []
        vacancies = self.get_vacancies(text, per_page)
        for vacancy in vacancies:
            filter_vacancies.append({
                "name": vacancy["name"],
                "salary": vacancy["salary"],
                "url": vacancy["alternate_url"],
                "employer": vacancy["employer"]["name"]
            })
        return filter_vacancies
