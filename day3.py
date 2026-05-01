phonebook = {
    "Amit": 9876543210,
    "Riya" :9123456780
}
print(phonebook)
def addcontact(name,phone):
    if name in phonebook:
        print("contact already exists")
    else:
      phonebook[name] = phone

addcontact("suman",985632147)

print(phonebook)

def searchcontact(name):
    if name in phonebook:
        print(phonebook[name])
    else:
        print("contact not found")

def deletecontact(name):
    if name in phonebook:
        del phonebook[name]

    else:
        print("contact not find")

searchcontact("Amit")
deletecontact("suman")
print(phonebook)

def partialsearch(chunk):
    for name in phonebook:
        if chunk in name:
            print(name)
        

partialsearch("Am")