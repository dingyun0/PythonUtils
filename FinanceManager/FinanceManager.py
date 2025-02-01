import csv
from datetime import datetime
class Transaction:
    def __init__(self,amount,category,date=None,transaction_type="expense"):
        self.amount=amount
        self.category=category
        self.date=date if date else datetime.now().strftime("%Y-%m-%d")
        self.transaction_type=transaction_type
    
    def __str__(self):
        return f"{self.date} - {self.transaction_type} - {self.category}: {self.amount}"


class FinanceManager:
    def __init__(self,filename="transactions.csv"):
        self.filename=filename
        self.transactions=[]
        self.load_data()

    def add_transaction(self,transaction):
        self.transactions.append(transaction)
        self.save_data()

    def load_data(self):
        try:
            with open(self.filename,mode="r",newline="")as file:
                reader=csv.reader(file)
                next(reader)
                for row in reader:
                    date,transaction_type,category,amount=row
                    amount=float(amount)
                    self.transactions.append(Transaction(amount,category,date,transaction_type))
        except FileNotFoundError:
            pass

    def save_data(self):
        with open(self.filename,mode="w",newline="") as file:
            writer=csv.writer(file)
            writer.writerow(["Date", "Type", "Category", "Amount"])
            for transaction in self.transactions:
                writer.writerow([transaction.date, transaction.transaction_type, transaction.category, transaction.amount])

    def get_total_income(self):
        """获取总收入"""
        return sum(t.amount for t in self.transactions if t.transaction_type == "income")

    def get_total_expense(self):
        """获取总支出"""
        return sum(t.amount for t in self.transactions if t.transaction_type == "expense")

    def get_balance(self):
        """计算账户余额"""
        return self.get_total_income() - self.get_total_expense()

    def generate_report(self):
        """生成收支报表"""
        income = self.get_total_income()
        expense = self.get_total_expense()
        balance = self.get_balance()

        report = f"Income: {income}\n"
        report += f"Expense: {expense}\n"
        report += f"Balance: {balance}\n"
        categories = {}
        for t in self.transactions:
            if t.category not in categories:
                categories[t.category] = {"income": 0, "expense": 0}
            if t.transaction_type == "income":
                categories[t.category]["income"] += t.amount
            else:
                categories[t.category]["expense"] += t.amount

        report += "\nCategory Breakdown:\n"
        for category, values in categories.items():
            report += f"{category}: Income - {values['income']}, Expense - {values['expense']}\n"

        return report


def main():
    finance_manager=FinanceManager()
    # 添加4条记录
    finance_manager.add_transaction(Transaction(5000,"Salary",transaction_type="income"))
    finance_manager.add_transaction(Transaction(1000,"Freelance",transaction_type="expense"))

    finance_manager.add_transaction(Transaction(2000,"Rent",transaction_type="expense"))
    finance_manager.add_transaction(Transaction(300,"Groceries",transaction_type="expense"))

    report=finance_manager.generate_report()
    print(report)

if __name__=="__main__":
    main()
