'''
Challenge: Offline Credential Manager

Create a CLI tool to manage login credentials (website, username, password) in an encoded local file (`vault.txt`).

Your program should:
1. Add new credentials (website, username, password)
2. Automatically rate password strength (weak/medium/strong)
3. Encode the saved content using Base64 for simple offline obfuscation
4. View all saved credentials (decoding them)
5. Update password for any existing website entry (assignment)

Bonus:
- Support searching for a website entry
- Mask password when showing in the list
'''

import base64
import os

VALUT_FILE = "vault.txt"

def encode(text):
    encoded = base64.b64encode(text.encode()).decode() #decode just converting text into regular string
    return encoded

def decode(text):
    decoded = base64.b64decode(text.encode()).decode()
    return decoded

def password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*().,<>" for c in password)

    score = sum([length >= 8, has_upper, has_digit, has_special])
    return ["Weak", "Medium", "Strong", "Very Strong"][min(score, 3)]

def add_credential():
    website = input("Website: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    strength = password_strength(password)

    line = f"{website} || {username} || {password}"
    encoded_line = encode(line)


    with open(VALUT_FILE, 'a', encoding="utf-8") as f:
        f.write(encoded_line + "\n")
    print("✅ Creadential saved")

def view_credentials():
    if not os.path.exists(VALUT_FILE):
        print("File not found")
        return
    with open(VALUT_FILE, 'r', encoding="utf-8") as f:
        for line in f:
            decoded = decode(line.strip())
            website, username, password = decoded.split("||")
            hidden_password = "*" * len(password)
            print(f"{website} | {username} | {password}")

def update_credentials():
    site = input("Enter the site which you wants to update: ").strip()
    if not site:
        print("Please enter the site!")
        return
    

    if not os.path.exists(VALUT_FILE):
        print("No credentials found!")
        return
    
    updated = False
    new_lines = []

    with open(VALUT_FILE, 'r', encoding="utf-8") as f:
        for line in f:
            decoded = decode(line.strip())

        website, username, password = [x.strip() for x in decoded.split("||")]

        if website.lower() ==  site.lower():
            print(f"Found {website} Current username: {username}, password: {password}")
            new_username = input("Enter new username: ").strip()
            new_password = input("Enter new password: ").strip()

            new_line = f"{website} || {new_username} || {new_password}"
            new_lines.append(encode(new_line) + "\n")
            updated = True 
        else:
            new_lines.append(line)

    if updated:
        with open(VALUT_FILE, 'w',encoding="utf-8") as f:
            f.writelines(new_lines)
        print("✅ Credential updated successfully!")
    else:
        print("❌ site not found in vault!")

def main():
    while True:
        print("\n🔒 Credential Manager")
        print("1. Add credential")
        print("2. View credentials")
        print("3. Update password")
        print("4. Exist")

        choice = input("Enter your choice: ")


        match choice:
            case "1":
                add_credential()
            case "2":
                view_credentials()
            case "3":
                update_credentials()
            case "4":
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()