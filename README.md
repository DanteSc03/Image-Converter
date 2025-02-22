# Image Resizer

This script resizes an image while maintaining its aspect ratio using the Python Imaging Library (PIL / Pillow).

## Features
- Resizes an image based on a specified width
- Maintains the original aspect ratio
- Saves the resized image with high quality

## Requirements
- Python 3.x
- Pillow (PIL Fork)

### Install Dependencies
To install Pillow, run:
```bash
pip install pillow
```

## Usage
Modify the script to include the correct input and output file paths and the desired width. Then, run the script:

```python
from PIL import Image

def resize_image(input_path, output_path, new_width):
    img = Image.open(input_path)
    aspect_ratio = img.height / img.width
    new_height = int(new_width * aspect_ratio)
    
    img_resized = img.resize((new_width, new_height), Image.LANCZOS)
    img_resized.save(output_path, quality=100)

resize_image("/Path/to/input.jpg", "/Path/to/output.jpg", 1280)
```

## Parameters
- `input_path` - Path to the input image
- `output_path` - Path to save the resized image
- `new_width` - Desired width of the resized image

## Example
```python
resize_image("image.jpg", "resized_image.jpg", 800)
```
This resizes `image.jpg` to a width of 800 pixels while keeping the aspect ratio.

## License
This project is open-source and available under the MIT License.

