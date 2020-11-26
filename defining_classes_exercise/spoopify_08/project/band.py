# from album import Album
# from song import Song


class Band:

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        matched_albums = [
            band_album for band_album in self.albums if band_album == album]
        if matched_albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        matched_albums = [
            band_album for band_album in self.albums if band_album.name == album_name]
        if matched_albums:
            album_to_remove = matched_albums[0]
            if not album_to_remove.published:
                self.albums.remove(album_to_remove)
                return f"Album {album_name} has been removed."

            return f"Album has been published. It cannot be removed."

        return f"Album {album_name} is not found."

    def details(self):
        info = f"Band {self.name}\n"
        for album in self.albums:
            info += f"{album.details()}" #removed \n

        return info


# song = Song("Running in the 90s", 3.45, False)
# nice_song = Song("boiz", 98, True)
# cool_song = Song("cHAINS", 3.33, False)
# single_song = Song("SINGLE", 4444, True)
# print(song.get_info())
# print(nice_song.get_info())
# print(cool_song.get_info())
# album = Album("Initial D", song, nice_song)
# second_song = Song("Around the World", 2.34, False)
# print(album.add_song(second_song))
# print(album.add_song(cool_song))
# print(album.add_song(single_song))
# print(album.details())
# print(album.publish())
# leet_song = Song("1337", 1337, False)
# ez_song = Song("ez", 37, True)
# print(album.add_song(leet_song))
# print(album.add_song(ez_song))
# band = Band("Manuel")
# print(band.add_album(album))
# print(band.remove_album("Initial D"))
# test_album = Album("test Album")
# print(band.add_album(test_album))
# print(band.remove_album("test Album"))
# print(band.remove_album("asjdfajshldlfhlasdjkf"))
# print(band.details())