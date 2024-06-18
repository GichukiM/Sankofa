
# Sankofa Inventory Management CLI Application

This CLI application is designed to manage inventory including products, suppliers, and transactions. It allows users to perform various operations such as adding, removing, updating, and searching for products and suppliers. Additionally, it facilitates recording supply transactions between products and suppliers, and viewing transaction history.

## Features

- **Products Management:**
  - Add new products with name and quantity.
  - Remove existing products by name.
  - Update product quantities.
  - Search for products by name.

- **Suppliers Management:**
  - Add new suppliers with name and contact information.
  - Remove existing suppliers by name.
  - Search for suppliers by name.

- **Transaction Management:**
  - Record supply transactions between products and suppliers.
  - View transaction history including product, supplier, and quantity.

## Installation

To run this application, ensure you have Python and Pipenv installed on your system:

1. Clone the repository:
   ```bash
   git clone <github url>
   cd <project>
   ```

2. Install dependencies using Pipenv:
   ```bash
   pipenv install
   ```

3. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

4. Run the CLI application:
   ```bash
   python main.py
   ```

## Usage

- **Adding a Product:**
  - Select option '1' from the main menu.
  - Enter the name and quantity of the product.

- **Removing a Product:**
  - Select option '2' from the main menu.
  - Enter the name of the product to remove.

- **Updating a Product:**
  - Select option '3' from the main menu.
  - Enter the name of the product and the updated quantity.

- **Searching for a Product:**
  - Select option '4' from the main menu.
  - Enter the name of the product to search for.

- **Adding a Supplier:**
  - Select option '5' from the main menu.
  - Enter the name and contact information of the supplier.

- **Removing a Supplier:**
  - Select option '6' from the main menu.
  - Enter the name of the supplier to remove.

- **Searching for a Supplier:**
  - Select option '7' from the main menu.
  - Enter the name of the supplier to search for.

- **Recording a Transaction:**
  - Select option '8' from the main menu.
  - Enter the name of the product, name of the supplier, and the quantity for the transaction.

- **Viewing Transaction History:**
  - Select option '9' from the main menu.
  - The application will display all recorded transactions.

- **Printing Inventory:**
  - Select option '10' from the main menu.
  - The application will display all products and their quantities.

- **Exiting the Application:**
  - Select option '11' from the main menu.

## Database Structure

The application uses SQLAlchemy ORM to interact with a SQLite database (`inventory.db`). The database schema includes the following tables:

- **products:** Stores information about products including name and quantity.
- **suppliers:** Stores information about suppliers including name and contact information.
- **transactions:** Stores records of transactions between products and suppliers including product_id, supplier_id, and quantity.

## Project Structure

The project structure is organized as follows:

```
inventory-cli/
│
├── main.py           # Entry point of the CLI application
├── database.py       # Database configuration and session management
├── models.py         # SQLAlchemy ORM models (Product, Supplier, Transaction)
├── product.py        # Product related functionality and manager
├── supplier.py       # Supplier related functionality and manager
├── transaction.py    # Transaction related functionality and manager
├── utils.py          # Utility functions for input validation
├── Pipfile           # Dependencies and virtual environment configuration
├── Pipfile.lock      # Locked dependencies for deterministic builds
└── README.md         # This file
```

## Requirements

- Python 3.6+
- Pipenv
- SQLAlchemy
- SQLite (comes with Python standard library)

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
