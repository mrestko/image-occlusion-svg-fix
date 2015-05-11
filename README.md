# image-occlusion-svg-fix
Repair broken SVG files created by the Image Occlusion 2.0 Anki addon

The popular Anki addon Image Occlusion 2.0 has been creating SVG files with a broken style attribute. This was working fine until a recent Android update stopped honoring the broken tags. I submitted a patch to the Image Occlusion repo which fixes this problem for new cards. However, old cards still need to be fixed and that is the purpose of this utility.

## Usage
0. Back up your Anki media collections directory
1. Copy the utility file `fix_image_occlusion_cards.py` into your Anki media collections directory.
2. Run the utility at the command line with `python fix_image_occlusion_cards.py`
3. Sync you Anki collection up to AnkiWeb and the down to your Android device

