# we can generate a nested dictionary by using a dictionary as a value for another dictionary
info = {
    "person1": {
        "name": "Alice",
        "age": 30
    },
    "person2": {
        "name": "Bob",
        "age": 25
    }
}
print(info) #output: {'person1': {'name': 'Alice', 'age': 30}, 'person2': {'name': 'Bob', 'age': 25}}   

#           accessing nested dictionary items
print(info["person1"]["name"]) #output: Alice
print(info["person1"]["age"])  #output: 30
print(info["person2"]["name"]) #output: Bob
print(info["person2"]["age"])  #output: 25

#           Modifying nested dictionary items
info["person1"]["age"] = 31
print(info) #output: {'person1': {'name': 'Alice', 'age': 31}, 'person2': {'name': 'Bob', 'age': 25}}   
