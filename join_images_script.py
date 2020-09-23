# SCRIPT JOINING SCREENS FROM SCANNING TOGETHER

from PIL import Image
from shutil import disk_usage
from psutil import virtual_memory
import sys
import datetime
import traceback
from os import path as pth
from subprocess import Popen

path = ""
cloudPath = ""
sType = ""
nameSensor = ""
NumberOfSensor = 0
pSensor = 1
programPath1 = ""
programPath2 = ""
logFile3 = ""
log = ""
completeLogPath = ""
except_con = 0
startArg = 0
endArg = 0
runNumber = 0


class ArgvError(Exception):
    pass


class ArrayError(Exception):
    pass


def test_print(num):
    """
    at = ""
    with open("C:\\Users\\Admin\\Desktop\\testPrint.txt", 'r') as f1:
        at = f1.read()
        f1.close()
    with open("C:\\Users\\Admin\\Desktop\\testPrint.txt", 'w') as f2:
        f2.write(at + str(num) + ", ")
        f2.close()
    """


def memory(memory_type):
    free_size = 0
    if memory_type == "RAM":
        free_size = virtual_memory()[4] / (2**20)
    else:
        free_size = disk_usage(memory_type)[2] / (2**30)

    return free_size


try:
    try:

        arg = [sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6],
               sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10], sys.argv[11], sys.argv[12]]

        path = sys.argv[2]
        cloudPath = sys.argv[3]
        sType = sys.argv[4]
        nameSensor = sys.argv[5]
        NumberOfSensor = int(sys.argv[6])
        pSensor = int(sys.argv[7])
        programPath1 = sys.argv[8]
        programPath2 = sys.argv[9]
        logFile = sys.argv[10]
        startArg = int(sys.argv[11])
        runNumber = int(sys.argv[11])
        """
        path = "D:\\"
        sType = "Downloads"
        nameSensor = "SN_18_02"
        NumberOfSensor = 1
        pSensor = 1
        programPath1 = "C:\\Users\\Uzivatel\\Desktop\\"
        programPath2 = ""
        logFile = "log_5_5.txt"
        """
        completeLogPath = programPath1 + " " + programPath2 + logFile

    except:
        raise ArgvError

    with open(programPath1 + " " + programPath2 + "JS_configFile_" + sType + ".txt", 'r') as config_file:  # mezeru
        c_del = config_file.readline()
        del c_del
        c_y = int(config_file.readline())

        defName = ["", ""]
        nX = 0
        nY = 0
        x = 0
        y = 0
        con = 0
        a = [0]*c_y
        b = [0]*c_y
        c = [0]*c_y
        d = [0]*c_y

        config_file.close()

    except_con = 1
    try:
        with open(programPath1 + " " + programPath2 + "JS_configFile_" + sType + ".txt", 'r') as config_file:  # mezeru
            c_char = ""
            c_num = 0

            c_del = config_file.readlines(2)
            del c_del

            c_v1 = ["", ""]
            c_v2 = ""
            c_v3 = [""]*c_y


            def get_txt_data(data_type=0):
                global c_char
                global c_num
                global c_y
                global c_v1
                global c_v2
                global c_v3

                if c_char == ";":   # ;
                    c_num += 1
                    # After program detect ';' it saving next string to next variable in array.
                else:
                    if data_type == 1:
                        c_v1[c_num] += c_char
                    elif data_type == 2:
                        c_v2 += c_char
                    elif data_type == 3:
                        c_v3[c_num] += c_char

                if data_type == 1 and c_v1[c_num] != "":
                    return c_v1[c_num]
                elif data_type == 2 and c_v2 != "":
                    return int(c_v2)
                elif data_type == 3 and c_v3[c_num] != "":
                    return int(c_v3[c_num])


            c_file = config_file.read()
            c_var = 0
            c_index = 0
            c_bool = False
            while c_index < len(c_file):
                c_char = c_file[c_index]  # Reading text one by one character.
                c_index += 1
                if c_char == " " or c_char == "\n":  # Deleting gabs and new line characters.
                    continue
                if c_char == "=":  # If program detect '=', it prepare to save next string.
                    c_var += 1
                    c_bool = True
                    continue
                if c_char == "#":  # If program detect '#', it end reading string.
                    c_num = 0
                    c_v1 = ["", ""]
                    c_v2 = ""
                    c_v3 = [""]*c_y
                    c_bool = False
                    # Reset variables.
                    continue

                if c_bool:  # Saving data only after detect '=' and before '#'.
                    if c_var == 1:
                        defName[c_num] = get_txt_data(1)
                    elif c_var == 2:
                        nX = get_txt_data(2)
                    elif c_var == 3:
                        nY = get_txt_data(2)
                    elif c_var == 4:
                        x = get_txt_data(2)
                    elif c_var == 5:
                        y = get_txt_data(2)
                    elif c_var == 6:
                        con = get_txt_data(2)
                    elif c_var == 7:
                        a[c_num] = get_txt_data(3)
                    elif c_var == 8:
                        b[c_num] = get_txt_data(3)
                    elif c_var == 9:
                        c[c_num] = get_txt_data(3)
                    elif c_var == 10:
                        d[c_num] = get_txt_data(3)
            config_file.close()

    except OSError:
        raise ArrayError
    """
    defName = ["Sensor_A12-", "_Scanning-"]
    nX = 4
    nY = 4
    x = 16
    y = 23
    a = [32, 14, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3,
         3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
         7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 16]
    b = [32, 10, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
         5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
    c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 16]
    d = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 14]
    if pSensor == 1:
        con = 225
    else:
        con = 5
    """
    m = startArg
    while m < (nX * nY):
        n = 0
        focus = 0
        pre_image_number = con
        finalImg = Image.new('RGB', (x * 640, y * 480))
        while n < y:
            o = 0
            lineImg = Image.new('RGB', (x * 640, 480))
            while o < x:
                if ((o + x * ((m + nX) % nX)) < a[n + y * (int(m / nX))]) or \
                        ((o - x * (nX - (m + nX) % nX)) >= - b[n + y * (int(m / nX))]) or \
                        (((o + x * ((m + nX) % nX)) >= c[n + y * (int(m / nX))]) and
                         ((o - x * (nX - (m + nX) % nX)) < - d[n + y * (int(m / nX))]) and
                         ((c[n + y * (int(m / nX))]) != 0 or d[n + y * (int(m / nX))] != 0)):
                    soloImg = Image.open(programPath1 + " " + programPath2 + "screens\\empty.BMP")  # mezeru do stringu
                else:
                    z = 0
                    k = 0
                    while k < (n + y * (int(m / nX)) + 1):
                        z += a[k]
                        k += 1
                    k = 0
                    while k < (n + y * (int(m / nX))):
                        z += b[k]
                        k += 1
                    k = 0
                    if (o - x * (nX - (m + nX) % nX)) > - d[n + y * (int(m / nX))]:
                        while k < (n + y * (int(m / nX)) + 1):
                            if c[k] != 0 or d[k] != 0:
                                z += ((nX * x) - (c[k] + d[k]))
                                if c[k] == 0:
                                    z -= (nX / 2 * x)
                                if d[k] == 0:
                                    z -= (nX / 2 * x)
                            k += 1
                    else:
                        while k < (n + y * (int(m / nX))):
                            if c[k] != 0 or d[k] != 0:
                                z += ((nX * x) - (c[k] + d[k]))
                                if c[k] == 0:
                                    z -= (nX / 2 * x)
                                if d[k] == 0:
                                    z -= (nX / 2 * x)
                            k += 1

                    image_number = x * y * nX * (int(m / nX))  # Added number of full scanned rows of tiles
                    #print(x * y * nX * (int(m / nX)))
                    image_number += x * n * nX  # Added all full scanned lines of sensor under scanned tiles
                    #print(x * n * nX)
                    image_number += x * (m % nX)  # Added all full scanned lines of tiles under ↑.
                    #print(x * (m % nX))
                    image_number += o  # Added rest of images in the last line.
                    #print(o)
                    image_number -= z  # Subtract number of all already used empty screens.
                    #print(z)
                    image_number *= 2  # Multiply by 2, because every of screens was created by 2 steps.
                    image_number += con  # Added number of origin steps.
                    #print(con)
                    #print(pre_image_number)
                    while pre_image_number < image_number + focus:
                        pre_image_number += 2
                        if not pth.exists(path + sType + "\\" + nameSensor + "\\" + str(defName[0]
                                          + sType + defName[1]) + str(pre_image_number) + "-"
                                          + str(runNumber) + ".BMP"):  # "R0" dat sType!!
                            focus += 2
                        if pre_image_number > 12000:
                            break

                    image_number += focus  # Added number of current used focus steps.
                    test_print(focus)

                    soloImg = Image.open(path + sType + "\\" + nameSensor + "\\" + str(defName[0]
                                         + sType + defName[1]) + str(image_number) + "-"
                                         + str(runNumber) + ".BMP")  # za "R0" dat sType!!

                    pre_image_number = image_number
                    test_print("\n")

                lineImg.paste(soloImg, (640 * o, 0))
                o += 1

            finalImg.paste(lineImg, (0, 480 * n))
            n += 1

        name = str(nY - int(m / nX)) + str(m % nX + 1)
        finalImg.save(path + sType + "\\" + nameSensor +
                      "\\output_" + name + "-" + str(runNumber) + ".BMP")
        m += 1
        print("Image number " + str(m) + " has been saved!")
        endArg = m

