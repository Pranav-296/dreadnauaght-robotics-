from rembg import remove
from PIL import Image

input_path = 'dreadnaught robotics task.png'
output_path = 'output_with_white_bg.jpg'


input_image = Image.open(input_path).convert("RGBA")


output_image = remove(input_image)


white_bg = Image.new("RGBA", output_image.size, (255, 255, 255, 255))

white_bg.paste(output_image, (0, 0), output_image)


white_bg.convert("RGB").save(output_path)

print("Background removed and replaced with white background. See 'output_with_white_bg.jpg'.")
