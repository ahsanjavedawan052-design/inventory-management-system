"""
Inventory Management System v1.1
Description: Pre-populated CLI for stock tracking with 10 default records.
"""

# --- GLOBAL DATA STORE (Pre-populated with 10 Default Records) ---
inventory: dict[int, dict] = {
    101: {"name": "MacBook Pro", "quantity": 10, "price": 1999.99},
    102: {"name": "Dell XPS 15", "quantity": 8, "price": 1450.00},
    103: {"name": "Magic Mouse", "quantity": 50, "price": 79.00},
    104: {"name": "Mechanical KB", "quantity": 30, "price": 120.50},
    105: {"name": "4K Monitor", "quantity": 15, "price": 350.00},
    106: {"name": "USB-C Hub", "quantity": 100, "price": 45.00},
    107: {"name": "Webcam HD", "quantity": 25, "price": 89.99},
    108: {"name": "Desk Lamp", "quantity": 40, "price": 29.50},
    109: {"name": "Office Chair", "quantity": 12, "price": 210.00},
    110: {"name": "HDMI Cable", "quantity": 200, "price": 15.00},
}

# --- CORE LOGIC FUNCTIONS ---

def add_item(item_id: int, name: str, quantity: int, price: float) -> None:
    if item_id in inventory:
        print(f"[!] Error: ID {item_id} exists. Use 'Update' instead.")
    else:
        inventory[item_id] = {"name": name, "quantity": quantity, "price": price}
        print(f"[*] Success: {name} added.")

def view_inventory() -> None:
    """Displays items in a formatted table. No longer shows 'Empty' by default."""
    print("\n" + "="*65)
    print(f"{'ID':<10} {'Name':<15} {'Qty':<10} {'Price':<12} {'Total':<10}")
    print("-" * 65)

    for item_id, details in inventory.items():
        item_total = details['quantity'] * details['price']
        print(f"{item_id:<10} {details['name']:<15} {details['quantity']:<10} "
              f"${details['price']:<11.2f} ${item_total:<9.2f}")
    print("="*65 + "\n")

def update_stock(item_id: int, new_quantity: int) -> None:
    if item_id in inventory:
        inventory[item_id]["quantity"] = new_quantity
        print(f"[*] Stock updated for ID {item_id}.")
    else:
        print(f"[!] Error: ID {item_id} not found.")

def delete_item(item_id: int) -> None:
    if item_id in inventory:
        removed = inventory.pop(item_id)
        print(f"[-] Removed: {removed['name']}.")
    else:
        print(f"[!] Error: ID {item_id} not found.")

def search_item(query: str) -> None:
    found = False
    for uid, data in inventory.items():
        if str(uid) == query or query.lower() in data['name'].lower():
            print(f"-> Found: {data['name']} (ID: {uid}) | Qty: {data['quantity']}")
            found = True
    if not found:
        print("[!] No matching items.")

def calculate_inventory_value() -> float:
    """Calculates total value. Works immediately due to pre-populated data."""
    total_val = sum(item['price'] * item['quantity'] for item in inventory.values())
    print(f"\n[Summary] Current Portfolio Worth: ${total_val:,.2f}")
    return total_val

# --- USER INTERFACE ---

def main():
    while True:
        print("\n--- INVENTORY DASHBOARD ---")
        print("1. Add | 2. Update | 3. Delete | 4. View | 5. Search | 6. Total | 7. Exit")
        choice = input("\nSelect Option: ")

        try:
            if choice == '1':
                add_item(int(input("ID: ")), input("Name: "), int(input("Qty: ")), float(input("Price: ")))
            elif choice == '2':
                update_stock(int(input("ID: ")), int(input("New Qty: ")))
            elif choice == '3':
                delete_item(int(input("ID: ")))
            elif choice == '4':
                view_inventory()
            elif choice == '5':
                search_item(input("Query: "))
            elif choice == '6':
                calculate_inventory_value()
            elif choice == '7':
                print("Exciting... TO VISIT AHSAN JAVED STORE")
                break
        except ValueError:
            print("[!] Numeric error: Please check your ID/Qty/Price inputs.")

if __name__ == "__main__":
    main()