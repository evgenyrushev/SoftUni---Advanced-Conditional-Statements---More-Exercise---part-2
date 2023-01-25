budget = float(input())
season = input()

total_amount = 0
location = ""
sleep = ""

if budget <= 1000:
    sleep = "Camp"
    if season == "Summer":
        location = "Alaska"
        total_amount = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        total_amount = budget * 0.45

if 1000 < budget <= 3000:
    sleep = "Hut"
    if season == "Summer":
        location = "Alaska"
        total_amount = budget * 0.80
    elif season == "Winter":
        location = "Morocco"
        total_amount = budget * 0.60

if budget > 3000:
    sleep = "Hotel"
    if season == "Summer":
        location = "Alaska"
        total_amount = budget * 0.90
    elif season == "Winter":
        location = "Morocco"
        total_amount = budget * 0.90

print(f"{location} - {sleep} - {total_amount:.2f}")




