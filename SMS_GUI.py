#  SCRIPT WITH FUNCTIONS CALL BY GUI AND SETTINGS OF GUI.
import pyautogui as pag
import traceback

try:
    from SMS_Process import*
    # Import script with declaring all of functions those using error system and other scripts.

    """
    def on_closing():
        close_confirm = pag.confirm("Do you really want to quit program and stop all measurement processes?",
                                    "Quit alert",
                                    buttons=['Close', 'Continue'], timeout=30*1000)
        if close_confirm == 'Close':
            save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                     "| Program has been closed by operator.")
            SMS.destroy()
    """


    def name_of_sensor_enter_cursor(event):
        NameOfSensor.select_range(0, END)


    def sensor_database(event):
        global databaseError

        NameOfSensor.select_range(0, 0)
        if len(NameOfSensor.get()) == 14:
            try:
                _product = np.array(df.loc[df['serialNumber'] == NameOfSensor.get()]['type'])[0]
                _data = np.array(df.loc[df['serialNumber'] == NameOfSensor.get()]['alternativeIdentifier'])[0]
                _batch, _wafer = _data.split('-')

                if ((("R0" in _product or "R1" in _product or "R2" in _product)
                     and holderType[NumberOfSensor] == 2)
                        or (("R3" in _product or "R4" in _product or "R5" in _product)
                            and holderType[NumberOfSensor] == 1)):
                    if databaseError == 0:
                        databaseError = 2
                        pag.alert("Holder type in actual position does not match with type of sensor from database!\n"
                                  "Control serial number of sensor or change holder type.", "Alert")
                    else:
                        databaseError -= 1
                else:
                    ProductType.delete(0, END)
                    SensorBatch.delete(0, END)
                    SensorWafer.delete(0, END)

                    ProductType.insert(0, _product)
                    SensorBatch.insert(0, _batch)
                    SensorWafer.insert(0, _wafer)

                    if "R0" in _product:
                        r0_select()
                    elif "R1" in _product:
                        r1_select()
                    elif "R2" in _product:
                        r2_select()
                    elif "R3" in _product:
                        r3_select()
                    elif "R4" in _product:
                        r4_select()
                    elif "R5" in _product:
                        r5_select()
                    elif "B" in _product:
                        b_select()

            except (AttributeError, IndexError):
                pass


    def control_database():
        try:
            LabPar.Automatic = True
            check_database()

            database_confirm = pag.confirm("Temperature: " + str(LabPar.Temperature) + " °C\nHumidity: "
                                           + str(LabPar.Humidity) + " %", "Confirm following data from "
                                                                          "database!",
                                           buttons=['Confirm', 'Set manually'], timeout=5*60*1000)
            if database_confirm == 'Set manually':
                raise ValueError

        except:
            LabPar.Automatic = False
            if traceback.format_exc().count("ValueError") == 0:
                pag.alert("Program can't find out values of temperature and humidity in the lab automatically."
                          "\n\nPLEASE, INSERT IT MANUALLY\n\n"
                          "More info is in file on desktop.", "Import data error")
                with open("C:\\Users\\Admin\\Desktop\\" + datetime.datetime.now().strftime("%y_%m_%d_%H_%M")
                          + "_error.txt", "w") as error_file:
                    error_file.write(traceback.format_exc())
                    error_file.close()

            try:
                LabPar.Temperature = float(pag.prompt("Insert temperature [°C]:",
                                                      "Temperature in the laboratory",
                                                      default=str(LabPar.Temperature)))
                LabPar.Humidity = float(pag.prompt("Insert humidity [%]:",
                                                   "Humidity in the laboratory", default=str(LabPar.Humidity)))
                if 0 > LabPar.Humidity or LabPar.Humidity > 100:
                    pag.alert("Humidity can be only between 0% and 100%", "Value error")
                    LabPar.Humidity = float(pag.prompt("Insert humidity [%]:",
                                                       "Humidity in the laboratory",
                                                       default=str(LabPar.Humidity)))
            except ValueError:
                pag.alert("You must insert temperature or humidity only with numbers, +, - or .", "Value error")
                LabPar.Temperature = float(pag.prompt("Insert temperature [°C]:",
                                                      "Temperature in the laboratory",
                                                      default=str(LabPar.Temperature)))
                LabPar.Humidity = float(pag.prompt("Insert humidity [%]:",
                                                   "Humidity in the laboratory", default=str(LabPar.Humidity)))
                if 0 > LabPar.Humidity or LabPar.Humidity > 100:
                    pag.alert("Humidity can be only between 0% and 100%", "Value error")
                    LabPar.Humidity = float(pag.prompt("Insert humidity [%]:",
                                                       "Humidity in the laboratory",
                                                       default=str(LabPar.Humidity)))
            except TypeError:
                pass


    def change_run_number(run_number):
        SensorRunNumber.delete(0, END)
        SensorRunNumber.insert(0, run_number)


    def control_run_number(control_path):
        if os.path.exists(control_path):
            files = os.listdir(control_path)
            for file in files:
                if (file.endswith(str(SensorRunNumber.get()) + ".BMP") and CheckS.var.get()) or\
                        (file.endswith(str(SensorRunNumber.get()) + ".dat") and CheckM.var.get()):
                    return True
            return False
        else:
            return False


    def control_type():
        if holderType[NumberOfSensor] == 1:
            if sType[NumberOfSensor] == "R0" or sType[NumberOfSensor] == "R1" or sType[NumberOfSensor] == "R2" \
                    or sType[NumberOfSensor] == "B" or sType[NumberOfSensor] == "E":
                return True
            else:
                return False
        elif holderType[NumberOfSensor] == 2:
            if sType[NumberOfSensor] == "R3" or sType[NumberOfSensor] == "R4" or sType[NumberOfSensor] == "R5" \
                    or sType[NumberOfSensor] == "B" or sType[NumberOfSensor] == "E":
                return True
            else:
                return False
        else:
            pag.alert("Bad char format in the config file - Holder type\n"
                      "Please, correct it and restart program", "ERROR")
            return False


    def set_active(rewrite_con):
        CheckP["state"] = "active"
        CheckM["state"] = "active"
        CheckS["state"] = "active"
        ProductType["state"] = "normal"
        SensorBatch["state"] = "normal"
        SensorWafer["state"] = "normal"
        NameOfSensor["state"] = "normal"
        SensorComments["state"] = "normal"
        SensorRunNumber["state"] = "normal"
        if pSensor[NumberOfSensor] == 1:
            CheckP.select()
        else:
            CheckP.deselect()
        if rewrite_con:
            ProductType.insert(0, productType[NumberOfSensor])
            SensorBatch.insert(0, sensorBatch[NumberOfSensor])
            SensorWafer.insert(0, sensorWafer[NumberOfSensor])
            if nameSensor[NumberOfSensor] == "":
                NameOfSensor.insert(0, dNameSensor[NumberOfSensor])
            else:
                NameOfSensor.insert(0, nameSensor[NumberOfSensor])
            SensorComments.insert(0, comments[NumberOfSensor])
            change_run_number(runNumber[NumberOfSensor])


    def edit_metrology():
        productType[NumberOfSensor] = ProductType.get()
        sensorBatch[NumberOfSensor] = SensorBatch.get()
        sensorWafer[NumberOfSensor] = SensorWafer.get()
        nameSensor[NumberOfSensor] = NameOfSensor.get()
        comments[NumberOfSensor] = SensorComments.get()
        runNumber[NumberOfSensor] = SensorRunNumber.get()
        pSensor[NumberOfSensor] = CheckP.var.get()
        mSensor[NumberOfSensor] = CheckM.var.get()
        sSensor[NumberOfSensor] = CheckS.var.get()

        if os.path.exists(measurePath + sType[NumberOfSensor] + "\\"
                          + nameSensor[NumberOfSensor] + "\\planarity.txt"):
            try:
                if firstProcess:
                    control_database()
                    save_log(sys.argv[0] + "\nSTART EDITING FILES: "
                             + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                             + "\nFree data size on DISK: " + str(memory(cloudPath))
                             + " GB\n___________________________________", True)
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
                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                         "| Edit of measured data and creating of header file have failed. "
                         "Program has probably problem with file. (Can't find, not permission, etc...)"
                         "\n" + traceback.format_exc())

            except ValueError:
                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                         "| Edit of measured data and creating of header file have failed. "
                         "Program has probably problem with data in file. (maybe too much of points)"
                         "\n" + traceback.format_exc())

            except (MemoryError, BufferError):
                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                         + "| Edit of measured data has failed. Program has probably problem "
                           "with memory.\nFree date size on RAM: " + str(memory("RAM"))
                         + " MB\nFree data size on DISK: " + str(memory(measurePath[0:2]))
                         + " GB\n" + traceback.format_exc())
            else:
                save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") +
                         "| Edit of measured data and creating of header file have "
                         "been successfully completed")
        else:
            pag.alert("In folder:\n" + measurePath + sType[NumberOfSensor] + "\\"
                      + nameSensor[NumberOfSensor] + "\nmissing planarity file, "
                                                     "program can not convert data without this file"
                                                     "\n\t1.) If there is file with name planarity_\"date\""
                                                     ".txt rename to planarity.txt).\n\t2.) or remeasure data",
                      "Missing file")


    def r0_select():
        rewrite = False
        if sType[NumberOfSensor] == "E":
            rewrite = True
        sType[NumberOfSensor] = "R0"
        TypeMenu["text"] = "Select type of sensor   -   " + sType[NumberOfSensor]
        set_active(rewrite)
    # ↑ Switch function of type of sensor. It will select type R0.


    def r1_select():
        rewrite = False
        if sType[NumberOfSensor] == "E":
            rewrite = True
        sType[NumberOfSensor] = "R1"
        TypeMenu["text"] = "Select type of sensor   -   " + sType[NumberOfSensor]
        set_active(rewrite)
        # ↑ Switch function of type of sensor. It will select type R1.


    def r2_select():
        rewrite = False
        if sType[NumberOfSensor] == "E":
            rewrite = True
        sType[NumberOfSensor] = "R2"
        TypeMenu["text"] = "Select type of sensor   -   " + sType[NumberOfSensor]
        set_active(rewrite)
        # ↑ Switch function of type of sensor. It will select type R2.


    def r3_select():
        rewrite = False
        if sType[NumberOfSensor] == "E":
            rewrite = True
        sType[NumberOfSensor] = "R3"
        TypeMenu["text"] = "Select type of sensor   -   " + sType[NumberOfSensor]
        set_active(rewrite)
        # ↑ Switch function of type of sensor. It will select type R3.


    def r4_select():
        rewrite = False
        if sType[NumberOfSensor] == "E":
            rewrite = True
        sType[NumberOfSensor] = "R4"
        TypeMenu["text"] = "Select type of sensor   -   " + sType[NumberOfSensor]
        set_active(rewrite)
    # ↑ Switch function of type of sensor. It will select type R4.


    def r5_select():
        rewrite = False
        if sType[NumberOfSensor] == "E":
            rewrite = True
        sType[NumberOfSensor] = "R5"
        TypeMenu["text"] = "Select type of sensor   -   " + sType[NumberOfSensor]
        set_active(rewrite)
        # ↑ Switch function of type of sensor. It will select type R5.


    def b_select():
        rewrite = False
        if sType[NumberOfSensor] == "E":
            rewrite = True
        sType[NumberOfSensor] = "B"
        TypeMenu["text"] = "Select type of sensor   -   " + sType[NumberOfSensor]
        CheckP["state"] = "disabled"
        CheckM["state"] = "active"
        CheckS["state"] = "active"
        ProductType["state"] = "normal"
        SensorBatch["state"] = "normal"
        SensorWafer["state"] = "normal"
        NameOfSensor["state"] = "normal"
        SensorComments["state"] = "normal"
        SensorRunNumber["state"] = "normal"
        CheckP.deselect()
        if rewrite:
            ProductType.insert(0, productType[NumberOfSensor])
            SensorBatch.insert(0, sensorBatch[NumberOfSensor])
            SensorWafer.insert(0, sensorWafer[NumberOfSensor])
            if nameSensor[NumberOfSensor] == "":
                NameOfSensor.insert(0, dNameSensor[NumberOfSensor])
            else:
                NameOfSensor.insert(0, nameSensor[NumberOfSensor])
            SensorComments.insert(0, comments[NumberOfSensor])
            change_run_number(runNumber[NumberOfSensor])


    def e_select():
        sType[NumberOfSensor] = "E"
        TypeMenu["text"] = "Select type of sensor   -   empty"
        CheckP["state"] = "disabled"
        CheckM["state"] = "disabled"
        CheckS["state"] = "disabled"
        ProductType.delete(0, END)
        SensorBatch.delete(0, END)
        SensorWafer.delete(0, END)
        NameOfSensor.delete(0, END)
        SensorComments.delete(0, END)
        SensorRunNumber.delete(0, END)
        ProductType["state"] = "disabled"
        SensorBatch["state"] = "disabled"
        SensorWafer["state"] = "disabled"
        NameOfSensor["state"] = "disabled"
        SensorComments["state"] = "disabled"
        SensorRunNumber["state"] = "disabled"

    # ↑ Switch function of type of sensor. It will select empty position.
    # ↑ 7 Switches for variable 'sType'. It performing if you click to button in GUI.


    def previous_sensor():
        global NumberOfSensor
        if NumberOfSensor > 0:
            if CheckM.var.get() == 0 and CheckS.var.get() == 0 and CheckP.var.get() == 0 \
                    and sType[NumberOfSensor] != "E":
                pag.alert("You must choice at least one possibility!", "Message")
            elif NameOfSensor.get() == dNameSensor[NumberOfSensor] and sType[NumberOfSensor] != "E":
                pag.alert("You must write unique serial number of sensor!\n\n "
                          "Serial number in the config file is the same as serial number in text box.", "Message")
            elif len(NameOfSensor.get()) != 14 and (sType[NumberOfSensor] != "E" and sType[NumberOfSensor] != ""):
                pag.alert("Serial number must have 14 characters!", "Message")
            elif (sType[NumberOfSensor] != "E" and sType[NumberOfSensor] != "") and \
                    ((not SensorRunNumber.get().isdigit())
                     or int(SensorRunNumber.get()) < 1 or int(SensorRunNumber.get()) > 999):
                pag.alert("Value of run number must be number between 1 and 999!", "Message")
            elif control_run_number(cloudPath + sType[NumberOfSensor] + "\\"
                                    + NameOfSensor.get() + "\\"):
                pag.alert("This sensor has been already measured, even with same run number!", "Message")
            elif control_run_number(measurePath + sType[NumberOfSensor] + "\\"
                                    + NameOfSensor.get() + "\\"):
                pag.alert("This sensor has been already measured, even with same run number!", "Message")
            elif not control_type():
                pag.alert("There is set incorrect combination of holder and sensor types in the config file!", "Alert")
            elif sType[NumberOfSensor] == "B" and "EC" in ProductType.get():
                pag.alert("Incorrect combination of product type (end-cap) and sensor type (barrel).")
            # ↑ Conditions for actual sensor.

            elif sType[NumberOfSensor] != "":
                if CheckM.var.get() == 0 and CheckS.var.get() == 0 \
                        and sType[NumberOfSensor] != "E":
                    pag.alert("WARNING!\n\nYou have not set measuring neither scanning of sensor.", "Alert")

                if sType[NumberOfSensor] != "E":
                    productType[NumberOfSensor] = ProductType.get()
                    ProductType.delete(0, END)
                    sensorBatch[NumberOfSensor] = SensorBatch.get()
                    SensorBatch.delete(0, END)
                    _wafer = ''.join(i for i in SensorWafer.get() if i.isdigit())
                    sensorWafer[NumberOfSensor] = "{:0>5d}".format(int(_wafer))
                    SensorWafer.delete(0, END)
                    nameSensor[NumberOfSensor] = NameOfSensor.get()
                    NameOfSensor.delete(0, END)
                    comments[NumberOfSensor] = SensorComments.get()
                    SensorComments.delete(0, END)
                    runNumber[NumberOfSensor] = SensorRunNumber.get()
                    SensorRunNumber.delete(0, END)
                    # ↑ Clear textbox for new data of next sensor.
                pSensor[NumberOfSensor] = CheckP.var.get()
                if sType[NumberOfSensor] == "B":
                    pSensor[NumberOfSensor] = 0
                mSensor[NumberOfSensor] = CheckM.var.get()
                sSensor[NumberOfSensor] = CheckS.var.get()

                NumberOfSensor = NumberOfSensor - 1  # It decrease number of sensor.
                LSensor2["text"] = "  Sensor " + str(NumberOfSensor + 1)  # Edit label of number of sensor.
                LSensor3["image"] = getattr(Img, "p" + str(NumberOfSensor))
                # ↑ Set image of position of sensor on table.

                TypeMenu.menu.delete(0, END)
                if holderType[NumberOfSensor] == 1:
                    TypeMenu.menu.add_command(command=r0_select, image=Img.R0)
                    TypeMenu.menu.add_command(command=r1_select, image=Img.R1)
                    TypeMenu.menu.add_command(command=r2_select, image=Img.R2)
                elif holderType[NumberOfSensor] == 2:
                    TypeMenu.menu.add_command(command=r3_select, image=Img.R3)
                    TypeMenu.menu.add_command(command=r4_select, image=Img.R4)
                    TypeMenu.menu.add_command(command=r5_select, image=Img.R5)
                TypeMenu.menu.add_command(command=b_select, image=Img.B)
                TypeMenu.menu.add_command(command=e_select, image=Img.E)
                TypeMenu.menu.add_command(command=edit_metrology, image=Img.em)
                # ↑ Set buttons in menu.

                if sType[NumberOfSensor] == "E":
                    TypeMenu["text"] = "Select type of sensor   -   empty"
                    CheckP["state"] = "disabled"
                    CheckM["state"] = "disabled"
                    CheckS["state"] = "disabled"
                    ProductType["state"] = "disabled"
                    SensorBatch["state"] = "disabled"
                    SensorWafer["state"] = "disabled"
                    NameOfSensor["state"] = "disabled"
                    SensorComments["state"] = "disabled"
                    SensorRunNumber["state"] = "disabled"
                else:
                    TypeMenu["text"] = "Select type of sensor   -   " + sType[NumberOfSensor]
                    if sType[NumberOfSensor] != "B":
                        CheckP["state"] = "active"
                    else:
                        CheckP["state"] = "disabled"
                    CheckM["state"] = "active"
                    CheckS["state"] = "active"
                    ProductType["state"] = "normal"
                    SensorBatch["state"] = "normal"
                    SensorWafer["state"] = "normal"
                    NameOfSensor["state"] = "normal"
                    SensorComments["state"] = "normal"
                    SensorRunNumber["state"] = "normal"
                # ↑ Write label of menu according to type of sensor.

                ProductType.insert(0, productType[NumberOfSensor])
                SensorBatch.insert(0, sensorBatch[NumberOfSensor])
                SensorWafer.insert(0, sensorWafer[NumberOfSensor])
                NameOfSensor.insert(0, nameSensor[NumberOfSensor])
                SensorComments.insert(0, comments[NumberOfSensor])
                change_run_number(runNumber[NumberOfSensor])
                if mSensor[NumberOfSensor] == 1:
                    CheckM.select()
                else:
                    CheckM.deselect()
                if sSensor[NumberOfSensor] == 1:
                    CheckS.select()
                else:
                    CheckS.deselect()
                if pSensor[NumberOfSensor] == 1:
                    CheckP.select()
                    if sType[NumberOfSensor] == "B":
                        CheckP.deselect()
                else:
                    CheckP.deselect()
                # ↑ Selecting or deselecting of checkbox buttons.

            else:
                pag.alert("You must choice type of sensor.")
        else:
            pag.alert("Only sensors between 0 and 9")


    def next_sensor():
        global NumberOfSensor
        if NumberOfSensor < 8:
            if CheckM.var.get() == 0 and CheckS.var.get() == 0 and CheckP.var.get() == 0 \
                    and sType[NumberOfSensor] != "E":
                pag.alert("You must choice at least one possibility!", "Message")
            elif NameOfSensor.get() == dNameSensor[NumberOfSensor] and sType[NumberOfSensor] != "E":
                pag.alert("You must write unique serial number of sensor!\n\n "
                          "Serial number in the config file is the same as serial number in text box.", "Message")
            elif len(NameOfSensor.get()) != 14 and (sType[NumberOfSensor] != "E" and sType[NumberOfSensor] != ""):
                pag.alert("Serial number must have 14 characters!", "Message")
            elif (sType[NumberOfSensor] != "E" and sType[NumberOfSensor] != "") and \
                    ((not SensorRunNumber.get().isdigit())
                     or int(SensorRunNumber.get()) < 1 or int(SensorRunNumber.get()) > 999):
                pag.alert("Value of run number must be number between 1 and 999!", "Message")
            elif control_run_number(cloudPath + sType[NumberOfSensor] + "\\"
                                    + NameOfSensor.get() + "\\"):
                pag.alert("This sensor has been already measured, even with same run number!", "Message")
            elif control_run_number(measurePath + sType[NumberOfSensor] + "\\"
                                    + NameOfSensor.get() + "\\"):
                pag.alert("This sensor has been already measured, even with same run number!", "Message")
            elif not control_type():
                pag.alert("There is set incorrect combination of holder and sensor types in the config file!", "Alert")
            elif sType[NumberOfSensor] == "B" and "EC" in ProductType.get():
                pag.alert("Incorrect combination of product type (end-cap) and sensor type (barrel).")
            # ↑ Conditions for actual sensor.

            elif sType[NumberOfSensor] != "":
                if CheckM.var.get() == 0 and CheckS.var.get() == 0 \
                        and sType[NumberOfSensor] != "E":
                    pag.alert("WARNING!\n\nYou have not set measuring neither scanning of sensor.", "Alert")

                if sType[NumberOfSensor] != "E":
                    productType[NumberOfSensor] = ProductType.get()
                    ProductType.delete(0, END)
                    sensorBatch[NumberOfSensor] = SensorBatch.get()
                    SensorBatch.delete(0, END)
                    _wafer = ''.join(i for i in SensorWafer.get() if i.isdigit())
                    sensorWafer[NumberOfSensor] = "{:0>5d}".format(int(_wafer))
                    SensorWafer.delete(0, END)
                    nameSensor[NumberOfSensor] = NameOfSensor.get()
                    NameOfSensor.delete(0, END)
                    comments[NumberOfSensor] = SensorComments.get()
                    SensorComments.delete(0, END)
                    runNumber[NumberOfSensor] = SensorRunNumber.get()
                    SensorRunNumber.delete(0, END)
                    # ↑ Clear textbox for new data of next sensor.
                pSensor[NumberOfSensor] = CheckP.var.get()
                if sType[NumberOfSensor] == "B":
                    pSensor[NumberOfSensor] = 0
                mSensor[NumberOfSensor] = CheckM.var.get()
                sSensor[NumberOfSensor] = CheckS.var.get()

                NumberOfSensor = NumberOfSensor + 1  # It increase number of sensor.
                LSensor2["text"] = "  Sensor " + str(NumberOfSensor + 1)  # Edit label of number of sensor.
                LSensor3["image"] = getattr(Img, "p" + str(NumberOfSensor))
                # ↑ Set image of position of sensor on table.

                TypeMenu.menu.delete(0, END)
                if holderType[NumberOfSensor] == 1:
                    TypeMenu.menu.add_command(command=r0_select, image=Img.R0)
                    TypeMenu.menu.add_command(command=r1_select, image=Img.R1)
                    TypeMenu.menu.add_command(command=r2_select, image=Img.R2)
                elif holderType[NumberOfSensor] == 2:
                    TypeMenu.menu.add_command(command=r3_select, image=Img.R3)
                    TypeMenu.menu.add_command(command=r4_select, image=Img.R4)
                    TypeMenu.menu.add_command(command=r5_select, image=Img.R5)
                TypeMenu.menu.add_command(command=b_select, image=Img.B)
                TypeMenu.menu.add_command(command=e_select, image=Img.E)
                TypeMenu.menu.add_command(command=edit_metrology, image=Img.em)
                # ↑ Set buttons in menu.

                if sType[NumberOfSensor] == "E" or sType[NumberOfSensor] == "":
                    if sType[NumberOfSensor] == "E":
                        TypeMenu["text"] = "Select type of sensor   -   empty"
                    else:
                        TypeMenu["text"] = "Select type of sensor"
                    CheckP["state"] = "disabled"
                    CheckM["state"] = "disabled"
                    CheckS["state"] = "disabled"
                    ProductType["state"] = "disabled"
                    SensorBatch["state"] = "disabled"
                    SensorWafer["state"] = "disabled"
                    NameOfSensor["state"] = "disabled"
                    SensorComments["state"] = "disabled"
                    SensorRunNumber["state"] = "disabled"
                else:
                    TypeMenu["text"] = "Select type of sensor   -   " + sType[NumberOfSensor]
                    if sType[NumberOfSensor] != "B":
                        CheckP["state"] = "active"
                    else:
                        CheckP["state"] = "disabled"
                    CheckM["state"] = "active"
                    CheckS["state"] = "active"
                    ProductType["state"] = "normal"
                    SensorBatch["state"] = "normal"
                    SensorWafer["state"] = "normal"
                    NameOfSensor["state"] = "normal"
                    SensorComments["state"] = "normal"
                    SensorRunNumber["state"] = "normal"
                # ↑ Write label of menu according to type of sensor.

                ProductType.insert(0, productType[NumberOfSensor])
                SensorBatch.insert(0, sensorBatch[NumberOfSensor])
                SensorWafer.insert(0, sensorWafer[NumberOfSensor])
                if nameSensor[NumberOfSensor] == "":
                    NameOfSensor.insert(0, dNameSensor[NumberOfSensor])
                else:
                    NameOfSensor.insert(0, nameSensor[NumberOfSensor])
                SensorComments.insert(0, comments[NumberOfSensor])
                change_run_number(runNumber[NumberOfSensor])
                # ↑ Write label of menu according to type of sensor.

                if mSensor[NumberOfSensor] == 1:
                    CheckM.select()
                else:
                    CheckM.deselect()
                if sSensor[NumberOfSensor] == 1:
                    CheckS.select()
                else:
                    CheckS.deselect()
                if pSensor[NumberOfSensor] == 1:
                    CheckP.select()
                    if sType[NumberOfSensor] == "B":
                        CheckP.deselect()
                else:
                    CheckP.deselect()
                # ↑ Selecting or deselecting of checkbox buttons.

            else:
                pag.alert("You must choice type of sensor.")
        else:
            pag.alert("Only sensors between 0 and 9")


    def back():
        global NumberOfSensor

        if if_bad_pos():
            change_sensor(NumberOfSensor)
            if not control_next_start():
                start()
            else:
                pre_start()
        else:
            frameTop.pack_forget()
            ButtonBack.pack_forget()
            ButtonPrevious.pack(side=LEFT)
            LSensor2.pack(side=RIGHT)
            LSensor3.pack(side=LEFT)
            ButtonNext.pack(side=LEFT)
            ButtonStart["text"] = "Start measuring"
            ButtonStart["bg"] = "light gray"
            ButtonStart["fg"] = "black"
            ButtonStart["activebackground"] = "dark red"
            ButtonStart["command"] = pre_start

            NumberOfSensor = 0
            LSensor2["text"] = "  Sensor " + str(NumberOfSensor + 1)  # Edit label of number of sensor.
            LSensor3["image"] = getattr(Img, "p" + str(NumberOfSensor))
            # ↑ Set image of position of sensor on table.

            TypeMenu.menu.delete(0, END)
            if holderType[NumberOfSensor] == 1:
                TypeMenu.menu.add_command(command=r0_select, image=Img.R0)
                TypeMenu.menu.add_command(command=r1_select, image=Img.R1)
                TypeMenu.menu.add_command(command=r2_select, image=Img.R2)
            elif holderType[NumberOfSensor] == 2:
                TypeMenu.menu.add_command(command=r3_select, image=Img.R3)
                TypeMenu.menu.add_command(command=r4_select, image=Img.R4)
                TypeMenu.menu.add_command(command=r5_select, image=Img.R5)
            TypeMenu.menu.add_command(command=b_select, image=Img.B)
            TypeMenu.menu.add_command(command=e_select, image=Img.E)
            TypeMenu.menu.add_command(command=edit_metrology, image=Img.em)
            # ↑ Set buttons in menu.

            if sType[NumberOfSensor] == "E" or sType[NumberOfSensor] == "":
                if sType[NumberOfSensor] == "E":
                    TypeMenu["text"] = "Select type of sensor   -   empty"
                else:
                    TypeMenu["text"] = "Select type of sensor"
                CheckP["state"] = "disabled"
                CheckM["state"] = "disabled"
                CheckS["state"] = "disabled"
                ProductType["state"] = "disabled"
                SensorBatch["state"] = "disabled"
                SensorWafer["state"] = "disabled"
                NameOfSensor["state"] = "disabled"
                SensorComments["state"] = "disabled"
                SensorRunNumber["state"] = "disabled"
            else:
                TypeMenu["text"] = "Select type of sensor   -   " + sType[NumberOfSensor]
                if sType[NumberOfSensor] != "B":
                    CheckP["state"] = "active"
                else:
                    CheckP["state"] = "disabled"
                CheckM["state"] = "active"
                CheckS["state"] = "active"
                ProductType["state"] = "normal"
                SensorBatch["state"] = "normal"
                SensorWafer["state"] = "normal"
                NameOfSensor["state"] = "normal"
                SensorComments["state"] = "normal"
                SensorRunNumber["state"] = "normal"
            # ↑ Write label of menu according to type of sensor.

            ProductType.delete(0, END)
            SensorBatch.delete(0, END)
            SensorWafer.delete(0, END)
            NameOfSensor.delete(0, END)
            SensorComments.delete(0, END)
            SensorRunNumber.delete(0, END)
            # ↑ Clear textbox for new data of next sensor.
            ProductType.insert(0, productType[NumberOfSensor])
            SensorBatch.insert(0, sensorBatch[NumberOfSensor])
            SensorWafer.insert(0, sensorWafer[NumberOfSensor])
            if nameSensor[NumberOfSensor] == "":
                NameOfSensor.insert(0, dNameSensor[NumberOfSensor])
            else:
                NameOfSensor.insert(0, nameSensor[NumberOfSensor])
            SensorComments.insert(0, comments[NumberOfSensor])
            change_run_number(runNumber[NumberOfSensor])
            # ↑ Write label of menu according to type of sensor.

            if mSensor[NumberOfSensor] == 1:
                CheckM.select()
            else:
                CheckM.deselect()
            if sSensor[NumberOfSensor] == 1:
                CheckS.select()
            else:
                CheckS.deselect()
            if pSensor[NumberOfSensor] == 1:
                CheckP.select()
                if sType[NumberOfSensor] == "B":
                    CheckP.deselect()
            else:
                CheckP.deselect()
            # ↑ Selecting or deselecting of checkbox buttons.


    def confirm():
        global NumberOfSensor
        if if_bad_pos():
            change_sensor(NumberOfSensor)
            if not control_next_start():
                start()
            else:
                pre_start()
        elif CheckM.var.get() == 0 and CheckS.var.get() == 0 and CheckP.var.get() == 0 \
                and sType[NumberOfSensor] != "E":
            pag.alert("You must choice at least one possibility!", "Message")
        elif NameOfSensor.get() == dNameSensor[NumberOfSensor] and sType[NumberOfSensor] != "E":
            pag.alert("You must write unique serial number of sensor!\n\n "
                      "Serial number in the config file is the same as serial number in text box.", "Message")
        elif len(NameOfSensor.get()) != 14 and (sType[NumberOfSensor] != "E" and sType[NumberOfSensor] != ""):
            pag.alert("Serial number must have 14 characters!", "Message")
        elif (sType[NumberOfSensor] != "E" and sType[NumberOfSensor] != "") and ((not SensorRunNumber.get().isdigit())
                                                                                 or int(SensorRunNumber.get()) < 1
                                                                                 or int(SensorRunNumber.get()) > 999):
            pag.alert("Value of run number must be number between 1 and 999!", "Message")
        elif control_run_number(cloudPath + sType[NumberOfSensor] + "\\"
                                + NameOfSensor.get() + "\\"):
            pag.alert("This sensor has been already measured, even with same run number!", "Message")
        elif control_run_number(measurePath + sType[NumberOfSensor] + "\\"
                                + NameOfSensor.get() + "\\"):
            pag.alert("This sensor has been already measured, even with same run number!", "Message")
        elif sType[NumberOfSensor] == "B" and "EC" in ProductType.get():
            pag.alert("Incorrect combination of product type (end-cap) and sensor type (barrel).")
        elif ((not os.path.exists(measurePath + "Routines\\" + str(NumberOfSensor + 1) + "_right.RTN")) and
                CheckM.var.get() == 1 and CheckP.var.get() == 0) or \
                ((not os.path.exists(measurePath + "Routines\\" + str(NumberOfSensor + 1) + "_left.RTN"))
                 and CheckP.var.get() == 0):
            pag.alert("There are no routine for position of the right bottom corner of the sensor!\n"
                      "You must create it first to measure planarity of the sensor manually.", "Message")
        # ↑ Conditions for actual sensor.
        else:
            if CheckM.var.get() == 0 and CheckS.var.get() == 0 \
                    and sType[NumberOfSensor] != "E":
                pag.alert("WARNING!\n\nYou have not set measuring neither scanning of sensor.", "Alert")
            if CheckP.var.get() == 0:
                routine_l_age = os.stat(measurePath + "Routines\\" + str(NumberOfSensor + 1) + "_left.RTN")
                routine_r_age = os.stat(measurePath + "Routines\\" + str(NumberOfSensor + 1) + "_right.RTN")
                if (time.time() - routine_l_age.st_mtime > 60*60) or (time.time() - routine_r_age.st_mtime > 60*60):
                    pag.alert("WARNING!\n\nRoutines with position of the current sensor are suspiciously old.\n"
                              "Check it, please. ONLY then confirm this alert.", "Alert")
            productType[NumberOfSensor] = ProductType.get()
            ProductType.delete(0, END)
            sensorBatch[NumberOfSensor] = SensorBatch.get()
            SensorBatch.delete(0, END)
            _wafer = ''.join(i for i in SensorWafer.get() if i.isdigit())
            sensorWafer[NumberOfSensor] = "{:0>5d}".format(int(_wafer))
            SensorWafer.delete(0, END)
            nameSensor[NumberOfSensor] = NameOfSensor.get()
            NameOfSensor.delete(0, END)
            comments[NumberOfSensor] = SensorComments.get()
            SensorComments.delete(0, END)
            runNumber[NumberOfSensor] = SensorRunNumber.get()
            SensorRunNumber.delete(0, END)
            # ↑ Clear textbox for new data of next sensor.
            pSensor[NumberOfSensor] = CheckP.var.get()
            if sType[NumberOfSensor] == "B":
                pSensor[NumberOfSensor] = 0
            mSensor[NumberOfSensor] = CheckM.var.get()
            sSensor[NumberOfSensor] = CheckS.var.get()

            NumberOfSensor += 1
            while NumberOfSensor < 9 and ((sType[NumberOfSensor] == "" or sType[NumberOfSensor] == "E")
                                          or (nameSensor[NumberOfSensor] == ""
                                              or nameSensor[NumberOfSensor] == dNameSensor[NumberOfSensor])):
                NumberOfSensor += 1

            if NumberOfSensor < 9:
                LSensor0left["image"] = getattr(Img, "p" + str(NumberOfSensor) + "L")
                LSensor0right["image"] = getattr(Img, sType[NumberOfSensor] + "L")
                TypeMenu.menu.delete(0, END)
                if holderType[NumberOfSensor] == 1:
                    TypeMenu.menu.add_command(command=r0_select, image=Img.R0)
                    TypeMenu.menu.add_command(command=r1_select, image=Img.R1)
                    TypeMenu.menu.add_command(command=r2_select, image=Img.R2)
                elif holderType[NumberOfSensor] == 2:
                    TypeMenu.menu.add_command(command=r3_select, image=Img.R3)
                    TypeMenu.menu.add_command(command=r4_select, image=Img.R4)
                    TypeMenu.menu.add_command(command=r5_select, image=Img.R5)
                TypeMenu.menu.add_command(command=b_select, image=Img.B)
                TypeMenu.menu.add_command(command=e_select, image=Img.E)
                # ↑ Set buttons in menu.

                if sType[NumberOfSensor] == "E" or sType[NumberOfSensor] == "":
                    if sType[NumberOfSensor] == "E":
                        TypeMenu["text"] = "Select type of sensor   -   empty"
                    else:
                        TypeMenu["text"] = "Select type of sensor"
                    CheckP["state"] = "disabled"
                    CheckM["state"] = "disabled"
                    CheckS["state"] = "disabled"
                    ProductType["state"] = "disabled"
                    SensorBatch["state"] = "disabled"
                    SensorWafer["state"] = "disabled"
                    NameOfSensor["state"] = "disabled"
                    SensorComments["state"] = "disabled"
                    SensorRunNumber["state"] = "disabled"
                else:
                    TypeMenu["text"] = "Select type of sensor   -   " + sType[NumberOfSensor]
                    if sType[NumberOfSensor] != "B":
                        CheckP["state"] = "active"
                    else:
                        CheckP["state"] = "disabled"
                    CheckM["state"] = "active"
                    CheckS["state"] = "active"
                    ProductType["state"] = "normal"
                    SensorBatch["state"] = "normal"
                    SensorWafer["state"] = "normal"
                    NameOfSensor["state"] = "normal"
                    SensorComments["state"] = "normal"
                    SensorRunNumber["state"] = "normal"
                # ↑ Write label of menu according to type of sensor.

                ProductType.insert(0, productType[NumberOfSensor])
                SensorBatch.insert(0, sensorBatch[NumberOfSensor])
                SensorWafer.insert(0, sensorWafer[NumberOfSensor])
                if nameSensor[NumberOfSensor] == "":
                    NameOfSensor.insert(0, dNameSensor[NumberOfSensor])
                else:
                    NameOfSensor.insert(0, nameSensor[NumberOfSensor])
                SensorComments.insert(0, comments[NumberOfSensor])
                change_run_number(runNumber[NumberOfSensor])
                # ↑ Write label of menu according to type of sensor.

                if mSensor[NumberOfSensor] == 1:
                    CheckM.select()
                else:
                    CheckM.deselect()
                if sSensor[NumberOfSensor] == 1:
                    CheckS.select()
                else:
                    CheckS.deselect()
                if pSensor[NumberOfSensor] == 1:
                    CheckP.select()
                    if sType[NumberOfSensor] == "B":
                        CheckP.deselect()
                else:
                    CheckP.deselect()
                # ↑ Selecting or deselecting of checkbox buttons.

            else:
                frameTop.pack_forget()
                ButtonBack.pack_forget()
                ButtonPrevious.pack(side=LEFT)
                LSensor2.pack(side=RIGHT)
                LSensor3.pack(side=LEFT)
                ButtonNext.pack(side=LEFT)
                ButtonStart["text"] = "Start measuring"
                ButtonStart["bg"] = "light gray"
                ButtonStart["fg"] = "black"
                ButtonStart["activebackground"] = "dark red"
                ButtonStart["command"] = pre_start

                NumberOfSensor = 0
                LSensor2["text"] = "  Sensor " + str(NumberOfSensor + 1)  # Edit label of number of sensor.
                TypeMenu.menu.delete(0, END)
                if holderType[NumberOfSensor] == 1:
                    TypeMenu.menu.add_command(command=r0_select, image=Img.R0)
                    TypeMenu.menu.add_command(command=r1_select, image=Img.R1)
                    TypeMenu.menu.add_command(command=r2_select, image=Img.R2)
                elif holderType[NumberOfSensor] == 2:
                    TypeMenu.menu.add_command(command=r3_select, image=Img.R3)
                    TypeMenu.menu.add_command(command=r4_select, image=Img.R4)
                    TypeMenu.menu.add_command(command=r5_select, image=Img.R5)
                TypeMenu.menu.add_command(command=b_select, image=Img.B)
                TypeMenu.menu.add_command(command=e_select, image=Img.E)
                TypeMenu.menu.add_command(command=edit_metrology, image=Img.em)
                # ↑ Set buttons in menu.

                if sType[NumberOfSensor] == "E" or sType[NumberOfSensor] == "":
                    if sType[NumberOfSensor] == "E":
                        TypeMenu["text"] = "Select type of sensor   -   empty"
                    else:
                        TypeMenu["text"] = "Select type of sensor"
                    CheckP["state"] = "disabled"
                    CheckM["state"] = "disabled"
                    CheckS["state"] = "disabled"
                    ProductType["state"] = "disabled"
                    SensorBatch["state"] = "disabled"
                    SensorWafer["state"] = "disabled"
                    NameOfSensor["state"] = "disabled"
                    SensorComments["state"] = "disabled"
                    SensorRunNumber["state"] = "disabled"
                else:
                    TypeMenu["text"] = "Select type of sensor   -   " + sType[NumberOfSensor]
                    if sType[NumberOfSensor] != "B":
                        CheckP["state"] = "active"
                    else:
                        CheckP["state"] = "disabled"
                    CheckM["state"] = "active"
                    CheckS["state"] = "active"
                    ProductType["state"] = "normal"
                    SensorBatch["state"] = "normal"
                    SensorWafer["state"] = "normal"
                    NameOfSensor["state"] = "normal"
                    SensorComments["state"] = "normal"
                    SensorRunNumber["state"] = "normal"
                # ↑ Write label of menu according to type of sensor.

                LSensor3["image"] = getattr(Img, "p" + str(NumberOfSensor))
                ProductType.insert(0, productType[NumberOfSensor])
                SensorBatch.insert(0, sensorBatch[NumberOfSensor])
                SensorWafer.insert(0, sensorWafer[NumberOfSensor])
                if nameSensor[NumberOfSensor] == "":
                    NameOfSensor.insert(0, dNameSensor[NumberOfSensor])
                else:
                    NameOfSensor.insert(0, nameSensor[NumberOfSensor])
                SensorComments.insert(0, comments[NumberOfSensor])
                change_run_number(runNumber[NumberOfSensor])
                # ↑ Write label of menu according to type of sensor.

                if mSensor[NumberOfSensor] == 1:
                    CheckM.select()
                else:
                    CheckM.deselect()
                if sSensor[NumberOfSensor] == 1:
                    CheckS.select()
                else:
                    CheckS.deselect()
                if pSensor[NumberOfSensor] == 1:
                    CheckP.select()
                    if sType[NumberOfSensor] == "B":
                        CheckP.deselect()
                else:
                    CheckP.deselect()
                # ↑ Selecting or deselecting of checkbox buttons.

                control_database()

                start()  # Start program.
                if if_bad_pos():
                    if NumberOfSensor < 9:
                        pre_start()
                    else:
                        start()
                #  ↑ opening GUI for updating setting after APS.


    def pre_start():
        global running
        global NumberOfSensor
        running += 1
        check_running()

        if CheckM.var.get() == 0 and CheckS.var.get() == 0 and CheckP.var.get() == 0 \
                and sType[NumberOfSensor] != "E":
            pag.alert("You must choice at least one possibility!", "Message")
        elif sType[NumberOfSensor] == "":
            pag.alert("You must choice type of sensor!", "Message")
        elif NameOfSensor.get() == dNameSensor[NumberOfSensor] and sType[NumberOfSensor] != "E":
            pag.alert("You must write unique serial number of sensor!\n\n "
                      "Serial number in the config file is the same as serial number in text box.", "Message")
        elif len(NameOfSensor.get()) != 14 and (sType[NumberOfSensor] != "E" and sType[NumberOfSensor] != ""):
            pag.alert("Serial number must have 14 characters!", "Message")
        elif (sType[NumberOfSensor] != "E" and sType[NumberOfSensor] != "") and ((not SensorRunNumber.get().isdigit())
                                                                                 or int(SensorRunNumber.get()) < 1
                                                                                 or int(SensorRunNumber.get()) > 999):
            pag.alert("Value of run number must be number between 1 and 999!", "Message")
        elif control_run_number(cloudPath + sType[NumberOfSensor] + "\\"
                                + NameOfSensor.get() + "\\"):
            pag.alert("This sensor has been already measured, even with same run number!", "Message")
        elif control_run_number(measurePath + sType[NumberOfSensor] + "\\"
                                + NameOfSensor.get() + "\\"):
            pag.alert("This sensor has been already measured, even with same run number!", "Message")
        elif not control_type():
            pag.alert("There is set incorrect combination of holder and sensor types in the config file!", "Alert")
        elif sType[NumberOfSensor] == "B" and "EC" in ProductType.get():
            pag.alert("Incorrect combination of product type (end-cap) and sensor type (barrel).")
        # ↑ Conditions for actual sensor.
        else:
            if CheckM.var.get() == 0 and CheckS.var.get() == 0 \
                    and sType[NumberOfSensor] != "E":
                pag.alert("WARNING!\n\nYou have not set measuring neither scanning of sensor.", "Alert")

            productType[NumberOfSensor] = ProductType.get()
            ProductType.delete(0, END)
            sensorBatch[NumberOfSensor] = SensorBatch.get()
            SensorBatch.delete(0, END)
            _wafer = ''.join(i for i in SensorWafer.get() if i.isdigit())
            sensorWafer[NumberOfSensor] = "{:0>5d}".format(int(_wafer))
            SensorWafer.delete(0, END)
            nameSensor[NumberOfSensor] = NameOfSensor.get()
            NameOfSensor.delete(0, END)
            comments[NumberOfSensor] = SensorComments.get()
            SensorComments.delete(0, END)
            runNumber[NumberOfSensor] = SensorRunNumber.get()
            SensorRunNumber.delete(0, END)
            # ↑ Clear textbox for new data of next sensor.
            pSensor[NumberOfSensor] = CheckP.var.get()
            if sType[NumberOfSensor] == "B":
                pSensor[NumberOfSensor] = 0
            mSensor[NumberOfSensor] = CheckM.var.get()
            sSensor[NumberOfSensor] = CheckS.var.get()

            NumberOfSensor = 0
            while (sType[NumberOfSensor] == "" or sType[NumberOfSensor] == "E")\
                    or (nameSensor[NumberOfSensor] == ""
                        or nameSensor[NumberOfSensor] == dNameSensor[NumberOfSensor]):
                NumberOfSensor += 1
                if NumberOfSensor >= 9:
                    break
            if NumberOfSensor >= 9:
                pag.alert("No sensors have been set!")
                NumberOfSensor = 0
            else:
                frameTop.pack(side=TOP, fill=BOTH)
                ButtonBack.pack(side=LEFT, fill=BOTH)
                LSensor0left["image"] = getattr(Img, "p" + str(NumberOfSensor) + "L")
                LSensor0right["image"] = getattr(Img, sType[NumberOfSensor] + "L")

                TypeMenu.menu.delete(0, END)
                if holderType[NumberOfSensor] == 1:
                    TypeMenu.menu.add_command(command=r0_select, image=Img.R0)
                    TypeMenu.menu.add_command(command=r1_select, image=Img.R1)
                    TypeMenu.menu.add_command(command=r2_select, image=Img.R2)
                elif holderType[NumberOfSensor] == 2:
                    TypeMenu.menu.add_command(command=r3_select, image=Img.R3)
                    TypeMenu.menu.add_command(command=r4_select, image=Img.R4)
                    TypeMenu.menu.add_command(command=r5_select, image=Img.R5)
                TypeMenu.menu.add_command(command=b_select, image=Img.B)
                TypeMenu.menu.add_command(command=e_select, image=Img.E)
                TypeMenu.menu.add_command(command=edit_metrology, image=Img.em)
                # ↑ Set buttons in menu.

                if sType[NumberOfSensor] == "E" or sType[NumberOfSensor] == "":
                    if sType[NumberOfSensor] == "E":
                        TypeMenu["text"] = "Select type of sensor   -   empty"
                    else:
                        TypeMenu["text"] = "Select type of sensor"
                    CheckP["state"] = "disabled"
                    CheckM["state"] = "disabled"
                    CheckS["state"] = "disabled"
                    ProductType["state"] = "disabled"
                    SensorBatch["state"] = "disabled"
                    SensorWafer["state"] = "disabled"
                    NameOfSensor["state"] = "disabled"
                    SensorComments["state"] = "disabled"
                    SensorRunNumber["state"] = "disabled"
                else:
                    TypeMenu["text"] = "Select type of sensor   -   " + sType[NumberOfSensor]
                    if sType[NumberOfSensor] != "B":
                        CheckP["state"] = "active"
                    else:
                        CheckP["state"] = "disabled"
                    CheckM["state"] = "active"
                    CheckS["state"] = "active"
                    ProductType["state"] = "normal"
                    SensorBatch["state"] = "normal"
                    SensorWafer["state"] = "normal"
                    NameOfSensor["state"] = "normal"
                    SensorComments["state"] = "normal"
                    SensorRunNumber["state"] = "normal"
                # ↑ Write label of menu according to type of sensor.

                ProductType.insert(0, productType[NumberOfSensor])
                SensorBatch.insert(0, sensorBatch[NumberOfSensor])
                SensorWafer.insert(0, sensorWafer[NumberOfSensor])
                if nameSensor[NumberOfSensor] == "":
                    NameOfSensor.insert(0, dNameSensor[NumberOfSensor])
                else:
                    NameOfSensor.insert(0, nameSensor[NumberOfSensor])
                SensorComments.insert(0, comments[NumberOfSensor])
                change_run_number(runNumber[NumberOfSensor])
                # ↑ Write label of menu according to type of sensor.

                if mSensor[NumberOfSensor] == 1:
                    CheckM.select()
                else:
                    CheckM.deselect()
                if sSensor[NumberOfSensor] == 1:
                    CheckS.select()
                else:
                    CheckS.deselect()
                if pSensor[NumberOfSensor] == 1:
                    CheckP.select()
                    if sType[NumberOfSensor] == "B":
                        CheckP.deselect()
                else:
                    CheckP.deselect()
                    # ↑ Selecting or deselecting of checkbox buttons.

                ButtonNext.pack_forget()
                ButtonPrevious.pack_forget()
                LSensor2.pack_forget()
                LSensor3.pack_forget()
                ButtonStart["text"] = "CONFIRM SENSOR SETTINGS"
                ButtonStart["bg"] = "dark red"
                ButtonStart["fg"] = "white"
                ButtonStart["activebackground"] = "light gray"
                ButtonStart["activeforeground"] = "black"
                ButtonStart["command"] = confirm


    checkP = IntVar()
    checkM = IntVar()
    checkS = IntVar()

    frameTop = tkinter.Frame(SMS)
    frameDown = tkinter.Frame(SMS)

    LSensor0left = tkinter.Label(frameTop)
    LSensor0right = tkinter.Label(frameTop)

    frameT = tkinter.Frame(frameDown)
    frameD = tkinter.Frame(frameDown)
    frameTT = tkinter.Frame(frameT)
    frameTB = tkinter.Frame(frameT)
    frameTTT = tkinter.Frame(frameTT)
    frameTTB = tkinter.Frame(frameTT)
    frameTBT = tkinter.Frame(frameTB)
    frameTBB = tkinter.Frame(frameTB)
    frameTTTT = tkinter.Frame(frameTTT)
    frameTTTB = tkinter.Frame(frameTTT)
    frameTTBT = tkinter.Frame(frameTTB)
    frameTTBB = tkinter.Frame(frameTTB)
    frameTBTT = tkinter.Frame(frameTBT)
    frameTBTTT = tkinter.Frame(frameTBTT)
    frameTBTTB = tkinter.Frame(frameTBTT)
    frameTBTTBT = tkinter.Frame(frameTBTTB)
    frameTBTTBB = tkinter.Frame(frameTBTTB)
    frameTBTB = tkinter.Frame(frameTBT, bg="light gray", height=7, width=400)
    frameTBBT = tkinter.Frame(frameTBB)
    frameTBBB = tkinter.Frame(frameTBB, bg="light gray", height=7, width=400)
    LProductType = tkinter.Label(frameTTTT, text="Product type: ", height=1, width=20)
    ProductType = tkinter.Entry(frameTTTT, bd=3, width=41)
    LSensorBatch = tkinter.Label(frameTTTB, text="Sensor batch: ", height=1, width=20)
    SensorBatch = tkinter.Entry(frameTTTB, bd=3, width=41)
    LSensorWafer = tkinter.Label(frameTTBT, text="Sensor wafer: ", height=1, width=20)
    SensorWafer = tkinter.Entry(frameTTBT, bd=3, width=41)
    LSensorSerial = tkinter.Label(frameTBTTT, text="Serial number: ", height=1, width=21)
    NameOfSensor = tkinter.Entry(frameTBTTT, bd=3, width=41)
    LComments = tkinter.Label(frameTBTTBT, text="Comments: ", height=1, width=19)
    SensorComments = tkinter.Entry(frameTBTTBT, bd=3, width=41)
    LRunNumber = tkinter.Label(frameTBTTBB, text="Run number:   ", height=1, width=21)
    SensorRunNumber = tkinter.Spinbox(frameTBTTBB, from_=1, to_=999, width=3, bd=3)
    CheckP = tkinter.Checkbutton(frameTBBT, text="Automatic position system", width=20, variable=checkP)
    CheckP.var = checkP
    CheckM = tkinter.Checkbutton(frameTBBT, text="Measuring", width=10, variable=checkM)
    CheckM.var = checkM
    CheckS = tkinter.Checkbutton(frameTBBT, text="Scanning", width=10, variable=checkS)
    CheckS.var = checkS

    frameD1 = tkinter.Frame(frameD)
    frameD2 = tkinter.Frame(frameD)
    frameD3 = tkinter.Frame(frameD)
    ButtonPrevious = tkinter.Button(frameD1, text="Previous sensor", command=previous_sensor, bg="light gray",
                                    activebackground="gray", activeforeground="white")
    LSensor2 = tkinter.Label(frameD1, text="  Sensor 1")
    LSensor3 = tkinter.Label(frameD, image=Img.p0)
    ButtonNext = tkinter.Button(frameD, text=" Next sensor ", command=next_sensor, bg="light gray",
                                activebackground="gray", activeforeground="white")
    ButtonStart = tkinter.Button(frameD3, text="Start measuring", command=pre_start, bg="light gray",
                                 activebackground="dark red", activeforeground="white")
    ButtonBack = tkinter.Button(frameD1, text="Back to settings", command=back, bg="light gray",
                                activebackground="gray", activeforeground="white")
    # ↑ Set properties of window and objects(buttons, menu, etc...).

    if sType[0] == "E" or sType[0] == "":
        if sType[0] == "E":
            TypeMenu = tkinter.Menubutton(SMS, text="Select type of sensor   -   empty", relief=SUNKEN,
                                          bg="light gray", activebackground="gray", activeforeground="white")
        else:
            TypeMenu = tkinter.Menubutton(SMS, text="Select type of sensor", relief=SUNKEN,
                                          bg="light gray", activebackground="gray", activeforeground="white")
        CheckP["state"] = "disabled"
        CheckM["state"] = "disabled"
        CheckS["state"] = "disabled"
        ProductType["state"] = "disabled"
        SensorBatch["state"] = "disabled"
        SensorWafer["state"] = "disabled"
        NameOfSensor["state"] = "disabled"
        SensorComments["state"] = "disabled"
        SensorRunNumber["state"] = "disabled"
    else:
        TypeMenu = tkinter.Menubutton(SMS, text="Select type of sensor   -   " + str(sType[0]), relief=SUNKEN,
                                      bg="light gray", activebackground="gray", activeforeground="white")
        if sType[0] != "B":
            CheckP["state"] = "active"
        else:
            CheckP["state"] = "disabled"
        CheckM["state"] = "active"
        CheckS["state"] = "active"
        ProductType["state"] = "normal"
        SensorBatch["state"] = "normal"
        SensorWafer["state"] = "normal"
        NameOfSensor["state"] = "normal"
        SensorComments["state"] = "normal"
        SensorRunNumber["state"] = "normal"
    # ↑ Write label of menu according to type of sensor.
    # Conditionals for insert title on menu.

    progress.pack_forget()
    TypeMenu.grid()
    TypeMenu.menu = Menu(TypeMenu, tearoff=1)
    TypeMenu["menu"] = TypeMenu.menu
    NameOfSensor.bind("<Leave>", sensor_database)
    NameOfSensor.bind("<Enter>", name_of_sensor_enter_cursor)

    if holderType[0] == 1:
        TypeMenu.menu.add_command(command=r0_select, image=Img.R0)
        TypeMenu.menu.add_command(command=r1_select, image=Img.R1)
        TypeMenu.menu.add_command(command=r2_select, image=Img.R2)
    elif holderType[0] == 2:
        TypeMenu.menu.add_command(command=r3_select, image=Img.R3)
        TypeMenu.menu.add_command(command=r4_select, image=Img.R4)
        TypeMenu.menu.add_command(command=r5_select, image=Img.R5)
    TypeMenu.menu.add_command(command=b_select, image=Img.B)
    TypeMenu.menu.add_command(command=e_select, image=Img.E)
    TypeMenu.menu.add_command(command=edit_metrology, image=Img.em)
    # Insert images to submenu.

    if mSensor[0] == 1:
        CheckM.select()
    if sSensor[0] == 1:
        CheckS.select()
    if pSensor[0] == 1:
        CheckP.select()
        if sType[0] == "B":
            CheckP.deselect()
    # ↑ Set Checkbox to correct position.

    ProductType.insert(0, productType[0])
    SensorBatch.insert(0, sensorBatch[0])
    SensorWafer.insert(0, sensorWafer[0])
    NameOfSensor.insert(0, dNameSensor[0])
    SensorComments.insert(0, comments[0])
    change_run_number(runNumber[0])
    # Write default name of first sensor to textbox.

    TypeMenu.pack(side=TOP, fill=BOTH)

    frameDown.pack(side=BOTTOM, fill=BOTH)
    LSensor0left.pack(side=LEFT, fill=BOTH)
    LSensor0right.pack(side=RIGHT, fill=BOTH)

    frameT.pack(side=TOP, fill=BOTH)
    frameTT.pack(side=TOP, fill=BOTH)
    frameTB.pack(side=BOTTOM, fill=BOTH)
    frameTTT.pack(side=TOP, fill=BOTH)
    frameTTB.pack(side=BOTTOM, fill=BOTH)
    frameTBT.pack(side=TOP, fill=BOTH)
    frameTBB.pack(side=BOTTOM, fill=BOTH)
    frameTTTT.pack(side=TOP, fill=BOTH)
    frameTTTB.pack(side=BOTTOM, fill=BOTH)
    frameTTBT.pack(side=TOP, fill=BOTH)
    frameTTBB.pack(side=BOTTOM, fill=BOTH)
    frameTBTT.pack(side=TOP, fill=BOTH)
    frameTBTTT.pack(side=TOP, fill=BOTH)
    frameTBTTB.pack(side=BOTTOM, fill=BOTH)
    frameTBTTBT.pack(side=TOP, fill=BOTH)
    frameTBTTBB.pack(side=BOTTOM, fill=BOTH)
    frameTBTB.pack(side=BOTTOM)
    frameTBBT.pack(side=TOP, fill=BOTH)
    frameTBBB.pack(side=BOTTOM)
    LProductType.pack(side=LEFT, fill=BOTH)
    ProductType.pack(side=RIGHT, fill=BOTH)
    LSensorBatch.pack(side=LEFT, fill=BOTH)
    SensorBatch.pack(side=RIGHT, fill=BOTH)
    LSensorWafer.pack(side=LEFT, fill=BOTH)
    SensorWafer.pack(side=RIGHT, fill=BOTH)
    LSensorSerial.pack(side=LEFT, fill=BOTH)
    NameOfSensor.pack(side=RIGHT, fill=BOTH)
    LComments.pack(side=LEFT, fill=BOTH)
    SensorComments.pack(side=RIGHT, fill=BOTH)
    LRunNumber.pack(side=LEFT, fill=BOTH)
    SensorRunNumber.pack(side=LEFT, fill=BOTH)

    frameD.pack(side=BOTTOM, fill=BOTH)
    CheckP.pack(side=LEFT)
    CheckM.pack(side=LEFT)
    CheckS.pack(side=RIGHT)
    frameD1.pack(side=LEFT, fill=BOTH)
    frameD2.pack()
    frameD3.pack(side=RIGHT, fill=BOTH)
    ButtonPrevious.pack(side=LEFT, fill=BOTH)
    LSensor2.pack(side=RIGHT, fill=BOTH)
    LSensor3.pack(side=LEFT, fill=BOTH)
    ButtonNext.pack(side=LEFT, fill=BOTH)
    ButtonStart.pack(side=RIGHT, fill=BOTH)
    # ↑ Set position of objects.

    try:
        SMS.iconbitmap(programPath + "screens\\SensorMeasurement.ico")
    except TclError:
        pass  # It doesn't matter, if program can't import icon.
    # ↑ Set options of GUI.

    # SMS.protocol("WM_DELETE_WINDOW", on_closing)
    SMS.mainloop()
    # ↑ Loop of GUI. It maintains window opened.

