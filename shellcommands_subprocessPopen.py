__author__ = 'panc'


import subprocess

# subprocess.Popen is an alternative to
# os.popen to execute Shell commands.
x = subprocess.Popen(['touch', 'xyz'])
print x
print x.poll()
print x.returncode

# Vanilla usage of subprocess.Popen,
# i.e. commands as a list
# There is no need to escape the Shell metacharacters like $, >
p = subprocess.Popen(['cp', '-r', "xyz", "abc"])

# Alternatively, by setting `shell=True`, one can
# emulate the behavior of os.system
p2 = subprocess.Popen("cp -r xyz abc", shell=True)

# Set `stdout=subprocess.PIPE` in order to capture
# the output from the Shell commands into Python
p3 = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)
print p3.stdout.read()

# If a shell command or shell script has been started
# with Popen(), the Python script doesn't wait until
# the shell command or shell script is finished. To wait
# until it is finished, you have to use the wait() method:
p4 = subprocess.Popen(['ls', '-la'], stdout=subprocess.PIPE)
p4.wait()