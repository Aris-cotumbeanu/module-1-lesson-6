day     = input("What day is it? (monday to sunday):").strip().capitalize()
wearther    = input("whatis the weather? (sunny/rainy/cloudy)").strip().lower()
homework    = input("is your homework done? (yes/no):").strip().lower()

print()
print(f"=== your plan for {day}===")
print("_" * 35 )

if day in ("Saturday", "Sunday"):
    print("day type     :weekend- enjoy your free time!")
elif day == "Monday":
    print("day type     :first day of the week.pack your weekly planner.")
elif day == "Friday":
    print("day type     :last day of school for the week.")
elif day == "Friday":
    print("day type     :middle of the week, keep pushing")
elif day == ("Tuesday", "Wednesday", "Thursday"):
       print("day type     :middle of the week, keep pushing")
else:
     print("day type    : day not regonised. please check spelling.")