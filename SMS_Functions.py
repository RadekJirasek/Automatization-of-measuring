# SCRIPT DECLARING ALL BASIC FUNCTION THOSE NOT CALL BY GUI OR NOT USING ERROR SYSTEM

from SMS_Initialize import*
# Import script with data about bookmarks and declaring of variables.


def open_routine():
    pag.click(Position.file)  # Click to "File".
    wait(sleep_until="open.png")
    if sensorPos[NumberOfSensor] != 0:
        pag.click(Position.open)  # Open routine.
        wait(sleep_until="folderOn.png")


def search_file():
    pag.hotkey("f4")  # Mark searching textbox.
    wait(sleep_until="f4On.png")
    if sensorPos[NumberOfSensor] != 0:
        pag.hotkey("ctrl", "a")  # Select all text in searching box for transcription.
        wait(sleep_until="ctrlaOn.png")
# ↑ For saving file of measuring.


def reset_origins():
    pag.click(Position.resetX)

    if sensorPos[NumberOfSensor] != 0:
        pag.click(Position.resetY)

    if sensorPos[NumberOfSensor] != 0:
        pag.click(Position.resetAngle)
        wait(sleep_until="resetAngleOn.png")
# ↑ Reset origin of mm3d for start measuring new sensor. Click to three buttons.


def start_routine(routine):
    open_routine()
    if sensorPos[NumberOfSensor] != 0:
        search_file()
    if sensorPos[NumberOfSensor] != 0:
        pag.typewrite(measurePath + "Routines")  # Search place in pc.
        wait(sleep_until="f4On.png")
    if sensorPos[NumberOfSensor] != 0:
        pag.typewrite(["enter"])
        wait(sleep_until="folderOn.png")
    if sensorPos[NumberOfSensor] != 0:
        pag.hotkey("alt", "n")  # Switch to textbox of 'Name file'.
        wait(sleep_until="altnOn.png")
    if sensorPos[NumberOfSensor] != 0:
        pag.typewrite(routine)  # Write name of routine.
        wait(sleep_until="filenameOn.png")
    if sensorPos[NumberOfSensor] != 0:
        pag.typewrite(["enter"])
        wait(sleep_until="mm3dOn.png")
    if sensorPos[NumberOfSensor] != 0:
        pag.click(Position.start)  # Start routine.
        wait(sleep_until="startRoutineOn.png")
    if sensorPos[NumberOfSensor] != 0:
        pag.typewrite(["enter"])  # Confirming start.


def save_file(save_path):
    pag.typewrite(save_path)  # Search sensor folder.
    wait(sleep_until="f4On.png")
    if sensorPos[NumberOfSensor] != 0:
        pag.typewrite(["enter"])
        wait(sleep_until="folderOn.png")
    if sensorPos[NumberOfSensor] != 0:
        pag.click(Position.save)  # Save file.
        wait(sleep_until="mm3dOn.png")
    if sensorPos[NumberOfSensor] != 0:
        pag.moveTo(900, 0)  # Move cursor from 'save' button.


def save_log(text, first_run=False):
    log = ""
    global logFile
    if not first_run:
        with open(logFile, 'r') as log_file:
            log = log_file.read()
            log_file.close()
    else:
        logFile = programPath + "logs\\" \
                  + datetime.datetime.now().strftime("%y_%m_%d_%H_%M") + ".txt"
    # If not first write to log file, read already exist text and save to 'log'.
    with open(logFile, 'w') as log_file:
        log_file.write(log + text)
        log_file.close()
    # Write data from argument 'text' of function and variable 'log' to file.
# Function writing information to a log file.


def reset_mm3d(mm3d=False, desktop=False):
    if mm3d:
        pag.click(Position.mm3d)
        wait(sleep_until="m3dOn.png")
    # ↑ Switch to mm3d for next reset.
    if sensorPos[NumberOfSensor] != 0:
        pag.click(Position.system)
        wait(sleep_until="resetSystem.png")
    if sensorPos[NumberOfSensor] != 0:
        pag.click(Position.resetSystem)
        wait(sleep_until="system.png")
    # ↑ Reset all system of mm3d.
    if desktop and sensorPos[NumberOfSensor] != 0:
        pag.click(Position.desktop)
        wait(sleep_until="desktopOn.png")
    # ↑ Switch to desktop.
