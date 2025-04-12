from PIL import Image
from services.utils import select_image_in_folder

END_MARKER = '1111111111111110'  # ENDING MARKER TO INDICATE THE END OF DATA

def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)

def hide_data_in_image(image_path, output_path, data):
    img = Image.open(image_path)
    binary_data = text_to_binary(data) + END_MARKER
    data_index = 0
    if img.mode != 'RGB':
        img = img.convert('RGB')
    pixels = list(img.getdata())
    new_pixels = []
    for pixel in pixels:
        if data_index >= len(binary_data):
            new_pixels.append(pixel)
            continue
        r, g, b = pixel
        r = (r & ~1) | int(binary_data[data_index])
        data_index += 1
        if data_index < len(binary_data):
            g = (g & ~1) | int(binary_data[data_index])
            data_index += 1
        if data_index < len(binary_data):
            b = (b & ~1) | int(binary_data[data_index])
            data_index += 1
        new_pixels.append((r, g, b))
    img.putdata(new_pixels)
    img.save(output_path)

def __binary_to_text(binary_data):
    chars = [chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8)]
    return ''.join(chars)

def extract_data_from_image():
    image_output = select_image_in_folder("outputs")
    img = Image.open(image_output)
    binary_data = ''
    pixels = img.load()
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)
    end_index = binary_data.find(END_MARKER)
    if end_index != -1:
        binary_data = binary_data[:end_index]
    else:
        raise ValueError("End !")
    print("Extracted Data:", __binary_to_text(binary_data))
    return 