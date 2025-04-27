"""
system_health_checker.py
Provides basic system health checks for disk, CPU, memory, and folders.
"""

import os
import shutil
import psutil
import platform
import time

def check_disk_space(path='.'):
    """
    Check available disk space at given path.
    """
    total, used, free = shutil.disk_usage(path)
    print(f"Disk Total: {total // (2**30)} GB")
    print(f"Disk Used : {used // (2**30)} GB")
    print(f"Disk Free : {free // (2**30)} GB")
    return {"total_gb": total // (2**30), "used_gb": used // (2**30), "free_gb": free // (2**30)}

def check_cpu_usage():
    """
    Check current CPU usage percentage.
    """
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"Current CPU Usage: {cpu_percent}%")
    return cpu_percent

def check_memory_usage():
    """
    Check current memory (RAM) usage.
    """
    mem = psutil.virtual_memory()
    print(f"Total Memory: {mem.total // (2**20)} MB")
    print(f"Available Memory: {mem.available // (2**20)} MB")
    print(f"Used Memory: {mem.used // (2**20)} MB")
    print(f"Memory Usage: {mem.percent}%")
    return {"total_mb": mem.total // (2**20), "available_mb": mem.available // (2**20), "used_mb": mem.used // (2**20), "percent_used": mem.percent}

def calculate_folder_size(folder):
    """
    Calculate the total size of a folder in MB.
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.isfile(fp):
                total_size += os.path.getsize(fp)
    total_size_mb = total_size / (1024 * 1024)
    print(f"Folder '{folder}' size: {total_size_mb:.2f} MB")
    return total_size_mb

def system_info_summary():
    """
    Print basic system information.
    """
    print("\nSystem Info:")
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Processor: {platform.processor()}")

def simulate_system_health_check():
    """
    Simulate running a full system health check.
    """
    print("\nRunning System Health Check...")
    system_info_summary()
    check_disk_space()
    check_cpu_usage()
    check_memory_usage()

    # Assuming 'moved_files' or 'texts' directory exists for folder monitoring
    if os.path.exists('moved_files'):
        calculate_folder_size('moved_files')
    elif os.path.exists('texts'):
        calculate_folder_size('texts')
    else:
        print("No monitored folders found.")

    print("\nSystem health check completed.")

