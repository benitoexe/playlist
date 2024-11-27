songs = ["A", "B", "C", "D", "E"]

#button 1 moves the first song to the end
def button1():
    songs.append(songs.pop(0))

#button 2 moves the last song to the beginning 
def button2():
    songs.insert(0, songs.pop(-1))

#button 3 shuffles the playlist
import random
def button3():
    random.shuffle(songs)
    print("Playlist shuffled!")

#button 4 restores the order of the playlist
original_songs = ["A", "B", "C", "D", "E"]
def button4():
    global songs
    songs = original_songs[:]
    print("Playlist restarted!")

#button 5 shows all songs in the playlist
def button5():
    print("\nCurrent Playlist:")
    for song in songs:
        print(song)

#printing menu instructions
print("""Enter a number between 1 and 5:
1: Move the first song to the end
2: Move the last song to the beginning
3: Shuffle the playlist
4: Restart the playlist
5: Display the playlist and exit
""")

#loop 
option = ''
while option != '5':
    option = input("Choose an option (1-5): ").strip()
    if option == '1':
        button1()
    elif option == '2':
        button2()
    elif option == '3':
        button3()
    elif option == '4':
        button4()
    elif option == '5':
        button5()
        break
    else:
        print("Invalid input. Please try again.")
