'''
A tea stall offers different prices for different cup sizes. Write a program that calculates the price based on size

Task:
- Input: "small", "medium", "large"
- Small -> 10Rs, Medium -> 15Rs, Large -> 20Rs
- If invalid: show "Unknown cup size"
'''

cup = input("Choose your cup size (small/medium/large): ").lower()

if cup == "small":
    print("Price is 10 rupees")
elif cup == "medium":
    print(("Price is 15 rupees"))
elif cup == "large":
    print("Price is 20 rupees")
else:
    print("Unknown cup size")