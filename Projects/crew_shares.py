#BH 2nd Crew shares

members = float(input("How many crew members are there:"))
money = float(input("How much money did your crew earn in total: "))

shares = members + 10
share_value = money / shares 
print(share_value)

captain_share = float(input(share_value * 7))
firstmate_share = float(input(share_value * 3))
cerwmember_share = float(input(share_value - 500))

print("How much money was earned:", money )
print("\n\n", "How many crew members are there (not including the captain and first mate): ")