#           Dictionary is a collection of key-value pairs

intro = {
    "intro": "Tayyab",
    "age": 25,
    "city": "Lahore",
    "height": 5.4,
    "hobbies_list" : [  "coding", "reading", "traveling"],
    "brothers_tuple": ("Ali", "Ahmed", "Hassan")
}
print(intro) #output: {'intro': 'Tayyab', 'age': 25, 'city': 'Lahore', 'height': 5.4, 'hobbies_list': ['coding', 'reading', 'traveling'], 'brothers_tuple': ('Ali', 'Ahmed', 'Hassan')}

#          accessing introionary items

print(intro["intro"])  #output: Tayyab
print(intro["age"])   #output: 25
print(intro["city"])  #output: Lahore
print(intro["height"]) #output: 5.4
print(intro["hobbies_list"]) #output: ['coding', 'reading', 'traveling']
print(intro["brothers_tuple"]) #output: ('Ali', 'Ahmed', 'Hassan')

#          Modifying introionary items

intro["age"] = 26
print(intro) #output: {'intro': 'Tayyab', 'age': 26, 'city': 'Lahore', 'height': 5.4, 'hobbies_list': ['coding', 'reading', 'traveling']}

#          adding new key-value pair to the introionary

intro["country"] = "Pakistan"
print(intro) #output: {'intro': 'Tayyab', 'age': 26, 'city': 'Lahore', 'height': 5.4, 'country': 'Pakistan'}

#          removing a key-value pair from the introionary

del intro["country"]
print(intro) #output: {'intro': 'Tayyab', 'age': 26, 'city': 'Lahore', 'height': 5.4, 'hobbies_list': ['coding', 'reading', 'traveling']} 

#          introionary methods

print(intro.keys()) #output: intro_keys(['intro', 'age', 'city', 'height'])
print(intro.values()) #output: intro_values(['Tayyab', 26, 'Lahore', 5.4])
print(intro.items()) #output: intro_items([('intro', 'Tayyab'), ('age', 26), ('city', 'Lahore'), ('height', 5.4)]) 
print(intro.get("intro")) #output: Tayyab
print(intro.get("country", "Key not found")) #output: Key not found(since "country" key is not present in the introionary)
print(intro.pop("age")) #output: 26(removes the "age" key-value pair from the introionary and returns the value)
clear_intro = intro.copy() #creates a copy of the introionary
clear_intro.clear() #removes all key-value pairs from the copied introionary
print(clear_intro) #output: {}