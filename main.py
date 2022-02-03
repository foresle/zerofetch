from packages import *
import os


def run():
    # Getting all data from packages
    left_col: list = AsciiLogo().__list__().copy()
    right_col: list = [' ' for i in range(2)] + SessionInfo().__list__().copy() + MemoryInfo().__list__().copy()

    ts: os.terminal_size = os.get_terminal_size()

    output_list: list = []

    if len(left_col) > len(right_col) or len(left_col) == len(right_col):
        for line in range(0, len(right_col)):
            output_list.append(f'{left_col[line]}  {right_col[line]}')

        for line in range(len(right_col) - 1, len(left_col)):
            output_list.append(f'{left_col[line]}')

    else:
        for line in range(len(left_col) - 1, len(right_col)):
            output_list.append('' * len(left_col[0]) + f'  {right_col[line]}')

    for line_index in range(0, len(output_list)):
        output_list[line_index] = output_list[line_index][:ts.columns]

    output_string: str = '\n'.join(output_list)
    addons_output_string: str = ''

    print(output_string)
    print(addons_output_string)


if __name__ == '__main__':
    run()
