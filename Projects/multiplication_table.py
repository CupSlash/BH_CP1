#BH 2nd Multiplication Table

table = ()

for table in range (1,13):
    for x in range (1,13):
        print(f"{table * x:4}", end="")
    print()