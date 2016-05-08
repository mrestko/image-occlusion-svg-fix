# image-occlusion-svg-fix
Repair broken SVG files created by the Image Occlusion 2.0 Anki addon

The popular Anki addon Image Occlusion 2.0 has been creating SVG files with a broken style attribute. This was working fine until a recent Android update stopped honoring the broken tags. I submitted a patch to the Image Occlusion repo which fixes this problem for new cards. However, old cards still need to be fixed and that is the purpose of this utility.

## Usage
The Anki **media collections directory** is a folder where Anki stores all of the images associated with your flashcards. By default, it is located at `Documents/Anki/User 1/collection.media`.

### Method 1 (Windows only)
0. Back up your Anki media collections directory by finding the folder and making a copy of it somewhere else on your computer. (Once you have completed all the steps and verfied that all of your cards are still working, you can delete this backup folder.)
1. Copy the file `fix_image_occlusion_cards.exe` from the `bin/` folder in the dowloaded zip file into your Anki **media collections directory**.
2. Double-click `fix_image_occlusion_cards.exe` to fix your broken Image Occlusion cards
3. Sync you Anki collection up to AnkiWeb and then down to your Android device

### Method 2
(This method requires that you use the command line. I can't explain all the steps for using the command line here, but I've found command line "getting started" resources for: [Windows](http://www.computerhope.com/issues/chusedos.htm) and [Mac OS X](http://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line))
0. Back up your Anki media collections directory by finding the folder and making a copy of it somewhere else on your computer. (Once you have completed all the steps and verfied that all of your cards are still working, you can delete this backup folder.)
1. Your computer must have Python installed. This is installed by default on Mac OS X but on Windows you will need to go to https://www.python.org/downloads/ and follow the instructions to download and install **Python 2.7**.
1. This script needs `lxml` which can be installed by running  `pip install -r requirements.txt`
1. Copy the file `fix_image_occlusion_cards.py` into your Anki media collections directory.
2. Run the script at the command line with `python fix_image_occlusion_cards.py`
3. Sync you Anki collection up to AnkiWeb and then down to your Android device
