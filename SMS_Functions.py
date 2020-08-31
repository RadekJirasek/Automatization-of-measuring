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
        wait(sleep_until="folderOn.png")


def search_file():
    pag.hotkey("f4")  # Mark searching textbox.
    wait(sleep_until="f4On.png")
    if not if_find_error():
        pag.hotkey("ctrl", "a")  # Select all text in searching box for transcription.
        wait(sleep_until="ctrlaOn.png")
# ↑ For saving file of measuring.


def reset_origins():
    time.sleep(3)
    pag.click(Position.resetX)
    pag.moveRel(0, 100)
    wait(sleep_until="resetXOn.png")
    if not if_find_error():
        pag.click(Position.resetY)
        pag.moveRel(0, 100)
        wait(sleep_until="resetYOn.png")
    # ↑ Reset origin of mm3d for start measuring new sensor. Click to three buttons.


def start_routine(routine, control_wait=True):
    open_routine()
    if not if_find_error():
        search_file()
    if not if_find_error():
        pag.typewrite(measurePath + "Routines")  # Search place in pc.
        wait(sleep_until="f4On.png")
    if not if_find_error():
        time.sleep(0.2)
        pag.typewrite(["enter"])
        time.sleep(0.2)
        pag.typewrite(["enter"])
        time.sleep(0.2)
        pag.typewrite(["enter"])
        wait(sleep_until="folderOn.png")
    if not if_find_error():
        pag.hotkey("alt", "n")  # Switch to textbox of 'Name file'.
        time.sleep(1)
    if not if_find_error():
        pag.typewrite(routine)  # Write name of routine.
        if control_wait:
            wait(sleep_until="filenameOn.png")
        else:
            time.sleep(1)
    if not if_find_error():
        pag.typewrite(["enter"])
        wait(sleep_until=["mm3dOn.png", "mm3dOn2.png", "mm3dOn3.png", "mm3dOn4.png"])
    if not if_find_error():
        time.sleep(1)
        pag.click(Position.start)  # Start routine.
        wait(sleep_until="startRoutineOn.png")
    if not if_find_error():
        pag.typewrite(["enter"])  # Confirming start.


def save_file(save_path, save_name="", control_wait=True):
    pag.typewrite(save_path)  # Search sensor folder.
    wait(sleep_until="f4On.png")
    if not if_find_error():
        pag.typewrite(["enter"])
        time.sleep(0.1)
        pag.typewrite(["enter"])
        wait(sleep_until="ctrlaOn.png")
        pag.typewrite(["enter"])
        wait(sleep_until="folderOn.png")
    if not if_find_error() and save_name != "":
        if not if_find_error():
            pag.hotkey("alt", "n")  # Switch to textbox of 'Name file'.
            time.sleep(1)
        if not if_find_error():
            pag.typewrite(save_name)  # Write name of routine.
            if control_wait:
                wait(sleep_until="filenameOn.png")
            else:
                time.sleep(1)
    if not if_find_error():
        pag.click(Position.save)  # Save file.
        wait(sleep_until=["mm3dOn.png", "mm3dOn2.png", "mm3dOn3.png", "mm3dOn4.png"])
    if not if_find_error():
        pag.moveTo(900, 0)  # Move cursor from 'save' button.


def save_log(text, first_run=False):
    log = ""
    global logFile
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

    if defaultRepetition < 3:
        defaultRepetition = defaultRepetition + 1
        pag.screenshot(programPath + "Error Screenshots\\"
                       + datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S") + ".png")
        time.sleep(0.5)

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
                or pag.locateCenterOnScreen(programPath + "screens\\ctrlaOn.png"):
            pag.click()
            time.sleep(0.1)
            pag.typewrite("esc")
            if mm3d_on():
                pag.click(Position.mm3d)
                wait(sleep_until=["mm3dOn.png", "mm3dOn2.png", "mm3dOn3.png", "mm3dOn4.png"])
        else:
            pag.click(Position.mm3d)
            wait(sleep_until=["mm3dOn.png", "mm3dOn2.png", "mm3dOn3.png", "mm3dOn4.png"])

        defaultRepetition = 0
        if proces_var:
            set_process_error()
        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                 "| It seems that system has been successfully reset by 'default function'.")
    else:
        raise WaitError("Error has been occurred in 'default' function.\n"
                        "The program has failed to solve the problem even three times in a row.")

