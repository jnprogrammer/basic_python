welcome = "Welcome to my Nightmare" , "Alice Cooper", 1975
bad = "Bad Company" "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981

imdela = "More Mayhem", "imilda May", 2011, ([(1, "Pulling the rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Walz")])
# You can't change a tuple, but you can add to a list of tuples.
print(imdela)

title, artist, year, tracks = imdela
for song in tracks:
    track, title = song
    print("\tTrack number {}, Title: {}".format(track, title))

print("=" * 50)

imdela[3].append((5, "All for you"))
for song in tracks:
    track, title = song
    print("\tTrack number {}, Title: {}".format(track, title))

print("=" * 50)

imdela[3].append((6, "Eternity"))
for song in tracks:
    track, title = song
    print("\tTrack number {}, Title: {}".format(track, title))

metallica = "Ride the lighting", "Metallica", 1984

# title, artist, year = imdela
# print(title)


# print(artist)
# print(year)
# print(track1)
# print(track2)
# print(track3)
# print(track4)


