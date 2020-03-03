import datetime
import re

class Student:
    __id = 1

    def __init__(self, FAMILY: str, NAME: str, MIIDDLENAME: str, DATE: str, ADRESS: str, TELEPHON:str, FACULTY:str, COURSE: int, GROUP: int):
        self.__student = {
            "family": FAMILY,
            "name": NAME,
            "middleName": MIIDDLENAME,
            "date": DATE,
            "adress": ADRESS,
            "telephon": TELEPHON,
            "faculty": FACULTY,
            "course": COURSE,
            "group": GROUP,
        }
        print("Студент создан")
        self.__student["id"] = self.__class__.__id
        self.__class__.__id += 1

    # def __setattr__(self, attr, value):
    #     if attr == 'id' or attr == 'family' or attr == 'name' or attr == 'middleName' or \
    #             attr == 'date' or attr == 'adress' or attr == 'telephone' or attr == "faculty" or \
    #             attr == "course" or attr == "group":
    #         self.__dict__[attr] = value
    #     else:
    #         raise AttributeError(attr + ' not allowed')

    def setName(self, Name: str):
        if type(Name) == str and len(Name) > 1:
            self.__student["name"] = Name
        else:
            print("Введены неверные данные. Информация не записана")

    def setTelephon(self, Telephon):
        if type(Telephon) == str and len(Telephon) == 11:
            self.__student["telephon"] = Telephon
        else:
            print("Введены неверные данные. Информация не записана")

    def getName(self):
        return self.__student["name"]

    def getTelephone(self):
        return self.__student["telephon"]




    def setGroup(self, Group: int):
        if type(Group) == int and Group <=20:
            self.__student["group"] = Group
        else:
            print("Введены неверные данные. Информация не записана")

    def getGroup(self):
        return self.__student["group"]

    def getDate(self):
        return self.__student["date"]
    def getFacult(self):
        return self.__student["faculty"]

    def getAge(self):
        '''function returns age'''
        lst = self.getDate().split(".")
        lst = [int(x) for x in lst]
        dt = datetime.datetime(lst[2], lst[1], lst[0])
        now = datetime.datetime.now()
        return ((now - dt).days // 365)

    def showInfo(self):
        '''function shows information'''
        for i, item in self.__student.items():
            print(str(i) + ': ' + str(item))

collection = [
    Student("Кравцова", "Диана", "Вячеславовна", "10.11.2001", "ул.Белорусская 21", "80297896325", "ФИТ", 2, 4),
    Student("Боженкова", "Екатерина", "Андреевна", "13.07.2001", "ул.Белорусская 19", "80297441171", "ТОВ", 2, 9),
    Student("Храмова", "Елизавета", "Сергеевна", "06.04.2001", "ул.Белорусская 19", "80444569856", "ФИТ", 2, 9),
    Student("Ожередова", "Полина", "Андреевна", "23.02.2001", "ул.Белорусская 21", "80291234567", "ФИТ", 2, 5),
    Student("Грамович", "Дана", "Геннадьевна", "13.05.2000", "ул.Белорусская 21 ", "80332416596", "ХТИТ", 2, 11),
]
n = int(input("Insert n:\n"))
query1 = [x for x in collection if x.getGroup() == n]
for i in query1:
    print(i.getName())
f = input("Введите факультет :\n")
query2 = [x for x in collection if x.getFacult() == f]
for i in query2:
    print(i.getName())
if len(query2) == 0:
    print("Факультет пуст  либо вы ввели неверный факультет")

print("Возраст студента Боженкова Екатерина:")
print(collection[2].getAge());