# ↑ Complete reset MeasureMind 3d program to default settings.


def after_error_reset():
    global NumberOfSensor
    global error
    error = 0
    NumberOfSensor = 0
    for NumberOfSensor in range(0, 9):
        sensorPos[NumberOfSensor] = 0
    NumberOfSensor = 0


def default():
    pag.screenshot(programPath + "Error Screenshots\\"
                   + datetime.datetime.now().strftime("%y_%m_%d_%H_%M") + ".png")
    if not pag.locateCenterOnScreen(Img.desktopOn, grayscale=True):
        if pag.locateCenterOnScreen(Img.mm3dOn, grayscale=True):

            if pag.locateCenterOnScreen(Img.folderOn, grayscale=True):
                pag.typewrite(["esc"])
            else:
                pag.typewrite(["enter"])

            stop_on = pag.locateCenterOnScreen(Img.stopOn, grayscale=True)
            if stop_on:
                Position.stop = list(stop_on)
                pag.click(Position.stop)
                wait(sleep_until="end_w.png")
                pag.typewrite(["enter"])

            if sensorPos[NumberOfSensor] != 0:
                img_reset_system = pag.locateCenterOnScreen(Img.resetSystem, grayscale=True)
                if img_reset_system:
                    Position.resetSystem = list(img_reset_system)
                    pag.click(Position.system)
                else:
                    time.sleep(1)

                pag.click(Position.system)
                wait(sleep_until="resetSystem.png")
                if sensorPos[NumberOfSensor] != 0:
                    pag.click(Position.resetSystem)
                    wait(sleep_until="system.png")
                if sensorPos[NumberOfSensor] != 0:
                    pag.click(Position.desktop)
                    wait(sleep_until="desktopOn.png")

        else:
            pag.click(pag.locateCenterOnScreen(Img.cross, grayscale=True))

            if not pag.locateCenterOnScreen(Img.desktopOn, grayscale=True):
                pag.click(pag.locateCenterOnScreen(Img.cross, grayscale=True))

# ↑ Set computer to default (know) position - desktop.


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
                string += str(protocol_c)
            if line == 2:
                if ErrorId.createFolder[protocol_c] == 0:
                    string += "-"
                elif ErrorId.createFolder[protocol_c] == 1:
                    string += "O"
                else:
                    string += "X"
            if line == 3:
                if ErrorId.completeMeasuring[protocol_c] == 0:
                    string += "-"
                elif ErrorId.completeMeasuring[protocol_c] == 1:
                    string += "O"
                else:
                    string += "X"
            if line == 4:
                if ErrorId.editOutput[protocol_c] == 0:
                    string += "-"
                elif ErrorId.editOutput[protocol_c] == 1:
                    string += "O"
                else:
                    string += "X"
            if line == 5:
                if ErrorId.moveTrash[protocol_c] == 0:
                    string += "-"
                elif ErrorId.moveTrash[protocol_c] == 1:
                    string += "O"
                else:
                    string += "X"
            if line == 6:
                if ErrorId.completeScanning[protocol_c] == 0:
                    string += "-"
                elif ErrorId.completeScanning[protocol_c] == 1:
                    string += "O"
                else:
                    string += "X"
            if line == 7:
                if ErrorId.moveScreens[protocol_c] == 0:
                    string += "-"
                elif ErrorId.moveScreens[protocol_c] == 1:
                    string += "O"
                else:
                    string += "X"
            if line == 8:
                if ErrorId.completeJoinScreens[protocol_c] == 0:
                    string += "-"
                elif ErrorId.completeJoinScreens[protocol_c] == 1:
                    string += "O"
                else:
                    string += "X"
            if line == 9:
                if ErrorId.dataSizeTest[protocol_c] == 0:
                    string += "-"
                elif ErrorId.dataSizeTest[protocol_c] == 1:
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
        temp_write += "\nCreate a folder    ||" + protocol_loop(2)
        temp_write += "\nMeasuring          ||" + protocol_loop(3)
        temp_write += "\nData transcription ||" + protocol_loop(4)
        temp_write += "\nMove trash         ||" + protocol_loop(5)
        temp_write += "\nScanning           ||" + protocol_loop(6)
        temp_write += "\nMove screens       ||" + protocol_loop(7)
        temp_write += "\nJoin screens       ||" + protocol_loop(8)
        temp_write += "\nData size test     ||" + protocol_loop(9)

        protocol_file.write(temp_write)
        protocol_file.close()
