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
    file = open('musicrecplus.txt', 'r+')
    users = {}

    for line in file:
        user, band = line.strip().split(":")
        bands = band.split(",")
        bands.sort()
        users[user] = bands
    return users
file_verf()
print(load_users("musicrecplus.txt"))

def get_pref(username, users):
    pass

def get_rec(current_user, prefs,users):
    pass

def match_best_users(cuurrent_user, prefs, users):
    pass

def drop(l1, l2):
    pass

def numMatch(l1, l2):
    pass

def save_pref(username, prefs, users, file):
    pass

def main():
    file_verf()
    users = load_users(pref_file)
    print("Welcome To Music Recommendator")

    username = input("Please Enter Your Username: ")
    print(f"Welcome {username} to Music Recommendator")
    pref = get_pref(username, users)