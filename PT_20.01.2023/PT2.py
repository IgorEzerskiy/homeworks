student = {"Igor Ezerskiy": [],
           "Vasia Pupkin": [],
           "Oleg Fomenko": [],
           "Ilia Gorban": []}
student_list_first = []


def more(a: dict) -> list:
    student_list = []
    for k, v in a.items():
        if len(v) >= 2:
            student_list.append(k)
    return student_list


def no_front_end(a: dict) -> list:
    student_list = []
    true_fornt_end = False
    for k, v in a.items():
        for i in v:
            if i == "FrontEnd":
                true_fornt_end = True
                break
        if true_fornt_end is False:
            if k not in student_list:
                student_list.append(k)
        true_fornt_end = False
    return student_list


def python_or_java(a: dict) -> list:
    student_list = []
    for k, v in a.items():
        for i in v:
            if (i == "Python") or (i == "Java"):
                if k not in student_list:
                    student_list.append(k)
    return student_list


for k, v in student.items():
    print("Student - ", k)
    specialyti_amount = int(input("Write amount of speciality: "))
    while len(student_list_first) < specialyti_amount:
        i = input("Write speciality of this student: ")
        student_list_first.append(i)
    student[k] += student_list_first
    student_list_first.clear()
    print("\n")

print("Student who studing more: ", more(student))
print("Student who don't studing at FrontEnd: ", no_front_end(student))
print("Student who studing at Python or Java: ", python_or_java(student))
