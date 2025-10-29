from ETR import Expense
import calendar
import datetime



def main():
    print(f'Running Expense Tracker!')
    expense_file_path="expenses.csv"
    budget=2000

    # Write their expense to a file.
    all_expenses = get_user_expense()

    # Save each expense to file
    if all_expenses:
        for expense in all_expenses:
            save_expense_to_file(expense, expense_file_path)
    else:
        print("No expenses entered.")
    # Read file and summarize expenses.
    summarize_expenses(expense_file_path,budget)

def get_user_expense():
    print(f'Getting User Expense')
    new_expenses=[]
    expense_categories=[
        "Orders",
        "Super Market",
        "Petrol",
        "Etc",
        "Fun",
        "Butcher Shop"
    ]
    while True:
        expense_name = input('Enter expense name: ')
        if expense_name=="Stop":
            return (new_expenses)
        else:
            expense_amount = float(input('Enter expense amount: '))
            while True:
                print('Select a category: ')
                for i,category_name in enumerate(expense_categories,start=1):
                    print(f'{i}.{category_name}')
                value_range=f"[1-{len(expense_categories)}]"
                selected_index=int(input(f"Enter a category number {value_range}: "))-1

                if selected_index in range(len(expense_categories)):
                    selected_category=expense_categories[selected_index]
                    new_expense=Expense(name=expense_name,category=selected_category,amount=expense_amount)
                    new_expenses.append(new_expense)

                    break
                else:
                    print('Invalid category.Please try again')

def save_expense_to_file(expense:Expense,expense_file_path):
    print(f'Saving User Expense: {expense} to {expense_file_path}')
    with open(expense_file_path,"a") as f:
        #a for append
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")
def summarize_expenses(expense_file_path, budget):
    print(f'Summarize User Expense')
    expenses:list[Expense]=[]
    with open(expense_file_path,'r') as f:
        lines=f.readlines()
        if lines and lines[0]=='\n':
            lines.pop(0)
        for line in lines:
            expense_name,expense_amount,expense_category=line.strip().split(',')
            line_expense=Expense(name=expense_name,amount=float(expense_amount),category=expense_category)
            expenses.append(line_expense)

    amount_by_category={}
    for expense in expenses:
        key=expense.category
        if key in amount_by_category:
            amount_by_category[key]+=expense.amount
        else:
            amount_by_category[key]=expense.amount
    print('Expenses By category')
    for key,amount in amount_by_category.items():
        print(f' {key}: ${amount:.2f}')

    total_spent=sum([x.amount for x in expenses])
    print(f" You've spent ${total_spent:.2f} this month!")

    remaining_budget=budget-total_spent
    print(f" Budget Remaining: ${remaining_budget:.2f} this month!")

    now=datetime.datetime.now()
    print(now)

    days_in_month=calendar.monthrange(now.year,now.month)[1]
    print(days_in_month)
    remaining_days=days_in_month-now.day

    if remaining_days > 0:
        daily_budget = remaining_budget / remaining_days
    else:
        daily_budget = 0

    print(green(f'Daily budget: ${daily_budget:.2f}'))

def green(text):
    return f"\033[92m{text}\033[0m"




if __name__=='__main__':
   main()


