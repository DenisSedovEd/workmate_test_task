import json

from validate import Employee


def print_report(list_of_employees: json) -> None:
    print(json.loads(list_of_employees, indent=4))


def payout_report(employees: list[Employee]) -> json:
    result: list = []
    for person in employees:
        person.payout = person.hours_worked * person.rate
        result.append(person.__repr__())
    return result
