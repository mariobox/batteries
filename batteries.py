import sqlite3
from tabulate import tabulate  # sudo apt install python3-tabulate

# Connect to (or create) a database file
conn = sqlite3.connect("batteries.db")

# Create a cursor object to interact with the database
cursor = conn.cursor()

def print_reports():
    print("\nDevice Inventory:")
    cursor.execute("""SELECT id, name, type, battery_type, battery_qty FROM devices""")
    devices = cursor.fetchall()
    # Get column names from cursor.description
    headers = [desc[0] for desc in cursor.description]

    # Print in table format
    print(tabulate(devices, headers=headers, tablefmt="grid"))
     
    print("\nBattery Inventory:")
    cursor.execute("""
        SELECT id, kind, inventory, usage FROM batteries
        JOIN (SELECT "battery_type", SUM("battery_qty") AS "usage" FROM "devices"
        GROUP BY "battery_type"
        ) 
        ON "batteries"."kind" = "battery_type"
        """)
    batteries = cursor.fetchall()
    # Get column names from cursor.description
    headers = [desc[0] for desc in cursor.description]
    print(tabulate(batteries, headers=headers, tablefmt="grid"))

    print("\nBattery Replacement History:")
    cursor.execute("""
        SELECT changes.device_id, devices.name, changes.date 
        FROM changes 
        JOIN devices ON changes.device_id = devices.id
    """)
    changes = cursor.fetchall()
    # Get column names from cursor.description
    headers = [desc[0] for desc in cursor.description]
    print(tabulate(changes, headers=headers, tablefmt="grid"))
    print("\n")
    print(input("Press Enter to continue..."))

def add_device():
    device_name = input("Enter the name of the new device: ")
    device_type = input("Enter the type of the device: ")
    battery_type = input("Enter the battery type required: ")
    battery_qty = int(input("Enter the quantity of batteries required: "))
    cursor.execute("""
        INSERT INTO devices(name, type, battery_type, battery_qty) 
        VALUES (?,?,?,?)""", (device_name, device_type, battery_type, battery_qty)) 
    print("\nDevice added successfully.\n\n")

def replace_batteries():
    device_id = int(input("Enter the device ID to replace batteries for: "))
    replacement_date = input("Enter the replacement date (YYYY-MM-DD): ")
    cursor.execute("""
        INSERT INTO changes(device_id, date) 
        VALUES (?, ?)""", (device_id, replacement_date))
    print("\nBatteries replaced successfully.\n\n")

def add_batteries():
    battery_kind = input("Enter the battery kind to add: ")
    quantity = int(input("Enter the quantity to add: "))
    cursor.execute("""
        UPDATE batteries 
        SET inventory = inventory + ? 
        WHERE kind = ?""", (quantity, battery_kind))
    print("\nBatteries added to inventory successfully.\n\n")

def main():
    while True:
        print("Menu:")
        print("0. Print reports")
        print("1. Add new device")
        print("2. Replace batteries")
        print("3. Add batteries to inventory")
        print("4. Exit program")

        try:
            choice = int(input("Chose menu number: "))
            if choice == 0:
                print("Printing reports...")
                print_reports()
            elif choice == 1:
                print("Adding new device...")
                add_device()
            elif choice == 2:
                print("Replacing batteries...")
                replace_batteries()
            elif choice == 3:
                print("Adding batteries to inventory...")
                add_batteries()
            elif choice == 4:
                print("Exiting program...")
                conn.commit()
                conn.close()
                break
            else:
                print("Invalid choice. Please try again.\n")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Call the function
if __name__ == "__main__":
    main()