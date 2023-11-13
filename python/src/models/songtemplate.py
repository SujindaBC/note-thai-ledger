class SongTemplate:
    def __init__(self, title, writer, tempo=None, rhythm=None):
        self.title = title
        self.writer = writer
        self.tempo = tempo
        self.rhythm = rhythm
        self.table = []
        
    def log_song_info(self):
        print(f"Song title: {self.title}")
