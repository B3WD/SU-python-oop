class Album:

    def __init__(self, name, *songs):
        self.name = name
        # self.songs = list(songs)
        self.songs = []
        self.published = False

        for song in list(songs):
            self.add_song(song)

        

    def add_song(self, song):
        matches = [included_song for included_song in self.songs if included_song.name == song.name]

        if matches:
            return f"Song is already in the album."

        if self.published:
            return f"Cannot add songs. Album is published."

        if song.single:
            return f"Cannot add {song.name}. It's a single"

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

        # if not matches:
        #     if not song.single:
        #         self.songs.append(song)
        #         return f"Song {song.name} has been added to the album {self.name}."

        #     return f"Cannot add {song.name}. It's a single"

        # elif self.published:
        #     return f"Cannot add songs. Album is published."

        # return f"Song is already in the album."

    def remove_song(self, song_name):
        matches = [song for song in self.songs if song.name == song_name]

        if matches:
            if not self.published:
                song_to_remove = matches[0]
                self.songs.remove(song_to_remove)
                return f"Removed song {song_name} from album {self.name}."
            
            return "Cannot remove songs. Album is published."

        return "Song is not in the album."
        
    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        info = f"Album {self.name}\n"
        
        for song in self.songs:
            info += f"== {song.get_info()}\n"

        return info