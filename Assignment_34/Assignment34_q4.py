import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile
import smtplib
from email.message import EmailMessage




def write_log(message, log_file):
    try:
        with open(log_file, "a") as f:
            f.write(message + "\n")
    except Exception:
        pass




def send_email(log_file, zip_file):
    try:
        sender_email = "your_email@gmail.com"
        sender_password = "your_app_password"
        receiver_email = "receiver_email@gmail.com"

        msg = EmailMessage()
        msg["Subject"] = "Marvellous Data Shield Backup Report"
        msg["From"] = sender_email
        msg["To"] = receiver_email

        msg.set_content(
            "Backup completed successfully.\n\n"
            "Attached:\n1. Log File\n2. Zip Backup File"
        )

        # Attach Log File
        if os.path.exists(log_file):
            with open(log_file, "rb") as f:
                msg.add_attachment(
                    f.read(),
                    maintype="application",
                    subtype="octet-stream",
                    filename=os.path.basename(log_file)
                )

        # Attach Zip File
        if zip_file and os.path.exists(zip_file):
            with open(zip_file, "rb") as f:
                msg.add_attachment(
                    f.read(),
                    maintype="application",
                    subtype="octet-stream",
                    filename=os.path.basename(zip_file)
                )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)

    except Exception:
        pass




def make_zip(folder):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = folder + "_" + timestamp + ".zip"

    try:
        with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zobj:
            for root, dirs, files in os.walk(folder):
                for file in files:
                    full_path = os.path.join(root, file)
                    relative = os.path.relpath(full_path, folder)
                    zobj.write(full_path, relative)
        return zip_name
    except Exception:
        return None




def calculate_hash(path):
    hobj = hashlib.md5()
    try:
        with open(path, "rb") as fobj:
            while True:
                data = fobj.read(1024)
                if not data:
                    break
                hobj.update(data)
        return hobj.hexdigest()
    except Exception:
        return None


# ----------------------------------------------------
# Backup Files (with Exclude Support)
# ----------------------------------------------------

def BackupFiles(Source, Destination, ExcludedExt):
    Copied_Files = []

    os.makedirs(Destination, exist_ok=True)

    for root, dirs, files in os.walk(Source):
        for file in files:

            # Skip excluded extensions
            if any(file.lower().endswith(ext) for ext in ExcludedExt):
                continue

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




def restore_backup(zip_file, destination):
    try:
        if not os.path.exists(zip_file):
            print("Zip file does not exist.")
            return

        os.makedirs(destination, exist_ok=True)

        with zipfile.ZipFile(zip_file, "r") as zobj:
            zobj.extractall(destination)

        print("Restore completed successfully.")

    except Exception:
        print("Error during restore.")




def marvellousDataShieldStart(Source="Data", ExcludedExt=None):

    if ExcludedExt is None:
        ExcludedExt = [".tmp", ".log", ".exe"]

    Border = "-" * 50
    BackupName = "MarvellousBackup"

    os.makedirs("Logs", exist_ok=True)

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    log_file = os.path.join("Logs", f"BackupLog_{timestamp}.txt")

    write_log(Border, log_file)
    write_log("Backup Started at: " + time.ctime(), log_file)
    write_log("Source Directory: " + Source, log_file)
    write_log("Excluded Extensions: " + ",".join(ExcludedExt), log_file)
    write_log(Border, log_file)

    try:
        files = BackupFiles(Source, BackupName, ExcludedExt)

        write_log("Files Copied:", log_file)
        for file in files:
            write_log(file, log_file)

        write_log("Total Files Copied: " + str(len(files)), log_file)

        zip_file = make_zip(BackupName)

        write_log("Zip Created: " + str(zip_file), log_file)
        write_log("Backup Completed at: " + time.ctime(), log_file)

        if zip_file:
            send_email(log_file, zip_file)

    except Exception as e:
        write_log("Error: " + str(e), log_file)

    write_log(Border, log_file)




def main():

    Border = "-" * 50
    print(Border)
    print("Marvellous Data Shield System")
    print(Border)

    # Restore Mode
    if len(sys.argv) == 4 and sys.argv[1] == "--restore":
        restore_backup(sys.argv[2], sys.argv[3])
        return

    # Backup Mode
    elif len(sys.argv) >= 3:

        try:
            interval = int(sys.argv[1])
            source_dir = sys.argv[2]

            if not os.path.exists(source_dir):
                print("Source directory does not exist.")
                return

            # Default excluded
            excluded = [".tmp", ".log", ".exe"]

            # Custom excluded
            if len(sys.argv) == 4:
                user_ext = sys.argv[3].split(",")
                excluded.extend(user_ext)

            schedule.every(interval).minutes.do(
                marvellousDataShieldStart,
                source_dir,
                excluded
            )

            print("Backup system started...")
            print("Interval (minutes):", interval)
            print("Excluded:", excluded)
            print("Press CTRL + C to stop")

            while True:
                schedule.run_pending()
                time.sleep(1)

        except ValueError:
            print("TimeInterval must be integer")

    else:
        print("Usage:")
        print("Backup:  python first.py Interval SourceDirectory")
        print("Custom:  python first.py 1 Data .pdf,.jpg")
        print("Restore: python first.py --restore ZipFile Destination")

    print(Border)


if __name__ == "__main__":
    main()
