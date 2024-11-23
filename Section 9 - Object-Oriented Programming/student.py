'''
student
'''

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house


    def __str__(self):
        return f"{self.name} from {self.house}"

    
    # Getter - gets some attributes
    @property
    def house(self):
        return self.house


    # Setter - sets some values
    house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravensclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.house = house



def main():
    student = get_student()
    student.house = "Number Four, Privet Drive"
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
    

if __name__ == "__main__":
    main()



'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house


    def __str__(self):
        return f"{self.name} from {self.house}"

    
    # Getter - gets some attributes
    def house(self):
        return self.house


    # Setter - sets some values
    def house(self, house):
        self.house = house



def main():
    student = get_student()
    student.house = "Number Four, Privet Drive"
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
    

if __name__ == "__main__":
    main()



class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house


    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    student.house = "Number Four, Privet Drive"
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
    

if __name__ == "__main__":
    main()



class Student:
    def __init__(self, name, house, patronous):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.patronous = patronous


    def __str__(self):
        return f"{self.name} from {self.house}"


    def charm(self):
        match self.patronous:
            case "Horse":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Dog":
                return "🐶"
            case "Cat":
                return "🐱"
            case _:
                return "🪄"


def main():
    student = get_student()
    print("Expecto patronum")
    print(student.charm())


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronous = input("Patronous: ")
    return Student(name, house, patronous)
    

if __name__ == "__main__":
    main()



class Student:
    def __init__(self, name, house, patronous):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.patronous = patronous

    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronous = input("Patronous: ")
    return Student(name, house, patronous)
    

if __name__ == "__main__":
    main()



class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house

    def __str__(self):
        return "a student"

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
    

if __name__ == "__main__":
    main()



class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
    

if __name__ == "__main__":
    main()



class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    try:
        return Student(name, house)
    except Value:
        ...

if __name__ == "__main__":
    main()



class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
    

if __name__ == "__main__":
    main()



class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student

if __name__ == "__main__":
    main()



class Student:
    def __init__(self):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student

if __name__ == "__main__":
    main()



class Student:
    ...


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

if __name__ == "__main__":
    main()



def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")

def get_student():
    student = {}
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()



def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    student = {}
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()



def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student

if __name__ == "__main__":
    main()



def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] == 'Ravenclaw'
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]

if __name__ == "__main__":
    main()



def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)

if __name__ == "__main__":
    main()



def main():
    name, house = get_student()
    print(f"{name} from {house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house

if __name__ == "__main__":
    main()



def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")

def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

if __name__ == "__main__":
    main()



def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")

def get_name():
    name = input("Name: ")
    return name



name = input("Name: ")
house = input("House: ")
print(f"{name} from {house}")
'''