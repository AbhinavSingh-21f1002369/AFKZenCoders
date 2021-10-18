import subprocess

process = subprocess.run(["ping","iot.ccnet.in","-c","2"], capture_output=True, text=True)
standard_out = process.stdout
standard_out = standard_out.split("\n")
print(type(standard_out))
print(standard_out)