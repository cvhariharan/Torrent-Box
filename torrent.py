import queue, os

def torrent_downloader():
	for file in torrent_files:
		if file.endswith(".torrent"):
			q.put(from_dir+file)

	while not q.empty():
		x = q.get()
		print(x)
		command = "aria2c -T " + x
		command = command + " -d /media/pi/UUI/Downloaded"
		os.system(command)
		os.remove(from_dir+x)

from_dir = "/media/pi/UUI/Torrent/"
torrent_files = os.listdir(from_dir)
q = queue.Queue()
while True:
	torrent_downloader()
	

	
	

