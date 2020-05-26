for i in range(5):
    print(i)

names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(name)

s = set()
s.add(1)
s.add(2)
s.add(1)
s.add(6)
s.add(0)
print(s)

ages = {"Alice": 22, "Bob": 27}
ages["Charlie"] = 30
ages["Alice"] += 1
print(ages)
