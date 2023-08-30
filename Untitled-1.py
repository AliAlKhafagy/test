"""print("hej")
print("Ali")
print("Tjabba")

#lägger man till upper.() så blir allt i stora bokstäver.
citat =" datatyper har inbyggda metoder "
print (citat.upper())
#Hur man avrundar till ett heltal.
UserNumber = float(input("Enter a number:  "))
NärmasteHeltal = round(UserNumber)
print("Här är närmaste heltal", NärmasteHeltal)

#Input är frågor där användaren matar in svar.
print("Hello!")
myName= input("What is your name?: ")
myLast = input ("Cool! What is your last name?: ")
print("Nice to meet you",myName, myLast)

#program som räknar ut om hur många år du fyller 18
myAge = int(input ("How old are you?: "))
adulthood = 18 - myAge
if adulthood > 0:
    print (f"You are 18 in {adulthood} years!") 
"""
#Konstruera ett program i vilken en användare matar in fem heltal. 
# Avgör med den matematiska standardfunktionen max det högsta
# inmatade talet och presentera detta för användaren.

A = int (input ("Please enter a number:"))
B = int (input("Please enter another number: "))
C = int (input("And yet another number: "))
D = int (input("Please enter your fourth number: "))
E = int (input("Please enter your last number: "))
numbers = [A,B,C,D,E]
maximum_number = max(numbers)
print("The biggest number you have entered is:", maximum_number)