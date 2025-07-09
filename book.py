from datetime import datetime, timedelta
from collections import UserDict
from schema import Name, Phone, Birthday

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_birthday(self, input_date):
        date = Birthday(input_date)
        self.phones.append(date)
   
    def add_phone(self, number):
        phone = Phone(number)
        self.phones.append(phone)

    def remove_phone(self, phone):
        fined = self.find_phone(phone)
       
        if fined:
            self.phones.remove(fined)
        else:
            raise ValueError(f"Phone number {phone} not found in record.")

    def edit_phone(self, old_number, new_number):
        updated = Phone(new_number) 
        
        fined = self.find_phone(old_number)
        if fined:
            index = self.phones.index(fined)
            self.phones[index] = updated
        else:
            raise ValueError(f"Phone number {old_number} not found for editing.")

    def find_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                return phone
        return None

    def __str__(self):
        phones = '; '.join(p.value for p in self.phones)
        birthday = f", birthday: {self.birthday.value}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phones}{birthday}"

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            print(f"Contact with name '{name}' not found.")
   
    def get_upcoming_birthdays(self):
        result = []
        today = datetime.today().date()
        endDate = today + timedelta(days=7)

        for record in self.data.values():
            if record.birthday:
                bday = datetime.strptime(record.birthday.value, "%d.%m.%Y").date()
                currentYearB = bday.replace(year=today.year)
                if currentYearB < today:
                    currentYearB = bday.replace(year=today.year + 1)
                if today <= currentYearB < endDate:
                    congratsDate = currentYearB
                    if congratsDate.weekday() == 5:
                        congratsDate += timedelta(days=2)
                    elif congratsDate.weekday() == 6:
                        congratsDate += timedelta(days=1)
                    result.append({
                        "name": record.name.value,
                        "congratulation_date": congratsDate.strftime("%d.%m.%Y")
                    })
        return result




