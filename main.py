print("================================")
print("       PROFESSOR MIA")
print("================================")

name = input("What is your name? ")

print()
print("Hello", name + "!")
print("Welcome to Professor Mia.")
print()

print("What subject do you want to study?")
print("1. Maths")
print("2. Biology")
print("3. Computer Science")
print("4. Chemistry")

choice = input("Choose a subject: ")

if choice == "1":
    subject = "Maths"
elif choice == "2":
    subject = "Biology"
elif choice == "3":
    subject = "Computer Science"
elif choice == "4":
    subject = "Chemistry"
else:
    subject = "Unknown"

print()
print("You selected:", subject)
print("Let's start learning!")