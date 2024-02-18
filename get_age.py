class AgeError(Exception):
    def __init__(self, age, message="Invalid age"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}: {self.age}'


def get_age():
    try:
        # Convert to integer and check if it's a valid number
        age = int(input("Input age: "))
    except ValueError:
        raise AgeError(age, "Age must be a number")

    return age


