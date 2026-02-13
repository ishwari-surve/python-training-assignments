# Command Line Input

import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile




def write_log(message, log_file):
    with open(log_file, "a") as f:
        f.write(message + "\n")




def make_zip(folder):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = folder + "_" + timestamp + ".zip"

    try:
        zobj = zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED)

        for root, dirs, files in os.walk(folder):
            for file in files:
                full_path = os.path.join(root, file)
                relative = os.path.relpath(full_path, folder)
                zobj.write(full_path, relative)

        zobj.close()
        return zip_name

    except Exception as e:
        return f"Error creating zip: {str(e)}"




def calculate_hash(path):
    hobj = hashlib.md5()

    with open(path, "rb") as fobj:
        while True:
            data = fobj.read(1024)
            if not data:
                break
            hobj.update(data)

    return hobj.hexdigest()


# ----------------------------------------------------
# Backup Files Function
# ----------------------------------------------------

def BackupFiles(Source, Destination):
    Copied_Files = []

    os.makedirs(Destination, exist_ok=True)

    for root, dirs, files in os.walk(Source):
        for file in files:
            src_path = os.path.join(root, file)
            relative = os.path.relpath(src_path, Source)
            dest_path = os.path.join(Destination, relative)

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            try:
                if (not os.path.exists(dest_path)) or \
                        (calculate_hash(src_path) != calculate_hash(dest_path)):
                    shutil.copy2(src_path, dest_path)
                    Copied_Files.append(relative)

            except Exception:
                pass

    return Copied_Files




def marvellousDataShieldStart(Source="Data"):

    Border = "-" * 50

    BackupName = "MarvellousBackup"

    # Create Logs folder
    os.makedirs("Logs", exist_ok=True)

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    log_file = os.path.join("Logs", f"BackupLog_{timestamp}.txt")

    write_log(Border, log_file)
    write_log("Backup Process Started at: " + time.ctime(), log_file)
    write_log("Source Directory: " + Source, log_file)
    write_log(Border, log_file)

    try:
        files = BackupFiles(Source, BackupName)

        write_log("Files Copied:", log_file)

        for file in files:
            write_log(file, log_file)

        write_log(f"Total Files Copied: {len(files)}", log_file)

        zip_file = make_zip(BackupName)

        write_log("Zip File Created: " + str(zip_file), log_file)

        write_log("Backup Completed Successfully at: " + time.ctime(), log_file)

    except Exception as e:
        write_log("Error Occurred: " + str(e), log_file)

    write_log(Border, log_file)




def main():

    Border = "-" * 50
    print(Border)
    print("----------Marvellous Data Shield System-----------")
    print(Border)

    if len(sys.argv) == 2:

        if sys.argv[1] in ("--h", "--H"):
            print("1 : Text autobackup at given time")
            print("2 : Backup only new and updated files")
            print("3 : Create archive of the backup periodically")
            print("4 : Logging system added")

        elif sys.argv[1] in ("--u", "--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeInterval: Time in minutes")
            print("SourceDirectory : Directory to be backed up")

        else:
            print("Invalid option. Use --h or --u")

    elif len(sys.argv) == 3:

        try:
            interval = int(sys.argv[1])
            source_dir = sys.argv[2]

            schedule.every(interval).minutes.do(
                marvellousDataShieldStart,
                source_dir
            )

            print(Border)
            print("Data Shield System started successfully")
            print("Time Interval (minutes):", interval)
            print("Press CTRL + C to stop execution")

            while True:
                schedule.run_pending()
                time.sleep(1)

        except ValueError:
            print("TimeInterval must be integer")

    else:
        print("Invalid number of command line arguments")
        print("Use --h or --u for help")

    print(Border)
    print("----------Thank you for using our script----------")
    print(Border)


if __name__ == "__main__":
    main()
