from pygame import pygame
import glob
def create_playlist(path):
    for song in glob.glob (path):
        print ("Playing..."+song)
        pygame(song)

# Corrected file path using double backslashes
path_to_song = r"C:\\Users\Lab\OneDrive - Catholic Education Western Australia\y2mate.is - taylor_swift___haunted__taylor_s_version___lyric_video_-4cC6fw8EqWU-192k-1692078554.mp3"

# Call the function with the path to the song
create_playlist(path_to_song)