def infinite_chai():
    count = 1
    while True:
        yield f"Refil #{count}"
        count += 1

refill = infinite_chai()
user2 = infinite_chai()

for __ in range(3):
    print(next(refill))

for _ in range(6):
    print(next(user2))

