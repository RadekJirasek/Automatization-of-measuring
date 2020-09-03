# SCRIPT DETERMINING COURSE OF PROGRAM (FUNCTIONS USING ERROR SYSTEM)

from SMS_Functions import*
# Import script with declaring all of functions those not call by graphical user interface or use error system
# (include another script).


def save_position(number_of_sensor=0):
    pag.click(Position.centroid)
    time.sleep(1)

    if pag.locateCenterOnScreen(Img.touchBoundary, grayscale=True):
        pag.click(Position.touchBoundary)
    time.sleep(0.5)
    if pag.locateCenterOnScreen(Img.autoIllumination, grayscale=True):
        pag.click(Position.autoIllumination)
    time.sleep(0.5)
    if pag.locateCenterOnScreen(Img.mm3dOn, grayscale=True) \
            or pag.locateCenterOnScreen(Img.mm3dOn2, grayscale=True):
        increase_threashold = pag.size()[0] / 3.162, pag.size()[1] / 1.215
    else:
        increase_threashold = pag.size()[0] / 3.162, pag.size()[1] / 1.205
    pag.moveTo(increase_threashold)
    pag.dragRel(0.001, 0.001, 5, button='left')

    time.sleep(0.5)
    pag.click(pag.size()[0] / 5.5, pag.size()[1] / 4)
    wait(sleep_until="quitStep.png")
    if not if_find_error():
        pag.typewrite(["enter"])
        time.sleep(2)
        pag.click(Position.saveRoutine)
        time.sleep(4)
    if not if_find_error():
        search_file()
        if if_find_error():
            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                     "| Has been detected that result of previous line of"
                     " code was unsuccessful - function 'search_file()'.")
    if not if_find_error():
        try:
            os.remove(measurePath + "Routines\\" + str(number_of_sensor + 1) + "_left.RTN")
        except OSError:
            # Probably file not exist yet.
            pass

        save_file(measurePath + "Routines", str(number_of_sensor + 1) + "_left", saving=True)
        if if_find_error():
            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                     "| Has been detected that result of previous line of"
                     " code was unsuccessful - function 'save_file()'.")
        else:
            time.sleep(1)
            pag.typewrite(["enter"])


def prepare_process(process_type, manually_on):

    start_routine(str(NumberOfSensor + 1) + "_left.RTN")
    if if_find_error():
        if process_type == "Measurement":
            ErrorId.startMeasuring[NumberOfSensor] = 2
        elif process_type == "Scanning":
            ErrorId.startScanning[NumberOfSensor] = 2
        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                 "| " + process_type + " of the sensor has failed at startup "
                 "(during start of position routine).")
    else:
        time.sleep(5)
        wait(False)
        if if_find_error():
            if process_type == "Measurement":
                ErrorId.startMeasuring[NumberOfSensor] = 2
            elif process_type == "Scanning":
                ErrorId.startScanning[NumberOfSensor] = 2
            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                     "| " + process_type + " of the sensor has failed at startup "
                     "(during process of position routine).")

    if not if_find_error():
        time.sleep(0.5)
        pag.click(Position.resetRoutine)
        wait(sleep_until="resetRoutineOn.png")
        if if_find_error():
            if process_type == "Measurement":
                ErrorId.startMeasuring[NumberOfSensor] = 2
            elif process_type == "Scanning":
                ErrorId.startScanning[NumberOfSensor] = 2
            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                     "| Has been detected that result of previous line of"
                     " code was unsuccessful - wait function (locate on screen)"
                     " of 'resetRoutine.png'.")
        if not if_find_error():
            reset_origins()
            if if_find_error():
                if process_type == "Measurement":
                    ErrorId.startMeasuring[NumberOfSensor] = 2
                elif process_type == "Scanning":
                    ErrorId.startScanning[NumberOfSensor] = 2
                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                         + "| " + process_type + " of the sensor has failed at startup"
                           " (during resetting the origins of axis).")
    if process_type == "Measurement" and manually_on:
        if not if_find_error():
            start_routine(str(NumberOfSensor + 1) + "_right.RTN")
            if if_find_error():
                if process_type == "Measurement":
                    ErrorId.startMeasuring[NumberOfSensor] = 2
                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                         "| " + process_type + " of the sensor has failed at startup "
                         "(during start of angle routine).")
            else:
                time.sleep(5)
                wait(False)
                if if_find_error():
                    if process_type == "Measurement":
                        ErrorId.startMeasuring[NumberOfSensor] = 2
                    save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                             "| " + process_type + " of the sensor has failed at startup "
                             "(during process of angle routine).")
        if not if_find_error():
            time.sleep(0.5)
            pag.click(Position.resetRoutine)
            wait(sleep_until="resetRoutineOn.png")
            if if_find_error():
                if process_type == "Measurement":
                    ErrorId.startMeasuring[NumberOfSensor] = 2
                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                         "| Has been detected that result of previous line of"
                         " code was unsuccessful - wait function (locate on screen)"
                         " of 'resetRoutine.png'.")
            if not if_find_error():
                pag.click(Position.resetAngle)
                pag.moveRel(0, 100)
                wait(sleep_until="resetAngleOn.png")
                if if_find_error():
                    if process_type == "Measurement":
                        ErrorId.startMeasuring[NumberOfSensor] = 2
                    save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                             + "| " + process_type + " of the sensor has failed at startup"
                             " (during resetting the angle of axis).")


