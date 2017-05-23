import queue, os

def torrent_downloader():
	torrent_files = os.listdir(from_dir)
	if torrent_files:
		for file in torrent_files:
			if file.endswith(".torrent"):
				q.put(file)
	else:
		return

	while not q.empty():
		x = q.get()
		#print(x)

		command = "aria2c --max-upload-limit=20K --seed-ratio=0.097 --enable-peer-exchange=true --file-allocation=none -T " + from_dir + x
		command = command + " -d /media/pi/UUI/Downloaded"
		os.system(command)
		aria_files = os.listdir("/media/pi/UUI/Downloaded")
		for file in aria_files:
			if file.endswith(".aria2"):
				flag = 1
			else:
				flag = 0
		if flag == 0:   #To see if the file is downloaded check if aria file exists which is deleted once the download is complete
			os.remove(from_dir+x)   
			print("Deleted "+from_dir+x)

from_dir = "/media/pi/UUI/Torrent/"

q = queue.Queue()
while True:
	torrent_downloader()
	

	
	

