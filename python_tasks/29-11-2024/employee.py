from person import Person

class Employee(Person):

    def __init__(
        self,
        name: str,
        age: int,
        dob: str,
        phone: str,
        gender: str,
        number: int,
        street: str,
        city: str,
        state: str,
        id: str,
        email: str,
        level: int
    ):
        super().__init__(name, age, dob, phone, gender, number, street, city, state)
        self.__id = id
        self.__email = email
        self.__level = level

    def __str__(self) -> str:
        return f"""
            {super().__str__()}
            ID: {self.__id}
            Email: {self.__email}
            Level: {self.__level}
        """