# SCRIPT DECLARING ALL BASIC FUNCTION THOSE NOT CALL BY GUI OR NOT USING ERROR SYSTEM

from SMS_Initialize import*
# Import script with data about bookmarks and declaring of variables.


def mm3d_on():
    if pag.locateCenterOnScreen(Img.mm3dOn, grayscale=True) \
            or pag.locateCenterOnScreen(Img.mm3dOn2, grayscale=True) \
            or pag.locateCenterOnScreen(Img.mm3dOn3, grayscale=True) \
            or pag.locateCenterOnScreen(Img.mm3dOn4, grayscale=True):
        return True
    else:
        return False


def open_routine():
    pag.click(Position.file)  # Click to "File".
    wait(sleep_until="open.png")
    if not if_find_error():
        pag.click(Position.open)  # Open routine.
        time.sleep(2)


def search_file():
    pag.hotkey("alt", "d")  # Select all text in searching box for transcription.
    time.sleep(0.5)
# ↑ For saving file of measuring.


def reset_origins():
    time.sleep(3)
    pag.click(Position.resetX)
    pag.moveRel(0, 100)
    wait(sleep_until=["resetXOn+.png", "resetXOn-.png"])
    if not if_find_error():
        time.sleep(0.5)
        pag.click(Position.resetY)
        pag.moveRel(0, 100)
        wait(sleep_until=["resetYOn+.png", "resetYOn-.png"])
    # ↑ Reset origin of mm3d for start measuring new sensor. Click to three buttons.


def start_routine(routine):
    open_routine()
    if not if_find_error():
        search_file()
    if not if_find_error():
        pag.typewrite(measurePath + "Routines")  # Search place in pc.
        time.sleep(1)
    if not if_find_error():
        pag.typewrite(["enter"])
        wait(sleep_until="folderOn.png")
    if not if_find_error():
        file_name = pag.locateCenterOnScreen(programPath + "screens\\filenameOn.png")
        if file_name:
            time.sleep(0.5)
            pag.click(file_name[0] + 100, file_name[1])
            time.sleep(0.2)
            pag.hotkey("ctrl", "a")
        else:
            time.sleep(0.3)
            pag.hotkey("alt", "n")  # Switch to textbox of 'Name file'.
            time.sleep(0.5)
    if not if_find_error():
        pag.typewrite(routine)  # Write name of routine.
        time.sleep(1)
    if not if_find_error():
        pag.typewrite(["enter"])
        wait(sleep_until=["mm3dOn.png", "mm3dOn2.png", "mm3dOn3.png", "mm3dOn4.png"])
    if not if_find_error():
        time.sleep(5)
        pag.click(Position.start)  # Start routine.
        wait(sleep_until="startRoutineOn.png")
    if not if_find_error():
        pag.typewrite(["enter"])  # Confirming start.


def save_file(save_path, save_name=""):
    pag.typewrite(save_path)  # Search sensor folder.
    time.sleep(1)
    if not if_find_error():
        pag.typewrite(["enter"])
        wait(sleep_until="folderOn.png")
    if not if_find_error() and save_name != "":
        if not if_find_error():
            file_name = pag.locateCenterOnScreen(programPath + "screens\\filenameOn.png")
            if file_name:
                pag.click(file_name[0] + 100, file_name[1])
                time.sleep(0.2)
                pag.hotkey("ctrl", "a")
            else:
                time.sleep(0.3)
                pag.hotkey("alt", "n")  # Switch to textbox of 'Name file'.
                time.sleep(0.5)
        if not if_find_error():
            pag.typewrite(save_name)  # Write name of routine.
            time.sleep(1)
    if not if_find_error():
        pag.click(Position.save)  # Save file.
        wait(sleep_until=["mm3dOn.png", "mm3dOn2.png", "mm3dOn3.png", "mm3dOn4.png"])
    if not if_find_error():
        pag.moveTo(900, 0)  # Move cursor from 'save' button.


def save_log(text="", first_run=False, return_log_file=False):
    log = ""
    global logFile
    if return_log_file:
        return logFile
    else:
        if not first_run:
            with open(programPath + logFile, 'r') as log_file:
                log = log_file.read()
                log_file.close()
        else:
            logFile = "logs\\" + datetime.datetime.now().strftime("%y_%m_%d_%H_%M") + ".txt"
        # If not first write to log file, read already exist text and save to 'log'.
        with open(programPath + logFile, 'w') as log_file:
            log_file.write(log + text)
            log_file.close()
        # Write data from argument 'text' of function and variable 'log' to file.
