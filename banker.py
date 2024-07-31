from db_connection import create_connection

class Banker:
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
            cursor.execute("SELECT * FROM bankers WHERE username = ?", (username,))
            if cursor.fetchone():
                print("Username already exists.")
                return

            cursor.execute("INSERT INTO bankers (username, password) VALUES (?, ?)", (username, password))
            self.connection.commit()
            print("Banker registered successfully.")
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
            cursor.execute("SELECT * FROM bankers WHERE username = ? AND password = ?", (username, password))
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

    def update_customer(self, customer_id, new_balance):
        if not self.logged_in:
            print("You must be logged in to perform this action.")
            return

        if new_balance < 0:
            print("Balance cannot be negative.")
            return
        
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM customers WHERE id = ?", (customer_id,))
            if not cursor.fetchone():
                print("Customer ID does not exist.")
                return
            
            cursor.execute("UPDATE customers SET balance = ? WHERE id = ?", (new_balance, customer_id))
            self.connection.commit()
            print("Customer balance updated successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def view_customers(self):
        if not self.logged_in:
            print("You must be logged in to perform this action.")
            return
        
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM customers")
            rows = cursor.fetchall()
            if not rows:
                print("No customers found.")
                return
            for row in rows:
                print(row)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def delete_customer(self, customer_id):
        if not self.logged_in:
            print("You must be logged in to perform this action.")
            return

        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM customers WHERE id = ?", (customer_id,))
            if not cursor.fetchone():
                print("Customer ID does not exist.")
                return

            confirmation = input("Are you sure you want to delete this customer? (Y/N): ")
            if confirmation.upper() != 'Y':
                print("Deletion cancelled.")
                return
            
            cursor.execute("DELETE FROM customers WHERE id = ?", (customer_id,))
            self.connection.commit()
            print("Customer deleted successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
