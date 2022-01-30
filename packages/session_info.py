from package_output_template import PackageTemplate
from datetime import timedelta


class SessionInfo(PackageTemplate):
    def __init__(self):
        super().__init__()

    def get_uptime(self):
        with open("/proc/uptime", "r") as uptime_file:
            file_output = uptime_file.read()
            uptime = timedelta(seconds=float(file_output.split(" ")[0]))
            str_uptime = str(uptime).split(":")
            self.output_text.append(f'{str_uptime[0]} Hours {str_uptime[1]} Minutes {float(str_uptime[2]).__ceil__()} seconds')


# Debug
if __name__ == '__main__':
    session_info: SessionInfo = SessionInfo()
    session_info.get_uptime()
    print(session_info.output_text)
