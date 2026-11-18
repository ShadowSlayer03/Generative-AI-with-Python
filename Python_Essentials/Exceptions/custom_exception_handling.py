class OutOfIngredientsError(Exception):
    pass

def brew_chai(milk, sugar):
    if milk ==0 or sugar ==0:
        raise OutOfIngredientsError("One or more ingredients not found")
    print("Brewing chai")


brew_chai(0,2)
