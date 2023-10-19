# Define a class for a Person
class Person:
    def __init__(self, name, age, job=None):
        self.name = name
        self.age = age
        self.job = job
        self.connections = {}  # Dictionary to store relationships

    def add_connection(self, person, relation):
        """Add a connection to another person."""
        self.connections[person.name] = {"relation": relation, "person": person}
        # Assuming the relationship is reciprocal
        person.connections[self.name] = {"relation": relation, "person": self}

    def __repr__(self):
        return f"{self.name}, {self.age}, {self.job}, connections: {[person for person in self.connections]}"

# Create instances of the class
jill = Person("Jill", 26, "biologist")
zalika = Person("Zalika", 28, "artist")
john = Person("John", 27, "writer")
nash = Person("Nash", 34, "chef")

# Add connections
jill.add_connection(zalika, "friend")
jill.add_connection(john, "partner")
john.add_connection(jill, "partner")
john.add_connection(nash, "cousin")
nash.add_connection(zalika, "landlord")

# Print the persons
print(jill)
print(zalika)
print(john)
print(nash)