# Function writing information to a log file.


def reset_mm3d(mm3d=False):
    time.sleep(0.5)
    if mm3d:
        if not mm3d_on():
            pag.click(Position.mm3d)
            wait(sleep_until=["mm3dOn.png", "mm3dOn2.png", "mm3dOn3.png", "mm3dOn4.png"])
    # ↑ Switch to mm3d for next reset.
    if not if_find_error():
        if pag.locateCenterOnScreen(Img.quitStep, grayscale=True):
            pag.click(Position.quitStep)
            time.sleep(1)
    if not if_find_error():
        pag.click(Position.system)
        wait(sleep_until="resetSystem.png")
    if not if_find_error():
        pag.click(Position.resetSystem)
        if not pag.locateCenterOnScreen(Img.system, grayscale=True):
            time.sleep(0.5)
            pag.typewrite(["enter"])
        wait(sleep_until="system.png")
    # ↑ Reset all system of mm3d.
    if not if_find_error():
        time.sleep(0.5)
        pag.typewrite(["enter"])
# ↑ Complete reset MeasureMind 3d program to default settings.


def default():
    global defaultRepetition
    proces_var = False

    if not if_find_error():
        proces_var = True

    control_language()
    # ↑ Switch to eng keyboard if it doesn't.

    if defaultRepetition < 4:
        if defaultRepetition == 2:
            time.sleep(60*2)
            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                     + "| Program has been gone to sleep for 2 minutes, because system don't respond.")
        defaultRepetition = defaultRepetition + 1
        try:
            pag.screenshot(programPath + "Error Screenshots\\"
                           + datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S") + ".png")
        except (MemoryError, BufferError):
            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                     + "| Taking of the screenshot has failed - (RAM: "
                     + str(memory("RAM")) + " MB, DISK: " + str(memory(programPath[0:2]))
                     + " GB).\n" + traceback.format_exc())

        time.sleep(0.5)
        error_icon = pag.locateCenterOnScreen(Img.error, grayscale=True)
        if error_icon:
            pag.click(error_icon)

        if if_repeat_measure() and defaultRepetition < 2:

            pag.typewrite(["enter"])
            time.sleep(1)

            Position.stop = pag.locateCenterOnScreen(Img.stopOn, grayscale=True)
            pag.click(Position.stop)
            wait(sleep_until="end_w.png")
            pag.typewrite(["enter"])
            time.sleep(1)

            pag.click(Position.centroid)
            time.sleep(1)
            pag.typewrite(["enter"])

        else:
            if pag.locateCenterOnScreen(Img.folderOn, grayscale=True):
                pag.typewrite(["esc"])
            elif defaultRepetition < 2:
                pag.typewrite(["enter"])

        if mm3d_on():
            stop_on = pag.locateCenterOnScreen(Img.stopOn, grayscale=True)
            if stop_on:
                Position.stop = list(stop_on)
                pag.click(Position.stop)
                wait(sleep_until="end_w.png")
                pag.typewrite(["enter"])

            if pag.locateCenterOnScreen(Img.quitStep, grayscale=True):
                pag.click(Position.quitStep)
                time.sleep(1)

            img_reset_system = pag.locateCenterOnScreen(Img.resetSystem, grayscale=True)
            if img_reset_system:
                Position.resetSystem = list(img_reset_system)
                pag.click(Position.system)
                time.sleep(0.5)

            pag.click(Position.system)
            wait(sleep_until="resetSystem.png")

            pag.click(Position.resetSystem)
            time.sleep(0.5)
            pag.typewrite(["enter"])
        elif pag.locateCenterOnScreen(programPath + "screens\\folderOn.png") \
                or pag.locateCenterOnScreen(programPath + "screens\\f4On.png") \
                or pag.locateCenterOnScreen(programPath + "screens\\ctrlaOn.png")\
                or pag.locateCenterOnScreen(programPath + "screens\\filenameOn.png"):
            pag.click()
            time.sleep(0.1)
            pag.typewrite("esc")
            time.sleep(0.1)
            pag.typewrite("esc")
            if mm3d_on():
                pag.click(Position.mm3d)
                wait(sleep_until=["mm3dOn.png", "mm3dOn2.png", "mm3dOn3.png", "mm3dOn4.png"])
        else:
            time.sleep(0.1)
            pag.typewrite("esc")
            time.sleep(0.2)
            pag.typewrite("esc")
            time.sleep(0.2)
            pag.click(Position.mm3d)
            wait(sleep_until=["mm3dOn.png", "mm3dOn2.png", "mm3dOn3.png", "mm3dOn4.png"])

        defaultRepetition = 0
        if proces_var:
            set_process_error()
        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                 "| It seems that system has been successfully reset by 'default function'.")
    else:
        raise WaitError("Error has been occurred in 'default' function.\n"
                        "The program has failed to solve the problem even four times in a row.")

