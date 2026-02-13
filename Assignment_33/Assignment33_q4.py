# Platform Surveillance System
# Features:
# CPU, RAM, Disk, Network Monitoring
# Process, Threads, Open Files Monitoring
# Actual Memory Allocation (RSS, VMS)
# Periodic Log Creation
# Automatic Email Reporting

import psutil
import sys
import os
import time
import schedule
import smtplib
from email.message import EmailMessage


# --------------------------------------------------
# Process Scanning Function
# --------------------------------------------------

def ProcessScan():

    listprocess = []

    # Warm-up CPU calculation
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

            # Convert Start Time
            try:
                info["create_time"] = time.strftime(
                    "%Y-%m-%d %H:%M:%S",
                    time.localtime(info["create_time"])
                )
            except:
                info["create_time"] = "NA"

            # CPU Usage
            info["cpu_percent"] = proc.cpu_percent(interval=0.0)

            # Memory %
            info["memory_percent"] = proc.memory_percent()

            # Thread Count
            info["thread_count"] = proc.num_threads()

            # Actual Memory Allocation
            try:
                mem = proc.memory_info()
                info["rss"] = round(mem.rss / (1024 * 1024), 2)
                info["vms"] = round(mem.vms / (1024 * 1024), 2)
            except:
                info["rss"] = "NA"
                info["vms"] = "NA"

            # Open Files
            try:
                files = proc.open_files()
                info["open_files_count"] = len(files)
            except:
                info["open_files_count"] = "NA"

            listprocess.append(info)

        except:
            pass

    return listprocess



def SendEmail(LogFileName, ProcessData):

    try:
        sender_email = "sanikasurve2211@gmail.com"
        sender_password = "aqav aqcp ckil iwbu"
        receiver_email = "surveishwari296@gmail.com"

        msg = EmailMessage()
        msg["Subject"] = "Platform Surveillance System Report"
        msg["From"] = sender_email
        msg["To"] = receiver_email

        total_processes = len(ProcessData)

        # Sorting for top usage
        top_cpu = sorted(ProcessData,
                         key=lambda x: x["cpu_percent"],
                         reverse=True)[:5]

        top_memory = sorted(ProcessData,
                            key=lambda x: x["memory_percent"],
                            reverse=True)[:5]

        top_threads = sorted(ProcessData,
                             key=lambda x: x["thread_count"],
                             reverse=True)[:5]

        top_files = sorted(ProcessData,
                           key=lambda x: 0 if isinstance(
                               x["open_files_count"], str)
                           else x["open_files_count"],
                           reverse=True)[:5]

        body = f"""
Platform Surveillance System Report

Total Processes : {total_processes}

Top 5 CPU Usage Processes:
"""

        for proc in top_cpu:
            body += f"{proc['name']} (PID {proc['pid']}) - {proc['cpu_percent']}%\n"

        body += "\nTop 5 Memory Usage Processes:\n"
        for proc in top_memory:
            body += f"{proc['name']} (PID {proc['pid']}) - {proc['memory_percent']}%\n"

        body += "\nTop 5 Thread Count Processes:\n"
        for proc in top_threads:
            body += f"{proc['name']} (PID {proc['pid']}) - {proc['thread_count']} Threads\n"

        body += "\nTop 5 Open File Processes:\n"
        for proc in top_files:
            body += f"{proc['name']} (PID {proc['pid']}) - {proc['open_files_count']} Files\n"

        msg.set_content(body)

        # Attach Log File
        with open(LogFileName, "rb") as f:
            file_data = f.read()
            file_name = os.path.basename(LogFileName)

        msg.add_attachment(file_data,
                           maintype="application",
                           subtype="octet-stream",
                           filename=file_name)

        # Send Mail
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)

    except:
        pass



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

        ProcessData = ProcessScan()

        with open(FileName, "w") as fobj:

            fobj.write(Border + "\n")
            fobj.write("Marvellous Platform Surveillance System\n")
            fobj.write("Log Created at : " + time.ctime() + "\n")
            fobj.write(Border + "\n\n")

            # System Summary
            fobj.write("System Summary\n")
            fobj.write(Border + "\n")
            fobj.write("CPU Usage : %s %%\n" %
                       psutil.cpu_percent())

            mem = psutil.virtual_memory()
            fobj.write("RAM Usage : %s %%\n" %
                       mem.percent)

            fobj.write("Total Processes : %d\n" %
                       len(ProcessData))
            fobj.write(Border + "\n\n")

            # Process Details
            for info in ProcessData:

                fobj.write("PID : %s\n" % info.get("pid"))
                fobj.write("Process Name : %s\n" % info.get("name"))
                fobj.write("Username : %s\n" % info.get("username"))
                fobj.write("Status : %s\n" % info.get("status"))
                fobj.write("Start Time : %s\n" % info.get("create_time"))
                fobj.write("CPU %% : %.2f\n" % info.get("cpu_percent"))
                fobj.write("Memory %% : %.2f\n" % info.get("memory_percent"))
                fobj.write("RSS (MB) : %s\n" % info.get("rss"))
                fobj.write("VMS (MB) : %s\n" % info.get("vms"))
                fobj.write("Thread Count : %s\n" % info.get("thread_count"))
                fobj.write("Open Files : %s\n" % info.get("open_files_count"))
                fobj.write(Border + "\n")

        # Send Email After Log Creation
        SendEmail(FileName, ProcessData)

    except:
        pass




def main():

    Border = "-" * 70

    print(Border)
    print("Marvellous Platform Surveillance System")
    print(Border)

    if len(sys.argv) == 3:

        try:
            interval = int(sys.argv[1])
            FolderName = sys.argv[2]

            schedule.every(interval).minutes.do(
                CreateLog,
                FolderName
            )

            print("System started...")
            print("Press CTRL + C to stop")

            while True:
                schedule.run_pending()
                time.sleep(1)

        except ValueError:
            print("TimeInterval must be integer")

    else:
        print("Usage : ScriptName.py TimeInterval DirectoryName")

    print(Border)


if __name__ == "__main__":
    main()
