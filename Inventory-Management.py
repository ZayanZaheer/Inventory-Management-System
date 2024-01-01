import os
import datetime
os.system('cls')
def log_activity(activity):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {activity}\n"
    with open('log.txt', 'a') as f:
        f.write(log_entry)

Accounts = []
with open('Users.txt', 'r') as f:
    Accounts = [account.rstrip().split(',') for account in f.readlines()]

def admin_menu():
    while True:
        print("Please enter the number for what you wish to do.")
        print("1. Add user")
        print("2. Manipulate stock")
        admin_choi = input("Please enter number (done if your are finished): ")
        
        if admin_choi == '1':
            while True:
                user = input("Please enter the username of the new user: ")
                pass_word = input("Please enter the password for new account: ")
                role = input("Please enter role of new user: ")
                
                new_user = [user, pass_word, role]
                Accounts.append(new_user)
                with open('Users.txt', 'a') as k:
                    k.write(','.join(str(users) for users in new_user) + '\n')
                print("User has been added.")
                log_activity(f"Added new user: {user}")
                # print(Accounts)
                fin = input("Are there anymore accounts to add? ")
                if fin.lower() == 'y' or fin.lower() == 'yes':
                    continue
                elif fin.lower() == 'n' or fin.lower() == 'no':
                    break
        
        elif admin_choi == '2':
            main_menu()
        
        elif admin_choi.lower() == 'done':
            break

def stocker_menu():
    while True:
        print("Please enter the number for the service you need: ")
        print("1. Stock Taking")
        print("2. Search item")
        stocker_choi = input("Please enter number (done if your are finished): ")
        if stocker_choi == '1':
            stock_take()
        elif stocker_choi == '2':
            search()
        elif stocker_choi.lower() == 'done':
            break
        
def purchaser_menu():
    while True:
        print("Enter number for service you wish to excute")
        print("1. View Replenish list")
        print("2. Stock Replenishment")
        print("3. Search")
        purchaser_choi = input("Please enter number (done if your are finished): ")
        if purchaser_choi == '1':
            replenish()
        elif purchaser_choi == '2':
            stock_rep()
        elif purchaser_choi == '3':
            search()
        elif purchaser_choi.lower() == 'done':
            break
                    
lines = []
with open('Grocery.txt', 'r') as f:
    lines = [line.rstrip().split(',') for line in f]

    modified_lines = []
    for q in lines:
        if len(q) > 0:
            if q[0] != '':
                q[0] = int(q[0])
        if len(q) > 4:
            if q[4] != '':
                q[4] = float(q[4])
        if len(q) > 5:
            if q[5] != '':
                q[5] = int(q[5])
        if len(q) > 6:
            if q[6] != '':
                q[6] = int(q[6])
        modified_lines.append(q)

def add():
    while True:
        code = input("Please enter item code (or 'done' to exit): ")
        if code.lower() == 'done':
            break
        
        it = input("Please enter the name of the item: ")
        it = it.capitalize()
        des = input("Please enter the description of the item: ")
        des = des.capitalize()
        uni = input("Please enter the type of unit: ")
        uni = uni.capitalize()
        lim = int(input("Please enter the minimum: "))
        quantity = int(input("Please enter the number of items: "))
        cost = float(input("Please enter the price of the item: "))

        new_item = [code, it, des, uni, cost, quantity, lim]
        lines.append(new_item)

        with open('Grocery.txt', 'a') as f:
            f.write(','.join(str(item) for item in new_item) + '\n\n')

        print(new_item)
        log_activity(f"Added new item: {new_item[0]} - {new_item[1]}")

def remove(lines):
    while True:
        item = input("Please enter the code of the item you wish to remove (or 'done' to exit): ")
        if item.lower() == 'done':
            break

        item = int(item)

        new_lines = []
        for line in lines:
            if len(line) > 0:
                if line[0] != '':
                    if item != int(line[0]):
                        new_lines.append(line)

        lines = new_lines
        print(lines)
        log_activity(f"Removed item: {item}")

        with open('Grocery.txt', 'w') as f:
            for line in lines:
                f.write(','.join(str(item) for item in line) + '\n')
    
    return lines

def replenish(lines):
    for line in lines:
        if len(line) >= 7:
            if float(line[5]) < float(line[6]):
                print("Please restock item {}".format(line[0]))
        else:
            print("Invalid line: {}".format(line))
            
    log_activity("Replenish list viewed")

def stock_rep():
    while True:
        item = input("Please enter the code of the item you wish to stock (or 'done' to exit): ")
        if item.lower() == 'done':
            break

        item = int(item)

        found = False
        for line in lines:
            if line[0] == item:
                found = True
                print(line)
                update = int(input("Please enter the new stock of the item code {}: ".format(item)))
                line[5] = update
                print(line)
                break

        if not found:
            print("Item {} not found.".format(item))

        with open('Grocery.txt', 'w') as f:
            for line in lines:
                f.write(','.join(str(item) for item in line) + '\n')
        log_activity(f"Stocked item: {item}")

