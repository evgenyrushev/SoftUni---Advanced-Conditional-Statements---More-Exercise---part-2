season = input()
group = input()
kids_number = int(input())
sleep_nights = int(input())

sport = ""
vacation_price = 0

if season == "Winter":
    if group == "boys" or group == "girls":
        vacation_price = kids_number * sleep_nights * 9.60
    else:
        vacation_price = kids_number * sleep_nights * 10

if season == "Spring":
    if group == "boys" or group == "girls":
        vacation_price = kids_number * sleep_nights * 7.20
    else:
        vacation_price = kids_number * sleep_nights * 9.50

if season == "Summer":
    if group == "boys" or group == "girls":
        vacation_price = kids_number * sleep_nights * 15
    else:
        vacation_price = kids_number * sleep_nights * 20

if kids_number >= 50:
    vacation_price *= 0.50
elif 20 <= kids_number < 50:
    vacation_price *= 0.85
elif 10 <= kids_number < 20:
    vacation_price *= 0.95

if season == "Winter":
    if group == "girls":
        sport = "Gymnastics"
    elif group == "boys":
        sport = "Judo"
    else:
        sport = "Ski"

if season == "Spring":
    if group == "girls":
        sport = "Athletics"
    elif group == "boys":
        sport = "Tennis"
    else:
        sport = "Cycling"

if season == "Summer":
    if group == "girls":
        sport = "Volleyball"
    elif group == "boys":
        sport = "Football"
    else:
        sport = "Swimming"

print(f"{sport} {vacation_price:.2f} lv.")