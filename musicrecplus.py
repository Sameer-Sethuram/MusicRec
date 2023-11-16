import os
import os

pref_file = 'musicrecplus.txt'

def file_verf():
    #Elian F
    if os.path.exists("musicrecplus.txt"):
        print("Database Found!")
    else:
        with open("musicrecplus.txt", "a+") as f:
            print('New file named musicrecplus.txt created!')


def get_menu():
    load_users(pref_file)
    while True:
        choice = input("""
        Enter a letter to choose an option: 
        e - Enter preferences
        r - Get recommendations
        p - Show most popular artists
        h - How popular is the most popular 
        m - Which user has the most likes
        q - Save and quit
        >>""")
        
        if choice == 'e':
            username = input("Enter your username: ")
            users = load_users(pref_file)
            get_pref(username, users)
        elif choice == 'r':
            # Assuming you pass current_user, prefs, and users to get recommendations
            
            get_rec(current_user, prefs, users)
        elif choice == 'p':
            # Show most popular artists 
            pass
        elif choice == 'h':
            # How popular 
            pass
        elif choice == 'm':
            # Which user has the most likes 
            pass
        elif choice == 'q':
            save_pref(username, prefs, users, pref_file)
            break

def load_users(file):
    #Elian F   
    users = {}
    with open(file, 'r+') as file:
        for line in file:
            user, band = line.strip().split(":")
            bands = band.split(",")
            bands.sort()
            users[user] = bands
    return users

def get_pref(username, users):
    if username in users:
        pref = users[username]
        print(f"Welcome back to musicrecplus, {username}!")
        get_menu()
    else:
        prefs = []
        print(f"Welcome to musicrecplus, {username}!")

        while True:
            new_pref = input("Please Enter Your Artist/Band (or press Enter to finish): ")
            if not new_pref:
                break
            prefs.append(new_pref.strip().title())
        
        users[username] = prefs
        print("Your preferences have been saved!")
        get_menu()
    return users

# Assuming load_users returns the dictionary of users
users = load_users(pref_file)
username = input("Enter your username: ")
updated_users = get_pref(username, users)
#TESTING CODE

def get_rec(current_user, prefs, users):
    #Elian F
    best_user = get_best_users(current_user, prefs, users)
    print(users[best_user])
    print(prefs)
    print(drop(users[best_user]))
    recommendations = drop(prefs, users[best_user])
    return recommendations

def get_best_users(current_user, prefs, users):
    pass  # Define how to match best users

def save_pref(username, prefs, users, file):
    with open(file, 'w') as f:
        for user, bands in users.items():
            bands_str = ",".join(bands)
            f.write(f"{user}:{bands_str}\n")

def drop(l1, l2):
    pass  # Define how to drop users
