from PIL import Image

def split_image_into_thirds(input_path, output_dir):
    img = Image.open(input_path)
    width, height = img.size
    third_width = width // 3
    
    left = img.crop((0, 0, third_width, height))
    middle = img.crop((third_width, 0, 2 * third_width, height))
    right = img.crop((2 * third_width, 0, width, height))
    
    left.save(f"{output_dir}/left_third.jpg", quality=100)
    middle.save(f"{output_dir}/middle_third.jpg", quality=100)
    right.save(f"{output_dir}/right_third.jpg", quality=100)
    
    print("Images saved successfully.")

split_image_into_thirds("/Path/to/input", "path/to/output")