def repeat_measurement(process_type, manually_on):
    global delFinishedSteps
    global error
    finished_steps = 0

    save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
             "| Solvable error has been occurred! Process will be repeated.")

    if process_type == "Measurement":
        try:
            with open(measurePath + sType[NumberOfSensor] + "\\" + nameSensor[NumberOfSensor] + "\\planarity.txt",
                      'r') as finished_planarity_file:
                finished_planarity_lines = finished_planarity_file.readlines()
                finished_steps = len(finished_planarity_lines)

            steps_index = 0
            while steps_index < finished_steps:
                if finished_planarity_lines[steps_index] == "\n" \
                        or finished_planarity_lines[steps_index] == "":
                    finished_steps -= 1
                steps_index += 1

        except OSError:
            if os.path.exists(measurePath + sType[NumberOfSensor] + "\\"
                              + nameSensor[NumberOfSensor] + "\\planarity.txt"):
                set_process_error(1)
                error = 2
                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                         "| Calculating number of finished steps of measurement routine has failed.")
            else:
                finished_steps = 0
                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                         "| Number of finished steps of measurement routine has been calculated. - count = "
                         + str(finished_steps))
        else:
            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                     "| Number of finished steps of measurement routine has been calculated. - count = "
                     + str(finished_steps))
    elif process_type == "Scanning":
        try:
            if ErrorId.moveTrash[NumberOfSensor] == 1:
                move_image_files = os.listdir(measurePath)
                for move_image_file in move_image_files:
                    if move_image_file.endswith(".BMP"):
                        file_name = "-".join(move_image_file.split('-')[:1]) + "-" \
                                    + str(delFinishedSteps
                                          + int(move_image_file.split('-')[len(move_image_file.split('-')) - 2])) \
                                    + "-1.BMP"
                        os.rename(measurePath + move_image_file, measurePath + sType[NumberOfSensor] + "\\"
                                  + nameSensor[NumberOfSensor] + "\\" + file_name)

            if_finished_steps = False
            bmp_steps = os.listdir(measurePath + sType[NumberOfSensor] + "\\" + nameSensor[NumberOfSensor])
            for bmp_step in bmp_steps:
                if bmp_step.endswith(".BMP"):
                    if_finished_steps = True

            if if_finished_steps:
                list_of_images = glob(measurePath + sType[NumberOfSensor] + '\\'
                                      + nameSensor[NumberOfSensor] + '\\*')
                last_image = max(list_of_images, key=os.path.getctime)
                if last_image.endswith(".BMP"):
                    finished_steps = int(last_image.split('-')[len(last_image.split('-')) - 2])

            else:
                finished_steps = 0
                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                         "| Warning: Last file in the folder is not a image (.BMP) - "
                         "probably no images has been taken or screens has been lost in other images.")
        except OSError:
            set_process_error(1)
            error = 2
            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                     "| Calculating number of finished steps of scanning routine has failed.\n"
                     + traceback.format_exc())
        else:
            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                     "| Number of finished steps of scanning routine has been calculated. - count = "
                     + str(finished_steps))

    prepare_process(process_type=process_type, manually_on=manually_on)

    if not if_find_error():
        open_routine()
        if if_find_error():
            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                     "| " + process_type + " of the sensor has failed (during file search).")
    if not if_find_error():
        search_file()
        if if_find_error():
            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                     "| " + process_type + " of the sensor has failed (during file search).")
    if not if_find_error():
        pag.typewrite(measurePath + "Routines")  # Search place in pc.
        time.sleep(1)
    if not if_find_error():
        pag.typewrite(["enter"])
        time.sleep(0.1)
        pag.typewrite(["enter"])
        time.sleep(0.5)
        pag.typewrite(["enter"])
        wait(sleep_until="folderOn.png")
        if if_find_error():
            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                     + "| Opening of " + process_type + " routine has failed (writing folder path).")
    if not if_find_error():
        time.sleep(0.2)
        pag.hotkey("alt", "n")  # Switch to textbox of 'Name file'.
        time.sleep(1)
    if not if_find_error():
        if process_type == "Measurement" and not manually_on:
            pag.typewrite("ATLASITK_" + sType[NumberOfSensor]
                          + "_Measuring.RTN")  # Write name of routine.
        elif process_type == "Measurement" and manually_on:
            pag.typewrite("ATLASITK_" + sType[NumberOfSensor]
                          + "_Measuring-Manually.RTN")  # Write name of routine.
        elif process_type == "Scanning":
            pag.typewrite("ATLASITK_" + sType[NumberOfSensor]
                          + "_Scanning.RTN")  # Write name of routine.
        time.sleep(1)
        if if_find_error():
            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                     + "| Opening of " + process_type + " routine has failed (writing name of sensor).")
    if not if_find_error():
        pag.typewrite(["enter"])
        wait(sleep_until=["mm3dOn.png", "mm3dOn2.png", "mm3dOn3.png", "mm3dOn4.png"])
        if not if_find_error():
            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                     + "| Opening of " + process_type + " routine has been successfully completed.")
        else:
            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                     + "| Opening of " + process_type + " routine has failed (switching to mm3d).")

    if not if_find_error() and finished_steps != 0:
        time.sleep(5)
        pag.click(Position.deleteSteps)
        wait(sleep_until="deleteStepsOn.png")
        if not if_find_error():
            if process_type == "Measurement" and not manually_on:
                pag.typewrite("184-" + str(finished_steps + 183))
            elif process_type == "Measurement" and manually_on:
                pag.typewrite("11-" + str(finished_steps + 10))
            elif process_type == "Scanning":
                pag.typewrite("5-" + str(finished_steps))
                delFinishedSteps = finished_steps - 4
            time.sleep(1)
            pag.typewrite(["enter"])
            time.sleep(1)
            pag.typewrite(["enter"])
        else:
            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                     + "| Deleting finished steps of " + process_type + " routine has failed.")
    if not if_find_error():
        time.sleep(5)
        pag.click(Position.start)  # Start routine.
        wait(sleep_until="startRoutineOn.png")

    if not if_find_error():
        pag.typewrite(["enter"])  # Confirming start.
        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                 + "| " + process_type + " of the sensor has been started")

    if if_find_error():
        if process_type == "Measurement":
            ErrorId.startMeasuring[NumberOfSensor] = 2
        elif process_type == "Scanning":
            ErrorId.startScanning[NumberOfSensor] = 2
        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                 + "| " + process_type + " repetition of the sensor has failed"
                 " (during start of routine)")

    if process_type == "Measurement":
        if not if_find_error():
            wait()  # Wait to saving measuring.

            if if_repeat_measure():
                error = 2
                set_process_error(1)
            if if_find_error():
                ErrorId.completeMeasuring[NumberOfSensor] = 2
                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                         "| Measurement of the sensor has failed (before saving).")
        if not if_find_error():
            search_file()
            if if_find_error():
                ErrorId.completeMeasuring[NumberOfSensor] = 2
                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                         "| Measurement of the sensor has failed (during file search).")
        if not if_find_error():
            save_file(measurePath + sType[NumberOfSensor] + "\\" + nameSensor[NumberOfSensor])
            if if_find_error():
                ErrorId.completeMeasuring[NumberOfSensor] = 2
                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                         "| Measurement of the sensor has failed (during saving).")


