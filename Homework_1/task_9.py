class Item:
    def __init__(self, name, price, weight):
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        if weight <= 0:
            raise ValueError("Вес товара должен быть больше нуля")
        self.name = name
        self.price = price
        self.weight = weight


class Parcel:
    def __init__(self, weight, distance=0):
        if weight <= 0:
            raise ValueError("Вес посылки должен быть больше нуля")
        if distance < 0:
            raise ValueError("Расстояние не может быть отрицательным")
        self.weight = weight
        self.distance = distance


class Delivery:
    name = "Доставка"

    def calculate_cost(self, parcel):
        raise NotImplementedError("Метод должен быть переопределен")


class CourierDelivery(Delivery):
    name = "Курьер"
    BASE = 200
    PER_KG = 50
    PER_KM = 10

    def calculate_cost(self, parcel):
        return self.BASE + self.PER_KG * parcel.weight + self.PER_KM * parcel.distance


class PostDelivery(Delivery):
    name = "Почта"
    BASE = 150
    PER_KG = 20

    def calculate_cost(self, parcel):
        return self.BASE + self.PER_KG * parcel.weight


class PickupDelivery(Delivery):
    name = "Самовывоз"

    def calculate_cost(self, parcel):
        return 0


class Order:
    def __init__(self, items, delivery, distance=0):
        if len(items) == 0:
            raise ValueError("В заказе нет товаров")
        self.items = items
        self.delivery = delivery
        self.distance = distance

    def total_weight(self):
        total = 0
        for item in self.items:
            total += item.weight
        return total

    def items_cost(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

    def delivery_cost(self):
        parcel = Parcel(self.total_weight(), self.distance)
        return self.delivery.calculate_cost(parcel)

    def total_cost(self):
        return self.items_cost() + self.delivery_cost()

    def print_info(self):
        print("Способ доставки:", self.delivery.name)
        print("Вес заказа:", self.total_weight(), "кг")
        print("Стоимость товаров:", self.items_cost())
        print("Стоимость доставки:", self.delivery_cost())
        print("Итого:", self.total_cost())
        print()


items = [Item("Книга", 500, 0.5), Item("Наушники", 3000, 0.3), Item("Чайник", 2500, 1.7)]

methods = [CourierDelivery(), PostDelivery(), PickupDelivery()]
for method in methods:
    order = Order(items, method, 12)
    order.print_info()

print("Проверка некорректных данных")
try:
    Item("Ошибка", 100, 0)
except ValueError as error:
    print("Ошибка:", error)
try:
    Parcel(-1, 5)
except ValueError as error:
    print("Ошибка:", error)
try:
    Parcel(1, -5)
except ValueError as error:
    print("Ошибка:", error)
try:
    Order([], PostDelivery())
except ValueError as error:
    print("Ошибка:", error)