class Item:

    def __init__(self, name, price):
        self._name = name
        self.set_price(price)

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def set_price(self, price):
        if price <= 0:
            raise ValueError("Price cannot be 0 or less")
        self._price = price


class TaxableItem(Item):

    def __init__(self, name, price, tax_rate):
        super().__init__(name, price)
        # not a fan of this, because you have to use self
        # Item.__init__(self, name, price)
        self.set_tax_rate(tax_rate)

    def set_tax_rate(self, tax_rate):
        if tax_rate >= 1:
            self._tax_rate = tax_rate / 100
        elif tax_rate > 0:
            self._tax_rate = tax_rate
        else:
            raise ValueError("Tax rate cannot be 0 or less")

    def get_price(self):
        return super().get_price() * (self._tax_rate + 1)
        #return Item.get_price(self) * (self._tax_rate + 1)

chips = Item("Chips", 1.5)
soap = TaxableItem("soap", 2, .06)

print(f'{chips.get_name()} cost: ${chips.get_price()}')
print(f'{soap.get_name()} cost: ${soap.get_price()}')

