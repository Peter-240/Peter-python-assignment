lst = []
for i in range(1, 21):
    lst.append(i)

lst = [n for n in lst if n % 2 == 0]  # remove odd
lst.sort(reverse=True)
print(lst[:3])  # top 3
