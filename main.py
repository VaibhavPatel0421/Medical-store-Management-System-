# Medical Store Management Project
# Simple Python script for medical shop

# Sample inventory data
inventory = [
    {"name": "Paracetamol 650", "price": 15.0, "quantity": 50},
    {"name": "Dolo 650", "price": 30.0, "quantity": 8},
    {"name": "Combiflam", "price": 25.0, "quantity": 40},
    {"name": "Pantop 40", "price": 55.0, "quantity": 5}
]


def show_medicines():
    print("\n Medicine List ")
    if len(inventory) == 0:
        print("Stock is empty.")
        return
    
    print("Name | Price | Quantity")
    for item in inventory:
        print(item["name"], "| Rs.", item["price"], "|", item["quantity"])


def add_medicine():
    print("\n Add Medicine ")
    name = input("Enter medicine name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    # Check if already in list
    for item in inventory:
        if item["name"].lower() == name.lower():
            item["quantity"] = item["quantity"] + quantity
            print("Stock updated successfully!")
            return

    # Adding new item
    new_med = {"name": name, "price": price, "quantity": quantity}
    inventory.append(new_med)
    print("New medicine added!")


def make_bill():
    print("\n Billing System ")
    if len(inventory) == 0:
        print("No stock available.")
        return

    total = 0
    bill_list = []

    while True:
        med_name = input("Enter medicine name to buy (or type 'done' to stop): ")
        if med_name.lower() == "done":
            break

        found = False
        for item in inventory:
            if item["name"].lower() == med_name.lower():
                found = True
                qty = int(input("Enter quantity: "))
                
                if qty > item["quantity"]:
                    print("Not enough stock! Available:", item["quantity"])
                else:
                    item["quantity"] = item["quantity"] - qty
                    cost = qty * item["price"]
                    total = total + cost
                    bill_list.append({"name": item["name"], "qty": qty, "cost": cost})
                    print("Added to bill.")
                break

        if not found:
            print("Medicine not found in inventory!")

    # Print receipt
    if len(bill_list) > 0:
        print("\n FINAL BILL ")
        for b in bill_list:
            print(b["name"], "x", b["qty"], "=", "Rs.", b["cost"])
        print("Total Amount: Rs.", total)


def check_low_stock():
    print("\n Low Stock Alert ")
    found_any = False
    for item in inventory:
        if item["quantity"] < 10:
            print("ALERT:", item["name"], "- Only", item["quantity"], "left!")
            found_any = True
            
    if not found_any:
        print("All items have enough stock.")


# Main Menu Loop
while True:
    print("\n MEDICAL STORE SYSTEM")
    print("1. View Medicines")
    print("2. Add Medicine")
    print("3. Create Bill")
    print("4. Check Low Stock")
    print("5. Exit")

    choice = input("Enter option (1-5): ")

    if choice == "1":
        show_medicines()
    elif choice == "2":
        add_medicine()
    elif choice == "3":
        make_bill()
    elif choice == "4":
        check_low_stock()
    elif choice == "5":
        print("Thank you! Exiting program...")
        break
    else:
        print("Invalid choice, try again.")
