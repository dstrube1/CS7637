from itertools import zip_longest
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

import os
import shutil

old_folders = set()
root_dir = r'C:\Users\me\Path\To\Problems'
font = ImageFont.truetype(r'C:\Users\me\Path\To\Palatino Font.ttf', 40)


def generate_composite():
    for image, answer, destination in generate_data():
        with image as base:
            x, y = base.size
            answer_txt = Image.new('RGBA', base.size, (255, 255, 255, 0))
            draw = ImageDraw.Draw(answer_txt)
            draw.text((x - 15, y - 15), f'Answer: {answer}', (0, 0, 0), font, 'rb')

            composite = Image.alpha_composite(base, answer_txt)
            yield composite, destination


def generate_data():
    for root, dirs, files in os.walk(root_dir):
        for image_file, answer_file in grouper(files, 2):
            destination = Path(root).resolve().parent / image_file
            image_file = os.path.join(root, image_file)
            answer_file = os.path.join(root, answer_file)

            image = Image.open(image_file).convert('RGBA')
            answer = get_answer(answer_file)

            old_folders.add(root)
            yield image, answer, destination


def get_answer(file):
    with open(os.path.abspath(file), 'r') as answer:
        return answer.read(1)


def grouper(iterable, n, fillvalue=None):
    'Collect data into non-overlapping fixed-length chunks or blocks'
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def cleanup_dirs():
    for folder in old_folders:
        try:
            shutil.rmtree(folder)
        except:
            print('error')


def run():
    for composite, destination in generate_composite():
        composite.save(destination, 'PNG')
    cleanup_dirs()


if __name__ == '__main__':
    run()
