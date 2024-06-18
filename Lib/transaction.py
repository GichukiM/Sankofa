from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

class TransactionManager:
    @staticmethod
    def record_supply_transaction():
        session = Session()
        print("Recording Supply Transaction")
        print("===========================")
        product_name = input("Enter the name of the product: ")
        supplier_name = input("Enter the name of the supplier: ")
        quantity = input("Enter the quantity supplied: ")

        try:
            product = session.query(Product).filter_by(name=product_name).first()
            supplier = session.query(Supplier).filter_by(name=supplier_name).first()

            if product and supplier:
                transaction = Transaction(product_id=product.id, supplier_id=supplier.id, quantity=int(quantity))
                session.add(transaction)
                session.commit()  # Commit the transaction to the database
                print("Supply transaction recorded successfully!")
            else:
                print("Product or Supplier not found.")
        except Exception as e:
            print(f"Error recording transaction: {e}")
            session.rollback()  # Rollback the transaction in case of error
        finally:
            session.close()  # Close the session to release resources
