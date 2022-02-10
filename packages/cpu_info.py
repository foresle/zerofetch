from package_output_template import PackageTemplate
import re


class CpuInfo(PackageTemplate):
    def __init__(self):
        super().__init__()
        self.output_text.clear()
        self.get_cpu_name()

    def get_cpu_name(self):
        cpu_name: str

        with open('/proc/cpuinfo', 'r') as cpu_file:
            for line in cpu_file:
                if 'model name	: ' in line:
                    cpu_name = line.replace('model name	: ', '').strip()
                    break

        self.output_text.append(f'CPU: {cpu_name}')

# Debug
if __name__ == '__main__':
    cpu_info: CpuInfo = CpuInfo()
    print(cpu_info.output_text)
