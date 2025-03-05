from PIL import Image
from PIL.ExifTags import TAGS

def resize_image(input_path, output_path, new_width):
    img = Image.open(input_path)
    exif_data = img.info.get("exif")  # Retrieve EXIF data if present
    
    aspect_ratio = img.height / img.width
    new_height = int(new_width * aspect_ratio)
    
    img_resized = img.resize((new_width, new_height), Image.LANCZOS)
    
    # Save with EXIF data
    img_resized.save(output_path, quality=100, exif=exif_data) if exif_data else img_resized.save(output_path, quality=100)


resize_image("/Path/to/input.jpg", "/Path/to/output.jpg", 1280)
