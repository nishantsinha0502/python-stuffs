# DOWNLOADS MULTIPLE PLAYLISTS AND SAVE THEM TO THE DESTINATION FOLDERS
from pytube import Playlist

links=['URL_1','URL_2','URL_3']


folders=['PATH/TO/FIRST/VIDEO','PATH/TO/SECOND/VIDEO','PATH/TO/THIRD/VIDEO']

for i in range(len(links)):
	pl = Playlist(links[i])
	pl.download_all(folders[i])
