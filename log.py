import subprocess
import shlex


def cmd(command):
    # subprocess.call(shlex.split('adb logcat -c'))
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    # process = subprocess.check_output(shlex.split('adb logcat -d'))
    while True:
        output = process.stdout.readline().decode()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
    rc = process.poll()
    return rc


cmd('tail -f /var/log/system.log')
