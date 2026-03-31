# Write your solution here
def add_student(dictionary:dict , name:str):
    dictionary[name]= []
    return dictionary

def print_student(dictionary: dict ,name:str):
    if name in dictionary and dictionary[name] == []:print(f"{name}:\n no completed courses")
    elif name in dictionary:
        mean = 0
        print(f"{name}:\n {len(dictionary[name])} completed courses:")
        for items in dictionary[name]:
            print(f"  {items[0]} {items[1]}")
        for items in dictionary[name]:
            mean += items[1]
        print(f" average grade {mean/len(dictionary[name])}")
    else:print(f"{name}: no such person in the database")

def add_course(dictionary: dict, name: str,course: tuple):
    if not course in dictionary[name]:
        for item in dictionary[name]:
            if item[0].lower() == course[0].lower():
                if item[1] < course[1]:
                    dictionary[name].remove(item)
                else:
                    return dictionary
    if course[1]==0:
        return dictionary
    else:
        dictionary.setdefault(name,[]).append(course)
    return dictionary

def summary(dictionary: dict):
    print("students",len(dictionary))
    course = []
    name = []
    grade = 0 
    eln = 0
    averge_grade =[]
    for student in dictionary:
        
        name.append(student)
        for item in dictionary[student]:
            eln += 1
            grade += item[1]
        grade /= eln 
        course.append(eln)
        averge_grade.append(grade)
        grade = 0
        eln = 0
    index1 , index2 = course.index(max(course)) , averge_grade.index(max(averge_grade))
    print(f"most courses completed {max(course)} {name[index1]}")
    print(f"best average grade {max(averge_grade)} {name[index2]}")
        
    





        









if __name__ == "__main__":
    students = {}
    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Software Development Methods", 4))
    add_course(students, "Emily", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students, "Peter", ("Models of Computation", 0))
    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students, "Peter", ("Introduction to Computer Science", 1))
    print_student(students, "Emily")
    print_student(students, "Peter")