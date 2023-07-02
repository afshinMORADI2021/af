password = input("Enter new password :")
results = {}
if len(password) >= 8:
    results["lenght"] = True
else:
    results["lenght"] = False
digit = False
for i in password:
    if i.isdigit():
        digit = True
results["digit"]= digit
uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

results["upper-case"] = uppercase
print(results)
print(all(results.values()))

if all(results):
    print("Strong")
else:
    print("Weak")




