#DOWNLOADS A SINGLE PLAYLIST, AND SAVE IT TO THE DESTINATION FILE.
from pytube import Playlist

URL_LINK = input('enter the link: ')
pl= Playlist(URL_LINK)
pl.download_all('/PATH/TO/DOWNLOAD/')  #mention the path, where you need to download the file
