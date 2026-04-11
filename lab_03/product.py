# ========================================
# Szkielet pliku: product.py
# Uzupelnij implementacje!
# ========================================

class Product:
    """Reprezentuje produkt w sklepie internetowym."""

    def __init__(self, name: str, price: float, quantity: int):
        # TODO: Zapisz atrybuty name, price, quantity
        # Pamietaj o walidacji: price >= 0, quantity >= 0
        if price < 0 :
            raise ValueError("Cena nie może byc ujemna")
        if quantity < 0:
            raise ValueError("Ilosc nie może byc ujemna")
        
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount: int):
        # TODO: Dodaj ilosc do magazynu. Rzuc ValueError jesli amount < 0
        if amount < 0:
            raise ValueError("Ilosc w magazynie nie moze byc mniejsze niz 0")
        self.quantity += amount


    def remove_stock(self, amount: int):
        # TODO: Usun ilosc z magazynu.
        # Rzuc ValueError jesli amount < 0 lub amount > quantity
        if amount < 0 or amount > self.quantity:
            raise ValueError("Nieprawidlowa ilosc do usuniecia")
        self.quantity -= amount

    def is_available(self) -> bool:
        # TODO: Zwroc True jesli quantity > 0
        if self.quantity > 0:
            return True
        return False

    def total_value(self) -> float:
        # TODO: Zwroc price * quantity
        res = self.price * self.quantity
        return res

    def apply_discount(self, percent: float):
        if percent < 0 or percent > 100:
            raise "Obnizka musi byc podana w procentach od 0 do 100" 
        self.price = self.price * (1 - percent / 100)
    