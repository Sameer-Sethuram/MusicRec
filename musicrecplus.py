import os
from os import path

pref_file = 'musicrecplus.txt'


def file_verf():
    #Elian F
    if os.path.exists("musicrecplus.txt"):
        print("Database Found!")
    else:
        with open("musicrecplus.txt", "a+") as f:
            print('New file named musicrecplus.txt created!')

def load_users(file):
    #Elian F   
    users = {}
    with open(file, 'a+') as file:
        for line in file:
            user, band = line.strip().split(":")
            bands = band.split(",")
            bands.sort()
            users[user] = bands
    return users

def get_menu(name, preferences):
    '''This function displays the menu'''
    #Luke Morella
    if preferences == [] or preferences.strip() == '':
        preferences = newList()
        preferences.sort()
    x = 0
    while x == 0:
        print("Enter a letter to choose an option:\ne - Enter preferences\nr - Get recommendations\np - Show most popular artists\nh - How popular is the most popular\nm - Which user has the most likes\nq - Save and quit")
        selection = input()
        if selection == "e":
            preferences = newList()
            preferences.sort()
        elif selection == "r":
            get_recommendations(preferences, name)
        elif selection == "p":
            get_mostpopularartist(preferences, name)
        elif selection == "h":
            get_howpopular(preferences, name)
        elif selection == "m":
            get_mostlikes(name, len(preferences))
        elif selection == "q":
            saveandquit(username, prefs, users, file)
            x = 1
        else:
            print("Invalid value")


def get_preference(username, users):
    #Elian F
    if '$' in username:
        print("Your preferences have been privated!")
    if username in users:
        pref = users[username]
        print(f"Welcome back to musicrecplus, {username}!")
    else:
        prefs = []
        print(f"Welcome to musicrecplus, {username}!")

        while True:
            new_pref = input("Please Enter Your Artist/Band (press enter to finish): ")
            if not new_pref:
                break
            prefs.append(new_pref.strip().title())

        users[username] = prefs
        print("Your preferences have been saved!")
    return users

def get_recommendations(database):
    ''' Gets recommendations for the user '''
    #Sameer Sethuram
    best_user = get_best_users(database)
    L1 = database[username]
    L2 = database[best_user]
    recommendations = list(filter(lambda x: x not in L1 , L2))
    if recommendations== []:
        return "No recommendatios available at this time."
    return recommendations

def get_best_users(database):
    ''' Gets the user that is most similar to the current user's taste '''
    # Sameer Sethuram
    similarity = [0, '']

    for member in database:
        temp = 0
        if member[-1] == '$' or member == username:
            continue
        if database[member] == database[username]:
            continue
        for pref in database[member]:
            if pref in database[username]:
                temp += 1
        if temp > similarity[0]:
            similarity = [temp, member] #list(filter(lambda x: x not in users[username] , users[member])]

    return similarity[1]

def get_mostpopularartist(preferences, users):
    '''This function prints the top 3 artists liked by the most users'''
    #Luke Morella
    database = open('musicrecplus.txt', 'a+')
    artists = {}
    if type(preferences) != list:
        x = preferences.split(',')
    else:
        x = preferences
    for i in x:
        i = i.strip()
        if i in artists:
            artists[i] += 1
        else:
            artists[i] = 1
    for line in database:
        x = line.split(':')
        if '$' not in x[0] and x[0].lower().strip() != name.lower().strip():
            y = x[1].split(',')
            for i in y:
                i = i.strip()
                if i in artists:
                    artists[i] += 1
                else:
                    artists[i] = 1
    if len(artists) == 0:
        print('Sorry, no artists found.')
    first = ('', 0)
    second = ('', 0)
    third = ('', 0)
    for i in artists:
        if artists[i] > first[1]:
            first = (i, artists[i])
        elif artists[i] > second[1]:
            second = (i, artists[i])
        elif artists[i] > third[1]:
            third = (i, artists[i])
    if first[0] != '':
        print(first[0].strip())
    if second[0] != '':
        print(second[0].strip())
    if third[0] != '':
        print(third[0].strip())

def get_howpopular(preferences, name):
    '''This function returns how popular the most popular artist is (only number)'''
    #Luke Morella
    database = open('musicrecplus.txt', 'a+')
    artists = {}
    for i in preferences:
        i = i.strip()
        if i in artists:
            artists[i] += 1
        else:
            artists[i] = 1
    for line in database:
        x = line.split(':')
        if '$' not in x[0] and x[0].lower().strip() != name.lower().strip():
            y = x[1].split(',')
            for i in y:
                #print(i)
                i = i.strip()
                if i in artists:
                    artists[i] += 1
                else:
                    artists[i] = 1
    if len(artists) == 0:
        print('Sorry, no artists found.')
    first = ('', 0)
    for i in artists:
        if artists[i] > first[1]:
            first = (i, artists[i])
    print(first[1])


def get_mostlikes(name, number):
    '''This function returns the print of the full name(s) of the user(s) who
like(s) the most artists'''
    #Luke Morella
    database = open('musicrecplus.txt', 'a+')
    highest_likes = (name, number)
    for ln in database:
        x = ln.split(':')
        y = x[1].split(',')
        if '$' not in x[0]:
            if len(y) > highest[1]:
                highest = (x[0], len(y))
    print(highest[0])


    
def saveandquit(username, prefs, users, file):
    #Elian F
    with open(file, 'w') as f:
        for user, bands in users.items():
            bands_str = ",".join(bands)
            f.write(f"{user}:{bands_str}\n")
            
def drop(l1, l2):
    pass  # Define how to drop users

if __name__ == "__main__":
    file_verf()
    users = load_users(pref_file)
    username = input("Enter your username: ")
    users = get_preference(username, users)
    get_menu(username, users)
