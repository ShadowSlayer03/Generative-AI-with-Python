def chai_customer():
    print("Welcome! What chai do you like?")
    # program stops here expecting a value
    order = yield
    while True:
        print(f"Preparing: {order}")
        # program stops here too expecting a value
        order = yield

stall = chai_customer()
next(stall)

stall.send("Masala Chai")
stall.send("Lemon Chai")
stall.send("Ginger Chai")
