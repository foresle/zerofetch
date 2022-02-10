from package_output_template import PackageTemplate
import re


# Converter kb functions
def convert_to_gb(value: float) -> float:
    return round(value / 1024 / 1024, 1)


def convert_to_mb(value: float) -> float:
    return round(value / 1024, 1)


class MemoryInfo(PackageTemplate):
    def __init__(self):
        super().__init__()
        self.output_text.clear()
        self.get_ram()
        self.get_swap()

    def get_ram(self):
        ram_total: int
        ram_free: int
        ram_used: int
        ram_buffer: int
        ram_cache: int

        with open("/proc/meminfo", "r") as memory_file:
            for line in memory_file:
                if re.match('^Cached:.{1,}[0-9]{1,}.kB$', line):
                    ram_cache = int(re.search('\d+', line)[0])

                if re.match('^MemTotal:.{1,}[0-9]{1,}.kB$', line):
                    ram_total = int(re.search('\d+', line)[0])

                if re.match('^MemFree:.{1,}[0-9]{1,}.kB$', line):
                    ram_free = int(re.search('\d+', line)[0])

                if re.match('^Buffers:.{1,}[0-9]{1,}.kB$', line):
                    ram_buffer = int(re.search('\d+', line)[0])

        ram_used = ram_total - ram_free - ram_cache - ram_buffer
        self.output_text.append(f'Memory used: {convert_to_gb(ram_used)}Gb of {convert_to_gb(ram_total)}Gb')

    def get_swap(self):
        swap_total: int
        swap_free: int

        with open("/proc/meminfo", "r") as memory_file:
            for line in memory_file:
                if re.match('^SwapTotal:.{1,}[0-9]{1,}.kB$', line):
                    swap_total = float(re.search("\d+", line)[0])

                if re.match('^SwapFree:.{1,}[0-9]{1,}.kB$', line):
                    swap_free = float(re.search("\d+", line)[0])

        self.output_text.append(f'Swap used: {convert_to_gb(swap_total - swap_free)} of {convert_to_gb(swap_total)} Gb')


# Debug
if __name__ == '__main__':
    memory_info: MemoryInfo = MemoryInfo()
    print(memory_info.output_text)
