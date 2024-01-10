import pickle
 
# Define a Python object
person = {
    "name": "Alice",
    "age": 30,
    "gender": "female"
}
 
# Pickle the object to a binary file
with open("person.pickle", "wb") as file:
    pickle.dump(person, file)
 
print("Pickling completed")