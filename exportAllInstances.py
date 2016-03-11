#MenuTitle: Export All Instances
# -*- coding: utf-8 -*-

__doc__ = """
Exports all instances of all opened files
"""

for font in Glyphs.fonts:
	for instance in font.instances:
		instance.generate('~/Desktop')
