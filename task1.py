import json

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def create_dict(limit):
    primes = {}
    count = 1
    for num in range(2, limit + 1):
        if is_prime(num):
            primes[count] = num
            count += 1
    return primes

def save_to_json(primes, filename="primes.json"):
    with open(filename, "w") as f:
        json.dump(primes, f)

def load_from_json(filename="primes.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def menu():
    limit = int(input("Enter upper limit for primes: "))
    prime_dict = create_dict(limit)
    print(f"Prime dictionary created with {len(prime_dict)} entries.")
    
    while True:
        print("\nMenu:\n1. View all primes\n2. Get prime by position\n3. Search prime\n4. Save to file\n5. Load from file\n6. Exit")
        choice = input("Choose: ")
        
        if choice == "1":
            print(prime_dict)
        elif choice == "2":
            pos = int(input("Enter position: "))
            print(f"Prime at position {pos} is {prime_dict[pos]}")
        elif choice == "3":
            num = int(input("Enter prime number to search: "))
            for k, v in prime_dict.items():
                if v == num:
                    found = k
                    break
            else:
                found = 0
            print(f"Position: {found}" if found else "Not found")
        elif choice == "4":
            save_to_json(prime_dict)
            print("Primes saved.")
        elif choice == "5":
            prime_dict = load_from_json()
            # print(prime_dict)
            print("Primes loaded.")
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

menu()