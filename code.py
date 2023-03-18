salary = 200000
name = "Прокопий"
print(f"У сотрудника {name} зарплата {salary} в месяц и {salary*12} в год")

employee = {"salary": 200000,"name" : "Прокопий"}
print(f"У сотрудника {employee['name']} зарплата {employee['salary']} в месяц и {salary*12} в год")
employees_list = [
        {
        'name': 'Данил',
        'salary': 200000,
    },
    {
        'name': 'Олег',
        'salary': 150000,
    },
    {
        'name': 'Иван',
        'salary': 180000,
    }
    ]

print(employees_list[0])

for emp in employees_list:
     print(f"У сотрудника {emp['name']} зарплата {emp['salary']} в месяц и {emp['salary']*12} в год")   

employees_list.append(employee)

print(f'Кол-во сотрудников в отделе: {len(employees_list)}')

class Employee:
    def __init__(self, name, salary, on_vacation = False, is_good_employee = True):
        self.name = name
        self.salary = salary
        self.on_vacation = on_vacation
        self.is_good_employee = is_good_employee
    def get_info(self):
        return f'У {self.name} зарплата в месяц = {self.salary}. В отпуске? - {self.on_vacation}'
 
employees = [Employee('Данил', 200000), Employee('Никита', 250000,True,False), Employee('Ваня', 150000)]

for employee in employees:
    print(employee.get_info())
print(f'Кол-во сотрудников в отделе: {len(employees)}')
l = []
for i in range(len(employees)):
    if employees[i].is_good_employee == False: l.append(i)
for i in l:
    del(employees[i])
print(f'Кол-во сотрудников в отделе: {len(employees)}')