# ↑ Generating protocol text file.


def check_size(source):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(source):
        for p in filenames:
            pp = os.path.join(dirpath, p)
            total_size += os.path.getsize(pp)
    return total_size
# ↑ Function for control of size of folder with data.


def limit_size():
    limit = [0, 0]

    if sType[NumberOfSensor] == "R0":
        if mSensor[NumberOfSensor]:
            limit[0] += LimitSize.R0[0]
            limit[1] += LimitSize.R0[1]
        if sSensor[NumberOfSensor]:
            limit[0] += LimitSize.R0[2]
            limit[1] += LimitSize.R0[3]
    elif sType[NumberOfSensor] == "R1":
        if mSensor[NumberOfSensor]:
            limit[0] += LimitSize.R1[0]
            limit[1] += LimitSize.R1[1]
        if sSensor[NumberOfSensor]:
            limit[0] += LimitSize.R1[2]
            limit[1] += LimitSize.R1[3]
    elif sType[NumberOfSensor] == "R2":
        if mSensor[NumberOfSensor]:
            limit[0] += LimitSize.R2[0]
            limit[1] += LimitSize.R2[1]
        if sSensor[NumberOfSensor]:
            limit[0] += LimitSize.R2[2]
            limit[1] += LimitSize.R2[3]
    elif sType[NumberOfSensor] == "R3":
        if mSensor[NumberOfSensor]:
            limit[0] += LimitSize.R3[0]
            limit[1] += LimitSize.R3[1]
        if sSensor[NumberOfSensor]:
            limit[0] += LimitSize.R3[2]
            limit[1] += LimitSize.R3[3]
    elif sType[NumberOfSensor] == "R4":
        if mSensor[NumberOfSensor]:
            limit[0] += LimitSize.R4[0]
            limit[1] += LimitSize.R4[1]
        if sSensor[NumberOfSensor]:
            limit[0] += LimitSize.R4[2]
            limit[1] += LimitSize.R4[3]
    elif sType[NumberOfSensor] == "R5":
        if mSensor[NumberOfSensor]:
            limit[0] += LimitSize.R5[0]
            limit[1] += LimitSize.R5[1]
        if sSensor[NumberOfSensor]:
            limit[0] += LimitSize.R5[2]
            limit[1] += LimitSize.R5[3]
    elif sType[NumberOfSensor] == "B":
        if mSensor[NumberOfSensor]:
            limit[0] += LimitSize.B[0]
            limit[1] += LimitSize.B[1]
        if sSensor[NumberOfSensor]:
            limit[0] += LimitSize.B[2]
            limit[1] += LimitSize.B[3]

    return limit


def wait(saving=True, sleep_until="", new_time=True, sleep_time_s=0, sleep_time_m=0):
    global error
    global NumberOfSensor
    sensorPos[NumberOfSensor] = 1
    if sleep_until != "":
        if not pag.locateCenterOnScreen(programPath + "screens\\" + sleep_until, grayscale=True):
            if new_time:
                sleep_time_s = datetime.datetime.now().second + datetime.datetime.now().microsecond / 1000000
                sleep_time_m = datetime.datetime.now().minute
            sleep_time = datetime.datetime.now().second + datetime.datetime.now().microsecond / 1000000
            if datetime.datetime.now().minute != sleep_time_m:
                sleep_time += 60
            if sleep_time - sleep_time_s < max_sleep_time:
                wait(saving, sleep_until, new_time=False, sleep_time_s=sleep_time_s, sleep_time_m=sleep_time_m)
            else:
                error = 2
                default()
                sensorPos[NumberOfSensor] = 0
    else:
        if pag.locateCenterOnScreen(Img.error, grayscale=True):
            error = 2
            default()
            sensorPos[NumberOfSensor] = 0
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
                wait(saving, sleep_until)  # Repeat code until it executed commands in 'try'.

