cup_sizes = ["small", "medium", "large"]
cup_prices = (10,15,20)

print("Welcome to Chai Price Calculator!\n")

chai_size = input("What size of chai do you want to order?\n").lower()

if chai_size in cup_sizes:
    print("Calculating price......")
    for index,item in enumerate(cup_sizes):
        if chai_size == item:
            print(f"The price for {chai_size} cup of tea is Rs {cup_prices[index]}")
            break
else:
    print("Unknown cup size")
