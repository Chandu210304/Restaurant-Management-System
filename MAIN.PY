
This file will be the entry point for the system, where users interact with different modules.

```python
from orders import OrderManager
from tables import TableManager
from inventory import InventoryManager
from staff import StaffManager

def main():
    print("Welcome to the Restaurant Management System!")
    
    # Create managers for each module
    order_manager = OrderManager()
    table_manager = TableManager()
    inventory_manager = InventoryManager()
    staff_manager = StaffManager()
    
    # Menu for user interaction
    while True:
        print("\n1. Manage Orders")
        print("2. Manage Tables")
        print("3. Manage Inventory")
        print("4. Manage Staff")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            order_manager.manage_orders()
        elif choice == '2':
            table_manager.manage_tables()
        elif choice == '3':
            inventory_manager.manage_inventory()
        elif choice == '4':
            staff_manager.manage_staff()
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
