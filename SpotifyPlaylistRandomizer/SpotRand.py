import random
import re
import pyperclip


links_str = pyperclip.paste()
link_pattern = r'(https?://\S+)'
links = re.findall(link_pattern, links_str)

random.shuffle(links)

print("Shuffled Spotify links:")
for link in links:
    print(link.strip())  

print("Make a new playlist and paste these in.")

