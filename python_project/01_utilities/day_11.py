'''
🧠 Challenge: Friendship Compatibility Calculator

Build a Python script that calculates a fun "compatibility score" between two friends based on their names.

Your program should:
1. Ask for two names (friend A and friend B).
2. Count shared letters, vowels, and character positions to create a compatibiliy score (0-100).
3. Display the percentage with a themed message like:
    "Your're like chai and samosa - made for each other!" or
    "Well... opposites attract, maybe?"

Bonus:
- Use emojis in the result
- Give playful advice based on the scsore range
- Captitalize and center the final output in a framed box

'''

def friendship_score(name1, name2):
    name1, name2 = name1.lower(), name2.lower()
    score = 0
    shared_letters = set(name1) & set(name2)
    vowels = set("aeiou")

    score += len(shared_letters) * 5
    score += len(vowels & shared_letters) * 10

    return min(score, 100)
 
def run_friendship_calculator():
    print("❤️ Friendship Compatibility Calculator ❤️")
    name1 = input("Enter first name: ")
    name2 = input("Enter Second name: ")

    if not name1 or not name2:
        raise ValueError("Please Enter both names!")

    score = friendship_score(name1, name2)

    print(f"\nFriendship Compatibility Score {score}")

    if score >  80 :
        print("Your're like chai and samosa - made for each other!")
    elif score > 50:
        print("You are like a worm spies")
    else:
        print("Hey, maybe you like tea and your friend likes coffee—you are not going to gel together.")

run_friendship_calculator()

    