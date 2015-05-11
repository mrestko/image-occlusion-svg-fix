from lxml import etree
import os
import re

def get_image_occlusion_files(media_directory="."):
	files = os.listdir(media_directory)
	img_occ_patt = re.compile(r"_(Q|A)(_|\s)\d*\.svg$")
	target_files = [f for f in files if img_occ_patt.search(f) is not None]
	return target_files

def fix_elem(elem):
	style = elem.get("style")
	styles = style.split(";")
	style_dict = dict(s.split(":") for s in styles)
	fill_color = "#" + style_dict["fill"]
	elem.attrib["fill"] = fill_color
	del elem.attrib["style"]

def fix_file(filename):
	doc = etree.parse(filename)
	root = doc.getroot()
	bad_elems = [elem for elem in root.getiterator()
					if "style" in elem.attrib]
	if len(bad_elems) == 0:
		return False
	else:
		print "Fixing %s" % filename
		map(fix_elem, bad_elems)
		with open(filename, "w") as fp:
			fp.write(etree.tostring(root))
		return True

def fix_files(files):
	return sum(fix_file(fname) for fname in files)

def main():	
	files = get_image_occlusion_files()
	print "Found %i Image Occlusion files" % len(files)
	num_fixed_files = fix_files(files)
	print "Fixed %i files" % num_fixed_files

if __name__ == '__main__':
	main()
