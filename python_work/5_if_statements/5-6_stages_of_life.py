person_age = 5 
baby_message = "You are a baby."
toddler_message = "You are a toddler."
kid_message = "You are a kid."
teenager_message = "You are a teenager."
adult_message = "You are an adult."
elder_message = "You are an elder."

if person_age < 2:
    print(baby_message)
elif person_age >= 2 and person_age < 4:
    print(toddler_message)
elif person_age >= 4 and person_age < 13:
    print(kid_message)
elif person_age >= 13 and person_age < 20:
    print(teenager_message)
elif person_age >= 20 and person_age < 65:
    print(adult_message)
elif person_age >= 65:
    print(elder_message)