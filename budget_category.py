"""
    A class to represent a budget category.

    Attributes:
    - category_name (str): The name of the budget category.
    - allocated_budget (float): The initial allocated budget for the category.
    - remaining_budget (float): The remaining budget after expenses.

    Methods:
    - __init__(self, category_name, allocated_budget): Initializes a BudgetCategory object with the given name and allocated budget.
    - get_category_name(self): Returns the name of the budget category.
    - set_category_name(self, new_name): Sets the name of the budget category to the given new name.
    - get_allocated_budget(self): Returns the allocated budget for the category.
    - set_allocated_budget(self, new_budget): Sets the allocated budget for the category to the given new budget.
    - add_expense(self, amount): Adds an expense to the category and updates the remaining budget accordingly.
    - display_category_summary(self): Displays the details of the budget category, including name, allocated budget, and remaining budget.
    """
class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget

    def get_category_name(self):
        return self.__category_name

    def set_category_name(self, new_name):
        self.__category_name = new_name

    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_allocated_budget(self, new_budget):
        if new_budget >= 0:
            self.__allocated_budget = new_budget
            self.__remaining_budget = new_budget
        else:
            print("Error: Budget must be a positive number.")

    def add_expense(self, amount):
        if amount >= 0:
            if amount <= self.__remaining_budget:
                self.__remaining_budget -= amount
                print(f"${amount} expense added to {self.__category_name} category.")
            else:
                print("Error: Expense exceeds remaining budget.")
        else:
            print("Error: Expense amount must be a positive number.")

    def display_category_summary(self):
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget}")
        print(f"Remaining Budget: ${self.__remaining_budget}")