# Create class category that instantiate objects like food, clothing, ent and variable ledger
# the same class should have methods deposit, withdraw, get_balance, transfer, check_funds
# return should be a title line of 30 chars with the name of category in the center, list of items first 23 chars should be displayed then the amount. Amount should be right aligned max 7 chars. Lastly, should display total

class Category:

    def __init__(self, name):
        self.name =  name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
    
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False
    
    def get_balance(self):
        return sum(item['amount'] for item in self.ledger )
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False
    
    def check_funds(self, amount):
        return amount <= self.get_balance()
    
    def __str__(self):
        output = f"{self.name:*^30}\n"
        for item in self.ledger:
            description = f"{item['description'][:23]:<23}"
            amount = f"{item['amount']:.2f}"[:7]
            output += f"{description}{amount:>7}\n"
        output += f"Total: {self.get_balance():.2f}"
        return output

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)


"""
Besides the Category class, create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. It should return a string that is a bar chart.

The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with withdrawals and not with deposits. Down the left side of the chart should be labels 0 - 100. The 'bars' in the bar chart should be made out of the 'o' character. The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. Each category name should be written vertically below the bar. There should be a title at the top that says 'Percentage spent by category'.

This function will be tested with up to four categories.

"""

def create_spend_chart(categories):
    total_spent = 0
    category_spent = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                spent += abs(item['amount'])
        total_spent += spent
        category_spent.append((category.name, spent))

    percentages = [
        (name, int((spent / total_spent) * 100 // 10) * 10)
        for name, spent in category_spent
    ]

    chart = "Percentage spent by category\n"
    for level in range(100, -1, -10):
        chart += f"{level:>3}| "
        for _, percent in percentages:
            chart += "o  " if percent >= level else "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(name) for name, _ in percentages)
    for i in range(max_len):
        chart += "     "
        for name, _ in percentages:
            chart += (name[i] + "  ") if i < len(name) else "   "
        chart += "\n"

    return chart.rstrip("\n")