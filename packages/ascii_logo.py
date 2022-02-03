import random

import xtermcolor
from package_output_template import PackageTemplate
from PIL import Image

ascii_images: list = [
    '''.==============================================.
|                                              |
|                           .'\                |
|                          //  ;               |
|                         /'   |               |
|        .----..._    _../ |   \               |
|         \\'---._ `.-'      `  .'              |
|          `.    '              `.             |
|            :            _,.    '.            |
|            |     ,_    (() '    |            |
|            ;   .'(().  '      _/__..-        |
|            \ _ '       __  _.-'--._          |
|            ,'.'...____'::-'  \     `'        |
|           / |   /         .---.              |
|     .-.  '  '  / ,---.   (     )             |
|    / /       ,' (     )---`-`-`-.._          |
|   : '       /  '-`-`-`..........--'\         |
|   ' :      /  /                     '.       |
|   :  \    |  .'         o             \      |
|    \  '  .' /          o       .       '     |
|     \  `.|  :      ,    : _o--'.\      |     |
|      `. /  '       ))    (   )  \>     |     |
|        ;   |      ((      \ /    \___  |     |
|        ;   |      _))      `'.-'. ,-'` '     |
|        |    `.   ((`            |/    /      |
|        \     ).  .))            '    .       |
|     ----`-'-'  `''.::.________:::mx'' ---    |
|                                              |
|                                              |
|                                              |
'=============================================='
    ''', '''     
      ____________
     /\  ________ \\
    /  \ \______/\ \\
   / /\ \ \  / /\ \ \\
  / / /\ \ \/ / /\ \ \\
 / / /__\_\/ / /__\_\ \\
/ /_/_______/ /________\\
\ \ \______ \ \______  /
 \ \ \  / /\ \ \  / / /
  \ \ \/ / /\ \ \/ / /
   \ \/ / /__\_\/ / /
    \  / /______\/ /
     \/___________/
    ''']


# class AsciiLogoError(Exception):
#     text: str
#
#     def __init__(self, text: str):
#         self.text = text
#
#     def __str__(self):
#         return self.text


class AsciiLogo(PackageTemplate):
    def __init__(self, ascii_file: str = None):
        super().__init__()
        self.output_text.clear()
        self.generate_from_ascii_txt(ascii_file)
        # self.generate_ascii_from_image('./packages/600px-NewTux.svg.png')

    def generate_from_ascii_txt(self, text_path: str) -> None:
        biggest_line: int = 0
        try:
            with open(text_path, 'r') as file:
                for line in file.read().split('\n'):
                    self.output_text.append(line)
                    if biggest_line < len(line):
                        biggest_line = len(line)

        except FileNotFoundError:
            for line in random.choice(ascii_images).split('\n'):
                self.output_text.append(line)
                if biggest_line < len(line):
                    biggest_line = len(line)

        for line_index in range(0, len(self.output_text)):
            self.output_text[line_index] = self.output_text[line_index] + ' ' * (
                    biggest_line - len(self.output_text[line_index]))

    def generate_ascii_from_image(self, image_path: str) -> None:
        img = Image.open(image_path)

        width, height = img.size
        aspect_ratio: float = height / width
        new_width: int = 80
        new_height: int = int(aspect_ratio * new_width * 0.5)

        img: Image = img.resize((new_width, new_height))
        img: Image = img.convert('LA')
        img.save('some.image.png')
        pixels = img.getdata()

        chars = [xtermcolor.colorize('B', rgb=0x000000), xtermcolor.colorize('S', rgb=0x171717),
                 xtermcolor.colorize('#', rgb=0x2E2E2E), xtermcolor.colorize('&', rgb=0x454545),
                 xtermcolor.colorize('@', rgb=0x5C5C5C), xtermcolor.colorize('$', rgb=0x707070),
                 xtermcolor.colorize('%', rgb=0x8B8B8B), xtermcolor.colorize('*', rgb=0xA2A2A2),
                 xtermcolor.colorize('!', rgb=0xB9B9B9), xtermcolor.colorize('.', rgb=0xD0D0D0),
                 xtermcolor.colorize(' ', rgb=0xFFFFFF)]
        pixel_literals = []
        for pixel in pixels:
            if pixel[1] == 255:
                pixel_literals.append(chars[pixel[0] // 25])
            else:
                pixel_literals.append(chars[10])

        pixel_literals = ''.join(pixel_literals)

        pixel_literals_count = len(pixel_literals)
        ascii_image = []
        for pixel_literal_string_start in range(0, pixel_literals_count, new_width * 16 - 1):
            ascii_image.append(
                pixel_literals[pixel_literal_string_start:pixel_literal_string_start + new_width * 16 - 1])

        self.output_text = ascii_image
        ascii_image = '\n'.join(ascii_image)
        print(ascii_image)

        with open('ascii_image.txt', 'w') as f:
            f.write(ascii_image)


if __name__ == '__main__':
    ascii_logo: AsciiLogo = AsciiLogo()
    ascii_logo.generate_ascii_from_image('600px-NewTux.svg.png')
