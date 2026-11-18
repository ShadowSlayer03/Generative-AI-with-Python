chai_menu = {"masala": 30, "ginger": 20, "lemon": 10}

print("Program starts")
try:
    print(chai_menu["elaichi"])
except KeyError as e:
    print("Exception occurred:", e)
finally:
    print("Program ended")
