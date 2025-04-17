from animal_shelter import AnimalShelter

# Create the object from the class
shelter = AnimalShelter("myUserAdmin", "trinidad1")
data = {"age_upon_outcome": "1.7 years", "animal_type": "Cat"}

if shelter.create(data):  # Ensure create() returns True/False
    print("Animal added")
else:  # Fix indentation
    print("Error")

# Print the value of the created record by reading it back from the database
print(shelter.read(data))
