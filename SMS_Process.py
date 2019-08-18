# SCRIPT DETERMINING COURSE OF PROGRAM (FUNCTIONS USING ERROR SYSTEM)

from SMS_Functions import*
# Import script with declaring all of functions those not call by graphical user interface or use error system
# (include another script).


def process(manually=False):
    global NumberOfSensor
    global error
    global logFile

    for NumberOfSensor in range(0, 9):
        try:
            if sType[NumberOfSensor] == "" or sType[NumberOfSensor] == "E":
                continue

            if manually and pSensor[NumberOfSensor] == 1:
                continue

            elif not manually and pSensor[NumberOfSensor] == 0:
                continue

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
            save_log("\nFree RAM: " + str(round(memory("RAM"), 3)) + " MB")

            reset_mm3d(mm3d=True)
            if sensorPos[NumberOfSensor] == 0:
                raise WaitError("Error has been occurred in 'reset_mm3d' function.")

            if manually:
                pag.alert("Steps:" + "\n" + "1.) You must set axes in the program manually (Use manual)." + "\n" +
                          "2.) The lower left hand corner of sensor is zero position of X a Y axes." + "\n" +
                          "3.) The lower right hand corner of sensor is zero position of angle." + "\n" +
                          "4.) Click here to 'Start' button.", "Set manually position of sensor", "START", root=SMS)

                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                         "| Manually setting position of " + str(NumberOfSensor + 1) +
                         ". sensor has been successfully completed")
                pag.click(Position.desktop)
                wait(sleep_until="desktopOn.png")
                if sensorPos[NumberOfSensor] == 0:
                    save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                             "| Has been detected that result of previous line of code was unsuccessful"
                             " - wait function (locate on screen) of 'desktopOn.png'.")
                    continue

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
                ErrorId.createFolder[NumberOfSensor] = 1
                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                         "| Folder has been created with name: " + nameSensor[NumberOfSensor])

            if mSensor[NumberOfSensor] == 1:
                pag.click(Position.mm3d)  # Switch to MeasureMind3D (MM3D).
                wait(sleep_until="mm3dOn.png")
                if sensorPos[NumberOfSensor] == 0:
                    ErrorId.startMeasuring[NumberOfSensor] = 2
                    save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                             "| Has been detected that result of previous line of code was unsuccessful"
                             " - wait function (locate on screen) of 'mm3dOn.png'.")
                try:
                    if ErrorId.startMeasuring[NumberOfSensor] == 0:
                        start_routine("Sensor_A12-AllType_Z-Origin.RTN")
                        if sensorPos[NumberOfSensor] == 0:
                            ErrorId.startMeasuring[NumberOfSensor] = 2
                            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                     "| Setting origin of Z axis has failed (during start of Z origin routine).")
                        else:
                            wait(False)
                            if sensorPos[NumberOfSensor] == 0:
                                ErrorId.startMeasuring[NumberOfSensor] = 2
                                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                         "| Setting origin of Z axis has failed (during process of Z origin routine).")
                        if sensorPos[NumberOfSensor] != 0:
                            pag.click(Position.resetRoutine)
                            wait(sleep_until="resetRoutine.png")
                            if sensorPos[NumberOfSensor] == 0:
                                ErrorId.startMeasuring[NumberOfSensor] = 2
                                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                         "| Has been detected that result of previous line of code was unsuccessful"
                                         " - wait function (locate on screen) of 'resetRoutine.png'.")
                            if ErrorId.startMeasuring[NumberOfSensor] == 0:
                                pag.click(Position.resetZ)
                                wait(sleep_until="resetZOn.png")
                                if sensorPos[NumberOfSensor] == 0:
                                    ErrorId.startMeasuring[NumberOfSensor] = 2
                                    save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                             "| Has been detected that result of previous line of code was unsuccessful"
                                             " - wait function (locate on screen) of 'resetZOn.png'.")
                                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                         "| Origin of Z axis has been successfully set")

                        if ErrorId.startMeasuring[NumberOfSensor] == 0:
                            if manually:
                                start_routine("Sensor_A12-" + sType[NumberOfSensor] + "_Measuring-Manually.RTN")
                                if sensorPos[NumberOfSensor] == 0:
                                    ErrorId.startMeasuring[NumberOfSensor] = 2
                                    save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                             "| Measurement of the sensor has failed at startup "
                                             "(during start of routine).")
                            else:
                                start_routine("Sensor_A12_Position-" + str(NumberOfSensor + 1) + ".RTN")
                                if sensorPos[NumberOfSensor] == 0:
                                    ErrorId.startMeasuring[NumberOfSensor] = 2
                                    save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                             "| Measurement of the sensor has failed at startup "
                                             "(during start of position routine).")
                                else:
                                    wait(False)
                                    if sensorPos[NumberOfSensor] == 0:
                                        ErrorId.startMeasuring[NumberOfSensor] = 2
                                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                                 "| Measurement of the sensor has failed at startup "
                                                 "(during process of position routine).")
                                if sensorPos[NumberOfSensor] != 0:
                                    pag.click(Position.resetRoutine)
                                    wait(sleep_until="resetRoutine.png")
                                    if sensorPos[NumberOfSensor] == 0:
                                        ErrorId.startMeasuring[NumberOfSensor] = 2
                                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                                 "| Has been detected that result of previous line of"
                                                 " code was unsuccessful - wait function (locate on screen)"
                                                 " of 'resetRoutine.png'.")
                                    if ErrorId.startMeasuring[NumberOfSensor] == 0:
                                        reset_origins()
                                        if sensorPos[NumberOfSensor] == 0:
                                            ErrorId.startMeasuring[NumberOfSensor] = 2
                                            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                                                     + "| Measurement of the sensor has failed at startup"
                                                       " (during resetting the origins of axis).")
                                        else:
                                            start_routine("Sensor_A12-" + sType[NumberOfSensor] + "_Measuring.RTN")
                                            if sensorPos[NumberOfSensor] != 0:
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
                    if sensorPos[NumberOfSensor] == 0:
                        raise WaitError("Error has been occurred in 'default' function.")

                else:
                    if ErrorId.startMeasuring[NumberOfSensor] != 2:
                        ErrorId.startMeasuring[NumberOfSensor] = 1
                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                 "| Measurement of the sensor has been started")

                if ErrorId.startMeasuring[NumberOfSensor] == 1:
                    wait()  # Wait to saving measuring.
                    if sensorPos[NumberOfSensor] == 0:
                        ErrorId.completeMeasuring[NumberOfSensor] = 2
                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                 "| Measurement of the sensor has failed (before saving).")
                    if sensorPos[NumberOfSensor] != 0:
                        search_file()
                        if sensorPos[NumberOfSensor] == 0:
                            ErrorId.completeMeasuring[NumberOfSensor] = 2
                            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                     "| Measurement of the sensor has failed (during file search).")
                    if sensorPos[NumberOfSensor] != 0:
                        save_file(measurePath + sType[NumberOfSensor] + "\\" + nameSensor[NumberOfSensor])
                        if sensorPos[NumberOfSensor] == 0:
                            ErrorId.completeMeasuring[NumberOfSensor] = 2
                            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                     "| Measurement of the sensor has failed (during saving).")
                    if sensorPos[NumberOfSensor] != 0:
                        wait(False)  # Wait to complete measuring.
                        if sensorPos[NumberOfSensor] == 0:
                            ErrorId.completeMeasuring[NumberOfSensor] = 2
                            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                     "| Measurement of the sensor has failed (during measurement).")

                    if sensorPos[NumberOfSensor] != 0:
                        ErrorId.completeMeasuring[NumberOfSensor] = 1
                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                 "| Measurement of the sensor has been successfully completed")

                if ErrorId.completeMeasuring[NumberOfSensor] == 1:
                    try:
                        if sType == "R0":
                            edit_output('tempfile.txt', 890, 1, 0, " ")
                            edit_output('data_stream.DAT', -80, 3, 1, "")
                        elif sType == "R1":
                            edit_output('tempfile.txt', 890, 1, 0, " ")
                            edit_output('data_stream.DAT', -80, 3, 1, "")
                        elif sType == "R2":
                            edit_output('tempfile.txt', 890, 1, 0, " ")
                            edit_output('data_stream.DAT', -80, 3, 1, "")
                        elif sType == "R3":
                            edit_output('tempfile.txt', 890, 1, 0, " ")
                            edit_output('data_stream.DAT', -80, 3, 1, "")
                        elif sType == "R4":
                            edit_output('tempfile.txt', 890, 1, 0, " ")
                            edit_output('data_stream.DAT', -80, 3, 1, "")
                        elif sType == "R5":
                            edit_output('tempfile.txt', 890, 1, 0, " ")
                            edit_output('data_stream.DAT', -80, 3, 1, "")
                        elif sType == "B":
                            edit_output('tempfile.txt', 890, 1, 0, " ")
                            edit_output('data_stream.DAT', -80, 3, 1, "")
                        # ↑ Edit data output for correct sensor type.

                    except OSError:
                        error = 2
                        ErrorId.editOutput[NumberOfSensor] = 2
                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                 "| Edit of measured data has failed. Program has probably problem "
                                 "with file. (Can't find, not permission, etc...)\n" + traceback.format_exc())

                    except (MemoryError, BufferError):
                        error = 2
                        ErrorId.editOutput[NumberOfSensor] = 2
                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                                 + "| Edit of measured data has failed. Program has probably problem "
                                 "with memory.\nFree date size on RAM: " + str(round(memory("RAM"), 3))
                                 + " MB\nFree data size on DISK: " + str(round(memory("DISK"), 3))
                                 + " GB\n" + traceback.format_exc())

                    else:
                        if ErrorId.editOutput[NumberOfSensor] != 2:
                            ErrorId.editOutput[NumberOfSensor] = 1
                            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                     "| Edit of measured data has been successfully completed")

            if sSensor[NumberOfSensor] == 1:
                try:
                    files = os.listdir(measurePath)
                    for file in files:
                        if file.endswith(".BMP"):
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
                    pag.click(Position.mm3d)
                    wait(sleep_until="mm3dOn.png")
                    if sensorPos[NumberOfSensor] == 0:
                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                 "| Has been detected that result of previous line of code was unsuccessful"
                                 " - wait function (locate on screen) of 'mm3dOn.png'.")
                        continue

                if manually and (ErrorId.completeMeasuring[NumberOfSensor] == 2
                                 or ErrorId.startMeasuring[NumberOfSensor] == 2):
                    manually_set = pag.confirm("During measuring error has been occurred, you must set position "
                                               "of sensor again!\n\nDo you want set position of sensor manually?"
                                               "\nIf not, this sensor will be skipped.",
                                               "Set manually position of sensor", ["Confirm", "Skip"],
                                               root=SMS, timeout=5*60*1000)

                    if manually_set == "Confirm":
                        pag.alert("Steps:\n1.) You must set axes in the program manually (Use manual)."
                                  "\n2.) The lower left hand corner of sensor is zero position of X a Y axes."
                                  "\n3.) The lower right hand corner of sensor is zero position of angle."
                                  "\n4.) Click here to 'Start' button.", "Set manually position of sensor",
                                  "START", root=SMS)
                        pag.click(Position.mm3d)
                        wait(sleep_until="mm3dOn.png")
                        if sensorPos[NumberOfSensor] == 0:
                            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                     "| Has been detected that result of previous line of code was unsuccessful"
                                     " - wait function (locate on screen) of 'mm3dOn.png'.")
                            continue
                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                 "| Manually setting position of " + str(NumberOfSensor + 1) +
                                 ". sensor has been successfully completed")

                    else:
                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                 "| Manually setting position of " + str(NumberOfSensor + 1) +
                                 ". sensor has been stopped, this sensor will be skipped.")
                        pag.click(Position.desktop)
                        wait(sleep_until="desktopOn.png")
                        if sensorPos[NumberOfSensor] == 0:
                            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                     "| Has been detected that result of previous line of code was unsuccessful"
                                     " - wait function (locate on screen) of 'desktopOn.png'.")
                            continue
                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                 "| Manually setting position of " + str(NumberOfSensor + 1) +
                                 ". sensor has been stopped, this sensor will be skipped.")
                        continue

                try:
                    if not manually:
                        reset_mm3d()
                        if sensorPos[NumberOfSensor] == 0:
                            raise WaitError("Error has been occurred in 'reset_mm3d' function.")
                    if ErrorId.completeMeasuring[NumberOfSensor] != 1 or not manually:
                        start_routine("Sensor_A12-AllType_Z-Origin.RTN")
                        if sensorPos[NumberOfSensor] == 0:
                            ErrorId.startScanning[NumberOfSensor] = 2
                            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                     "| Setting origin of Z axis has failed (during start of Z origin routine).")
                            continue
                        wait(False)
                        if sensorPos[NumberOfSensor] == 0:
                            ErrorId.startScanning[NumberOfSensor] = 2
                            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                     "| Scanning of the sensor has failed at startup "
                                     "(during process of Z origin routine).")
                            continue
                        else:
                            pag.click(Position.resetRoutine)
                            wait(sleep_until="resetRoutine.png")
                            if sensorPos[NumberOfSensor] == 0:
                                ErrorId.startScanning[NumberOfSensor] = 2
                                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                         "| Has been detected that result of previous line of code was unsuccessful"
                                         " - wait function (locate on screen) of 'resetRoutine.png'.")
                                continue
                            pag.click(Position.resetZ)
                            wait(sleep_until="resetZOn.png")
                            if sensorPos[NumberOfSensor] == 0:
                                ErrorId.startScanning[NumberOfSensor] = 2
                                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                         "| Has been detected that result of previous line of code was unsuccessful"
                                         " - wait function (locate on screen) of 'resetZOn.png'.")
                                continue
                            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                     "| Origin of Z axis has been successfully set")

                    if ErrorId.startScanning[NumberOfSensor] == 0:
                        if manually:
                            pag.click(Position.resetAngle)
                            wait(sleep_until="resetAngleOn.png")
                            if sensorPos[NumberOfSensor] == 0:
                                ErrorId.startScanning[NumberOfSensor] = 2
                                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                         "| Has been detected that result of previous line of code was unsuccessful"
                                         " - wait function (locate on screen) of 'resetAngleOn.png'.")
                                continue
                            if ErrorId.startScanning[NumberOfSensor] == 0:
                                start_routine("Sensor_A12-" + sType[NumberOfSensor] + "_Scanning-Manually.RTN")
                                if sensorPos[NumberOfSensor] == 0:
                                    ErrorId.startScanning[NumberOfSensor] = 2
                                    save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                                             + "| Measurement of the sensor has failed at startup "
                                             "(during start of routine).")
                                    continue
                        else:
                            start_routine("Sensor_A12_Position-" + str(NumberOfSensor + 1) + ".RTN")
                            if sensorPos[NumberOfSensor] == 0:
                                ErrorId.startScanning[NumberOfSensor] = 2
                                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                                         + "| Measurement of the sensor has failed at startup "
                                         "(during start of position routine).")
                                continue
                            wait(False)
                            if sensorPos[NumberOfSensor] == 0:
                                ErrorId.startScanning[NumberOfSensor] = 2
                                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                                         + "| Scanning of the sensor has failed at startup "
                                         "(during process of position routine).")
                                continue
                            else:
                                pag.click(Position.resetRoutine)
                                wait(sleep_until="resetRoutineOn.png")
                                if sensorPos[NumberOfSensor] == 0:
                                    ErrorId.startScanning[NumberOfSensor] = 2
                                    save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                                             + "| Has been detected that result of previous line of code was "
                                             "unsuccessful - wait function (locate on screen) of"
                                             " 'resetRoutineOn.png'.")
                                    continue
                                if ErrorId.startScanning[NumberOfSensor] == 0:
                                    reset_origins()
                                    if sensorPos[NumberOfSensor] == 0:
                                        ErrorId.startScanning[NumberOfSensor] = 2
                                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                                                 + "| Measurement of the sensor has failed at startup"
                                                   " (during resetting the origins of axis).")
                                        continue
                                    start_routine("Sensor_A12-" + sType[NumberOfSensor] + "_Scanning.RTN")
                                    if sensorPos[NumberOfSensor] != 0:
                                        ErrorId.startScanning[NumberOfSensor] = 2
                                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                                                 + "| Measurement of the sensor has failed at startup"
                                                   " (during start of routine).")
                                        continue
                    # ↑ Start routine for correct sensor type.

                except (OSError, TypeError, ValueError):
                    error = 2
                    ErrorId.startScanning[NumberOfSensor] = 2
                    save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                             "| Scanning of the sensor has failed at startup\n" + traceback.format_exc())
                    default()
                    if sensorPos[NumberOfSensor] == 0:
                        raise WaitError("Error has been occurred in 'default' function.")
                    continue

                else:
                    if ErrorId.startScanning[NumberOfSensor] != 2:
                        ErrorId.startScanning[NumberOfSensor] = 1
                        save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                                 "| Scanning of the sensor has been started")

                wait(False)  # Waiting to end of scanning.

                if sensorPos[NumberOfSensor] == 0:
                    ErrorId.completeScanning[NumberOfSensor] = 2
                    save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                             "| Scanning of the sensor has failed")
                    continue

                ErrorId.completeScanning[NumberOfSensor] = 1
                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                         "| Scanning of the sensor has been successfully completed")

                pag.click(Position.desktop)
                wait(sleep_until="desktopOn.png")
                if sensorPos[NumberOfSensor] == 0:
                    ErrorId.moveScreens[NumberOfSensor] = 2
                    save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                             "| Has been detected that result of previous line of code was unsuccessful"
                             " - wait function (locate on screen) of 'desktopOn.png'.")
                    continue
                try:
                    files = os.listdir(measurePath)
                    for file in files:
                        if file.endswith(".BMP"):
                            move(measurePath + file, measurePath + sType[NumberOfSensor] + "\\"
                                 + nameSensor[NumberOfSensor])

                except OSError:
                    error = 2
                    ErrorId.moveScreens[NumberOfSensor] = 2
                    save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                             "| Move of screens has failed\n" + traceback.format_exc())
                    continue

                else:
                    ErrorId.moveScreens[NumberOfSensor] = 1
                    save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                             "| Move of screens has been successfully completed")

                try:
                    arg_js = programPath + "join_images_script.exe 1 " + measurePath \
                             + " " + sType[NumberOfSensor] + " " + nameSensor[NumberOfSensor] \
                             + " " + str(NumberOfSensor) + " " + str(pSensor[NumberOfSensor]) \
                             + " " + logFile + " " + programPath
                    subprocess.call(args=arg_js, shell=True)

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

                limit = [0, 0]
                test_size = 0
                try:
                    test_size = check_size(measurePath + "\\" + sType[NumberOfSensor] + "\\"
                                           + nameSensor[NumberOfSensor])
                    limit = limit_size()

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
                             "| Test of files has been completed with fault(s)")

        except (NameError, AttributeError):
            try:
                error = 2
                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                         "| Error has been occurred. Possible reasons of the problem are invalid or"
                         " unknown name or attribute of identifier (variable, function, etc...).\n"
                         + traceback.format_exc())
                default()
                if sensorPos[NumberOfSensor] == 0:
                    raise WaitError("Error has been occurred in 'default' function.")
            except:
                raise ErrorDuringProcessing

        except:
            try:
                error = 2
                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                         "| Unexpected error has been occurred:\n" + traceback.format_exc())
                default()
                if sensorPos[NumberOfSensor] == 0:
                    raise WaitError("Error has been occurred in 'default' function.")
            except:
                raise ErrorDuringProcessing


