season = input()
km_per_month = float(input())

total_amount = 0

if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        total_amount = km_per_month * 0.75
    elif season == "Summer":
        total_amount = km_per_month * 0.90
    else:
        total_amount = km_per_month * 1.05

if 5000 < km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        total_amount = km_per_month * 0.95
    elif season == "Summer":
        total_amount = km_per_month * 1.10
    else:
        total_amount = km_per_month * 1.25

if 10000 < km_per_month <= 20000:
    total_amount = km_per_month * 1.45

total_amount *= 4
total_amount *= 0.90

print(f"{total_amount:.2f}")