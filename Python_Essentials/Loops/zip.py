names = ["Arjun", "Kunal", "Prashant"]
bills = [20,200,58]

for name,amount in zip(names, bills):
    print(f"{name} paid this amount {amount}")