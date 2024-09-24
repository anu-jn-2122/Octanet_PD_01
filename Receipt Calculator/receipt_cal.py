import os
class Item:
    def __init__(self, name, price, quantity):
        """
        Initialize the item with name, price, and quantity.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

class Receipt:
    def __init__(self, tax_rate=0.07, discount_rate=0.1):
        """
        Initialize the receipt with an empty list of items, tax rate, and discount rate.
        """
        self.items = []
        self.tax_rate = tax_rate
        self.discount_rate = discount_rate

    def add_item(self, name, price, quantity):
        """
        Add an item to the receipt.
        """
        item = Item(name, price, quantity)
        self.items.append(item)

    def calculate_subtotal(self):
        """
        Calculate the subtotal by summing up the cost of each item.
        """
        return sum(item.price * item.quantity for item in self.items)

    def calculate_tax(self, subtotal):
        """
        Calculate the tax based on the subtotal.
        """
        return subtotal * self.tax_rate

    def calculate_discount(self, subtotal):
        """
        Calculate the discount based on the subtotal.
        """
        return subtotal * self.discount_rate

    def calculate_total(self, subtotal, tax, discount):
        """
        Calculate the final total by adding tax and subtracting discount from the subtotal.
        """
        return subtotal + tax - discount

    def generate_receipt(self):
        """
        Generate the receipt text, display it, and save it to a file.
        """
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax(subtotal)
        discount = self.calculate_discount(subtotal)
        total = self.calculate_total(subtotal, tax, discount)

        # Generate receipt text
        receipt_text = "\n----- Receipt -----\n"
        for item in self.items:
            receipt_text += f"{item.name} - ${item.price:.2f} x {item.quantity} = ${item.price * item.quantity:.2f}\n"
        receipt_text += f"\nSubtotal: ${subtotal:.2f}"
        receipt_text += f"\nTax ({self.tax_rate * 100}%): ${tax:.2f}"
        receipt_text += f"\nDiscount ({self.discount_rate * 100}%): -${discount:.2f}"
        receipt_text += f"\nTotal: ${total:.2f}"
        receipt_text += "\n-------------------\n"

        # Display receipt
        print(receipt_text)

        # Save receipt to a text file
        self.save_receipt_to_file(receipt_text)

    def save_receipt_to_file(self, receipt_text):
        """
        Save the receipt to a text file.
        """
        try:
            with open("receipt.txt", "w") as file:
                file.write(receipt_text)
            print("Receipt has been saved as 'receipt.txt'.")
        except IOError as e:
            print(f"Error saving receipt to file: {e}")

def main():
    """
    Main function to run the receipt calculator.
    """
    receipt = Receipt()

    # Accept input for items
    while True:
        name = input("Enter item name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        try:
            price = float(input(f"Enter price for '{name}': "))
            quantity = int(input(f"Enter quantity for '{name}': "))
            receipt.add_item(name, price, quantity)
        except ValueError:
            print("Invalid input. Please enter numeric values for price and quantity.")

    # Generate and display the receipt
    receipt.generate_receipt()

if __name__ == "__main__":
    main()
