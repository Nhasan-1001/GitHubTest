

# Average of all the list items

def Average (*lst):
    res = 0
    for i in range(len(lst)):
        res += lst[i]
    res = res / len(lst)
    print("Average of all the list element is: ",res)

sz = int(input("Enter the total number of list items: "))
l1 = []

for i in range(1, sz + 1):
    inp = int(input(f"Input {i}: "))
    l1.append(inp)
tup = tuple(l1)

Average(tup)