def stock_take():
    while True:
        check_item = input("Please enter the code of the item that you wish to check the stock of (or 'done' to exit): ")
        if check_item.lower() == 'done':
            break

        check_item = int(check_item)
        item_found = False

        for line in lines:
            if line[0] == check_item:
                print(line)
                item_found = True
                break

        if item_found:
            conf = input("Do you wish to make changes to the stock of {}? (y) if yes, (n) if no: ".format(check_item))

            if conf == 'y':
                new_stock = int(input("Please enter the new stock of {}: ".format(check_item)))

                for line in lines:
                    if line[0] == check_item:
                        line[5] = str(new_stock)
                        print(line)
                        break
                    

                with open('Grocery.txt', 'w') as f:
                    for line in lines:
                        f.write(','.join(str(item) for item in line) + '\n')
                log_activity(f"Updated stock of item: {check_item} - New stock: {new_stock}")
            elif conf == 'n':
                print("Very well.")
        else:
            print("Item {} not found.".format(check_item))

def update():
    while True:
        old = input("Please enter the code of the item you wish to make changes (or 'done' to exit): ")
        if old.lower() == 'done':
            break
        old = int(old)
        with open('Grocery.txt', 'r') as f:
            lines = [line.strip().split(',') for line in f]
        for line in lines:
            if line[0] == str(old):
                print("Current Code:", line[0])
                new_code = input("Please enter the new code for this item (or press Enter to keep current): ")
                line[0] = int(new_code) if new_code else int(line[0])
                
                print("Current Name:", line[1])
                new_name = input("Please enter the new name for this item (or press Enter to keep current): ")
                line[1] = new_name.capitalize() if new_name else line[1]

                print("Current Description:", line[2])
                new_des = input("Please enter the new description for this item (or press Enter to keep current): ")
                line[2] = new_des.capitalize() if new_des else line[2]

                print("Current Unit:", line[3])
                new_unit = input("Please enter the new unit for this item (or press Enter to keep current): ")
                line[3] = new_unit.capitalize() if new_unit else line[3]

                print("Current Price:", line[4])
                new_price = input("Please enter the new price for this item (or press Enter to keep current): ")
                line[4] = float(new_price) if new_price else float(line[4])

                print("Current Quantity:", line[5])
                new_quantity = input("Please enter the new quantity for this item (or press Enter to keep current): ")
                line[5] = int(new_quantity) if new_quantity else int(line[5])

                print("Current Minimum:", line[6])
                new_min = input("Please enter the new minimum for this item (or press Enter to keep current): ")
                line[6] = int(new_min) if new_min else int(line[6])

                break
        print(line)
        with open('Grocery.txt', 'w') as f:
            for line in lines:
                f.write(','.join(str(item) for item in line) + '\n')
        log_activity(f"Updated information of {old}/{new_code}")

def search():
    while True:
        print("Please enter how you would like to search")
        print("1) By description")
        print("2) By code range")
        print("3) By category")
        print("4) By price range")
        print("5) Quit")
        choice = input("Choice: ").strip()
        print('-' * 40)
        if choice == '1':
            choi1 = input("Please enter the description of the item: ")
            for line in lines:
                if len(line) > 1 and choi1.lower() in line[1].lower():
                    print(line)
            log_activity("Searched By Description")
        elif choice == '2':
            code_start = int(input("Please enter the starting code: "))
            code_end = int(input("Please enter the ending code: "))
            for line in lines:
                if len(line) > 0 and code_start <= int(line[0]) <= code_end:
                    print(line)
            log_activity("Searched By Code")
        elif choice == '3':
            choi3 = input("Please enter the category of the item you are searching for: ")
            for line in lines:
                if len(line) > 2 and choi3.lower() in line[2].lower():
                    print(line)
            log_activity("Searched By Category")
        elif choice == '4':
            min_price = float(input("Please enter the minimum price: "))
            max_price = float(input("Please enter the maximum price: "))
            for line in lines:
                if len(line) > 4 and min_price <= float(line[4]) <= max_price:
                    print(line)
            log_activity("Searched By Price")
        elif choice == '5':
            break
        else:
            print("Invalid choice")
            log_activity("Attempted Search")
        

def main_menu():
    while True:
        print('-'* 40)
        print("Please enter the number for the service you wish to execute.")
        print("1.To add item")
        print("2. To delete item")
        print("3. View replenish list")
        print("4. Stock Taking")
        print("5. Stock Replenish")
        print("6. Update Stock")
        print("7. Search")
        print("Enter 'done' once you are satisfied")
        req = input("Please enter the number: ")
        print('-'* 40)         
        if req == '1':
            add()
        elif req == '2':
            remove(lines)
        elif req == '3':
            replenish(lines)
        elif req == '4':
            stock_take()
        elif req == '5':
            stock_rep()
        elif req == '6':
            update()
        elif req == '7':
            search()
        elif req.lower() == 'done':
            break
        else:
            print("Invalid entry.")

while True:
    print('\t' + "WELCOME TO THE GROCERY MANAGMENT SYSTEM.")
    username = input("Please enter your user name (Enter 'shut down' to shut the system down): ")
    if username.lower() == "shut down" or username.lower() == "shutdown":
        break
    password = input("Please enter your password: ")
    for account in Accounts:
        if account[0] == username and account[1] == password:
            if account[2] == "Admin":
                print("Welcome Admin")
                admin_menu()
            elif account[2] == "Stocker":
                print("Welcome Stocker")
                stocker_menu()
            elif account[2] == "Buyer":
                print("Welcome Valued Customer")
                purchaser_menu()
            break
    else:
        print("Your username/password is incorrect.")