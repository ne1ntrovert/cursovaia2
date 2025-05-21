from src.hh_api import HHGateway
from src.savers import JSONHandler
from src.utils import salary_threshold, sort_by_pay


def run_app():
    connector = HHGateway()
    storage = JSONHandler()

    term = input("Введите слово для поиска вакансий: ")
    amount = int(input("Сколько вакансий загрузить? (например, 10): "))
    min_pay = int(input("Минимальная зарплата для отбора: "))
    show_top = int(input("Сколько лучших показать?: "))

    jobs = connector.fetch(term, amount)
    storage.write(jobs)

    filtered_jobs = salary_threshold(jobs, min_pay)
    ordered_jobs = sort_by_pay(filtered_jobs)

    for job in ordered_jobs[:show_top]:
        print(job)


if __name__ == "__main__":
    run_app()
