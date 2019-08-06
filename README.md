# python-subprocess

```python


log = subprocess.check_output(shlex.split('adb logcat -d'))
with open("loggy.file", "w") as f:
    f.write(log)

```
