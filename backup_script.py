import sys
import os
import datetime
import traceback
from shutil import disk_usage
from psutil import virtual_memory
from shutil import copytree, copy2

programPath = ""
measurePath = ""
cloudPath = ""
sType = ""
nameSensor = ""
logFile = ""
NumberOfSensor = 0
completeLogPath = ""
existing = False


class ArgvError(Exception):
    pass


def memory(memory_type):
    free_size = 0
    if memory_type == "RAM":
        free_size = virtual_memory()[4] / (2**20)
    else:
        free_size = disk_usage(memory_type)[2] / (2**30)

    return free_size


try:
    try:
        args = [sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7]]

        programPath = args[0].replace("backup_script.exe", "")
        measurePath = args[2]
        cloudPath = args[3]
        sType = args[4]
        nameSensor = args[5]
        logFile = args[6]
        NumberOfSensor = int(args[7])

        fromPath = measurePath + sType + "\\" + nameSensor
        toPath = cloudPath + sType + "\\" + nameSensor
        completeLogPath = programPath + logFile

    except:
        raise ArgvError

    print("Copy of data to server has been started ...")


    def copy_dir(src, dst, symlinks=False, ignore=None):
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                copytree(s, d, symlinks, ignore)
            else:
                copy2(s, d)

    copy_dir(fromPath, toPath)

except KeyboardInterrupt:
    with open(completeLogPath, 'r') as f:
        log = f.read()
        f.close()
    with open(completeLogPath, 'w') as f:
        log += "\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        log += "| Copy of data to cloud has stopped (" + str(NumberOfSensor + 1) + ". sensor). " \
               + "- User used keyboard-interrupt.\n"
        f.write(log)
        f.close()

except ArgvError:
    with open("C:\\Users\\Admin\\Desktop\\" + datetime.datetime.now().strftime("%y_%m_%d_%H_%M")
              + "_backup_script_error.txt", "w") as error_file:
        error_file.write(traceback.format_exc())
        error_file.close()

except OSError:
    with open(completeLogPath, 'r') as f:
        log = f.read()
        f.close()
    with open(completeLogPath, 'w') as f:
        log += "\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        log += "| Copy of data to cloud has failed (" + str(NumberOfSensor + 1) + ". sensor). " \
               + "- Program can't copy files (not permissions, not files or etc...).\n" + traceback.format_exc()
        f.write(log)
        f.close()


except (MemoryError, BufferError):
    with open(completeLogPath, 'r') as f:
        log = f.read()
        f.close()
    with open(completeLogPath, 'w') as f:
        log += "\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        log += "| Copy of data to cloud has failed (" + str(NumberOfSensor + 1) + ". sensor). " \
               + "- Problem with memory.\nFree date size on RAM: " + str(round(memory("RAM"), 3)) \
               + " MB\nFree data size on cloud: " + str(round(memory(cloudPath), 3)) \
               + " GB\n" + traceback.format_exc()
        f.write(log)
        f.close()

except:
    with open("C:\\Users\\Admin\\Desktop\\" + datetime.datetime.now().strftime("%y_%m_%d_%H_%M")
              + "_backup_script_error.txt", "w") as error_file:
        error_file.write(traceback.format_exc())
        error_file.close()

else:
    with open(completeLogPath, 'r') as f_read:
        log = f_read.read()
        f_read.close()
    with open(completeLogPath, 'w') as f_write:
        log += "\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        log += "| Copy of data to cloud of the " + str(NumberOfSensor + 1)
        log += ". sensor has been successfully completed.\n\t\t   Folder path: " + toPath
        f_write.write(log)
        f_write.close()
    with open(programPath + "BS_ok_" + str(NumberOfSensor) + ".txt", 'w') as f:
        f.close()
