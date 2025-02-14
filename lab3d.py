#!/usr/bin/env python3
# Author ID: 182853218
import subprocess

def free_space():
    output = subprocess.check_output("df -h | grep '/$' | awk '{print $4}'", shell=True)
    
    return output.decode('utf-8').strip()

print(free_space())