def process(manually=False):
    global delFinishedSteps
    global NumberOfSensor
    global firstProcess
    global error

    for NumberOfSensor in range(0, 9):
        try:
            if sType[NumberOfSensor] == "" or sType[NumberOfSensor] == "E" \
                    or nameSensor[NumberOfSensor] == "":
                continue

            if manually and pSensor[NumberOfSensor] == 1:
                continue

            elif not manually and pSensor[NumberOfSensor] == 0:
                continue

            this_sensor_data_size = limit_size(NumberOfSensor)[1]
            if memory(programPath[0:2]) < (round(this_sensor_data_size / (2 ** 30), 3)):
                if wait_end_process("backup_script.exe") or wait_end_process("join_images_script.exe"):
                    save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                             "| Too little free memory on local " + programPath[0:2] + " disk. Program will wait until"
                             + " previous process will be end and ask user to free up memory.")
                    while wait_end_process("join_images_script.exe"):
                        time.sleep(5)
                    while wait_end_process("backup_script.exe"):
                        time.sleep(5)
                memory_alert = pag.alert("There are too little memory on local " + programPath[0:2]
                                         + "disk. Please, free up disk space", "MEMORY ALERT",
                                         button=['Start measuring without scanning', 'Done - memory is free up'],
                                         timeout=60*60*1000)
                if memory_alert != 'Done - memory is free up':
                    for temp_nummber_of_sensor in range(NumberOfSensor, 9):
                        sSensor[temp_nummber_of_sensor] = 0
                    error = 2
                    save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                             "| The request has not been made. Program continue in measurement "
                             "without scanning processes")

            delFinishedSteps = 0
            set_process_error()

            control_language()
            # ↑ Switch to eng keyboard if it doesn't.

            save_log(2 * "\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                     "|SENSOR| Number: " + str(NumberOfSensor + 1) + " | Name: " +
                     nameSensor[NumberOfSensor] + " | Type: " + sType[NumberOfSensor] + " | APS: ")
            if pSensor[NumberOfSensor] == 1:
                save_log("YES")
            else:
                save_log("NO")
            save_log(" | Measuring: ")
            if mSensor[NumberOfSensor] == 1:
                save_log("YES")
            else:
                save_log("NO")
            save_log(" | Scanning: ")
            if sSensor[NumberOfSensor] == 1:
                save_log("YES")
            else:
                save_log("NO")
            save_log("\nFree RAM: " + str(memory("RAM")) + " MB")

            if not firstProcess:
                reset_mm3d(True)
            if if_find_error():
                raise WaitError("Error has been occurred in 'reset_mm3d' function.")

            try:
                os.mkdir(measurePath + sType[NumberOfSensor] + "\\" + nameSensor[NumberOfSensor])
                # ↑ Prepare location for data.

            except OSError:
                if os.path.exists(measurePath + sType[NumberOfSensor] + "\\" + nameSensor[NumberOfSensor]):
                    ErrorId.createFolder[NumberOfSensor] = 0
                    save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                             "| Creation of folder has failed because the folder is already exist." +
                             " It has tried with name: " + nameSensor[NumberOfSensor])
                else:
                    error = 2
                    ErrorId.createFolder[NumberOfSensor] = 2
                    save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                             "| Creation of folder has failed. It has tried with name: " +
                             nameSensor[NumberOfSensor] + "\n" + traceback.format_exc())
                    continue

            else:
                set_process_error()
                ErrorId.createFolder[NumberOfSensor] = 1
                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                         "| Folder has been created with name: " + nameSensor[NumberOfSensor])

            if mSensor[NumberOfSensor] == 1:
                if not mm3d_on():
                    pag.click(Position.mm3d)
                    wait(sleep_until=["mm3dOn.png", "mm3dOn2.png", "mm3dOn3.png", "mm3dOn4.png"])
                if if_find_error():
                    ErrorId.startMeasuring[NumberOfSensor] = 2
                    save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                             "| Has been detected that result of previous line of code was unsuccessful"
                             " - wait function (locate on screen) of 'mm3dOn.png'.")

                if ErrorId.startMeasuring[NumberOfSensor] == 0:
                    try:
                        prepare_process("Measurement", manually)

                        if not if_find_error():
                            if manually:
                                start_routine("ATLASITK_" + sType[NumberOfSensor]
                                              + "_Measuring-Manually.RTN")
                            else:
                                start_routine("ATLASITK_" + sType[NumberOfSensor]
                                              + "_Measuring.RTN")
                            if if_find_error():
                                ErrorId.startMeasuring[NumberOfSensor] = 2
                                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                                         + "| Measurement of the sensor has failed at startup"
                                         " (during start of routine).")
                        # ↑ Start routine for correct sensor type and position.

                    except (OSError, TypeError, ValueError):
                        error = 2
                        ErrorId.startMeasuring[NumberOfSensor] = 2
                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                 "| Measurement of the sensor has failed at startup\n" + traceback.format_exc())
                        default()

                    else:
                        if ErrorId.startMeasuring[NumberOfSensor] != 2:
                            ErrorId.startMeasuring[NumberOfSensor] = 1
                            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                     "| Measurement of the sensor has been started")

                if ErrorId.startMeasuring[NumberOfSensor] == 1:
                    wait()  # Wait to saving measuring.

                    if if_repeat_measure():
                        set_repeat_measure(1)
                        repeat_measurement("Measurement", manually)
                        if not if_find_error():
                            wait(False)  # Wait to complete measuring.
                            after_laser_error()

                    if if_repeat_measure():
                        error = 2
                        set_process_error(1)
                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                 "| Measurement: repetition of process has failed because "
                                 "(solvable) error has been occurred two times in a row.")
                    if if_find_error():
                        ErrorId.completeMeasuring[NumberOfSensor] = 2
                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                 "| Measurement of the sensor has failed (before saving).")
                    if not if_find_error():
                        search_file()
                        if if_find_error():
                            ErrorId.completeMeasuring[NumberOfSensor] = 2
                            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                     "| Measurement of the sensor has failed (during file search).")

                    if not if_find_error():
                        save_file(measurePath + sType[NumberOfSensor] + "\\" + nameSensor[NumberOfSensor])
                        if if_find_error():
                            ErrorId.completeMeasuring[NumberOfSensor] = 2
                            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                     "| Measurement of the sensor has failed (during saving).")
                    if not if_find_error():
                        wait(False)  # Wait to complete measuring.
                        if if_repeat_measure():
                            try:
                                set_repeat_measure(1)
                                repeat_measurement("Measurement", manually)
                                if not if_find_error():
                                    wait(False)  # Wait to complete measuring.
                                    after_laser_error()

                                if if_repeat_measure():
                                    set_repeat_measure(1)
                                    repeat_measurement("Measurement", manually)
                                    if not if_find_error():
                                        wait(False)  # Wait to complete measuring.
                                        after_laser_error()

                                if if_repeat_measure():
                                    error = 2
                                    set_process_error(1)
                                    save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                             "| Measurement: repetition of process has failed because "
                                             "(solvable) error has been occurred three times in a row.")
                                if if_find_error():
                                    ErrorId.completeMeasuring[NumberOfSensor] = 2
                                    save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                             "| Measurement of the sensor has failed (during measurement).")

                            except (OSError, TypeError, ValueError):
                                error = 2
                                ErrorId.startMeasuring[NumberOfSensor] = 2
                                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                         "| Measurement of the sensor has failed at startup\n" + traceback.format_exc())
                                default()

                    if not if_find_error():
                        ErrorId.completeMeasuring[NumberOfSensor] = 1
                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                 "| Measurement of the sensor has been successfully completed")

                if ErrorId.completeMeasuring[NumberOfSensor] == 1:
                    try:
                        edit_output(0, NumberOfSensor)
                        edit_output(1, NumberOfSensor)
                        edit_output(2, NumberOfSensor)
                        if os.path.exists(measurePath + sType[NumberOfSensor] + "\\"
                                          + nameSensor[NumberOfSensor] + "\\planarity.txt"):
                            os.rename(measurePath + sType[NumberOfSensor] + "\\"
                                      + nameSensor[NumberOfSensor] + "\\planarity.txt", measurePath
                                      + sType[NumberOfSensor] + "\\" + nameSensor[NumberOfSensor]
                                      + "\\planarity_" + datetime.datetime.now().strftime("%y_%m_%d_%H_%M") + ".txt")
                    except OSError:
                        error = 2
                        ErrorId.editOutput[NumberOfSensor] = 2
                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                 "| Edit of measured data and creating of header file have failed. "
                                 "Program has probably problem with file. (Can't find, not permission, etc...)"
                                 "\n" + traceback.format_exc())

                    except ValueError:
                        error = 2
                        ErrorId.editOutput[NumberOfSensor] = 2
                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                 "| Edit of measured data and creating of header file have failed. "
                                 "Program has probably problem data in file. (maybe too much of points)"
                                 "\n" + traceback.format_exc())

                    except (MemoryError, BufferError):
                        error = 2
                        ErrorId.editOutput[NumberOfSensor] = 2
                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                                 + "| Edit of measured data has failed. Program has probably problem "
                                 "with memory.\nFree date size on RAM: " + str(memory("RAM"))
                                 + " MB\nFree data size on DISK: " + str(memory(programPath[0:2]))
                                 + " GB\n" + traceback.format_exc())

                    else:
                        if ErrorId.editOutput[NumberOfSensor] != 2:
                            ErrorId.editOutput[NumberOfSensor] = 1
                            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                     "| Edit of measured data and creating of header file have "
                                     "been successfully completed")

                set_process_error()

            if sSensor[NumberOfSensor] == 1:
                """
                if ErrorId.completeMeasuring[NumberOfSensor] != 1:
                    try:
                        edit_output(1, NumberOfSensor)
                    except OSError:
                        error = 2
                        ErrorId.editOutput[NumberOfSensor] = 2
                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                 "| Creating of header file has failed. Program has probably problem "
                                 "with file. (Can't find, not permission, etc...)\n" + traceback.format_exc())

                    else:
                        if ErrorId.editOutput[NumberOfSensor] != 2:
                            ErrorId.editOutput[NumberOfSensor] = 1
                            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                     "| Creating of header file has been successfully completed")
                """
                try:
                    files = os.listdir(measurePath)
                    for file in files:
                        if file.endswith(".BMP"):
                            try:
                                move(measurePath + file, measurePath + "Trash")
                            except shutilError:
                                os.remove(measurePath + "Trash\\" + file)
                                move(measurePath + file, measurePath + "Trash")

                except OSError:
                    error = 2
                    ErrorId.moveTrash[NumberOfSensor] = 2
                    save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                             "| Moving of old screens has failed\n" + traceback.format_exc())

                else:
                    ErrorId.moveTrash[NumberOfSensor] = 1
                    save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                             "| Moving of old screens has been successfully completed")

                if ErrorId.completeMeasuring[NumberOfSensor] != 1:
                    if not mm3d_on():
                        pag.click(Position.mm3d)
                        wait(sleep_until=["mm3dOn.png", "mm3dOn2.png", "mm3dOn3.png", "mm3dOn4.png"])
                    if if_find_error():
                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                 "| Has been detected that result of previous line of code was unsuccessful"
                                 " - wait function (locate on screen) of 'mm3dOn.png'.")
                        continue

                try:
                    if not (mSensor[NumberOfSensor] == 0 and firstProcess):
                        reset_mm3d(True)
                        if if_find_error():
                            raise WaitError("Error has been occurred in 'reset_mm3d' function.")

                    if not if_find_error():
                        prepare_process("Scanning", manually)

                        if ErrorId.startScanning[NumberOfSensor] == 0:
                            start_routine("ATLASITK_" + sType[NumberOfSensor] + "_Scanning.RTN")
                            if if_find_error():
                                ErrorId.startScanning[NumberOfSensor] = 2
                                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                                         + "| Scanning of the sensor has failed at startup"
                                         " (during start of routine).")
                                continue

                except (OSError, TypeError, ValueError):
                    error = 2
                    ErrorId.startScanning[NumberOfSensor] = 2
                    save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                             "| Scanning of the sensor has failed at startup\n" + traceback.format_exc())
                    default()
                    continue

                else:
                    if ErrorId.startScanning[NumberOfSensor] != 2:
                        ErrorId.startScanning[NumberOfSensor] = 1
                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                 "| Scanning of the sensor has been started")

                if not if_find_error():
                    wait(False)  # Waiting to end of scanning.

                    if if_repeat_measure():
                        set_repeat_measure(1)
                        repeat_measurement("Scanning", manually)
                        if not if_find_error():
                            wait(False)  # Wait to complete measuring.
                            after_laser_error()

                    if if_repeat_measure():
                        set_repeat_measure(1)
                        repeat_measurement("Scanning", manually)
                        if not if_find_error():
                            wait(False)  # Wait to complete measuring.
                            after_laser_error()

                    if if_repeat_measure():
                        set_repeat_measure(1)
                        repeat_measurement("Scanning", manually)
                        if not if_find_error():
                            wait(False)  # Wait to complete measuring.
                            after_laser_error()

                    if if_repeat_measure():
                        error = 2
                        set_process_error(1)
                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                 "| Scanning: repetition of process has failed because "
                                 "(solvable) error has been occurred four times in a row.")
                    if if_find_error():
                        ErrorId.completeMeasuring[NumberOfSensor] = 2
                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                 "| Scanning of the sensor has failed (during measurement).")

                    if not if_find_error():
                        ErrorId.completeScanning[NumberOfSensor] = 1
                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                 "| Scanning of the sensor has been successfully completed")

                    if not mm3d_on():
                        pag.click(Position.mm3d)
                        wait(sleep_until=["mm3dOn.png", "mm3dOn2.png", "mm3dOn3.png", "mm3dOn4.png"])
                        if if_find_error():
                            ErrorId.moveScreens[NumberOfSensor] = 2
                            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                     "| Has been detected that result of previous line of code was unsuccessful"
                                     " - wait function (locate on screen) of 'mm3dOn.png'.")

                if ErrorId.startScanning[NumberOfSensor] == 1:
                    no_image = True
                    try:
                        files = os.listdir(measurePath)
                        for file in files:
                            if file.endswith(".BMP"):
                                no_image = False
                                file_name = "-".join(file.split('-')[:1]) + "-" \
                                            + str(delFinishedSteps + int(file.split('-')[len(file.split('-')) - 2])) \
                                            + "-1.BMP"
                                os.rename(measurePath + file, measurePath + sType[NumberOfSensor] + "\\"
                                          + nameSensor[NumberOfSensor] + "\\" + file_name)

                    except OSError:
                        error = 2
                        ErrorId.moveScreens[NumberOfSensor] = 2
                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                 "| Move of screens has failed\n" + traceback.format_exc())
                        continue

                    else:
                        if no_image:
                            ErrorId.moveScreens[NumberOfSensor] = 2
                            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                     "| Move of screens has failed. No images in the folder: " + measurePath)
                        else:
                            ErrorId.moveScreens[NumberOfSensor] = 1
                            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                     "| Move of screens has been successfully completed")

                limit = limit_size(NumberOfSensor)
                test_size = 0
                try:
                    test_size = check_size(measurePath + sType[NumberOfSensor] + "\\"
                                           + nameSensor[NumberOfSensor])

                except OSError:
                    error = 2
                    ErrorId.dataSizeTest[NumberOfSensor] = 2
                    save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                             "| Test of files has failed\n" + traceback.format_exc())

                if limit[0] < test_size < limit[1]:
                    ErrorId.dataSizeTest[NumberOfSensor] = 1
                    save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                             "| Test of files has been successfully completed")

                else:
                    error = 2
                    ErrorId.dataSizeTest[NumberOfSensor] = 2
                    save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                             "| Test of files has been completed with fault(s) - size: "
                             + str(test_size) + " B and not " + str(limit))

                if not if_find_error():
                    try:
                        arg_js = programPath + "join_images_script.exe 1 " + measurePath + " " + cloudPath\
                                 + " " + sType[NumberOfSensor] + " " + nameSensor[NumberOfSensor] \
                                 + " " + str(NumberOfSensor) + " " + str(pSensor[NumberOfSensor]) \
                                 + " " + programPath + " " + save_log(return_log_file=True) + " " + "0"
                        Popen(arg_js)

                    except OSError:
                        error = 2
                        ErrorId.startJoinScreens[NumberOfSensor] = 2
                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                 "| Joining of screens has failed at startup\n" + traceback.format_exc())
                        continue

                    else:
                        ErrorId.startJoinScreens[NumberOfSensor] = 1
                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                 "| Joining of screens has been successfully started")
            else:
                if ErrorId.editOutput[NumberOfSensor] == 1:
                    try:
                        arg_bs = programPath + "backup_script.exe 1 " + measurePath + " " + cloudPath \
                                 + " " + sType[NumberOfSensor] + " " + nameSensor[NumberOfSensor] \
                                 + " " + save_log(return_log_file=True) + " " + str(NumberOfSensor)
                        Popen(arg_bs)
                    except OSError:
                        error = 2
                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                 "| Copy of data to cloud has failed at startup\n" + traceback.format_exc())
                        continue

                    else:
                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                 "| Copy of data to cloud has been successfully started")
            firstProcess = False

        except WaitError:
            try:
                error = 2
                set_process_error()
                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                         "| Program has not been able to reset system to default position.\n"
                         + traceback.format_exc())
            except:
                raise ErrorDuringProcessing

        except (NameError, AttributeError):
            try:
                error = 2
                set_process_error()
                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                         "| Error has been occurred. Possible reasons of the problem are invalid or"
                         " unknown name or attribute of identifier (variable, function, etc...).\n"
                         + traceback.format_exc())
                default()
            except:
                raise ErrorDuringProcessing

        except:
            try:
                error = 2
                set_process_error()
                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                         "| Unexpected error has been occurred:\n" + traceback.format_exc())
                default()
            except:
                raise ErrorDuringProcessing


