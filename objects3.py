class Song:
    """ Class to represent a song
    
    Attributes:
        title(str): The title of the song
        artist(Artist): an Artist object that represents the songs artist
        duration(int): How long the song is in seconds, may be zero
    """

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """Class to represent Albam, using its track list

    Attributes:
        album_name (str): The name of Album
        year (int): The year the album was released.
        artist: (Artist): The Artist responsible for the album
            If Not specified the default will be "Various Artists
        tracks (List[Song]):

    Methods:
        addSong: Used to add a new song to the album's track list
        """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """
        Add a song to the track list

        Args:
            song (Song): A song to add.
            position (Optional[int]): If used, the song will be added to that position in the track
            between other songs as needed else it will be added to the end of the track.
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Stores artists details

    Attributes:
        name (str): The name of the artist.
        albums (List[Album]): A list of albums by this artist.
        The list includes only those albums in this collection

    Methods:
        add_album: Use to add a new album to the artist's albums list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """
        Add a new album to the list.

        Args:
            album (Album): Album object to add to the list.
                If the album is already present, it will not add it again (future)
        """
        self.albums.append(album)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", 'r') as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:
                # We've just read details for a new artist
                # store the current album in the current artists collection then create a new artist object
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.name != album_field:
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)

            # create a new song object and add it to the current albums collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

        # After reading the last line of file, we will have an artist and album that haven't been stored - process now.

        if new_artist is not None:
            if new_artist is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)

    return artist_list

def create_checkfile(artist_list):
    """Create a check file from the object data for comparison with the original file"""

    with open("checkfile.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song), file=checkfile)




if __name__ == '__main__':
    artists = load_data()
    print("There are {} artists".format(len(artists)))

    create_checkfile(artists)