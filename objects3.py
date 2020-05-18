class Song:
    """ Class to represent a song
    
    Attributes:
        title(str): The title of the song
        artist(Artist): an Artist object that represents the songs artist
        duration(int): How long the song is in seconds, may be zero
    """

    def __init__(self, title, artist, duration=0):
        """Song init method

        Args:
            title(str): Inits the title attribute
            artist(Artist): At Artist object representing the song's creator.
            duration(Optional(int): initial value will be zero if not specified
            """
        self.title = title
        self.artist = artist
        self.duration = duration
