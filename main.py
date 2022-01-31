from packages import *


def run():
    # Getting all data from packages
    ascii_logo_list: list = AsciiLogo().__list__().copy()
    session_info_list: list = SessionInfo().__list__().copy()

    output_list: list = []

    for line in range(0, len(session_info_list)):
        output_list.append(f'{ascii_logo_list[line]}\t{session_info_list[line]}')

    output_string: str = '\n'.join(output_list)

    print(output_string)


if __name__ == '__main__':
    run()
