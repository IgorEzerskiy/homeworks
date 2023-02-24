"""
Module contains class Developer
"""
from employee_class import Employee


class Developer(Employee):
    """
    Class Developer
    """
    def __init__(self, name: str, salary: float, email: str, tech_stack: list):
        super().__init__(name, salary, email)
        self.tech_stack = tech_stack

    def __add__(self, other):
        name = self.name + ' ' + other.name
        tech_steck = set(self.tech_stack + other.tech_stack)
        if self.salary > other.salary:
            salary = self.salary
        else:
            salary = other.salary
        return Developer(name=name, salary=salary, email='', tech_stack=list(tech_steck))

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
        """
        The method returns a message that the developer has come to the office.
        :return:
        """
        return super().work()[:-1] + ' and start coding.'
