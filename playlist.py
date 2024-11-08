
songs = ["A", "B", "C", "D", "E"]

def button1():
    song.append(songs.pop(0))
def button2():
    songs.insert(songs.pop(-1))
def button3():
    pass
def button4():
    pass
def button5():
    for song in songs:
        print(song)

print("""enter a number b/w 1 and 5
1: will move the ...
2: will ...
3: will ...
4: will ...
you can repeat 1 through 4 as many times as you like,
5 will play the songs in the...""")

option = ''

while option != '5':
    if option == '1':
        button1()
    elif option == '2':
        button2()
    elif option == '3':
        button3()
    elif option == '4':
        button4()
    elif option == '5':
        break
    else:
        print("invalid input :( try again")
        
