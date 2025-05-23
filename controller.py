from validate import validate_data
from reports_templates.payout import payout_report, print_report
from reports_templates.another_report import another_report


def controller(list_of_files: list[str], report_name: str) -> None:
    for el in list_of_files:
        if not el.endswith(".csv"):
            print("Неправильно указан исходный файл.")
            print("Проверьте имя файла или его расширение. Допускаются файлы .csv")
            raise FileNotFoundError
    data_set = set(list_of_files)
    data_list = validate_data(list(data_set))
    match report_name:
        case "payout":
            processed_data = payout_report(data_list)
            print_report(processed_data)
        case "another_report":
            another_report(data_list)
