import csv
from datetime import datetime

#GLOBAL list to store expenses
expenses = []
budget = 0

#Load expenses fron CSV file

def load_expenses(filename='expenses.csv'):
    global expenses
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            expenses = []
            for row in reader:
                expenses.append({
                    'date': row['date'],
                    'category': row['category'],
                    'amount': row['amount'],
                    'description': row['description'],
                })
            print('Expenses loaded Successfully')
    except FileNotFoundError:
        print('File Not Found')


#Save expenses to CSV
def save_expenses(filename='expenses.csv'):
    with open(filename, mode='w', newline='', encoding='UTF-8') as file:
        fieldnames = ['date', 'category', 'amount', 'description']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)
    print('Expenses saved Successfully')


#Add an expense
def add_expense():
    date = input('Enter Date (YYYY-MM-DD) : ')
    try:
        date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print('Invalid Date')
        return

    category = input('Enter Category (Food, Travel, etc.) : ')

    try:
        amount = float(input('Enter Amount : '))
    except ValueError:
        print('Invalid Amount')
        return

    description = input('Enter Description : ')

    expense = {
        'date': date,
        'category': category,
        'amount': amount,
        'description': description,
    }

    expenses.append(expense)

    print('Expenses added Successfully')


#View all expenses
def view_expenses():
    if not expenses:
        print('No expenses added')
        return
    print('\n --- Expense List ---')
    for expense in expenses:
        #print(expense['date'], expense['category'], expense['amount'])
        print(f"{expense['date']} | {expense['category']} | {expense['amount']} | {expense['description']}")
    print('--------------------\n')

#Set Budget
def set_budget():
    global budget
    try:
        budget = float(input('Enter your Monthly Budget : '))
        print(f' Budget Set To: Rs.{budget:.2f} ')
    except ValueError:
        print('Invalid input for Budget')

#Track Budget
def track_budget():
    if budget == 0:
        print('No budget set. Please set the budget')
        return
    total_spent = sum(float(exp['amount']) for exp in expenses)
    print(f'Total Spent: Rs.{total_spent:.2f}')
    if total_spent > budget:
        print('You have exceeded your budget')
    else:
        print(f'You have Rs.{budget - total_spent} left in your budget')


#Menu
def menu():
    load_expenses()  #Load previous data if available
    while True:
        print('\n--- Personal Expenses Tracker ---')
        print('1. Add Expense')
        print('2. View Expenses')
        print('3. Set Budget')
        print('4. Track budget')
        print('5. Save & Exit')
        choice = input('Enter Your Option : ')

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            set_budget()
        elif choice == '4':
            track_budget()
        elif choice == '5':
            save_expenses()
            print('Your data has been saved')
            break
        else:
            print('Invalid Choice. Please try again')


#Run the program
if __name__ == '__main__':
    menu()






