# ↑ Set computer to default (know) position - mm3d program.


def find_objects():
    Position.mm3d = pag.locateCenterOnScreen(Img.mm3d, grayscale=True)
    # ↑ Overwrite position of MM3D icon.
    pag.click(Position.mm3d)
    wait(sleep_until=["mm3dOn.png", "mm3dOn2.png", "mm3dOn3.png", "mm3dOn4.png"])
    if if_find_error():
        raise WaitError("Not located 'mm3dOn.png'")
    Position.file = pag.locateCenterOnScreen(Img.file, grayscale=True)
    Position.system = pag.locateCenterOnScreen(Img.system, grayscale=True)
    Position.resetRoutine = pag.locateCenterOnScreen(Img.resetRoutine, grayscale=True)
    Position.resetX = pag.locateCenterOnScreen(Img.resetX, grayscale=True)
    Position.resetY = pag.locateCenterOnScreen(Img.resetY, grayscale=True)
    Position.resetZ = pag.locateCenterOnScreen(Img.resetZ, grayscale=True)
    Position.resetAngle = pag.locateCenterOnScreen(Img.resetAngle, grayscale=True)
    Position.start = pag.locateCenterOnScreen(Img.start, grayscale=True)
    Position.saveRoutine = pag.locateCenterOnScreen(Img.saveRoutine, grayscale=True)
    Position.deleteSteps = pag.locateCenterOnScreen(Img.deleteSteps, grayscale=True)
    Position.centroid = pag.locateCenterOnScreen(Img.centroid, grayscale=True)
    pag.click(Position.centroid)
    time.sleep(1)
    pag.click(pag.size()[0] / 5.5, pag.size()[1] / 4)
    wait(sleep_until="quitStep.png")
    if if_find_error():
        raise WaitError("Not located 'quitStep.png'")
    Position.quitStep = pag.locateCenterOnScreen(Img.quitStep, grayscale=True)
    pag.click(Position.quitStep)
    time.sleep(1)
    pag.click(Position.file)
    wait(sleep_until="open.png")
    if if_find_error():
        raise WaitError("Not located 'open.png'")
    Position.open = pag.locateCenterOnScreen(Img.open, grayscale=True)
    pag.moveTo(Position.system)
    wait(sleep_until="resetSystem.png")
    if if_find_error():
        raise WaitError("Not located 'resetSystem.png'")
    Position.resetSystem = pag.locateCenterOnScreen(Img.resetSystem, grayscale=True)
    pag.click(Position.system)

    if not mm3d_on():
        pag.click(Position.mm3d)
        wait(sleep_until=["mm3dOn.png", "mm3dOn2.png", "mm3dOn3.png", "mm3dOn4.png"])
    if if_find_error():
        raise WaitError("Not located 'mm3dOn.png'")


