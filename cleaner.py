import os

delete = ["xz", "txt", "mp4"]
keep = ["py"]


for file in os.listdir():
	if file.split(".")[-1] in delete and file.split(".")[-1] not in keep:
		os.remove(file)