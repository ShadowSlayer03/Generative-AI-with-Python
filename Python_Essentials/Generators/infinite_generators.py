def infinite_chai():
    count = 1
    while True:
        yield f"Refill {count}"
        count+=1

user1 = infinite_chai()
user2 = infinite_chai()

for _ in range(5):
    print(next(user1))

print("\n")

for _ in range(10):
    print(next(user2))
