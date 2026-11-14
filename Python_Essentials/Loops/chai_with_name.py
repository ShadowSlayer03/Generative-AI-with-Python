name_list = []

for i in range(10):
    name = input("Input a name for the customer: ")
    name_list.append(name)

for i in range(len(name_list)):
    print(f"Order ready for {name_list[i]}")