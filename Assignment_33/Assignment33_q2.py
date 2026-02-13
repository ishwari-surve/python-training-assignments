# Platform Surveillance System
# Command Line Input Supported
# Features:
# CPU, RAM, Disk, Network, Process, Threads, Open Files Monitoring

import psutil
import sys
import os
import time
import schedule


def ProcessScan():

    listprocess = []

    # Warm-up for CPU calculation
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass

    time.sleep(0.2)

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=[
                "pid",
                "name",
                "username",
                "status",
                "create_time"
            ])

            # Convert start time
            try:
                info["create_time"] = time.strftime(
                    "%Y-%m-%d %H:%M:%S",
                    time.localtime(info["create_time"])
                )
            except:
                info["create_time"] = "NA"

            # CPU & Memory usage
            info["cpu_percent"] = proc.cpu_percent(interval=0.0)
            info["memory_percent"] = proc.memory_percent()

            # Thread Monitoring
            info["thread_count"] = proc.num_threads()

            # 🔥 Open Files Monitoring
            try:
                open_files = proc.open_files()
                info["open_files_count"] = len(open_files)
            except psutil.AccessDenied:
                info["open_files_count"] = "Access Denied"
            except:
                info["open_files_count"] = "NA"

            listprocess.append(info)

        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            pass

    return listprocess

def CreateLog(FolderName):

    Border = "-" * 70

    try:
        if not os.path.exists(FolderName):
            os.makedirs(FolderName)

        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        FileName = os.path.join(
            FolderName,
            "Marvellous_%s.log" % timestamp
        )

        with open(FileName, "w") as fobj:

            fobj.write(Border + "\n")
            fobj.write("Marvellous Platform Surveillance System\n")
            fobj.write("Log Created at : " + time.ctime() + "\n")
            fobj.write(Border + "\n\n")

            fobj.write("System Report\n")
            fobj.write(Border + "\n")

            # CPU
            fobj.write("CPU Usage : %s %%\n" %
                       psutil.cpu_percent())

            # RAM
            mem = psutil.virtual_memory()
            fobj.write("RAM Usage : %s %%\n" %
                       mem.percent)

            fobj.write(Border + "\n")

            # Disk
            fobj.write("Disk Usage Report\n")
            for part in psutil.disk_partitions():
                try:
                    usage = psutil.disk_usage(part.mountpoint)
                    fobj.write("%s -> %s %% used\n" %
                               (part.mountpoint,
                                usage.percent))
                except:
                    pass

            fobj.write(Border + "\n")

            # Network
            net = psutil.net_io_counters()
            fobj.write("Network Usage Report\n")
            fobj.write("Sent : %.2f MB\n" %
                       (net.bytes_sent / (1024 * 1024)))
            fobj.write("Received : %.2f MB\n" %
                       (net.bytes_recv / (1024 * 1024)))

            fobj.write(Border + "\n\n")


            fobj.write("Process, Thread & Open Files Monitoring\n")
            fobj.write(Border + "\n")

            Data = ProcessScan()

            for info in Data:

                fobj.write("PID : %s\n" %
                           info.get("pid"))

                fobj.write("Process Name : %s\n" %
                           info.get("name"))

                fobj.write("Thread Count : %s\n" %
                           info.get("thread_count"))

                fobj.write("Open Files Count : %s\n" %
                           info.get("open_files_count"))

                fobj.write("Username : %s\n" %
                           info.get("username"))

                fobj.write("Status : %s\n" %
                           info.get("status"))

                fobj.write("Start Time : %s\n" %
                           info.get("create_time"))

                fobj.write("CPU %% : %.2f\n" %
                           info.get("cpu_percent"))

                fobj.write("Memory %% : %.2f\n" %
                           info.get("memory_percent"))

                fobj.write(Border + "\n")

            fobj.write("End Of Log File\n")
            fobj.write(Border + "\n")

    except Exception:
        pass

def main():

    Border = "-" * 70

    print(Border)
    print("Marvellous Platform Surveillance System")
    print(Border)

    if len(sys.argv) == 2:

        if sys.argv[1] in ("--h", "--H"):
            print("This script creates periodic system logs.")
            print("Includes CPU, RAM, Disk, Network,")
            print("Process, Threads and Open Files Monitoring.")

        elif sys.argv[1] in ("--u", "--U"):
            print("Usage : ScriptName.py TimeInterval DirectoryName")
            print("TimeInterval : Time in minutes")
            print("DirectoryName : Folder for log files")

        else:
            print("Invalid option. Use --h or --u")

    elif len(sys.argv) == 3:

        try:
            interval = int(sys.argv[1])
            FolderName = sys.argv[2]

            schedule.every(interval).minutes.do(
                CreateLog,
                FolderName
            )

            print("Platform Surveillance System started...")
            print("Press CTRL + C to stop execution")

            while True:
                schedule.run_pending()
                time.sleep(1)

        except ValueError:
            print("TimeInterval must be integer")

    else:
        print("Invalid number of arguments")

    print(Border)
    print("Thank you for using our script")
    print(Border)

if __name__ == "__main__":
    main()