def protocol_loop(line):
    string = ""
    protocol_a = 0
    protocol_b = 0
    protocol_c = 0
    while protocol_a < 90:
        protocol_b += 1
        if protocol_b == 10:
            string += "|"
            protocol_b = 0
            protocol_c += 1
        elif protocol_b == 5:
            if line == 1:
                string += str(protocol_c + 1)
            if line == 2:
                if sType[protocol_c] == "" or sType[protocol_c] == "E" \
                        or pSensor[protocol_c] == 0 or nameSensor[protocol_c] == "":
                    string += "-"
                elif sensorPosition[protocol_c] == 1:
                    string += "O"
                else:
                    string += "X"
            if line == 3:
                if ErrorId.createFolder[protocol_c] == 0:
                    string += "-"
                elif ErrorId.createFolder[protocol_c] == 1:
                    string += "O"
                else:
                    string += "X"
            if line == 4:
                if ErrorId.completeMeasuring[protocol_c] == 0 and ErrorId.startMeasuring[protocol_c] == 0:
                    string += "-"
                elif ErrorId.completeMeasuring[protocol_c] == 1:
                    string += "O"
                else:
                    string += "X"
            if line == 5:
                if ErrorId.editOutput[protocol_c] == 0:
                    string += "-"
                elif ErrorId.editOutput[protocol_c] == 1:
                    string += "O"
                else:
                    string += "X"
            if line == 6:
                if ErrorId.moveTrash[protocol_c] == 0:
                    string += "-"
                elif ErrorId.moveTrash[protocol_c] == 1:
                    string += "O"
                else:
                    string += "X"
            if line == 7:
                if ErrorId.completeScanning[protocol_c] == 0 and ErrorId.startScanning[protocol_c] == 0:
                    string += "-"
                elif ErrorId.completeScanning[protocol_c] == 1:
                    string += "O"
                else:
                    string += "X"
            if line == 8:
                if ErrorId.moveScreens[protocol_c] == 0:
                    string += "-"
                elif ErrorId.moveScreens[protocol_c] == 1:
                    string += "O"
                else:
                    string += "X"
            if line == 9:
                if ErrorId.completeJoinScreens[protocol_c] == 0 and ErrorId.startJoinScreens[protocol_c] == 0:
                    string += "-"
                elif ErrorId.completeJoinScreens[protocol_c] == 1:
                    string += "O"
                else:
                    string += "X"
            if line == 10:
                if ErrorId.dataSizeTest[protocol_c] == 0:
                    string += "-"
                elif ErrorId.dataSizeTest[protocol_c] == 1:
                    string += "O"
                else:
                    string += "X"
            if line == 11:
                if ErrorId.copyToCloud[protocol_c] == 0:
                    string += "-"
                elif ErrorId.copyToCloud[protocol_c] == 1:
                    string += "O"
                else:
                    string += "X"

        elif protocol_b == 6 and line == 1:
            string += "."
        else:
            string += " "
        protocol_a += 1
    protocol_a = 0
    string += "\n"
    while protocol_a < 110:
        string += "_"
        protocol_a += 1

    return string
# ↑ Function generating strings for protocol.


def protocol():
    temp_write = ""

    with open(programPath + "Protocols\\" + "Protocol_" +
              datetime.datetime.now().strftime("%y_%m_%d_%H_%M") + ".txt", 'w') as protocol_file:
        temp_write += "\nDidn't do ......... - \nEverything done ... O \nError occurred .... X " \
                      "\n______________________________\n\n"
        temp_write += "______________________________________________________" \
                      "________________________________________________________"
        temp_write += "\nSENSOR:            ||" + protocol_loop(1)
        temp_write += "\n______________________________________________________" \
                      "________________________________________________________"
        temp_write += "\nControl sensor     ||" + protocol_loop(2)
        temp_write += "\nCreate a folder    ||" + protocol_loop(3)
        temp_write += "\nMeasuring          ||" + protocol_loop(4)
        temp_write += "\nData transcription ||" + protocol_loop(5)
        temp_write += "\nMove trash         ||" + protocol_loop(6)
        temp_write += "\nScanning           ||" + protocol_loop(7)
        temp_write += "\nMove screens       ||" + protocol_loop(8)
        temp_write += "\nJoin screens       ||" + protocol_loop(9)
        temp_write += "\nData size test     ||" + protocol_loop(10)
        temp_write += "\nCopy data to cloud ||" + protocol_loop(11)

        protocol_file.write(temp_write)
        protocol_file.close()
# ↑ Generating protocol text file.


def control_multi_runs(control_path):
    if os.path.exists(control_path):
        files = os.listdir(control_path)
        for file in files:
            if (not file.endswith(str(runNumber[NumberOfSensor]) + ".BMP") and file.endswith(".BMP")) or\
                    (not file.endswith(str(runNumber[NumberOfSensor]) + ".dat") and file.endswith(".dat")):
                return True
        return False
    else:
        return False


def check_size(source):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(source):
        for p in filenames:
            pp = os.path.join(dirpath, p)
            total_size += os.path.getsize(pp)
    return total_size
# ↑ Function for control of size of folder with data.


