# download individual videos and asks for link, until you enter 'n'.
from pytube import YouTube
while True:
	link= input('enter the link: ')
	if link=='n':
		break
	else:
		YouTube(link).streams.first().download('/PATH/TO/DOWNLOAD')
