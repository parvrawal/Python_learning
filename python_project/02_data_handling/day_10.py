'''
Challenge: Offline Notes Locker

Create a terminal-based app that allows users to save, view, and search personal notes securely in an encrypted file.

Your program should:
1. Let users add notes with title and content.
2. Automatically encrypt each note using Fernet (AES under the hood).
3. Store all encrypted notes in a single `.vault` file (JSON format)
4. Allow listing of titles and viewing/decrypting selected notes.
5. Support searching by title or keyword.

Bonus:
- Add timestamps to notes.
- Use a master password to unlock vault (optional).
'''

import json
import os
from cryptography.fernet import Fernet
from datetime import datetime


VALUT_FILE = "notes_vault.json"
KEY_FILE = "vault.key"

def load_or_create_key():
    if not os.path.exists(KEY_FILE):
        key =  Fernet.generate_key()
        with open(KEY_FILE, "wb") as f: # wb means write a binary file
            f.write(key)

    else:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
    
    return Fernet(key)

    
fernet =load_or_create_key()

def load_vault():
    if not os.path.exists(VALUT_FILE):
        return []
    with open(VALUT_FILE, 'r', encoding="utf-8") as f:
        return json.load(f)
    

def save_vault(data):
    with open(VALUT_FILE, 'w', encoding= "utf-8") as f:
        json.dump(data, f, indent=2)

def add_note():
    title = input("Enter note title: ").strip()
    content = input("Enter note content: ").strip()

    encrypted_title = fernet.encrypt(title.encode()).decode()
    encrypted_content = fernet.encrypt(content.encode()).decode()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = load_vault()
    data.append({
        "title": encrypted_title,
        "content": encrypted_content,
        "timestamp": timestamp
    })

    save_vault(data)
    print("✅ Data saved")


def list_notes():
    data = load_vault()
    if not data:
        print("No notes yet")

    for i, note in enumerate(data, 1):
        raw_note = note['title']
        decrypted_note = fernet.decrypt(raw_note.encode()).decode()

         
        print(f"{i}. {decrypted_note} {note["timestamp"]}")

    


def view_note():
    list_notes()
    try:
        index = int(input("Enter note number to view: ")) - 1
        data = load_vault()
        if 0 <= index <= len(data):
            encrypted_title = data[index]['title']
            encrypted_content =data[index]["content"]
            decrypted_title = fernet.decrypt(encrypted_title.encode()).decode()
            decrypted_content = fernet.decrypt(encrypted_content.encode()).decode()
            print(f"\n 📝 {decrypted_title} - {data[index]['timestamp']} \n\n {decrypted_content}")
        else:
            print("Invalid selection ")

    except:
        print("Invalid input")

# def search_note():
#     keyword =input("Enter the keyword to search: ").strip().lower()
#     data = load_vault()
#     found = [note for note in data if keyword in note['title'].lower()]
#     if not found:
#         print("No matching notes")
#     else:
#         for note in found:
#             print(f"{note['title']} {note['timestamp']}")

def search_note():
    keyword = input("Enter the keyword to search: ").strip().lower()
    data = load_vault()

    found = []
    for note in data:
        decrypted_title = fernet.decrypt(note["title"].encode()).decode()
        if keyword in decrypted_title.lower():
            found.append({
                "title": decrypted_title,
                "timestamp": note["timestamp"]
            })

    if not found:
        print("No matching notes")
    else:
        for note in found:
            print(f"{note['title']} {note['timestamp']}")

def main():
    while True:
        print("\n 🔒Offline Notes Locker")
        print("1. Add Note")
        print("2. List Notes")
        print("3. View Note")
        print("4. Search Notes")
        print("5. Exist")

        choice = input("Enter an option: ").strip()

        match choice:
            case "1":
                add_note()
            case "2":
                list_notes()
            case "3":
                view_note()
            case "4":
                search_note()
            case "5":
                break
            case _:
                print("Invalid input")


if __name__ == "__main__":
    main()
