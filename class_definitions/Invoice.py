class Invoice:

    def __init__(self,invoiceid,customerid,lname,fname,phone,addr,items =''):

        self._inoviceID = invoiceid
        self._customerID = customerid
        self._last_name = lname
        self._first_name = fname
        self._phone_number = phone
        self._address = addr
        self._items_with_price = dict(items)
        self._total = 0

    def set_total(self):
        self._total = 0

    def add_item(self,item):
        self._items_with_price.update(item)

    def total_price (self,_items_with_price):
        for k,v in self._items_with_price():
            total = total + v
        return total

    def create_invoice(self):
        return str(self._items_with_price) + '\nTotal: ' + str(self._total)


# Driver code
invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802', 'Mouse', 'Minnie', '555-867-5309')
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
#print(invoice.display())
print(invoice.create_invoice())