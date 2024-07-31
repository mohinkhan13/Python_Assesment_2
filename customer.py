from db_connection import create_connection

class Customer:
    def __init__(self):
        self.connection = create_connection()
        self.logged_in = False
        self.username = None

    def register(self, username, password):
        if not username or not password:
            print("Username and password cannot be empty.")
            return
        
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM customers WHERE username = ?", (username,))
            if cursor.fetchone():
                print("Username already exists.")
                return

            cursor.execute("INSERT INTO customers (username, password) VALUES (?, ?)", (username, password))
            self.connection.commit()
            print("Customer registered successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def login(self, username, password):
        if not username or not password:
            print("Username and password cannot be empty.")
            return False
        
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM customers WHERE username = ? AND password = ?", (username, password))
            if cursor.fetchone():
                self.logged_in = True
                self.username = username
                print("Login successful.")
                return True
            else:
                print("Invalid credentials.")
                return False
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            cursor.close()

    def logout(self):
        if self.logged_in:
            self.logged_in = False
            self.username = None
            print("Logged out successfully.")
        else:
            print("No user is logged in.")

    def withdraw(self, username, amount):
        if not self.logged_in:
            print("You must be logged in to perform this action.")
            return

        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT balance FROM customers WHERE username = ?", (username,))
            result = cursor.fetchone()
            if not result:
                print("Username does not exist.")
                return
            
            balance = result[0]
            if amount > balance:
                print("Insufficient funds.")
                return
            
            new_balance = balance - amount
            cursor.execute("UPDATE customers SET balance = ? WHERE username = ?", (new_balance, username))
            self.connection.commit()
            print("Withdrawal successful.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def deposit(self, username, amount):
        if not self.logged_in:
            print("You must be logged in to perform this action.")
            return

        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT balance FROM customers WHERE username = ?", (username,))
            result = cursor.fetchone()
            if not result:
                print("Username does not exist.")
                return

            balance = result[0]
            new_balance = balance + amount
            cursor.execute("UPDATE customers SET balance = ? WHERE username = ?", (new_balance, username))
            self.connection.commit()
            print("Deposit successful.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def view_balance(self, username):
        if not self.logged_in:
            print("You must be logged in to perform this action.")
            return
        
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT balance FROM customers WHERE username = ?", (username,))
            result = cursor.fetchone()
            if not result:
                print("Username does not exist.")
                return

            balance = result[0]
            print(f"Your balance is: {balance}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
