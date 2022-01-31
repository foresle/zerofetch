from package_output_template import PackageTemplate
import re


# Converter functions
def kB_to_Gb(value: float) -> float:
    return round(value / 1024 / 1024, 1)


def kB_to_Mb(value: float) -> float:
    return round(value / 1024, 1)


class MemoryInfo(PackageTemplate):
    def __init__(self):
        super().__init__()
        # self.get_ram()
        # self.get_swap()

    def get_ram(self):
        ram_total: float
        ram_available: float
        ram_used: float

        with open("/proc/meminfo", "r") as memory_file:
            for line in memory_file:
                if 'MemTotal:' in line:
                    ram_total = float(re.search('\d+', line)[0])

                if 'MemAvailable:' in line:
                    ram_available = float(re.search('\d+', line)[0])

        ram_used = ram_total - ram_available

        self.output_text.append(
            f'''Memory used: {str(kB_to_Gb(ram_used)) + 'Gb' if kB_to_Gb(ram_used) > 1 else str(kB_to_Mb(ram_used)) + 'Mb'}''' 
            f''' of {str(kB_to_Gb(ram_total)) + "Gb" if kB_to_Gb(ram_total) > 1 else str(kB_to_Mb(ram_total)) + "Mb"}''')

    def get_swap(self):
        swap_total: float
        swap_free: float

        with open("/proc/meminfo", "r") as memory_file:
            for line in memory_file:
                if 'SwapTotal:' in line:
                    swap_total = float(re.search("\d+", line)[0])

                if 'SwapFree:' in line:
                    swap_free = float(re.search("\d+", line)[0])

        # covert kB to Gb
        swap_total = round(swap_total / 1024, 2)
        swap_free = round(swap_free / 1024, 2)

        self.output_text.append(f'Swap used: {swap_total - swap_free} of {swap_total} Mb')


# Debug
if __name__ == '__main__':
    memory_info: MemoryInfo = MemoryInfo()
    memory_info.get_ram()
    memory_info.get_swap()
    print(memory_info.output_text)
