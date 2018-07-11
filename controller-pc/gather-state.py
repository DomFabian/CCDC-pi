import atexit
import os, os.path
import subprocess
import sys
import time

# pscp takes Windows paths.
state_dir = "C:\\tmp\\state\\"
# ssh_bin = "C:\\Program Files\\OpenSSH\\bin\\ssh.exe"
# scp_bin = "C:\\Program Files\\OpenSSH\\bin\\scp.exe"
scp_bin = "C:\\Program Files\\PuTTY\\pscp.exe"

# Remote host, remote file path, local file path.
files = [
    ("pi10", "/tmp/motorclock.state", "C:\\tmp\\py\\motorclock.state"),
    ("pi11", "/home/pi/CCDC-pi/binary/state.txt", "C:\\tmp\\py\\binary.state"),
    ("pi11", "/home/pi/CCDC-pi/logic/state.txt", "C:\\tmp\\py\\logic.state"),
    ("pi12", "/home/pi/CCDC-pi/switchbox/state.txt", "C:\\tmp\\py\\switchbox.state"),
#    ("pi13", "/tmp/", "keypad.state", "keypad.state"),
]

def read_first_line(file):
    """ Read and return the first line of file sans newline. """
    s = None
    try:
        f = open(file, "r")
        s = f.read().strip()
        f.close()
    except:
        pass
    return s

def gather_file(f):
    """ Grab the file from the location described in f. """
    host = f[0]
    remote_file = f[1]
    local_file = f[2]
    state = None
    try:
        arg_list = [
            scp_bin,
            "-i",
            "C:\\tmp\\py\\id_rsa.ppk",
            "pi@" + host + ":" + remote_file,
            local_file
        ]
        print("Calling: " + str(arg_list))
        subprocess.call(arg_list)
        state = read_first_line(local_file)
    except:
        pass            
    return "unknown" if state is None else state

last_state = ['running', 'running', 'running', 'running']
while True:
    state = []
    for f in files:
        state.append(gather_file(f))

    print("state: {}".format(":".join(state)))
    # check end
    if state[0] == 'expired':
        f = open("C:\\tmp\\py\\end.txt", "w")
        f.write("failure\n")
        f.close()
        break
    if state[1] == 'solved' and state[2] == 'solved' and state[3] == 'solved':
        f = open("C:\\tmp\\py\\end.txt", "w")
        f.write("success\n")
        f.close()
        break
    # Check binary puzzle state and punish wrong guesses.
    if (state[1] != last_state[1]) and \
        (len(state[1]) > 7) and \
        (state[1][7] == '-'):
        print("You got the binary puzzle wrong!")
        f = open("C:\\tmp\\py\\punish.txt", "w")
        f.write("punish\n")
        f.close()
    last_state = state
    time.sleep(1)
