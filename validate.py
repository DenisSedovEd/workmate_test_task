from dataclasses import dataclass

from list_of_parameters import possible_rates


@dataclass
class Employee:
    id: int
    name: str
    email: str
    department: str
    hours_worked: int
    rate: int
    payout: int = 0


# list1 = ["data1.csv", "data2.csv"]


def validate_data(list_of_files: list[str]) -> list | None:
    data = []
    for el in list_of_files:

        try:
            with open(el, "r") as f:
                tmp_data = f.readlines()
                headers = tmp_data[0].strip().split(",")
                index_id = headers.index("id")
                index_name = headers.index("name")
                index_email = headers.index("email")
                index_department = headers.index("department")
                index_hours_worked = headers.index("hours_worked")
                index_rate = headers.index(
                    next((key for key in possible_rates if key in headers), None)
                )
                for value in tmp_data[1:]:
                    list_value = value.strip().split(",")
                    person = Employee(
                        id=int(list_value[index_id]),
                        name=list_value[index_name],
                        email=list_value[index_email],
                        department=list_value[index_department],
                        hours_worked=int(list_value[index_hours_worked]),
                        rate=int(list_value[index_rate]),
                    )
                    data.append(person)
        except FileNotFoundError as e:
            print(f"{e}")

    return data


# validate_data(list1)
