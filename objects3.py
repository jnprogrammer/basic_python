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

