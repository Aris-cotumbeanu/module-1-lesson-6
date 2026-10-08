# ============================================
# SWIMMING POOL ENTRY CHECKER
# ============================================

print("=== Swimming Pool Entry Checker ===")
print("Answer 3 questions and I will tell you which pool you can use.\n")


# ---------- collect the three answers ----------
age = int(input("How old are you? "))
can_swim = input("Can you swim 25 metres? (yes / no): ").lower()
adult_here = input("Is an adult with you? (yes / no): ").lower()

print()
print("=== Entry Decision ===")
print("-" * 32)


# ---------- PART 1: age group, using if / elif / else on a NUMBER ----------
# Order matters: we must check the youngest limits first
if age < 4:
    age_group = "Toddler"
elif age < 12:
    age_group = "Child"
elif age < 18:
    age_group = "Teen"
else:
    age_group = "Adult"


# ---------- PART 2: did they actually answer yes or no? ----------
if can_swim != "yes" and can_swim != "no":
    print("Error: Input for swimming capability not understood.")
    swim_known = False
else:
    swim_known = True

if adult_here != "yes" and adult_here != "no":
    print("Error: Input for accompanying adult not understood.")
    adult_known = False
else:
    adult_known = True


# ---------- PART 3: AND - the deep pool ----------
# Allowed only when they CAN swim AND an adult IS present.
deep_pool_allowed = (can_swim == "yes" and adult_here == "yes")


# ---------- PART 4: OR - the shallow end ----------
# Warn when they are under 12 OR they cannot swim.
if age < 12 or can_swim == "no":
    print("Warning: Extra supervision or caution recommended in the shallow end.")


# ---------- PART 5: NOT - the lifeguard reminder ----------
# Remind when there is no adult - but only if adult_known is True.
if adult_known and adult_here != "yes":
    print("Lifeguard Reminder: Please pay extra attention to safety signs since no adult is accompanying you.")


# ---------- PART 6: the final verdict ----------
if not swim_known or not adult_known:
    print("Verdict: Cannot make a decision due to invalid input answers.")
else:
    if age_group == "Toddler":
        print("Verdict: Splash pool only, always with an adult.")
    elif age_group == "Child":
        if adult_here == "yes":
            print("Verdict: Allowed in the main pool with an adult.")
        else:
            print("Verdict: Access denied. Children must be accompanied by an adult.")
    elif age_group == "Teen":
        if can_swim == "yes":
            print("Verdict: Allowed in the main pool alone.")
        else:
            print("Verdict: Main pool allowed only if accompanied by an adult, or stick to the splash pool.")
    else:  # Adult
        print("Verdict: All pools open to you.")


print()
print("Have a safe swim!")