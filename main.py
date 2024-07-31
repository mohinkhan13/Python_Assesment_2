from banker import Banker
from customer import Customer
from db_connection import create_connection  

def create_tables():
    connection = create_connection()
    with connection:
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS bankers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            balance REAL NOT NULL DEFAULT 0.00
        )
        """)
        connection.commit()

def main():
    create_tables()
    while True:
        print("\nWelcome to the Banking Application")
        print("1. Banker Menu")
        print("2. Customer Menu")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            banker = Banker()
            while True:
                print("\nBanker Menu")
                print("1. Register")
                print("2. Login")
                print("3. Update Customer")
                print("4. View Customers")
                print("5. Delete Customer")
                print("6. Back to Main Menu")
                banker_choice = input("Enter your choice: ")

                if banker_choice == '1':
                    username = input("Enter username: ")
                    password = input("Enter password: ")
                    banker.register(username, password)
                elif banker_choice == '2':
                    username = input("Enter username: ")
                    password = input("Enter password: ")
                    banker.login(username, password)
                elif banker_choice == '3':
                    customer_id = int(input("Enter customer ID to update: "))
                    new_balance = float(input("Enter new balance: "))
                    banker.update_customer(customer_id, new_balance)
                elif banker_choice == '4':
                    banker.view_customers()
                elif banker_choice == '5':
                    customer_id = int(input("Enter customer ID to delete: "))
                    confirmation = input("Are you sure you want to delete this customer? (Y/N): ")
                    if confirmation.upper() == 'Y':
                        banker.delete_customer(customer_id)
                elif banker_choice == '6':
                    break
                else:
                    print("Invalid choice, please try again.")
        
        elif choice == '2':
            customer = Customer()
            while True:
                print("\nCustomer Menu")
                print("1. Register")
                print("2. Login")
                print("3. Withdraw Amount")
                print("4. Deposit Amount")
                print("5. View Balance")
                print("6. Back to Main Menu")
                customer_choice = input("Enter your choice: ")

                if customer_choice == '1':
                    username = input("Enter username: ")
                    password = input("Enter password: ")
                    customer.register(username, password)
                elif customer_choice == '2':
                    username = input("Enter username: ")
                    password = input("Enter password: ")
                    customer.login(username, password)
                elif customer_choice == '3':
                    username = input("Enter username: ")
                    amount = float(input("Enter amount to withdraw: "))
                    customer.withdraw(username, amount)
                elif customer_choice == '4':
                    username = input("Enter username: ")
                    amount = float(input("Enter amount to deposit: "))
                    customer.deposit(username, amount)
                elif customer_choice == '5':
                    username = input("Enter username: ")
                    customer.view_balance(username)
                elif customer_choice == '6':
                    break
                else:
                    print("Invalid choice, please try again.")
        
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
