"""
Module contains class Recruiter
"""
from employee_class import Employee


class Recruiter(Employee):
    """
    Class recruiter
    """
    def work(self):
        """
        The method returns a message that the recruiter has come to the office.
        :return:
        """
        return super().work()[:-1] + ' and start hiring.'
