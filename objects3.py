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
            print(artist_field, album_field, year_field, song_field)


if __name__ == '__main__':
    load_data()
