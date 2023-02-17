class Client:
    def __init__(self, name, city, balance):
        self.name = name
        self.city =city
        self.balance=balance

    def __str__(self):
        return f"{self.name}.{self.city}.Баланс:{self.balance} руб."
    def get_guest (self):
        return f"{self.name},г.{self.city}"


client_1=Client ("Иван Петров","Москва", 50)
print(client_1)

client_2= Client ("Константин Светлов","Сочи",55)
client_3= Client ("Людмила Пахомова","Новосибирск",40)

list_guests= [client_1,client_2, client_3]

for guest in list_guests:
    print(guest.get_guest())