def start():
    global NumberOfSensor
    global error

    try:
        if error == 0:
            sensors_size = 0
            NumberOfSensor = 0

            for NumberOfSensor in range(0, 9):
                if sType[NumberOfSensor] == "" or sType[NumberOfSensor] == "E":
                    continue
                sensors_size += limit_size()[1]
            assert memory("DISK") > \
                (round(sensors_size / (2 ** 30), 3)), "There is too little of memory on disk\n" \
                                                      "Required: " + str(round(sensors_size / (2 ** 30), 3)) \
                                                      + " GB, but is: " + str(round(memory("DISK"), 3)) + " GB"
            assert memory("RAM") > 1000, "There is too little of RAM memory, only: " \
                                         + str(round(memory("RAM"), 3)) + " MB"

            save_log("START MEASURING: " + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                     + "\nFree data size on DISK: " + str(round(memory("DISK"), 3))
                     + " GB\n___________________________________", True)

            pag.click(Position.desktop)
            Position.mm3d = pag.locateCenterOnScreen(Img.mm3d, grayscale=True)
            # ↑ Overwrite position of MM3D icon.
            Position.desktop = list(pag.size())
            pag.click(Position.mm3d)
            wait(sleep_until="mm3dOn.png")
            if sensorPos[NumberOfSensor] == 0:
                raise WaitError("Not located 'mm3dOn.png'")
            Position.file = pag.locateCenterOnScreen(Img.file, grayscale=True)
            Position.system = pag.locateCenterOnScreen(Img.system, grayscale=True)
            Position.resetRoutine = pag.locateCenterOnScreen(Img.resetRoutine, grayscale=True)
            Position.resetX = pag.locateCenterOnScreen(Img.resetX, grayscale=True)
            Position.resetY = pag.locateCenterOnScreen(Img.resetY, grayscale=True)
            Position.resetZ = pag.locateCenterOnScreen(Img.resetZ, grayscale=True)
            Position.resetAngle = pag.locateCenterOnScreen(Img.resetAngle, grayscale=True)
            Position.start = pag.locateCenterOnScreen(Img.start, grayscale=True)
            pag.click(Position.file)
            wait(sleep_until="open.png")
            if sensorPos[NumberOfSensor] == 0:
                raise WaitError("Not located 'open.png'")
            Position.open = pag.locateCenterOnScreen(Img.open, grayscale=True)
            pag.click(Position.system)
            wait(sleep_until="resetSystem.png")
            if sensorPos[NumberOfSensor] == 0:
                raise WaitError("Not located 'resetSystem.png'")
            Position.resetSystem = pag.locateCenterOnScreen(Img.resetSystem, grayscale=True)
            pag.click(Position.desktop)

            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                     " | Objects on screen has been successfully found")

        error = 0
        reset_mm3d(True)
        if sensorPos[NumberOfSensor] != 0:
            raise WaitError("Error has been occurred in 'reset_mm3d' function.")

        NumberOfSensor = 9
        start_routine("Sensor_A12-AllType_Z-Origin.RTN")
        if sensorPos[NumberOfSensor] == 0:
            raise WaitError("Error has been occurred in 'start_routine' function (specifically Z origin routine).")
        wait(False)
        if sensorPos[NumberOfSensor] == 0:
            raise ZAxisError
        pag.click(Position.resetRoutine)
        wait(sleep_until="resetRoutine.png")
        if sensorPos[NumberOfSensor] == 0:
            raise WaitError("Not located 'resetRoutine.png'")
        pag.click(Position.resetZ)
        wait(sleep_until="resetZOn.png")
        if sensorPos[NumberOfSensor] == 0:
            raise WaitError("Not located 'resetZOn.png'")

        NumberOfSensor = 0
        for NumberOfSensor in range(0, 9):
            if sType[NumberOfSensor] == "" or sType[NumberOfSensor] == "E" or\
                    sensorPos[NumberOfSensor] == 1 or pSensor[NumberOfSensor] == 0:
                continue
            start_routine("Sensor_A12_Position-" + str(NumberOfSensor + 1) + ".RTN")
            if sensorPos[NumberOfSensor] == 0:
                raise WaitError("Error has been occurred in 'start_routine' function (specifically position routine).")
            wait(False)
            if sensorPos[NumberOfSensor] == 0:
                error = 1
                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                         " | Program can't set position of sensor on table (Control Position System).")
            if error == 0:
                pag.click(Position.resetRoutine)
                wait(sleep_until="resetRoutineOn.png")
                if sensorPos[NumberOfSensor] == 0:
                    raise WaitError("Not located 'resetRoutineOn.png'")
                reset_origins()
                if sensorPos[NumberOfSensor] == 0:
                    raise WaitError("Error has been occurred in 'reset_origins' function.")
                start_routine("Sensor_A12-" + sType[NumberOfSensor] + "_Control.RTN")
                if sensorPos[NumberOfSensor] == 0:
                    raise WaitError("Error has been occurred in 'start_routine' function "
                                    "(specifically control routine).")
                wait()
                if sensorPos[NumberOfSensor] == 0:
                    error = 1
                else:
                    search_file()
                    if sensorPos[NumberOfSensor] == 0:
                        raise WaitError("Error has been occurred in 'search_file' function.")
                    save_file(programPath + "Control position system")
                    if sensorPos[NumberOfSensor] == 0:
                        raise WaitError("Error has been occurred in 'save_file' function.")

            if error == 0:
                aps_point = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                             0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
                with open(programPath + "Control position system\\control.txt", 'r') \
                        as aps_file:
                    aps_a = 0
                    aps_b = 0
                    while aps_a < 1000:
                        aps_t0 = aps_file.read(1)
                        if aps_t0 == "+" or aps_t0 == "-":
                            aps_c = 0
                            if aps_t0 == "-":
                                aps_t = "-"
                            else:
                                aps_t = ""
                            while aps_c < 10:
                                aps_t1 = aps_file.read(1)
                                if aps_t1 == "" or aps_t1 == "\n":
                                    aps_c = 10
                                    continue
                                aps_t += aps_t1
                                aps_c += 1
                            aps_point[aps_b] = float(aps_t)
                            aps_b += 1
                        aps_a += 1
                    aps_file.close()
                aps_vector_p0 = [aps_point[0] - aps_point[3], aps_point[1] - aps_point[4]]
                aps_vector_p90 = [aps_vector_p0[1], -1 * aps_vector_p0[0]]
                aps_vector_q0 = [aps_point[15] - aps_point[18], aps_point[16] - aps_point[19]]
                aps_vector_q90 = [aps_vector_q0[1], -1 * aps_vector_q0[0]]

                aps_phi = 180 / math.pi * math.acos(abs(aps_vector_p0[0] * aps_vector_q0[0] +
                                                        aps_vector_p0[1] * aps_vector_q0[1]) /
                                                    (math.sqrt(aps_vector_p0[0] ** 2 + aps_vector_p0[1] ** 2) *
                                                     math.sqrt(aps_vector_q0[0] ** 2 + aps_vector_q0[1] ** 2)))

                aps_distance_right = abs(aps_vector_p90[0] * aps_point[27] + aps_vector_p90[1] * aps_point[28]
                                         - (aps_vector_p90[0] * aps_point[0] + aps_vector_p90[1] * aps_point[1])
                                         ) / math.sqrt(aps_vector_p90[0] ** 2 + aps_vector_p90[1] ** 2)

                aps_distance_bottom = abs(aps_vector_q90[0] * aps_point[27] + aps_vector_q90[1] * aps_point[28] -
                                          (aps_vector_q90[0] * aps_point[0] + aps_vector_q90[1] * aps_point[1])
                                          ) / math.sqrt(aps_vector_q90[0] ** 2 + aps_vector_q90[1] ** 2)

                if aps_phi > LimitDistance.Phi \
                        and LimitDistance.RightD[0] > aps_distance_right > LimitDistance.RightD[1] \
                        and LimitDistance.BottomD[0] > aps_distance_bottom > LimitDistance.BottomD[1]:
                    sensorPos[NumberOfSensor] = 0
                    error = 1

                os.rename(programPath + "Control position system\\control.txt",
                          programPath + "Control position system\\"
                          + datetime.datetime.now().strftime("%y_%m_%d_%H_%M") + "-" + nameSensor[NumberOfSensor])

            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                     "| Position of " + str(NumberOfSensor + 1) + ". sensor (" +
                     nameSensor[NumberOfSensor] + ") is: ")
            if sensorPos[NumberOfSensor] == 0:
                    save_log("WRONG")
            elif sensorPos[NumberOfSensor] == 1:
                    save_log("OK")

            reset_mm3d()
            if sensorPos[NumberOfSensor] == 0:
                raise WaitError("Error has been occurred in 'reset_mm3d' function.")

        pag.click(Position.desktop)
        NumberOfSensor = 0

        if error == 0:
            process(True)  # Star measuring and scanning for sensors with manual setting of position.
            process()  # Star measuring and scanning for sensors with automatic setting of position.

        if error != 1:
            wait_end_process("join_image_script.exe")

            NumberOfSensor = 0
            for NumberOfSensor in range(0, 9):
                if os.path.exists(programPath + "JS_ok_"
                                  + str(NumberOfSensor) + ".txt"):
                    ErrorId.completeJoinScreens[NumberOfSensor] = 1
                    os.remove(programPath + "JS_ok_" + str(NumberOfSensor) + ".txt")
                else:
                    if ErrorId.startJoinScreens[NumberOfSensor] == 1:
                        ErrorId.completeJoinScreens[NumberOfSensor] = 2

            protocol()
            save_log("\nEND OF MEASURING: " + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                     + "\nFree data size on DISK: " + str(round(memory("DISK"), 3))
                     + " GB\n___________________________________")

        if error == 0:
            reset_mm3d(True, True)  # Reset mm3d and switch to desktop.
            if sensorPos[NumberOfSensor] == 0:
                raise WaitError("Error has been occurred in 'reset_mm3d' function.")
            pag.alert("Everything done!", "Message", root=SMS)  # Alert end of program.
            SMS.destroy()

        elif error == 1:
            reset_mm3d(False, True)  # Reset mm3d and switch to desktop.
            if sensorPos[NumberOfSensor] == 0:
                raise WaitError("Error has been occurred in 'reset_mm3d' function.")
            aps_error_string = ""
            NumberOfSensor = 0
            for NumberOfSensor in range(1, 9):
                if sensorPos[NumberOfSensor] == 1 or sType[NumberOfSensor] == "E" or\
                        sType[NumberOfSensor] == "":
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

    except ZAxisError:
        pag.alert("MesureMind 3D can't set origin of Z axis for control position system of sensors.",
                  "ERROR", root=SMS)

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
                      "error is problem with memory.\nFree date size on RAM: " + str(round(memory("RAM"), 3))
                      + " MB\nFree data size on DISK: " + str(round(memory("DISK"), 3)) + " GB"
                      + 3 * "\n" + traceback.format_exc(), "ERROR", root=SMS)
        else:
            with open("C:\\Users\\Admin\\Desktop\\" + datetime.datetime.now().strftime("%y_%m_%d_%H_%M")
                      + "_error.txt", "w") as error_file:
                error_file.write("Error has been occurred before or after measuring:\n\nPossible reason of the "
                                 "error is problem with memory.\nFree date size on RAM: "
                                 + str(round(memory("RAM"), 3)) + " MB\nFree data size on DISK: "
                                 + str(round(memory("DISK"), 3)) + " GB" + 3 * "\n" + traceback.format_exc())
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
