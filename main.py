from packages import *


def run():
    # Getting all data from packages
    ascii_logo_list: list = AsciiLogo().__list__().copy()
    session_info_list: list = SessionInfo().__list__().copy()

    output_list: list = []

    if len(ascii_logo_list) > len(session_info_list) or len(ascii_logo_list) == len(session_info_list):
        for line in range(0, len(session_info_list)):
            output_list.append(f'{ascii_logo_list[line]}\t{session_info_list[line]}')

        for line in range(len(session_info_list)-1, len(ascii_logo_list)):
            output_list.append(f'{ascii_logo_list[line]}')

    output_string: str = '\n'.join(output_list)
    addons_output_string: str = ''

    print(output_string)
    print(addons_output_string)


if __name__ == '__main__':
    run()
