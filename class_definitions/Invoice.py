class Invoice:

    def __init__(self,invoiceid,customerid,lname,fname,phone,addr,items =''):

        self._inoviceID = invoiceid
        self._customerID = customerid
        self._last_name = lname
        self._first_name = fname
        self._phone_number = phone
        self._address = addr
        self._items_with_price = dict()
        self._total = 0
        self._tax = 0
        self._total_with_tax = 0

    def set_total(self):
        self._total = 0

    def set_items_with_price(self,_items_with_price):
        self._items_with_price = dict()

    def add_item(self,item):
        self._items_with_price.update(item)

    def total_price (self):
        for v in self._items_with_price:
            self._total += self._items_with_price.get(v)

    def calc_tax(self):
        self._tax = self._total * .06
        self._tax = round(self._tax,2)

    def total_with_tax(self):
        self._total_with_tax = self._total + self._tax

    def create_invoice(self):
        return str(self._items_with_price) + '\nTotal before tax: ' + str(self._total) + '\nTax: ' + str(self._tax) + '\nTotal: '  + str(self._total_with_tax)


# Driver code
invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802', 'Mouse', 'Minnie', '555-867-5309')
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.total_price()
invoice.calc_tax()
invoice.total_with_tax()
print(invoice.create_invoice())

