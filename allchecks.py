#!/usr/bin/env python3
#Ram22HEL2231



import os
import sys
import shutil
import socket
import psutil


def check_disk_full(disk, min_gb,  min_percent):
	"""Returns True if there isnt enough disk space, False Otherwise."""
	du = shutil.disk_usage(disk)
	#Calculate the percentage of free space
	percent_free = 100 * du.free / du.total
	gigabytes_free =  du.free/2**30
	if percent_free < min_percent or gigabytes_free < min_gb:
		return True
	return False

def check_reboot():
	"""Returns True if the computer has a pending reboot."""
	return os.path.exists("/run/reboot-required")


def check_root_full():
	"""Returns True if the root partition is full, False Otherwise"""
	return check_disk_full(disk="/", min_gb=2, min_percent=10)

def check_cpu_constrained():
        """Returns True if the cpu is having too  much usage, False otherwise."""
        return psutil.cpu_percent(1) > 75




inssinc#Ram Tripathi



def check_no_network():
	"""Returns True if it falls to resolve GooglE'S URL, False otherwise"""
	try:
		socket.gethostbyname("www.google.com")
		return False
	except:
		return True

def main():
	checks=[
	     (check_reboot, "Pending Reboot"),
	     (check_root_full, "Root Partition Full"),
	     (check_no_network, "No working network."),
	     (check_cpu_constrained, "cpu overload"),

	]
	everything_ok=True

	for check, msg in checks:
		if check():
			print(msg)
			sys.exit(1)
			everything_ok= False
	if not everything_ok:
		sys.exit(1)


	if check_reboot():
		print("Pending reboot")
		sys.exit(1)

	if check_root_full():
		print("Root Partition Full.")
		sys.exit(1)

	print("Everything ok")
	sys.exit(0)

main()



#Ram Tripathi
