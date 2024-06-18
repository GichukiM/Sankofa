# cli.py
from product import ProductManager
from supplier import SupplierManager
from transaction import TransactionManager

def menu_display():
    while True:
        print('=============================')
        print('=== Welcome to Sankofa ===')
        print('=== Inventory Management ===')
        print('=== Menu ===')
        print('=============================')
        print('(1) Add New Product')
        print('(2) Remove Product')
        print('(3) Update Product')
        print('(4) Search Product')
        print('(5) Print Inventory Report')
        print('(6) Add New Supplier')
        print('(7) Remove Supplier')
        print('(8) Search Supplier')
        print('(9) Record Supply Transaction')
        print('(10) View Transactions')
        print('(11) Print Suppliers Report')
        print('(99) Quit')
        choice = input("Enter choice: ")
        
        if choice == '1':
            ProductManager.add_product()
        elif choice == '2':
            ProductManager.remove_product()
        elif choice == '3':
            ProductManager.update_product()
        elif choice == '4':
            ProductManager.search_product()
        elif choice == '5':
            ProductManager.print_inventory()
        elif choice == '6':
            SupplierManager.add_supplier()
        elif choice == '7':
            SupplierManager.remove_supplier()
        elif choice == '8':
            SupplierManager.search_supplier()
        elif choice == '9':
            TransactionManager.record_transaction()
        elif choice == '10':
            TransactionManager.view_transactions()
        elif choice == '11':
            SupplierManager.print_suppliers()
        elif choice == '99':
            print('=== Thank you for choosing us! ===')
            print('=== GoodBye ===')
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu_display()
