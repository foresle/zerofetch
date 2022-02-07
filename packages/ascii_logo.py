import random
import distro
from package_output_template import PackageTemplate

ascii_images: dict = {
    'tux':
        '''
          a8888b.
         d888888b.
         8P"YP"Y88
         8|o||o|88
         8'    .88
         8`._.' Y8.
        d/      `8b.
      .dP   .     Y8b.
     d8:'   "   `::88b.
    d8"           `Y88b
   :8P     '       :888
    8a.    :      _a88P
  ._/"Yaa_ :    .| 88P|
  \    YP"      `| 8P  `.
  /     \._____.d|    .'
  `--..__)888888P`._.'
        ''',
    'arch':
        '''
                   -`
                  .o+`
                 `ooo/
                `+oooo:
               `+oooooo:
               -+oooooo+:
             `/:-:++oooo+:
            `/++++/+++++++:
           `/++++++++++++++:
          `/+++ooooooooooooo/`
         ./ooosssso++osssssso+`
        .oossssso-````/ossssss+`
       -osssssso.      :ssssssso.
      :osssssss/        osssso+++.
     /ossssssss/        +ssssooo/-
   `/ossssso+/:-        -:/+osssso+-
  `+sso+:-`                 `.-/+oso:
 `++:.                           `-/+/
 .`                                 `
        '''
}


class AsciiLogo(PackageTemplate):
    def __init__(self, text_file: str | None = None, distro_id: str | None = None):
        super().__init__()

        if text_file is None:
            self.put_ascii_image_to_list(ascii_images.get(distro.id() if distro_id is None else distro_id, 'tux'))
        else:
            self.generate_from_text_file(text_file)

    def put_ascii_image_to_list(self, text: str) -> None:
        biggest_line: int = 0

        for line in text.split('\n'):
            self.output_text.append(line)
            if biggest_line < len(line):
                biggest_line = len(line)

        for line_index in range(0, len(self.output_text)):
            self.output_text[line_index] = self.output_text[line_index] + ' ' * (
                    biggest_line - len(self.output_text[line_index]))

    def generate_from_text_file(self, text_file_path: str) -> None:
        try:
            with open(text_file_path, 'r') as file:
                self.put_ascii_image_to_list(file.read())

        except FileNotFoundError:
            self.put_ascii_image_to_list(ascii_images['tux'])


if __name__ == '__main__':
    pass
