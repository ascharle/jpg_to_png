from PIL import Image
import sys, os

# grab the first and second argument

images = sys.argv[1]
new = sys.argv[2]

print(images)
print(new)

#check if new / exist , if not create it
if not os.path.exists(new):
    os.makedirs(new)

#loop through Pokedex
for filename in os.listdir(images):
    img = Image.open(f'{images}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{new}{clean_name}.png','png')
    print('All done ')
#Convert images to png

#save to the new folder.