# ↑ Set computer to default (know) position - mm3d program.


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


def after_error_reset():
    global NumberOfSensor
    global error
    error = 0
    NumberOfSensor = 0
    for NumberOfSensor in range(0, 9):
        set_repeat_measure()
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
    elif memory_type == "DISK":
        free_size = disk_usage(measurePath[0:2])[2] / (2**30)

    return round(free_size, 3)


def wait_end_process(program_name):
    for program in (p.name() for p in process_iter()):
        if program == program_name:
            return True
    return False
# ↑ Program will wait until end of process.


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


def edit_output(data_type, number_of_sensor):
    planarity_x = None
    planarity_y = None
    planarity_z = None
    if not data_type:
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

        planarity_x, planarity_y, planarity_z = np.loadtxt(
            measurePath + sType[number_of_sensor] + "\\" + nameSensor[number_of_sensor] + "\\planarity.txt",
            skiprows=1,
            unpack=True
        )

    with open(measurePath + sType[number_of_sensor] + "\\" + nameSensor[number_of_sensor]
              + "\\planarity.txt", 'w') as final_file:
        final_txt = "Manufacture: Hamamatsu"
        final_txt += "\nType: " + productType[number_of_sensor]
        final_txt += "\nBatch: " + sensorBatch[number_of_sensor]
        final_txt += "\nWafer: " + sensorWafer[number_of_sensor]
        final_txt += "\nSerial number: " + nameSensor[number_of_sensor]
        final_txt += "\nDate: " + datetime.datetime.now().strftime("%d %m %y")
        final_txt += "\nTime: " + datetime.datetime.now().strftime("%H:%M:%S")
        if LabPar.Automatic:
            try:
                check_database()
            except:
                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                         "| Data refresh from database (temperature, humidity) has been failed."
                         "\n Previous data will be used.\n" + traceback.format_exc())
            else:
                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                         "| Data have been successfully refreshed from database.\n\t\t   Temperature: "
                         + str(LabPar.Temperature) + " °C, Humidity: " + str(LabPar.Humidity) + " %")
        final_txt += "\nTemperature: " + str(LabPar.Temperature) + " °C"
        final_txt += "\nHumidity: " + str(LabPar.Humidity) + " %"
        final_txt += "\nInstitute: " + institute
        final_txt += "\nTest type: "
        if ErrorId.completeMeasuring[number_of_sensor] == 1 and sSensor[number_of_sensor] == 1:
            final_txt += "Metrology & Scanning"
        elif ErrorId.completeMeasuring[number_of_sensor] == 1:
            final_txt += "Metrology"
        else:
            final_txt += "Scanning"
        final_txt += "\nEquipment: OGP SmartScope CNC 500\n"

        if not data_type:
            planarity_bow = round(max(planarity_z) - min(planarity_z), 4)
            planarity_thickness = round(min(planarity_z), 4)
            final_txt += "\nBow (mm): " + str(planarity_bow)
            final_txt += "\nThickness (mm): " + str(planarity_thickness)
            final_txt += "\nx (mm)\t\t\ty (mm)\t\t\tz (mm)\t\t\tz-fit (mm)\n"
            ouput_row = 0
            while ouput_row < len(planarity_x):
                final_txt += str(round(planarity_x[ouput_row], 4))
                final_txt += "0"*(7 - len(str(round(planarity_x[ouput_row], 4)))) + "  \t\t"
                final_txt += str(round(planarity_y[ouput_row], 4))
                final_txt += "0"*(7 - len(str(round(planarity_y[ouput_row], 4)))) + "  \t\t"
                final_txt += str(round(planarity_z[ouput_row], 4))
                final_txt += "0"*(6 - len(str(round(planarity_z[ouput_row], 4)))) + "  \t\t"
                final_txt += str(round(planarity_z[ouput_row], 4))
                final_txt += "0"*(6 - len(str(round(planarity_z[ouput_row], 4)))) + "\n"
                ouput_row += 1

        else:
            final_txt += "\n No data about planarity of the sensor."

        final_file.write(final_txt)
# ↑ Function will edit output (text file) of measuring to better readable file for computer.
