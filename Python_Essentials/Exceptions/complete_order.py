class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu = {"masala": 20, "ginger": 30}
    try:
        if flavor not in menu:
            raise InvalidChaiError("Flavor not found")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an integer")
        total = menu[flavor] * cups
        print(f"Your bill for {cups} cups of {flavor} chai: rupees {total}")
    except Exception as e:
        print("Error:", e)
    finally:
        print("Thank you for visiting")

bill("ginger", 4)
bill("ginger", "4")
bill("lemon", "4")