except KeyboardInterrupt:
    with open(completeLogPath, 'r') as f:
        log = f.read()
        f.close()
    with open(completeLogPath, 'w') as f:
        log += "\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        log += "| Copy of data to cloud has stopped (" + str(NumberOfSensor + 1) + ". sensor). " \
               + "- User used keyboard-interrupt.\n\t\t   Saved joined images: " \
               + str(abs(endArg-startArg)) + " (" + str(startArg + 1) + "-" + str(endArg) + ")"
        f.write(log)
        f.close()

except ArgvError:
    with open("C:\\Users\\Admin\\Desktop\\" + datetime.datetime.now().strftime("%y_%m_%d_%H_%M")
              + "_join_image_script_error.txt", "w") as error_file:
        error_file.write(traceback.format_exc())
        error_file.close()

except ArrayError:
    with open(completeLogPath, 'r') as f:
        log = f.read()
        f.close()
    with open(completeLogPath, 'w') as f:
        log += "\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        log += "| Joining of screens has failed (" + str(NumberOfSensor + 1) + ". sensor). " \
               + "- Program can't read variables from text file.\n" + traceback.format_exc()
        f.write(log)
        f.close()

except OSError:
    with open(completeLogPath, 'r') as f:
        log = f.read()
        f.close()
    if except_con == 0:
        with open(completeLogPath, 'w') as f:
            log += "\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
            log += "| Joining of screens has failed (" + str(NumberOfSensor + 1) + ". sensor). "\
                   + "- Program can't read variables from text file.\n" + traceback.format_exc()
            f.write(log)
            f.close()
    else:
        with open(completeLogPath, 'w') as f:
            log += "\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
            log += "| Joining of screens has failed (" + str(NumberOfSensor + 1) + ". sensor). " \
                   + "- Maybe not found screens.\n" + traceback.format_exc()
            f.write(log)
            f.close()

