# Разработайте поиск учащихся
# в одном классе
# посещающих одну секцию.
# фильтрацию учащихся по их полу
# поиск ученика по имени

import json


def one_class(value):
    """Searching students who study in the same class"""
    with open("students.json", "r") as json_file:
        data = json.load(json_file)
        filtered = [s for s in data["student"] if s["Class"] == value]
        print(filtered)


def one_club(value):
    """Searching students who visit the same club"""
    with open("students.json", "r") as json_file:
        data = json.load(json_file)
        filtered = [s for s in data["student"] if s["Club"] == value]
        print(filtered)


def student_gender(value):
    """Filter list of students by their gender"""
    with open("students.json", "r") as json_file:
        data = json.load(json_file)
        filtered = [s for s in data["student"] if s["Gender"] == value]
        print(filtered)
        print(len(filtered), "persons")


# print(student_gender("W"))

def student_name(value):
    """Searching students in list by their name"""
    with open("students.json", "r") as json_file:
        data = json.load(json_file)
        filtered = [s for s in data["student"] if s["Name"] == value]
        print(filtered)


print(one_class("1b"))  # Output list of students who study in class "1b"
print()
print(one_club("Chess"))  # Output list of students who visit club "Chess"
print()
print(student_gender("W"))  # Output filter student by gender "W", female
print()
print(student_name("Koharu Hinata"))  # Output student datas by name "Koharu Hinata"
