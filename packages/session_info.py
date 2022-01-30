from package_output_template import PackageTemplate
from datetime import timedelta
import os


class SessionInfo(PackageTemplate):
    def __init__(self):
        super().__init__()

    def get_user(self):
        user_name = str.rstrip(os.popen("echo $USER").read())
        self.output_text.append(f'User: {user_name}')

    def get_session_type(self):
        session_type = str.rstrip(os.popen("echo $XDG_SESSION_TYPE").read())
        self.output_text.append(f'Session: {session_type}')

    def get_desktop_environment(self):
        de_type = str.rstrip(os.popen("echo $XDG_CURRENT_DESKTOP").read())
        self.output_text.append(f'DE: {de_type}')

    def get_shell(self):
        shell_type = str.rstrip(os.popen("echo $SHELL").read())
        self.output_text.append(f'Shell: {shell_type}')

    def get_uptime(self):
        with open("/proc/uptime", "r") as uptime_file:
            file_output = uptime_file.read()
            uptime = timedelta(seconds=float(file_output.split(" ")[0]))
            str_uptime = str(uptime).split(":")
            self.output_text.append(f'Uptime: {str_uptime[0]} hours {str_uptime[1]} mins ')


# Debug
if __name__ == '__main__':
    session_info: SessionInfo = SessionInfo()
    session_info.get_user()
    session_info.get_shell()
    session_info.get_uptime()
    session_info.get_desktop_environment()
    session_info.get_session_type()
    print(session_info.output_text)