def limit_size(sensor_number):
    temp_limit = [0, 0]

    if sType[sensor_number] == "R0":
        if mSensor[sensor_number] == 1:
            temp_limit[0] += LimitSize.R0[0]
            temp_limit[1] += LimitSize.R0[1]
        if sSensor[sensor_number] == 1:
            temp_limit[0] += LimitSize.R0[2]
            temp_limit[1] += LimitSize.R0[3]
    elif sType[sensor_number] == "R1":
        if mSensor[sensor_number] == 1:
            temp_limit[0] += LimitSize.R1[0]
            temp_limit[1] += LimitSize.R1[1]
        if sSensor[sensor_number] == 1:
            temp_limit[0] += LimitSize.R1[2]
            temp_limit[1] += LimitSize.R1[3]
    elif sType[sensor_number] == "R2":
        if mSensor[sensor_number] == 1:
            temp_limit[0] += LimitSize.R2[0]
            temp_limit[1] += LimitSize.R2[1]
        if sSensor[sensor_number] == 1:
            temp_limit[0] += LimitSize.R2[2]
            temp_limit[1] += LimitSize.R2[3]
    elif sType[sensor_number] == "R3":
        if mSensor[sensor_number] == 1:
            temp_limit[0] += LimitSize.R3[0]
            temp_limit[1] += LimitSize.R3[1]
        if sSensor[sensor_number] == 1:
            temp_limit[0] += LimitSize.R3[2]
            temp_limit[1] += LimitSize.R3[3]
    elif sType[sensor_number] == "R4":
        if mSensor[sensor_number] == 1:
            temp_limit[0] += LimitSize.R4[0]
            temp_limit[1] += LimitSize.R4[1]
        if sSensor[sensor_number] == 1:
            temp_limit[0] += LimitSize.R4[2]
            temp_limit[1] += LimitSize.R4[3]
    elif sType[sensor_number] == "R5":
        if mSensor[sensor_number] == 1:
            temp_limit[0] += LimitSize.R5[0]
            temp_limit[1] += LimitSize.R5[1]
        if sSensor[sensor_number] == 1:
            temp_limit[0] += LimitSize.R5[2]
            temp_limit[1] += LimitSize.R5[3]
    elif sType[sensor_number] == "B":
        if mSensor[sensor_number] == 1:
            temp_limit[0] += LimitSize.B[0]
            temp_limit[1] += LimitSize.B[1]
        if sSensor[sensor_number] == 1:
            temp_limit[0] += LimitSize.B[2]
            temp_limit[1] += LimitSize.B[3]

    return temp_limit


def after_laser_error():
    time.sleep(0.5)
    pag.click(Position.resetRoutine)
    time.sleep(0.5)
    pag.typewrite(["enter"])
    wait(sleep_until="resetRoutineOn.png")


def wait_previous(sleep_until):
    number_of_images = 0
    for images in sleep_until:
        if images != "":
            number_of_images += 1

    if number_of_images > 4 or number_of_images == 1:
        if pag.locateCenterOnScreen(programPath + "screens\\" + sleep_until[:]):
            return False
        else:
            return True

    elif number_of_images == 2:
        if pag.locateCenterOnScreen(programPath + "screens\\" + sleep_until[0]) \
                or pag.locateCenterOnScreen(programPath + "screens\\" + sleep_until[1]):
            return False
        else:
            return True

    elif number_of_images == 3:
        if pag.locateCenterOnScreen(programPath + "screens\\" + sleep_until[0]) \
                or pag.locateCenterOnScreen(programPath + "screens\\" + sleep_until[1]) \
                or pag.locateCenterOnScreen(programPath + "screens\\" + sleep_until[2]):
            return False
        else:
            return True

    elif number_of_images == 4:
        if pag.locateCenterOnScreen(programPath + "screens\\" + sleep_until[0])\
                or pag.locateCenterOnScreen(programPath + "screens\\" + sleep_until[1]) \
                or pag.locateCenterOnScreen(programPath + "screens\\" + sleep_until[2]) \
                or pag.locateCenterOnScreen(programPath + "screens\\" + sleep_until[3]):
            return False
        else:
            return True


def wait_measure(saving=True):
    global error
    if datetime.datetime.now().minute % 10 == 0 and datetime.datetime.now().second < 5:
        if not mm3d_on():
            pag.click(Position.mm3d)
    if pag.locateCenterOnScreen(Img.error, grayscale=True):
        if pag.locateCenterOnScreen(Img.laserError1, grayscale=True) \
                or pag.locateCenterOnScreen(Img.laserError2, grayscale=True):
            set_repeat_measure()
            default()
        else:
            error = 2
            default()
            set_process_error(1)
    else:
        if saving:
            end_wait = pag.locateCenterOnScreen(Img.end_s)
        else:
            end_wait = pag.locateCenterOnScreen(Img.end_w)
        # ↑ Finding image on screen.
        if end_wait:
            if saving:
                Position.save = list(end_wait)  # Overwrite position of save button.
            else:
                pag.typewrite(["enter"])  # Confirm end of routine.
        else:
            return True


