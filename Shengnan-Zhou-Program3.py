# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 3: Msuic CSV Library
# Shengnan Zhou
# Last Modified: June 21, 2018
# ---------------------------------------
# With users' input, direct to differene
# output with different functions.
# User could search for the longest song,
# the amount of song in the year they
# enter, and all the songs by the
# artist they enter.
# ---------------------------------------

# longest song

def longest_song():
    music_file = open("music.csv", "r")

    line = music_file.readline().split(",")

    songs = {}
    for each_line in music_file:
        song = each_line.split(",")
        title = song[-2]
        duration = round(float(song[9]))
        songs[title] = duration

    longest_duration = 0
    print_title = ""
    for duration in songs.values():
        if duration > longest_duration:
            longest_duration = duration

    for title, duration in songs.items():
        if duration >= longest_duration:
            print_title += title + " / "

    print("Title: " + print_title)
    print("Length to nearest second:", longest_duration)

    music_file.close()

# --------------------------------------

# song by year

def songs_by_year(year):
    music_file = open("music.csv", "r")

    line = music_file.readline().split(",")

    number_of_songs = 0
    for each_line in music_file:
        song = each_line.split(",")
        if year == int(song[-1]):
            number_of_songs += 1

    print("The number of songs from", year, "is", number_of_songs)

    music_file.close()

# --------------------------------------

# all songs by artist

def all_songs_by_artist(artist):
    music_file = open("music.csv", "r")

    line = music_file.readline().split(",")
    song_list = []

    for each_line in music_file:
        song = each_line.split(",")
        if artist == song[2].lower():
            song_list.append(song[-2])

    song_list.sort()

    print()
    print("Songs In Alphabetical Order")
    print("---------------------------")

    number = 1
    for i in song_list:
        print(str(number) + ". " + i)
        number += 1

    if song_list == []:
        print("There are no songs by this artist.")

    print("---------------------------")

    music_file.close()

# --------------------------------------

def menu():
    print()
    print("1. Identify longest song.")
    print("2. Identify number of songs in a given year.")
    print("3. Identify all songs by a given artist.")
    print("4. You choose something that is interesting and non-trivial.")
    print("5. Quit.")

# --------------------------------------

def main():
    choice = 0
    while (choice != 5):
        menu()
        choice = int(input("Enter your choice: "))
        if (choice == 1):
            longest_song()
        elif (choice == 2):
            year = int(input("Enter desired year: "))
            songs_by_year(year)
        elif (choice == 3):
            artist = input("Enter name of artist: ").lower()
            all_songs_by_artist(artist)
        elif (choice == 4):
            pass
        elif (choice != 5):
            print("That is not a valid option.  Please try again.")

# --------------------------------------

main()
