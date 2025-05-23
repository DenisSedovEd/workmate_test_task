import json

from validate import Employee


def another_report(employees: list[Employee]) -> json:
    result: list = []
    for person in employees:
        person.payout = person.hours_worked * person.rate
        result.append(person.__repr__())
    the_result_of_the_report = json.dumps(result)
    return the_result_of_the_report
