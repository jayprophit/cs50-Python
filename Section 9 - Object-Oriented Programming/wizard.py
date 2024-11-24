'''
wizard
'''


class Wiizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    ...

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    ...


class Professor(Wizard):
    def __inti__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    ...


'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house

    ...


class Professor:
    def __inti__(self, name, subject):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.subject = subject

    ...



class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    ...


class Professor:
    def __inti__(self, name, subject):
        self.name = name
        self.subject = subject

    ...
'''