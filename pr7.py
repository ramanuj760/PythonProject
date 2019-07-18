"""write a program  that print all the numbers from 0 to 6 except 3 and 6."""
a=0
for a in range(7):
    if a==3 or a==6:
        continue

    print(a)

