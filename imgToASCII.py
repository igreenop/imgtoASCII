from PIL import Image

def get_brightness(rgb: tuple[int, int, int]) -> float:
    return 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]

def get_ascii_char(brightness: float) -> str:
    ascii_chars = "▒@?OPoc:."
    '''
    "@%#*+=-:.^\",;~`'."
    '''

    num_chars = len(ascii_chars)
    index = int((brightness / 255) * (num_chars - 1))
    return ascii_chars[index]

def get_dimensions(filename: str):
    img_path = "/Users/iangreen/rooted/imgToASCII/images/" + filename
    with Image.open(img_path).convert('RGB') as image:
        pixel = image.load()
        width = image.width
        height = image.height
    return (pixel, height, width)

def print_file(pixel, height, width):
    text = ""
    for i in range(0, height, 10):
        for j in range(0, width, 5):
            text += get_ascii_char(get_brightness(pixel[j, i]))
        text += "\n"

    with open("/Users/iangreen/rooted/imgToASCII/ascii.txt", 'w') as file:
        file.write(text)

def img_to_ascii(filename):
    pixel, height, width = get_dimensions(filename)
    print_file(pixel, height, width)

img_to_ascii("suisei.jpg")
