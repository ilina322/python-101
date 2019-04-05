class Bill:
    money_holder = {}

    def __init__(self, amount):
        self.validate_init_data(amount)
        self.amount = amount
        if self.amount in self.money_holder:
            self.money_holder[self.amount] += 1
        else:
            self.money_holder[self.amount] = 1

    def validate_init_data(self, data):
        if data is int:
            print("data is valid!")

    def __int__(self):
        return self.amount

    def __str__(self):
        return 'A '+ str(self.amount) + '$ bill!'

    def __repr__(self):
        return str(self.amount) #'10'
        #return __str__(self) #A 10$ bill!

    def __eq__(self, other_bill):
        if self.amount == other_bill.amount:
            return True
        return False

    def get_amount(self):
        return self.amount



class BatchBill:
    def __init__(self, bills):
        self.validate_init_data(bills)
        self.bills = bills

    def validate_init_data(self, data):
        for element in data:
            if isinstance(element, Bill):
                continue
            else:
                raise Exception("Error!")

    def __len__(self):
        return len(self.bills)

    def get(self, index):
        return self.bills[index]

    def total(self):
        return sum([bill.get_amount() for bill in self.bills])

class CashDesk:
    current_sum = 0
    report = {}

    def take_money(self,money):
        if isinstance(money, Bill):
            self.current_sum += money.get_amount()
            self.add_bill_to_report(money)
        if isinstance(money, BatchBill):
            self.current_sum += money.total()
            for i in range(len(money)):
                self.add_bill_to_report(money.get(i))

    def add_bill_to_report(self, bill):
        if bill.get_amount() in self.report:
            self.report[bill.get_amount()] += 1
        if bill.get_amount() not in self.report:
            self.report[bill.get_amount()] = 1

    def total(self):
        return current_sum

    def inspect(self):
        message = 'We have a total of ' + str(self.current_sum) + '$ in the desk\nWe have the following count of bills:'
        for key, value in self.report.items():
            message += '\n' + str(key) + ': ' +str(value)

        return message


def main():
    bill1 = Bill(10)
    bill2 = Bill(10)
    bill3 = Bill(20)
    bill4 = Bill(50)

    print(Bill.money_holder)

    bills = [bill1, bill2, bill3]
    batchBill= BatchBill(bills)
    print(str(batchBill.get(0)))
    print(BatchBill.total(batchBill))

    cashDesk = CashDesk()
    cashDesk.take_money(bill4)
    print(CashDesk.report)
    cashDesk.take_money(batchBill)
    print(CashDesk.report)
    print(cashDesk.inspect())

if __name__ == '__main__':
    main()
