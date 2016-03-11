#MenuTitle: Export All Instances
# -*- coding: utf-8 -*-

__doc__ = """
Exports all instances of all opened files
"""

exportFolder = '~/Desktop'

for font in Glyphs.fonts:
	for instance in font.instances:
		instance.generate('OTF', exportFolder)

	Glyphs.showNotification('Export fonts', 'The export of %s was successful.' % (Glyphs.font.familyName))
