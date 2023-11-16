import os

def file_verf():
    #Elian F
    if os.path.exists("musicrecplus.txt"):
        print("DataBase Found!")
    else:
        f = open("musicrecplus.txt", "a+") 
        print('New file named musicrecplus.txt created!')
pref_file = 'musicrecplus.txt'

    
def load_users(file):
    #Elian F
    file = open('musicrecplus.txt', 'r+')
    users = {}

    for line in file:
        user, band = line.strip().split(":")
        bands = band.split(",")
        bands.sort()
        users[user] = bands
    return users
def get_pref(username, users):
    new_pref = ''
    if username in users:
        pref = users[username]
        print(f"Welcome back to musicrecplus {username}!")
        get_menu(current_user=username, pref=pref, users=users)
    else:
        prefs = []
        print(f"Welcome to musicrecplus {username}!")
        new_pref = input("Please Enter Your Artist/Bands: ")
        while new_pref != " ":
            prefs.append(new_pref.strip().title())
            print("Please Enter Another Artist/Bands: ")

        

def get_rec(current_user, prefs,users):
    pass

def match_best_users(cuurrent_user, prefs, users):
    pass


def save_pref(username, prefs, users, file):
    pass


def get_menu():

    choice = input("""
    Enter a letter to choose an option: 
    e - Enter preferences
    r - Get recommendations
    p - Show most popular artists
    h - How popular is the most popular 
    m - Which user has the most likes
    q - Save and quit
    >>""")
    if choice == 'r':
        users = load_users(pref_file)
        current_user = input("Please Enter Your Username: ")
        prefs = get_pref(current_user, users)
        get_rec(current_user, prefs, users)
    elif choice == 'p':
        pass
    elif choice == 'h':
        pass
    elif choice =='m':
        pass
    elif choice == 'q':
            save_pref(current_user, prefs, users, pref_file)
        
        
print(get_menu())

def main():
    file_verf()
    users = load_users(pref_file)
    print("Welcome To Music Recommendator")

    username = input("Please Enter Your Username: ")
    print(f"Welcome {username} to Music Recommendator")
    