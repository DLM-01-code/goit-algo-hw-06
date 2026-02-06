from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit():
            raise ValueError("Phone number must contain only digits")
        if len(value) != 10:
            raise ValueError("Phone number must be 10 digits long")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.phones.remove(phone_obj)
        else:
            raise ValueError("Phone not found")

# Исправлен код. Добавлена проверка на существование телефона

    def edit_phone(self, old_phone: str, new_phone: str): 
        phone_obj = self.find_phone(old_phone)
        if not phone_obj:
            raise ValueError("Phone not found")
        self.add_phone(new_phone)
        self.remove_phone(old_phone) 

    def find_phone(self, phone: str):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        return self.data.get(name, None)

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError("Record not found")

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())

print(":3"*5 + " " "Hi! I'm AddressBook" " " + ":3"*5)
print("") 
ad = AddressBook()

r1 = Record("Ala")
r1.add_phone("1234567890")
ad.add_record(r1)

r2 = Record("Bob")
r2.add_phone("0987654321")
ad.add_record(r2)

print(f"="*5 + "AddressBook" + "="*5)
print(ad)

r1.add_phone("2818384912")
print("\n=== After adding another phone to Ala ===")
print(ad)

r1.edit_phone("1234567890", "4837838345")
print("\n=== After editing Ala's phone ===")
print(ad)

r1.remove_phone("4837838345")
print("\n=== After removing Ala's phone ===")
print(ad)

found = ad.find("Ala")
print("\n=== Found Ala ===")
print(found)

not_found = ad.find("Charlie")
print("\n=== Found Charlie ===")
print(not_found if not_found else "Not found")