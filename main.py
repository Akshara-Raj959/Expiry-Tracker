from data_handler import load_data, save_data
from checker import check_expiry
from datetime import datetime

def add_item():
    name = input("Enter item name: ")
    category = input("Enter category (e.g. Food/Medicine): ")
    expiry = input("Enter expiry date (YYYY-MM-DD): ")

    try:
        datetime.strptime(expiry, "%Y-%m-%d")
    except ValueError:
        print("❌ Invalid date format. Try again.")
        return

    data = load_data()
    data.append({
        "name": name,
        "category": category,
        "expiry": expiry
    })
    save_data(data)
    print("✅ Item added successfully!")

def view_items():
    data = load_data()
    if not data:
        print("No items found.")
        return
    print("\n--- Stored Items ---")
    for i, item in enumerate(data, 1):
        print(f"{i}. {item['name']} ({item['category']}) - Expiry: {item['expiry']}")

def remove_item():
    data = load_data()
    view_items()

    # Ask which one to delete
    try:
        choice = int(input("\nEnter the number of the item to remove: "))
        if 1 <= choice <= len(data):
            removed_item = data.pop(choice - 1)
            save_data(data)
            print(f"✅ Removed: {removed_item['name']}")
        else:
            print("❌ Invalid item number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def remove_expired_items():
    """Remove all items whose expiry date is before today"""
    data = load_data()
    if not data:
        print("No items found.")
        return

    today = datetime.now().date()
    valid_items = []
    removed_items = []

    for item in data:
        exp_date = datetime.strptime(item["expiry"], "%Y-%m-%d").date()
        if exp_date < today:
            removed_items.append(item)
        else:
            valid_items.append(item)

    if removed_items:
        save_data(valid_items)
        print("\n🗑️ Removed expired items:")
        for item in removed_items:
            print(f" - {item['name']} ({item['expiry']})")
    else:
        print("\n✅ No expired items found!")
        
def search_item():
    data = load_data()
    if not data:
        print("\n📂 No items to search.\n")
        return

    query = input("Enter item name or category to search: ").lower()
    results = [item for item in data if query in item['name'].lower() or query in item['category'].lower()]

    if results:
        print("\n🔎 Search Results:")
        for i, item in enumerate(results, 1):
            print(f"{i}. {item['name']} ({item['category']}) - Expiry: {item['expiry']}")
    else:
        print("\n❌ No matching items found.")
    print()


def main_menu():
    while True:
        print("\n===== EXPIRY TRACKER =====")
        print("1. Add Item")
        print("2. View Items")
        print("3. Check Expiry")
        print("4. Remove Item")
        print("5. Remove Expired Items")
        print("6. Search Item")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            view_items()
        elif choice == "3":
            data = load_data()
            check_expiry(data)
        elif choice == "4":
            remove_item()
        elif choice == "5":
            remove_expired_items()
        elif choice == "6":
            search_item()
        elif choice == "7":
            print("Thankyou and Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main_menu()
