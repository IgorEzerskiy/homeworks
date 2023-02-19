"""
Module contains main class Employee
"""
import datetime


class Employee:
    """
    Class Employee
    """
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
        """
        The method returns a message that the employee has come to the office.
        :return:
        """
        return 'I come to the office.'

    def check_salary(self, days=0):
        """
        This method counts the salary from the beginning of the month
        to the current date, excluding weekends.
        :param days:
        :return:
        """
        if days != 0:
            return self.salary * days
        first_md = datetime.date.today().replace(day=1)
        today = datetime.date.today()
        day_gen = (first_md + datetime.timedelta(x + 1) for x in range((today - first_md).days+1))
        return self.salary * sum(day.weekday() < 5 for day in day_gen)
