class Employee:

    # Constructor
    def __init__(self, lname, fname,addr,phone,salaried,start_date,salary):

        def set_hourly_or_salary(self, _salaried, _salary):
            if self._salaried == True:
                self._payment = "Salaried employee: $" + str(self._salary) + "/year"
            else:
                self._payment = "Hourly employee paid at $" + str(self._salary) + "/hour"
            return self._payment

        self._last_name = lname
        self._first_name = fname
        self._home_address = addr
        self._home_phone = phone
        self._salaried = salaried
        self._start_date = start_date
        self._salary = salary
        self._payment = set_hourly_or_salary(self,salaried,salary)


    def set_last_name(self, lname):
        self._last_name = lname

    def set_first_name(self, fname):
        self._first_name = fname

    def set_home_address(self,addr):
        self._home_address = addr

    def set_home_phone(self,phone):
        self._home_phone = phone

    def set_salaried(self,salaried):
        self._salaried = salaried

    def set_start(self,start_date):
        self._start_date = start_date

    def set_salary(self,salary):
        self._salary = salary


    def change_first_name(self,fname):
        self._first_name = fname


    def display(self):
        return str(self._first_name) + " " + str(self._last_name) + '\n' + str(self._home_address) + '\nPhone: ' + str(self._home_phone) + '\n' + str(self._payment) + '\nStart Date: ' + str(self._start_date)

# Driver
emp = Employee('Ruiz', 'Matthew', '111 nw 35th street',"(515)555-5555",False,'1/1/2020',7.75)   # call the construtor, needs to have a first and last name in parameter
emp.change_first_name('Matt')
print(emp.display())                # display returns a str, so print the information

del emp                             # clean up!