order_amnt = int(input("Enter your order amount:\n"))

is_delivery_free = True if order_amnt >= 300 else False

if is_delivery_free:
    print("Delivery is free")
else:
    print("Delivery fee - Rs 30")