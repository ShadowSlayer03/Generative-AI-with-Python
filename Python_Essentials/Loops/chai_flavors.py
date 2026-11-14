chai_flavors = ["ginger", "elaichi", "cinnamon"]
out_of_stock_flavors = ["chocolate","vanilla"]
discontinued_flavors = ["mango"]


for i in range(2):
    user_chai = input("Enter the chai flavor you would like:\n")
    if user_chai in chai_flavors:
        print(f"Requested {user_chai} chai available! Preparing...")
    elif user_chai in out_of_stock_flavors:
        continue
    elif user_chai in discontinued_flavors:
        break