def wait(saving=True, sleep_until=None):
    global error

    if sleep_until:
        if os.path.exists(programPath + "skip_wait.dat"):
            time.sleep(1)
        else:
            first_time_s = datetime.datetime.now().second + datetime.datetime.now().microsecond / 1000000
            first_time_m = datetime.datetime.now().minute
            while wait_previous(sleep_until):
                act_time = datetime.datetime.now().second + datetime.datetime.now().microsecond / 1000000
                if datetime.datetime.now().minute != first_time_m:
                    act_time += 60
                if act_time - first_time_s > maxSleepTime:
                    error = 2
                    default()
                    set_process_error(1)
                    break
    else:
        while wait_measure(saving):
            pass

# ↑ Waiting system, if on screen will appear required image, loop will end.


def if_repeat_measure():

    if sensorPos == 0:
        return True
    else:
        return False


def set_repeat_measure(value=0):
    global sensorPos

    sensorPos = value


def if_bad_pos():
    global error
    if error == 1:
        return True
    else:
        return False


def after_error_reset():
    global NumberOfSensor
    global error
    error = 0
    NumberOfSensor = 0
    for NumberOfSensor in range(0, 9):
        set_repeat_measure()
        sensorPosition[NumberOfSensor] = 0
        ErrorId.createFolder[NumberOfSensor] = 0
        ErrorId.startMeasuring[NumberOfSensor] = 0
        ErrorId.completeMeasuring[NumberOfSensor] = 0
        ErrorId.editOutput[NumberOfSensor] = 0
        ErrorId.moveTrash[NumberOfSensor] = 0
        ErrorId.startScanning[NumberOfSensor] = 0
        ErrorId.completeScanning[NumberOfSensor] = 0
        ErrorId.moveScreens[NumberOfSensor] = 0
        ErrorId.startJoinScreens[NumberOfSensor] = 0
        ErrorId.completeJoinScreens[NumberOfSensor] = 0
        ErrorId.dataSizeTest[NumberOfSensor] = 0
        ErrorId.copyToCloud[NumberOfSensor] = 0
    NumberOfSensor = 0


def if_find_error():
    temp_error = bool(processError)

    return temp_error


def set_process_error(value=0):
    global processError

    processError = value


def memory(memory_type):
    free_size = 0
    if memory_type == "RAM":
        free_size = virtual_memory()[4] / (2**20)
    else:
        free_size = disk_usage(memory_type)[2] / (2**30)

    return round(free_size, 3)


def wait_end_process(program_name):
    for program in (p.name() for p in process_iter()):
        if program == program_name:
            return True
    return False
# ↑ Program will wait until end of process.


def control_language():
    if not pag.locateCenterOnScreen(Img.language, grayscale=True):
        pag.hotkey("alt", "shift")
        time.sleep(2)
        if not pag.locateCenterOnScreen(Img.language, grayscale=True):
            pag.hotkey("alt", "shift")
            time.sleep(2)
            if not pag.locateCenterOnScreen(Img.language, grayscale=True):
                pag.hotkey("alt", "shift")


def control_string(string):
    char_count = 0
    line_count = 0
    for char in string:
        line_count += 1
        if char == "\n":
            char_count += 1
    return char_count, line_count


def check_database():
    request = rq_get(LabPar.DatabasePath)

    with open(programPath + "values.xml", 'wb') as database:
        database.write(request.content)
        database.close()

    tree = ET.parse(programPath + "values.xml")
    root = tree.getroot()
    for part in root:
        if part.tag == LabPar.TempNum:
            for sub_part in part:
                if sub_part.tag == "v":
                    LabPar.Temperature = sub_part.text
        elif part.tag == LabPar.HumNum:
            for sub_part in part:
                if sub_part.tag == "v":
                    LabPar.Humidity = sub_part.text


def write_accuracy(number_of_sensor):
    return "\nAngle of sensor: " + str(round(ControlPar.Angle[number_of_sensor], 3)) \
           + " - limit interval is (" + str((getattr(LimitDistance, "Phi_" + sType[NumberOfSensor]))[0]) + " ; " \
           + str((getattr(LimitDistance, "Phi_" + sType[NumberOfSensor]))[1]) \
           + ")\nHorizontal deviation of sensor: " + str(round(ControlPar.Hdis[number_of_sensor], 3)) \
           + " - limit interval is (" + str(LimitDistance.RightD[0]) + " ; " + str(LimitDistance.RightD[1]) \
           + ")\nVertical deviation of sensor: " + str(round(ControlPar.Vdis[number_of_sensor], 3)) \
           + " - limit interval is (" + str(LimitDistance.BottomD[0]) + " ; " + str(LimitDistance.BottomD[1]) + ")"


