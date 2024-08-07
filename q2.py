# Q2: Take user input to add multiple elements to an array, then print the final array

user_array = []

n = int(input("How many elements do you want to add? "))

for _ in range(n):
    element = input("Enter an element: ")
    user_array.append(element)

print("Final array:", user_array)
