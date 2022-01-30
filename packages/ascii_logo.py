import xtermcolor
from package_output_template import PackageTemplate
from PIL import Image


class AsciiLogo(PackageTemplate):
    def __init__(self):
        super().__init__()

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
        for pixel_literal_string_start in range(0, pixel_literals_count, new_width*16-1):
            ascii_image.append(pixel_literals[pixel_literal_string_start:pixel_literal_string_start + new_width*16-1])

        self.output_text = ascii_image
        ascii_image = '\n'.join(ascii_image)
        print(ascii_image)

        with open('ascii_image.txt', 'w') as f:
            f.write(ascii_image)


if __name__ == '__main__':
    ascii_logo: AsciiLogo = AsciiLogo()
    ascii_logo.generate_ascii_from_image('600px-NewTux.svg.png')
