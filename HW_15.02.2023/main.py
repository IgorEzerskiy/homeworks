import datetime


class Employee:
    def __init__(self, name: str, salary: float):  # salary for 1 work day
        self.name = name
        self.salary = salary

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}'

    def __gt__(self, other):
        return self.salary > other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __ne__(self, other):
        return self.salary != other.salary

    def work(self):
        return f'I come to the office'

    def check_salary(self, days=0):
        if days != 0:
            return self.salary * days
        first_md = datetime.date.today().replace(day=1)
        today = datetime.date.today()
        day_gen = (first_md + datetime.timedelta(x + 1) for x in range((today - first_md).days+1))
        return self.salary * sum(day.weekday() < 5 for day in day_gen)


class Developer(Employee):
    def __init__(self, name: str, salary: float, tech_stack: list):
        super().__init__(name, salary)
        self.tech_stack = tech_stack

    def __add__(self, other):
        name = self.name + ' ' + other.name
        tech_steck = set(self.tech_stack + other.tech_stack)
        if self.salary > other.salary:
            salary = self.salary
        else:
            salary = other.salary
        return Developer(name=name, salary=salary, tech_stack=list(tech_steck))

    def __gt__(self, other):
        return len(self.tech_stack) > len(other.tech_stack)

    def __lt__(self, other):
        return len(self.tech_stack) < len(other.tech_stack)

    def __ge__(self, other):
        return len(self.tech_stack) >= len(other.tech_stack)

    def __le__(self, other):
        return len(self.tech_stack) <= len(other.tech_stack)

    def __eq__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)

    def __ne__(self, other):
        return len(self.tech_stack) != len(other.tech_stack)

    def work(self):
        return f'I come to the office and start coding.'


class Recruiter(Employee):
    def work(self):
        return f'I come to the office and start hiring.'


if __name__ == '__main__':
    employee = Employee(name='Igor', salary=550.0)
    print(employee.work(), '\n')

    dev = Developer(name='Andriy', salary=1100.0, tech_stack=['JS', 'C++', 'Python'])
    dev2 = Developer(name='Maxim', salary=1200.0, tech_stack=['JS', 'C++', 'Python', 'React'])
    print(dev.__str__())
    print(dev.work(), '\n')

    recruiter = Recruiter(name='Irina', salary=500.0)
    recruiter1 = Recruiter(name='Sasha', salary=600.0)
    print(recruiter.__str__())
    print(recruiter.work(), '\n')

    print(f'__Recruiter to recruiter__'
          f'>: {recruiter1 > recruiter} \n'
          f'<: {recruiter1 < recruiter} \n'
          f'>=: {recruiter1 >= recruiter} \n'
          f'<=: {recruiter1 <= recruiter} \n'
          f'==: {recruiter1 == recruiter} \n'
          f'!=: {recruiter1 != recruiter} \n')

    print(f'Check salary with days: {dev.check_salary(days=12)}')
    print(f'Check salary with days: {dev.check_salary()}, \n')

    print(f'Salary {dev.__str__()} - {dev.check_salary(days=22)}')
    print(f'Salary {dev2.__str__()} - {dev2.check_salary(days=22)}')
    print(f'Salary {recruiter.__str__()} - {recruiter.check_salary(days=22)} \n')

    print(f'__Dev to Dev__ \n'
          f'>: {dev > dev2} \n'
          f'<: {dev < dev2} \n'
          f'>=: {dev >= dev2} \n'
          f'<=: {dev <= dev2} \n'
          f'==: {dev == dev2} \n'
          f'!=: {dev != dev2} \n')

    dev3 = dev.__add__(dev2)
    print(dev3.name, dev3.salary, dev3.tech_stack)