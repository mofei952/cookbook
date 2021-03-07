import subprocess


out_bytes = subprocess.check_output(['netstat', '-a'])
out_text = out_bytes.decode('utf-8')
print(out_text)
print()


try:
    out_bytes = subprocess.check_output(['ls', '-abcde'])
except subprocess.CalledProcessError as e:
    out_bytes = e.output
    code = e.returncode
print(out_bytes, code)
print()


try:
    out_bytes = subprocess.check_output(['pwd', '-a'], stderr=subprocess.STDOUT)
except Exception as e:
    out_bytes = e.output
    code = e.returncode
print(out_bytes, code)
print()


try:
    out_bytes = subprocess.check_output(['sleep', '2'], timeout=1)
except subprocess.TimeoutExpired as e:
    print(e)
