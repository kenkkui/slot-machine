MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

def deposit():
    while True:
        amount = input("What woud you like to deposit? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else: 
                print("Amount must be greater than 0.")
                print()
        else:
            print("Please enter a number")
            print()
  
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{str(MAX_LINES)})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
                print()
        else:
            print("Enter a number.")
            print()
    return lines

def get_bet():
    while True:
        amount = input("What woud you like to bet on each line? $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else: 
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
                print()
        else:
            print("Please enter a number")
            print()
  
    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = bet * lines
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

main()