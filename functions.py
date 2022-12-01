def calc_next(lst) -> int:
    return str(int(lst[0]) + 1).encode()

def calc_area(lst) -> float:
    return str((int(lst[0]) * int(lst[1])) / 2).encode()


def send_image(filename):
    filename = './uploads/' + filename
    image_bytes = open(filename, 'rb').read()
    return image_bytes

    
functions = {
    'calculate-next': calc_next,
    'calculate-area': calc_area,
    'image': send_image
}