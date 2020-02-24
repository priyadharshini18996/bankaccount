import time

true = ["T", "t", "True"]
false = ["F", "f", "False"]
correct = 0 

name = input ("What's your name?") #user name

print ("\nOK, " +  name +", let's get started. Remember, the following answers are only True or False.")
time.sleep(2)

print ("\n The longest dam in India is Hirakud Dam   .")
choice = input(">>> ")
if choice in true:
  correct += 1 #If correct, the user gets one point
else:
  correct += 0
  
print ("\n Vatican City Smallest country in the world.")
choice = input(">>> ")
if choice in true:
  correct += 1
else:
  correct += 0  

print ("\nMumbai is known as Electronic City of India?   ")
choice = input(">>> ")
if choice in false:
  correct += 1
else:
  correct += 0 
  
print ("\nIndira Gandhi Centre for Atomic Research is located at  Kalpakkam.")
choice = input(">>> ")
if choice in true:
  correct += 1
else:
  correct += 0  
  
print ("\n  The largest and the oldest museum of India is located in West Bengal.")
choice = input(">>> ")
if choice in true:
  correct += 1
else:
  correct += 0
  
print ("\nThe famous Eiffel Tower is in France.")
choice = input(">>> ")
if choice in false:
  correct += 1
else:
  correct += 0
    
print ("\nYou're finished, " + name +". You got", correct, "out of 6 correct.")