def edit_output(data_type, number_of_sensor):
    global planarityX
    global planarityY
    global planarityZ
    if data_type == 0:
        output_file = ""
        with open(measurePath + sType[number_of_sensor] + "\\" + nameSensor[number_of_sensor]
                  + "\\planarity.txt", 'r') as data_file:
            output_index = 0
            while output_index < 6000:
                output_char = data_file.read(1)
                if output_char == "#" or output_char == "X" \
                        or output_char == "Y" or output_char == "Z":
                    pass
                else:
                    output_file += output_char
                output_index += 1
            data_file.close()
        with open(measurePath + sType[number_of_sensor] + "\\" + nameSensor[number_of_sensor]
                  + "\\planarity.txt", 'w') as data_file:
            data_file.write(output_file)
            data_file.close()

        planarityX, planarityY, planarityZ = np.loadtxt(
            measurePath + sType[number_of_sensor] + "\\" + nameSensor[number_of_sensor] + "\\planarity.txt",
            skiprows=1,
            unpack=True
        )
    main_name_file = ""
    if data_type == 0:
        main_name_file = "_Bow_"
    if data_type == 1:
        main_name_file = "_MAINThickness_"
    if data_type == 2:
        main_name_file = "_PRIVATE_"
    name_file = sensorBatch[number_of_sensor] + "-W" + sensorWafer[number_of_sensor] +\
        main_name_file + "0"*(3 - len(str(runNumber[number_of_sensor]))) + str(runNumber[number_of_sensor])\
        + ".dat"
    with open(measurePath + sType[number_of_sensor] + "\\" + nameSensor[number_of_sensor]
              + "\\" + name_file, 'w') as final_file:
        final_txt = name_file
        final_txt += "\nType: " + productType[number_of_sensor]
        final_txt += "\nBatch: " + sensorBatch[number_of_sensor]
        final_txt += "\nWafer: " + sensorWafer[number_of_sensor]
        final_txt += "\nComponent: " + nameSensor[number_of_sensor]
        final_txt += "\nDate: " + datetime.datetime.now().strftime("%d %b %Y")
        final_txt += "\nTime: " + datetime.datetime.now().strftime("%H:%M:%S")
        final_txt += "\nInstitute: " + institute
        if data_type == 0:
            final_txt += "\nTestType: ATLAS18_SHAPE_METROLOGY_V" + version
        if data_type == 1:
            final_txt += "\nTestType: ATLAS18_MAIN_THICKNESS_V" + version
        if data_type == 2:
            final_txt += "\nTestType: ATLAS18_BOTH_PRIVATE_V" + version
        if data_type == 0:
            final_txt += "\nCMM: OGP SmartScope CNC 500"
        if data_type == 1 or data_type == 2:
            final_txt += "\nInstrument: OGP SmartScope CNC 500"
        if data_type == 0 or data_type == 2:
            final_txt += "\nProbe: TTL Laser"
        final_txt += "\nRunNumber: " + str(runNumber[number_of_sensor])
        if LabPar.Automatic and data_type == 0:
            try:
                check_database()
            except:
                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                         "| Data refresh from database (temperature, humidity) has been failed."
                         "\n\t\t   Previous data will be used.\n" + traceback.format_exc())
            else:
                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                         "| Data have been successfully refreshed from database.\n\t\t   Temperature: "
                         + str(LabPar.Temperature) + " °C, Humidity: " + str(LabPar.Humidity) + " %")
        if data_type == 0 or data_type == 2:
            final_txt += "\nTemperature: " + str(LabPar.Temperature)
            final_txt += "\nHumidity: " + str(LabPar.Humidity)
        final_txt += "\nComments: " + comments[number_of_sensor]
        if data_type == 2:
            final_txt += write_accuracy(number_of_sensor)
        if data_type == 1 or data_type == 2:
            planarity_thickness = round((min(planarityZ) * 10**3), 1)
            final_txt += "\nAvThickness: " + str(planarity_thickness) + "\n"
        if data_type == 2:
            planarity_bow = round((max(planarityZ) - min(planarityZ)) * 10**3, 1)
            final_txt += "\nBow: " + str(planarity_bow)
        if data_type == 0 or data_type == 2:
            ouput_row = 0
            final_txt += "\nX[mm]\tY[mm]\tZ[mm]\tZ_bow[mm]\n"
            while ouput_row < len(planarityX):
                final_txt += "{:010.4f}".format(planarityX[ouput_row]) + "\t"
                final_txt += "{:010.4f}".format(planarityY[ouput_row]) + "\t"
                final_txt += "{:010.4f}".format(planarityZ[ouput_row]) + "\t"
                final_txt += "{:010.4f}".format(planarityZ[ouput_row]) + "\n"
                ouput_row += 1

        final_file.write(final_txt)

        if data_type == 2:
            try:
                fig = plt.figure()
                ax = plt.subplot(projection="3d")
                plot = ax.scatter(planarityX, planarityY, planarityZ, c=planarityZ, cmap='viridis', linewidth=1, s=100)
                cbaxes = fig.add_axes([0.88, 0.15, 0.03, 0.7])
                plt.colorbar(plot, cax=cbaxes)
                ax.view_init(50, -60)

                ax.set_title(nameSensor[number_of_sensor] + " - run n. " + str(runNumber[number_of_sensor]))
                ax.set_xlabel("X [mm]")
                ax.set_ylabel("Y [mm]")
                ax.set_zlabel("Z [mm]")
                plt.savefig(measurePath + sType[number_of_sensor] + "\\" + nameSensor[number_of_sensor]
                            + "\\" + sensorBatch[number_of_sensor] + "-W" + sensorWafer[number_of_sensor] +
                            "_Plot_" + "0"*(3 - len(str(runNumber[number_of_sensor])))
                            + str(runNumber[number_of_sensor]) + ".pdf")

            except:
                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                         "| Creating of plot with measured planarity of the sensor has failed." +
                         "\n" + traceback.format_exc())
            else:
                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                         "| Creating of plot with measured planarity of the sensor has been successfully completed.")