except (TypeError, ValueError):
    pag.alert("Error has been occurred:\n\nPossible reason of the problem is in config file."
              "\nIt seems like arguments aren't correct type."
              "\nFor example: 'Expected string not numbers or visa versa'." + 3*"\n"
              + traceback.format_exc(limit=-3), "ERROR")

except (MemoryError, BufferError):
    pag.alert("Error has been occurred:\n\nPossible reason of the "
              "error is problem with memory. Look up to disk and RAM memory."
              + 3 * "\n" + traceback.format_exc(limit=-3), "ERROR")

except (NameError, AttributeError):
    pag.alert("Error has been occurred:\n\nPossible reasons of the problem are invalid or"
              " unknown name or attribute of identifier (variable, function, etc...)."
              "\nProgram maybe didn't load data from directory with data file and screens."
              "\nUse error message below:" + 3 * "\n" + traceback.format_exc(limit=-3), "ERROR")

except OSError:
    pag.alert("Error has been occurred:\n\nPossible reasons of the problem are missing files or screens."
              "\nCheck program directory with data file and screens to locating function."
              "\nUse manual and look up to \n'C:\\Program Files\\MetrologyAndScanning'." + 3*"\n"
              + traceback.format_exc(limit=-3), "ERROR")

except LookupError:
    pag.alert("Error has been occurred:\n\nPossible reason of the problem is in arrays."
              "\nCheck numbers of arguments behind variables in config file.\nMaybe too much of arguments."
              "\nUse manual and look up to: \n'C:\\Program Files\\MetrologyAndScanning"
              "\\config.txt'." + 3*"\n" + traceback.format_exc(limit=-3), "ERROR")

except AssertionError:
    pag.alert("Error has been occurred:\n\nReason is result of test function (assert) initialize program."
              + 3 * "\n" + traceback.format_exc(limit=-3), "ERROR")

except:
    pag.alert("Unexpected error has been occurred:" + 3 * "\n" +
              traceback.format_exc(limit=-3), "ERROR")