def start():
    global NumberOfSensor
    global defaultRepetition
    global firstProcess
    global error

    try:
        mouse_1 = pag.position()
        mouse_2 = [0, 0]

        if error == 0:
            sensors_size = 0
            NumberOfSensor = 0

            for NumberOfSensor in range(0, 9):
                if sType[NumberOfSensor] == "" or sType[NumberOfSensor] == "E"\
                        or nameSensor[NumberOfSensor] == "":
                    continue
                sensors_size += limit_size(NumberOfSensor)[1]
            assert memory(cloudPath) > \
                (round(sensors_size / (2 ** 30), 3)), "There is too little of memory on disk\n" \
                                                      "Required: " + str(round(sensors_size / (2 ** 30), 3)) \
                                                      + " GB, but is: " + str(memory(cloudPath)) + " GB"
            assert memory("RAM") > 1000, "There is too little of RAM memory, only: " \
                                         + str(memory("RAM")) + " MB"
            assert memory(programPath[0:2]) > (round(sensors_size / (2 ** 30), 3)),\
                "There is too little of memory on local " + programPath[0:2] + "disk\nRequired: " \
                + str(round(sensors_size / (2 ** 30), 3)) + " GB, but is: " + str(memory(programPath[0:2])) + " GB"

            save_log("START MEASURING: " + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                     + "\nFree data size on DISK: " + str(memory(cloudPath))
                     + " GB\n___________________________________", True)

            time.sleep(1)
            while mouse_1 != mouse_2:
                mouse_1 = pag.position()
                time.sleep(0.5)
                mouse_2 = pag.position()
            # ↑ It declare more time for user to move down hand from mouse.
            control_language()
            # ↑ Switch to eng keyboard if it doesn't.

            NumberOfSensor = 0
            set_process_error()

            find_objects()

            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                     "| Objects on screen has been successfully found")

        else:
            defaultRepetition = 0
            firstProcess = True

            sensors_size = 0
            NumberOfSensor = 0
            for NumberOfSensor in range(0, 9):
                if sType[NumberOfSensor] == "" or sType[NumberOfSensor] == "E":
                    continue
                sensors_size += limit_size(NumberOfSensor)[1]
                # ↑ Calculation of size

                if os.path.exists(programPath + "BS_ok_"
                                  + str(NumberOfSensor) + ".txt"):
                    os.remove(programPath + "BS_ok_" + str(NumberOfSensor) + ".txt")
                if os.path.exists(programPath + "JS_ok_"
                                  + str(NumberOfSensor) + ".txt"):
                    os.remove(programPath + "JS_ok_" + str(NumberOfSensor) + ".txt")
                # ↑ Deleting of old js path files (created by manual joining of screens).

            assert memory(cloudPath) > \
                (round(sensors_size / (2 ** 30), 3)), "There is too little of memory on disk\n" \
                                                      "Required: " + str(round(sensors_size / (2 ** 30), 3)) \
                                                      + " GB, but is: " + str(memory(cloudPath)) + " GB"
            assert memory("RAM") > 1000, "There is too little of RAM memory, only: " \
                                         + str(memory("RAM")) + " MB"

            save_log("\n\nNEW START OF MEASURING: " + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                     + "\nFree data size on DISK: " + str(memory(cloudPath))
                     + " GB\n_________________________________________")

        error = 0
        set_process_error()

        mouse_1 = pag.position()
        while mouse_1 != mouse_2:
            mouse_1 = pag.position()
            time.sleep(0.5)
            mouse_2 = pag.position()
        # ↑ It declare more time for user to move down hand from mouse.
        reset_mm3d(True)
        if if_find_error():
            raise WaitError("Error has been occurred in 'reset_mm3d' function.")

        NumberOfSensor = 0
        for NumberOfSensor in range(0, 9):
            if sType[NumberOfSensor] == "" or sType[NumberOfSensor] == "E" or\
                    nameSensor[NumberOfSensor] == "" or sensorPosition[NumberOfSensor] == 1\
                    or pSensor[NumberOfSensor] == 0:
                continue
            start_routine("ATLASITK_Position-" + str(NumberOfSensor + 1) + ".RTN")
            if if_find_error():
                raise WaitError("Error has been occurred in 'start_routine' function (specifically position routine).")
            wait(False)
            if if_find_error():
                error = 1
                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                         " | Program can't set position of sensor on table (Control Position System).")
            else:
                time.sleep(0.5)
                pag.click(Position.resetRoutine)
                wait(sleep_until="resetRoutineOn.png")
                if if_find_error():
                    raise WaitError("Not located 'resetRoutineOn.png'")
                reset_origins()
                if if_find_error():
                    raise WaitError("Error has been occurred in 'reset_origins' function.")

                try:
                    os.remove(programPath + "Control position system\\control.txt")
                except OSError:
                    # Probably file not exist yet.
                    pass
                start_routine("ATLASITK_" + sType[NumberOfSensor] + "_Control.RTN")
                if if_find_error():
                    raise WaitError("Error has been occurred in 'start_routine' function "
                                    "(specifically control routine).")
                wait()
                if if_find_error():
                    error = 1
                else:
                    search_file()
                    if if_find_error():
                        raise WaitError("Error has been occurred in 'search_file' function.")
                    save_file(programPath + "Control position system")
                    if if_find_error():
                        raise WaitError("Error has been occurred in 'save_file' function.")
                    wait(False)
                    if if_find_error():
                        error = 1

            if not if_find_error():
                aps_nominal_points = [0.0, 0.0, 0.0, 0.0]
                aps_actual_points = [0.0, 0.0, 0.0, 0.0]
                with open(programPath + "Control position system\\control.txt", 'r') \
                        as aps_file:
                    aps_a = 0
                    aps_b = 0
                    aps_m = ""
                    while aps_a < 100:
                        aps_t0 = aps_file.read(1)
                        if aps_t0 == "+" or aps_t0 == "-" or aps_m == "-":
                            aps_c = 0
                            if aps_t0 == "-":
                                aps_t = "-"
                            else:
                                aps_t = "" + aps_m
                            while aps_c < 20:
                                aps_t1 = aps_file.read(1)
                                if aps_t1 == "" or aps_t1 == "\n" or aps_t1 == " " or aps_t1 == "\t"\
                                        or aps_t1 == "+":
                                    aps_c = 20
                                    continue
                                elif aps_t1 == "-":
                                    aps_c = 20
                                    aps_m = "-"
                                    continue
                                else:
                                    aps_m = ""
                                aps_t += aps_t1
                                aps_c += 1
                            if aps_b < 4:
                                aps_nominal_points[aps_b] = float(aps_t)
                            else:
                                aps_actual_points[aps_b - 4] = float(aps_t)
                            aps_b += 1
                        aps_a += 1
                    aps_file.close()

                aps_nominal_vector = [aps_nominal_points[2] - aps_nominal_points[0],
                                      aps_nominal_points[3] - aps_nominal_points[1]]
                aps_actual_vector = [aps_actual_points[2] - aps_actual_points[0],
                                     aps_actual_points[3] - aps_actual_points[1]]
                aps_nominal_angle = round(180 / math.pi * math.acos(abs(aps_nominal_vector[1]) /
                                                                    math.sqrt(aps_nominal_vector[0]
                                                                              * aps_nominal_vector[0]
                                                                              + aps_nominal_vector[1]
                                                                              * aps_nominal_vector[1])),
                                          4)
                if aps_nominal_points[2] > aps_nominal_points[0]:
                    aps_nominal_angle = 180 - aps_nominal_angle
                aps_actual_angle = round(180 / math.pi * math.acos(abs(aps_actual_vector[1]) /
                                                                   math.sqrt(aps_actual_vector[0]
                                                                             * aps_actual_vector[0]
                                                                             + aps_actual_vector[1]
                                                                             * aps_actual_vector[1])),
                                         4)
                if aps_actual_points[2] > aps_actual_points[0]:
                    aps_actual_angle = 180 - aps_actual_angle

                aps_distance_horizontal = aps_actual_points[2] - aps_nominal_points[2]
                aps_distance_vertical = aps_actual_points[3] - aps_nominal_points[3]
                aps_angle = aps_actual_angle - aps_nominal_angle

                if not (LimitDistance.Phi[0] < aps_angle < LimitDistance.Phi[1]) \
                        or not(LimitDistance.RightD[0] < aps_distance_horizontal < LimitDistance.RightD[1]) \
                        or not(LimitDistance.BottomD[0] < aps_distance_vertical < LimitDistance.BottomD[1]):
                    sensorPosition[NumberOfSensor] = 0
                    error = 1
                else:
                    sensorPosition[NumberOfSensor] = 1

                os.rename(programPath + "Control position system\\control.txt",
                          programPath + "Control position system\\"
                          + datetime.datetime.now().strftime("%y_%m_%d_%H_%M")
                          + "-" + nameSensor[NumberOfSensor] + ".txt")

            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                     "| Position of " + str(NumberOfSensor + 1) + ". sensor (" +
                     nameSensor[NumberOfSensor] + ") is: ")
            if sensorPosition[NumberOfSensor] == 0:
                save_log("WRONG")
            else:
                save_log("OK")

                reset_mm3d()
                time.sleep(1)
                save_position(NumberOfSensor)
                if not if_find_error():
                    save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                             "| Position of the " + str(NumberOfSensor + 1) + ". sensor has been successfully saved.")
                else:
                    sensorPosition[NumberOfSensor] = 0
                    error = 1
                    save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                             "| Position of the " + str(NumberOfSensor + 1) + ". sensor has not been saved.")

            set_process_error()
            reset_mm3d()
            if if_find_error():
                raise WaitError("Error has been occurred in 'reset_mm3d' function.")

        if not mm3d_on():
            pag.click(Position.mm3d)
            wait(sleep_until=["mm3dOn.png", "mm3dOn2.png", "mm3dOn3.png", "mm3dOn4.png"])
        NumberOfSensor = 0

        if error == 0:
            process(True)  # Star measuring and scanning for sensors with manual setting of position.
            process()  # Star measuring and scanning for sensors with automatic setting of position.

        if error != 1:

            while wait_end_process("join_images_script.exe"):
                time.sleep(10)
            while wait_end_process("backup_script.exe"):
                time.sleep(5)

            NumberOfSensor = 0
            for NumberOfSensor in range(0, 9):
                if ErrorId.startJoinScreens[NumberOfSensor] != 0:
                    if os.path.exists(programPath + "JS_ok_"
                                      + str(NumberOfSensor) + ".txt"):
                        ErrorId.completeJoinScreens[NumberOfSensor] = 1
                        os.remove(programPath + "JS_ok_" + str(NumberOfSensor) + ".txt")
                    else:
                        ErrorId.completeJoinScreens[NumberOfSensor] = 2
                if (sSensor[NumberOfSensor] == 0 and ErrorId.editOutput[NumberOfSensor] == 1) \
                        or (sSensor[NumberOfSensor] == 1 and ErrorId.completeJoinScreens[NumberOfSensor] == 1):
                    if os.path.exists(programPath + "BS_ok_"
                                      + str(NumberOfSensor) + ".txt"):
                        ErrorId.copyToCloud[NumberOfSensor] = 1
                        os.remove(programPath + "BS_ok_" + str(NumberOfSensor) + ".txt")
                    else:
                        ErrorId.copyToCloud[NumberOfSensor] = 2

            protocol()
            save_log("\n___________________________________\nEND OF MEASURING: "
                     + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                     + "\nFree data size on DISK: " + str(memory(cloudPath)) + " GB")

        set_process_error()

        if error == 0:
            reset_mm3d(True)  # Switch to mm3d and reset mm3d.
            SMS.destroy()
            pag.hotkey('win', 'd')
            pag.alert("Everything done!", "Message")  # Alert end of program.

        elif error == 1:
            reset_mm3d(True)  # Reset mm3d.
            if if_find_error():
                raise WaitError("Error has been occurred in 'reset_mm3d' function.")

            aps_error_string = ""
            NumberOfSensor = 0
            for NumberOfSensor in range(1, 9):
                if sensorPosition[NumberOfSensor] == 1 or sType[NumberOfSensor] == "E" or\
                        sType[NumberOfSensor] == "" or nameSensor[NumberOfSensor] == "" or\
                        pSensor[NumberOfSensor] == 0:
                    continue
                aps_error_string += str(NumberOfSensor + 1)
                aps_error_string += ", "

            pag.alert("SENSOR POSITION PROBLEM!" + 2*"\n" + "Please, improve the"
                      " position of the following sensor(s):" + "\n" + aps_error_string
                      + "\nThen click to 'Continue' button.", "ERROR", "Continue", root=SMS)

        else:
            after_error_reset()
            pag.alert("Error(s) was/were occurred during processing!" + 2*"\n" +
                      "More info about error is in protocol in folder:" + "\n" +
                      programPath + "Protocols", "ERROR", root=SMS)

    except WaitError:
        if control_string(traceback.format_exc())[0] <= 15 or control_string(traceback.format_exc())[1] <= 1200:
            pag.alert("Error has been occurred:\n\nHas been detected that result of previous line of code "
                      "was unsuccessful." + 3 * "\n" + traceback.format_exc(), "ERROR", root=SMS)
        else:
            with open("C:\\Users\\Admin\\Desktop\\" + datetime.datetime.now().strftime("%y_%m_%d_%H_%M")
                      + "_error.txt", "w") as error_file:
                error_file.write("Error has been occurred:\n\nHas been detected that result of previous "
                                 "line of code was unsuccessful." + 3 * "\n" + traceback.format_exc())
                error_file.close()
            pag.alert("Error is too long.\n\nIt will be in text file on desktop.", "ERROR", root=SMS)

    except ErrorDuringProcessing:
        after_error_reset()
        if control_string(traceback.format_exc())[0] <= 15 or control_string(traceback.format_exc())[1] <= 1200:
            pag.alert("Error has been occurred during measuring:\n\nPossible reasons of the problem are"
                      "default or log file system.\nUse manual and error message below:"
                      + 3 * "\n" + traceback.format_exc(), "ERROR", root=SMS)
        else:
            with open("C:\\Users\\Admin\\Desktop\\" + datetime.datetime.now().strftime("%y_%m_%d_%H_%M")
                      + "_error.txt", "w") as error_file:
                error_file.write("Error has been occurred during measuring:\n\nPossible reasons of the problem are"
                                 "default or log file system.\nUse manual and error message below:"
                                 + 3 * "\n" + traceback.format_exc())
                error_file.close()
            pag.alert("Error is too long.\n\nIt will be in text file on desktop.", "ERROR", root=SMS)

    except AssertionError:
        if control_string(traceback.format_exc())[0] <= 15 or control_string(traceback.format_exc())[1] <= 1200:
            pag.alert("Error has been occurred:\n\nReason is result of test function (assert) initialize program."
                      + 3 * "\n" + traceback.format_exc(), "ERROR", root=SMS)
        else:
            with open("C:\\Users\\Admin\\Desktop\\" + datetime.datetime.now().strftime("%y_%m_%d_%H_%M")
                      + "_error.txt", "w") as error_file:
                error_file.write("Error has been occurred:\n\nReason is result of test function (assert) "
                                 "initialize program." + 3 * "\n" + traceback.format_exc())
                error_file.close()
            pag.alert("Error is too long.\n\nIt will be in text file on desktop.", "ERROR", root=SMS)

    except OSError:
        after_error_reset()
        if control_string(traceback.format_exc())[0] <= 15 or control_string(traceback.format_exc())[1] <= 1200:
            pag.alert("Error has been occurred before or after measuring:\n\nPossible reasons of the problem"
                      " are missing files or screens.\nCheck program directory with data file and screens to"
                      " locating function.\nUse manual and look up to \n'C:\\Program Files\\MetrologyAndScanning'."
                      + 3*"\n" + traceback.format_exc(), "ERROR", root=SMS)
        else:
            with open("C:\\Users\\Admin\\Desktop\\" + datetime.datetime.now().strftime("%y_%m_%d_%H_%M")
                      + "_error.txt", "w") as error_file:
                error_file.write("Error has been occurred before or after measuring:\n\nPossible reasons "
                                 "of the proble are missing files or screens.\nCheck program directory with "
                                 "data file and screens to locating function.\nUse manual and look up to \n"
                                 "'C:\\Program Files\\MetrologyAndScanning'." + 3*"\n" + traceback.format_exc())
                error_file.close()
            pag.alert("Error is too long.\n\nIt will be in text file on desktop.", "ERROR", root=SMS)

    except (NameError, AttributeError):
        after_error_reset()
        if control_string(traceback.format_exc())[0] <= 15 or control_string(traceback.format_exc())[1] <= 1200:
            pag.alert("Error has been occurred before or after measuring:\n\n"
                      "Possible reasons of the problem are invalid or"
                      " unknown name or attribute of identifier (variable, function, etc...)."
                      + "\nProgram maybe didn't load data from directory with data file and screens."
                      + "\nUse error message below:" + 3 * "\n" + traceback.format_exc(), "ERROR", root=SMS)
        else:
            with open("C:\\Users\\Admin\\Desktop\\" + datetime.datetime.now().strftime("%y_%m_%d_%H_%M")
                      + "_error.txt", "w") as error_file:
                error_file.write("Error has been occurred before or after measuring:\n\n"
                                 "Possible reasons of the problem are invalid or"
                                 " unknown name or attribute of identifier (variable, function, etc...)."
                                 "\nProgram maybe didn't load data from directory with data file and screens."
                                 "\nUse error message below:" + 3 * "\n" + traceback.format_exc())
                error_file.close()
            pag.alert("Error is too long.\n\nIt will be in text file on desktop.", "ERROR", root=SMS)

    except (TypeError, ValueError):
        after_error_reset()
        if control_string(traceback.format_exc())[0] <= 15 or control_string(traceback.format_exc())[1] <= 1200:
            pag.alert("Error has been occurred before or after measuring:\n\nPossible reason"
                      " of the problem is bad type of variables.\nProblem can be in control position system "
                      "of sensors.\nUse error message below:" + 3 * "\n" + traceback.format_exc(), "ERROR", root=SMS)
        else:
            with open("C:\\Users\\Admin\\Desktop\\" + datetime.datetime.now().strftime("%y_%m_%d_%H_%M")
                      + "_error.txt", "w") as error_file:
                error_file.write("Error has been occurred before or after measuring:\n\nPossible reason"
                                 " of the problem is bad type of variables.\nProblem can be in control position system"
                                 " of sensors.\nUse error message below:" + 3 * "\n" + traceback.format_exc())
                error_file.close()
            pag.alert("Error is too long.\n\nIt will be in text file on desktop.", "ERROR", root=SMS)

    except (MemoryError, BufferError):
        after_error_reset()
        if control_string(traceback.format_exc())[0] <= 15 or control_string(traceback.format_exc())[1] <= 1200:
            pag.alert("Error has been occurred before or after measuring:\n\nPossible reason of the "
                      "error is problem with memory.\nFree date size on RAM: " + str(memory("RAM"))
                      + " MB\nFree data size on DISK: " + str(memory(programPath[0:2])) + " GB"
                      + 3 * "\n" + traceback.format_exc(), "ERROR", root=SMS)
        else:
            with open("C:\\Users\\Admin\\Desktop\\" + datetime.datetime.now().strftime("%y_%m_%d_%H_%M")
                      + "_error.txt", "w") as error_file:
                error_file.write("Error has been occurred before or after measuring:\n\nPossible reason of the "
                                 "error is problem with memory.\nFree date size on RAM: "
                                 + str(memory("RAM")) + " MB\nFree data size on DISK: "
                                 + str(memory(programPath[0:2])) + " GB" + 3 * "\n" + traceback.format_exc())
                error_file.close()
            pag.alert("Error is too long.\n\nIt will be in text file on desktop.", "ERROR", root=SMS)

    except:
        after_error_reset()
        if control_string(traceback.format_exc())[0] <= 15 or control_string(traceback.format_exc())[1] <= 1200:
            pag.alert("Unexpected error has been occurred before or after measuring:" + 3*"\n"
                      + traceback.format_exc(), "ERROR", root=SMS)
        else:
            with open("C:\\Users\\Admin\\Desktop\\" + datetime.datetime.now().strftime("%y_%m_%d_%H_%M")
                      + "_error.txt", "w") as error_file:
                error_file.write("Unexpected error has been occurred before or after measuring:" + 3*"\n"
                                 + traceback.format_exc())
                error_file.close()
            pag.alert("Error is too long.\n\nIt will be in text file on desktop.", "ERROR", root=SMS)
