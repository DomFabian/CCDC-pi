import atexit
import os, os.path
import subprocess
import sys
import time

vid_dir = "C:\\tmp\\vid"
vlc_bin = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"

# File tuples are the video name, the start time offset and the duration
# in seconds.
turbo = [
    ("turbo-encabulator.mp4", 0, 9999),
    ("rockwell-retro-encabulator.mkv", 0, 9999),
]

punish = [
    ("screechy.mp4", 25, 10),
    ("worst-10-x-factor.mkv", 379, 18),
    ("konis-hupen.mkv", 44, 15),
    ("zlad.mp4", 123, 15),
]

success_vids = [
    ("queen-we-are-the-champions.mp4", 4, 9999),
]

failure_vids = [
    ("paintbrush-cmon-lets-get-outa-here.mp4", 0, 30),
    ("trinity.mp4", 25, 23),
#    ("trinity-and-beyond.mp4", 173, 250),
]

PUNISH_FILE = os.path.join("c:/tmp/py", "punish.txt")
END_FILE = os.path.join("c:/tmp/py", "end.txt")
if os.path.exists(PUNISH_FILE):
    os.remove(PUNISH_FILE)
if os.path.exists(END_FILE):
    os.remove(END_FILE)

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

def need_to_punish():
    if os.path.exists(PUNISH_FILE):
        os.remove(PUNISH_FILE)
        return True
    return False

def time_to_end():
    if os.path.exists(END_FILE):
        return True
    return False    

turbo_index = 0
punish_index = 0
punishing = False
ending = False

while not ending:
    if punishing:
        file = punish[punish_index]
        punish_index = (punish_index + 1) % len(punish)
    else:
        file = turbo[turbo_index]
        turbo_index = (turbo_index + 1) % len(turbo)
    punishing = False
    arg_list = [
        vlc_bin,
        "--fullscreen",
        "--play-and-exit",
        "--mouse-hide-timeout=0",
        os.path.join(vid_dir, file[0]),
        ":start-time=" + str(file[1]),
        ":stop-time=" + str(file[1] + file[2]),
    ]
    print("command=" + str(arg_list))
    p = subprocess.Popen(arg_list)
    while True:
        if need_to_punish():
            punishing = True
            break
        if time_to_end():
            ending = True
            break
        p.poll()
        # print("p.returncode=", p.returncode)
        if p.returncode is not None:
            break
        time.sleep(1)
    p.terminate()

# The end.
end_reason = read_first_line(END_FILE)
os.remove(END_FILE)
vids = failure_vids
if end_reason == "success":
    vids = success_vids
index = 0
for file in vids:
    arg_list = [
        vlc_bin,
        "--fullscreen",
        "--play-and-exit",
        "--mouse-hide-timeout=0",
        os.path.join(vid_dir, file[0]),
        ":start-time=" + str(file[1]),
        ":stop-time=" + str(file[1] + file[2]),
    ]
    print("command=" + str(arg_list))
    p = subprocess.Popen(arg_list)
    while p.returncode is None:
        time.sleep(1)
        p.poll()
    p.terminate()
