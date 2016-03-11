openedFiles = Glyphs.fonts

for file in openedFiles:
	for instance in openedFiles[file].instances:
		openedFiles.instances[instance].generate()
