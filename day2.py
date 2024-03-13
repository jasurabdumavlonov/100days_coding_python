age = input("Enter your age: ")

age_int = int(age)

years = 90 - age_int
months = years * 12
weeks = years * 52
days = years * 365

print(f"You have {years} years or {months} months or {weeks} weeks or {days} days...")