# ↑ Function will edit output (text file) of measuring to better readable file for computer.


def change_sensor(number_of_sensor=0):
    global NumberOfSensor
    global error
    error = 1

    for n in range(number_of_sensor, 9):
        if sensorPosition[n] == 1 or sType[n] == "E" or sType[n] == "" \
                or nameSensor[n] == "" or pSensor[n] == 0:
            continue

        bad_pos = 0
        tips = ""
        continue_message = ''

        for nn in range(n, 9):
            if sensorPosition[nn] == 1 or sType[nn] == "E" or sType[nn] == "" \
                    or nameSensor[nn] == "" or pSensor[nn] == 0:
                continue
            bad_pos += 1
        if bad_pos == 1 or bad_pos == 0:
            continue_message = 'START MEASURING'
            NumberOfSensor = 9
        else:
            continue_message = 'continue to next one'

        if ControlPar.Angle[n] == 999:
            tips = "Angle has not been measured, try repeat."
        elif LimitDistance.Phi[0] > ControlPar.Angle[n]:
            tips = "rotate the sensor in clockwise"
        elif LimitDistance.Phi[1] < ControlPar.Angle[n]:
            tips = "rotate the sensor in anti-clockwise"
        if ControlPar.Hdis[n] == 999:
            tips += "\nHorizontal deviation has not been measured, try repeat."
        elif LimitDistance.RightD[0] > ControlPar.Hdis[n]:
            tips += "\nmove right with the sensor"
        elif LimitDistance.RightD[1] < ControlPar.Hdis[n]:
            tips += "\nmove left with the sensor"
        if ControlPar.Vdis[n] == 999:
            tips += "\nVertical deviation has not been measured, try repeat."
        elif LimitDistance.BottomD[0] > ControlPar.Vdis[n]:
            tips += "\nmove up with the sensor"
        elif LimitDistance.BottomD[1] < ControlPar.Vdis[n]:
            tips += "\nmove down with the sensor"

        ch_s_confirm = pag.confirm(write_accuracy(n) + "\n\nTIPS:\n" + tips,
                                   "APS PROBLEM:   Sensor num. " + str(n + 1),
                                   buttons=['edit sensor settings', continue_message])
        if ch_s_confirm == 'edit sensor settings':
            NumberOfSensor = n
            break


def control_next_start():
    if NumberOfSensor >= 8:
        return False
    else:
        return True


def check_running():
    if running > 20:
        SMS.destroy()
    elif running > 17:
        pag.alert("Suspicious behavior has been detected.\n"
                  "Processes is cycling or the program is running too long."
                  "\nPlease restart the program soon.", "Warning alert", timeout=1000*60*1)
