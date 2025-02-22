from PIL import Image

def resize_image(input_path, output_path, new_width):
    img = Image.open(input_path)
    aspect_ratio = img.height / img.width
    new_height = int(new_width * aspect_ratio)
    
    img_resized = img.resize((new_width, new_height), Image.LANCZOS)
    img_resized.save(output_path, quality=100)

resize_image("/Path/to/input.jpg", "/Path/to/output.jpg", 1280)
