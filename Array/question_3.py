max_num = int(input("Max number :"))
odd = []
for num in range(max_num+1):
    if num % 2 != 0:
        odd.append(num)

print(odd)