except (MemoryError, BufferError):
    with open(completeLogPath, 'r') as f:
        log = f.read()
        f.close()
    with open(completeLogPath, 'w') as f:
        log += "\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        log += "| Joining of screens has failed (" + str(NumberOfSensor + 1) + ". sensor). "\
               + "- Problem with memory.\nFree date size on RAM: " + str(round(memory("RAM"), 3))\
               + " MB\nFree data size on DISK: " + str(round(memory(programPath1[0:2]), 3))\
               + " GB\n" + traceback.format_exc()
        f.write(log)
        f.close()

except:
    with open("C:\\Users\\Admin\\Desktop\\" + datetime.datetime.now().strftime("%y_%m_%d_%H_%M")
              + "_join_image_script_error.txt", "w") as error_file:
        error_file.write(traceback.format_exc())
        error_file.close()

else:
    with open(completeLogPath, 'r') as f:
        log = f.read()
        f.close()
    with open(completeLogPath, 'w') as f:
        log += "\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        log += "| Joining of screens has been successfully completed (" + str(NumberOfSensor + 1) + ". sensor)"
        f.write(log)
        f.close()
    with open(programPath1 + " " + programPath2 + "JS_ok_" + str(NumberOfSensor) + ".txt", 'w') as f:
        f.close()

    try:
        arg_bs = programPath1 + " " + programPath2 + "backup_script.exe 1 " + path + " " + cloudPath \
                 + " " + sType + " " + nameSensor + " " + logFile + " " + str(NumberOfSensor)
        Popen(arg_bs)
    except OSError:
        with open(completeLogPath, 'r') as f:
            log = f.read()
            f.close()
        with open(completeLogPath, 'w') as f:
            log += "\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
            log += "| Copy of data (" + str(NumberOfSensor + 1) + ". sensor) to cloud has failed at startup\n"
            log += traceback.format_exc()
            f.write(log)
            f.close()

    else:
        with open(completeLogPath, 'r') as f:
            log = f.read()
            f.close()
        with open(completeLogPath, 'w') as f:
            log += "\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
            log += "| Copy of data to cloud of the "
            log += str(NumberOfSensor + 1) + ". has been successfully started"
            f.write(log)
            f.close()
