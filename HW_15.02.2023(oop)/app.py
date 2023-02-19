"""
Enter point module
"""
from employee_class import Employee
from dev_class import Developer
from recruiter_class import Recruiter


if __name__ == '__main__':
    employee = Employee(name='Igor', salary=550.0)
    print(employee.work(), '\n')

    dev = Developer(name='Andriy', salary=1100.0, tech_stack=['JS', 'C++', 'Python'])
    dev2 = Developer(name='Maxim', salary=1200.0, tech_stack=['JS', 'C++', 'Python', 'React'])
    print(str(dev))
    print(dev.work(), '\n')

    recruiter = Recruiter(name='Irina', salary=500.0)
    recruiter1 = Recruiter(name='Sasha', salary=600.0)
    print(str(recruiter))
    print(recruiter.work(), '\n')

    print(f'__Recruiter to recruiter__\n'
          f'>: {recruiter1 > recruiter} \n'
          f'<: {recruiter1 < recruiter} \n'
          f'>=: {recruiter1 >= recruiter} \n'
          f'<=: {recruiter1 <= recruiter} \n'
          f'==: {recruiter1 == recruiter} \n'
          f'!=: {recruiter1 != recruiter} \n')

    print(f'Check salary with days: {dev.check_salary(days=12)}')
    print(f'Check salary with days: {dev.check_salary()}, \n')

    print(f'Salary {str(dev)} - {dev.check_salary(days=22)}')
    print(f'Salary {str(dev2)} - {dev2.check_salary(days=22)}')
    print(f'Salary {str(recruiter)} - {recruiter.check_salary(days=22)} \n')

    print(f'__Dev to Dev__ \n'
          f'>: {dev > dev2} \n'
          f'<: {dev < dev2} \n'
          f'>=: {dev >= dev2} \n'
          f'<=: {dev <= dev2} \n'
          f'==: {dev == dev2} \n'
          f'!=: {dev != dev2} \n')

    dev3 = dev + dev2
    print(dev3.name, dev3.salary, dev3.tech_stack)