# ↑ Waiting system, if on screen will appear required image, loop will end.


def memory(memory_type):
    free_size = 0
    if memory_type == "RAM":
        free_size = virtual_memory()[4] / (2**20)
    elif memory_type == "DISK":
        free_size = disk_usage("/")[2] / (2**30)

    return free_size


def wait_end_process(name):
    r = os.popen('tasklist /v').read().strip().split('\n')
    for i in range(len(r)):
        if name in r[i]:
            time.sleep(15)
            wait_end_process(name)
# ↑ Program will wait until end of process.


def control_string(string):
    char_count = 0
    line_count = 0
    for char in string:
        line_count += 1
        if char == "\n":
            char_count += 1
    return char_count, line_count


def edit_output(file, fuse, k, start_point, gap):
    output_a = 0
    output_b = 0
    output_s = start_point
    output_t = False
    output_string = ""

    # ↑ Declaration variables.
    with open(measurePath + sType[NumberOfSensor] + "\\" + nameSensor[NumberOfSensor]
              + "\\" + file, 'r') as output_file:  # Open file with data (for read).
        while output_a < 50000:
            output_read = output_file.read(1)  # Execute read one by one character.
            if output_read == "+" or output_read == "-":
                output_t = True
                if output_a < fuse:
                    output_string += "Actual_Width "
                elif output_a <= (fuse + 110):
                    if output_b == 0:
                        output_string += "Nominal_Width "
                        output_b += 1
                    elif output_b == 1:
                        output_string += " Actual_Width "
                        output_b += 1
                    elif output_b == 2:
                        output_string += " Deviation_Width "
                        output_b += 1
                # ↑ Naming data of another types.
                else:
                    if output_s == 0:
                        output_string += "X_Nominal "
                    elif output_s == 1:
                        output_string += gap + "X_Actual "
                    elif output_s == 2:
                        output_string += " X_Deviation "
                    elif output_s == 3:
                        output_string += " Y_Nominal "
                    elif output_s == 4:
                        output_string += " Y_Actual "
                    elif output_s == 5:
                        output_string += " Y_Deviation "
                    elif output_s == 6:
                        output_string += " Z_Nominal "
                    elif output_s == 7:
                        output_string += " Z_Actual "
                    elif output_s == 8:
                        output_string += " Z_Deviation "
                    output_s += k
                # ↑ Naming data of normal type.
            elif output_read == " ":
                if output_t:
                    if a < fuse:
                        output_string += "\n"
                    elif a <= (fuse + 110) and output_b == 3:
                        output_string += "\n"
                    elif output_s > 8:
                        output_s = start_point
                        output_string += "\n"
                        if gap == "":
                            output_delete = output_file.read(16)
                            del output_delete
                # Creating new lines and reset variables.
                output_t = False

            if output_t:
                if output_read == "0" or output_read == "1" or output_read == "2" or output_read == "3" \
                        or output_read == "4" or output_read == "5" or output_read == "6" or \
                        output_read == "7" or output_read == "8" or output_read == "9" or \
                        output_read == "." or output_read == "+" or output_read == "-":
                    output_string += output_read  # Write of data to memory.
            output_a += 1
    output_file.close()
    with open(measurePath + sType[NumberOfSensor] + "\\" + nameSensor[NumberOfSensor]
              + "\\" + file, 'w') as output_file:  # Open file with data (for write).
        output_file.write(output_string)  # Write data to file.
    output_file.close()
# ↑ Function will edit output (text file) of measuring to better readable file for computer.
