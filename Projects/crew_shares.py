#BH 2nd Crew shares

members = float(input("How many crew members are there (not including the captain and first mate): "))
unrounded_money = float(input("How much money did your entire crew earn: "))

money = round(unrounded_money, 2)

shares = members + 10
share_value = money / shares 

captain_share = float(share_value * 7)
firstmate_share = float(share_value * 3)
crewmember_share = float(share_value - 500)
crew_cash = float(crewmember_share * members)

print("\n", "How much money was earned: ", money )
print("\n", "How many crew members are there (not including the captain and first mate): ", members)
print("\n", "The captain gets:", captain_share)
print("\n", "The first mate gets: ", firstmate_share)
print("\n", "Crew still needs: ", crew_cash)