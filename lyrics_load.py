import api_key
import os
import lyricsgenius

token = api_key.access_token

def get_lyrics(artist_list):
	for genre in artist_list:
		for name in genre:
			if os.path.isdir(f"{name}"):
				continue
			else:
				os.makedirs(f"{name}")
			while True:
				try:
					artist = genius.search_artist(name, max_songs=400, sort='popularity')
					break
				except:
					pass
			songs = artist.songs
			for song in songs:
				lyrics = song.lyrics
				if '/' in song.title:
					continue
				file = open(f"{name}/{song.title}.txt", "w", encoding="utf-8")
				file.write(lyrics)
				file.close()

pop_artists = ["Harry Styles", "ITZY", "Ed Sheeran", "Taylor Swift", "Dua Lipa", "Lizzo", "Bruno Mars", "BTS", "Billie Eilish", "Lady Gaga"]
rap_artists = ["Drake", "Post Malone", "Kendrick Lamar", "Kanye West", "Future", "Tyler, The Creator", "Lil Nas X", "J. Cole", "Eminem"]
rock_artists = ["Metallica", "Imagine Dragons", "Fleetwood Mac", "Journey", "Glass Animals", "Def Leppard", "Queen", "AC/DC", "Guns N' Roses", "Lynyrd Skynyrd"]
jazz_artists = ["Ella Fitzgerald", "Ray Charles", "Louis Armstrong", "Dinah Washington", "Frank Sinatra", "Nina Simone", "Billie Holiday", "Chet Baker", 'Nat King Cole', "Sarah Vaughan"]
artists = [pop_artists, rap_artists, rock_artists, jazz_artists]

genius = lyricsgenius.Genius(token)
genius.excluded_terms = ["(Remix)", "(Live)", "(Version)", "(Demo)", "(Mix)", "(Cover)", "(Unreleased)", "/"]
genius.remove_section_headers = True

get_lyrics(artists)