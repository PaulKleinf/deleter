import os

endungen = ["xz", "txt", "mp4"]
gutendungen = ["py"]


for file in os.listdir():
	if file.split(".")[-1] in endungen and file.split(".")[-1] not in gutendungen:
		os.remove(file)