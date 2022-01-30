from package_output_template import PackageTemplate
from datetime import datetime


class SessionInfo(PackageTemplate):
    def __init__(self):
        super().__init__()

    def get_uptime(self):
        with open("/proc/uptime", "r") as uptime_file:
            file_output = uptime_file.read()
            uptime = datetime.fromtimestamp(float(file_output.split(" ")[0]))
            self.output_text.append(uptime.strftime("%H hour(s) %M minutes %S seconds"))


if __name__ == '__main__':
    print("Hi")