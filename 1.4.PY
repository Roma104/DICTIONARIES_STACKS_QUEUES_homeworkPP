person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

print(person["name"])

print(person["hobby"])

for key, value in person.items():
   print(f"{key} : {value}")

person['surname'] ='Nowak'
person["married"] = False

person["gender"] = "male"
person['hobby'] = ["swimming","excursions","bicycle"]

#two ways to add a key value, 1.overwrite the whole thing;2.add just the new part
#person["phone"] = {"landline":"123444321","mobile":"777888999","work phone":"313131444"}
person["phone"]["work phone"] = "313131444"

for key, value in person.items():
   print(f"{key} : {value}")

