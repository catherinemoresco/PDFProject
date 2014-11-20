import subprocess

pipe = subprocess.Popen("pwd", stdout=subprocess.PIPE)
out, err = p.communitcate()

print out