#  SCRIPT WITH FUNCTIONS CALL BY GUI AND SETTINGS OF GUI.
import pyautogui as pag
import traceback

try:
    from SMS_Process import*
    # Import script with declaring all of functions those using error system and other scripts.


    def set_active(rewrite_con):
        CheckP["state"] = "active"
        CheckM["state"] = "active"
        CheckS["state"] = "active"
        ProductType["state"] = "normal"
        SensorBatch["state"] = "normal"
        SensorWafer["state"] = "normal"
        NameOfSensor["state"] = "normal"
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
        CheckP.deselect()
        if rewrite:
            ProductType.insert(0, productType[NumberOfSensor])
            SensorBatch.insert(0, sensorBatch[NumberOfSensor])
            SensorWafer.insert(0, sensorWafer[NumberOfSensor])
            if nameSensor[NumberOfSensor] == "":
                NameOfSensor.insert(0, dNameSensor[NumberOfSensor])
            else:
                NameOfSensor.insert(0, nameSensor[NumberOfSensor])


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
        ProductType["state"] = "disabled"
        SensorBatch["state"] = "disabled"
        SensorWafer["state"] = "disabled"
        NameOfSensor["state"] = "disabled"

    # ↑ Switch function of type of sensor. It will select empty position.
    # ↑ 7 Switches for variable 'sType'. It performing if you click to button in GUI.


    def previous_sensor():
        global NumberOfSensor
        if NumberOfSensor > 0:
            if mSensor[NumberOfSensor] == 0 and sSensor[NumberOfSensor] == 0 \
                 and sType[NumberOfSensor] != "E":
                pag.alert("You must choice at least one possibility!")
            elif NameOfSensor.get() == dNameSensor[NumberOfSensor] and sType[NumberOfSensor] != "E":
                pag.alert("You must unique serial number of sensor!")
            elif sType[NumberOfSensor] == "B" and "EC" in ProductType.get():
                pag.alert("Incorrect combination of product type (end-cap) and sensor type (barrel).")
            # ↑ Conditions for actual sensor.

            elif sType[NumberOfSensor] != "":
                productType[NumberOfSensor] = ProductType.get()
                ProductType.delete(0, END)
                sensorBatch[NumberOfSensor] = SensorBatch.get()
                SensorBatch.delete(0, END)
                sensorWafer[NumberOfSensor] = SensorWafer.get()
                SensorWafer.delete(0, END)
                nameSensor[NumberOfSensor] = NameOfSensor.get()
                NameOfSensor.delete(0, END)  # Clear textbox for new name of previous sensor.
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
                # ↑ Write label of menu according to type of sensor.

                ProductType.insert(0, productType[NumberOfSensor])
                SensorBatch.insert(0, sensorBatch[NumberOfSensor])
                SensorWafer.insert(0, sensorWafer[NumberOfSensor])
                NameOfSensor.insert(0, nameSensor[NumberOfSensor])
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
            if mSensor[NumberOfSensor] == 0 and sSensor[NumberOfSensor] == 0 \
                 and sType[NumberOfSensor] != "E":
                pag.alert("You must choice at least one possibility!")
            elif NameOfSensor.get() == dNameSensor[NumberOfSensor] and sType[NumberOfSensor] != "E":
                pag.alert("You must unique serial number of sensor!")
            elif sType[NumberOfSensor] == "B" and "EC" in ProductType.get():
                pag.alert("Incorrect combination of product type (end-cap) and sensor type (barrel).")
            # ↑ Conditions for actual sensor.

            elif sType[NumberOfSensor] != "":
                productType[NumberOfSensor] = ProductType.get()
                ProductType.delete(0, END)
                sensorBatch[NumberOfSensor] = SensorBatch.get()
                SensorBatch.delete(0, END)
                sensorWafer[NumberOfSensor] = SensorWafer.get()
                SensorWafer.delete(0, END)
                nameSensor[NumberOfSensor] = NameOfSensor.get()
                NameOfSensor.delete(0, END)  # Clear textbox for new name of next sensor.
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
                # ↑ Write label of menu according to type of sensor.

                ProductType.insert(0, productType[NumberOfSensor])
                SensorBatch.insert(0, sensorBatch[NumberOfSensor])
                SensorWafer.insert(0, sensorWafer[NumberOfSensor])
                if nameSensor[NumberOfSensor] == "":
                    NameOfSensor.insert(0, dNameSensor[NumberOfSensor])
                else:
                    NameOfSensor.insert(0, nameSensor[NumberOfSensor])
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
        # ↑ Write label of menu according to type of sensor.

        ProductType.delete(0, END)
        SensorBatch.delete(0, END)
        SensorWafer.delete(0, END)
        NameOfSensor.delete(0, END)  # Clear textbox for new name of next sensor.
        ProductType.insert(0, productType[NumberOfSensor])
        SensorBatch.insert(0, sensorBatch[NumberOfSensor])
        SensorWafer.insert(0, sensorWafer[NumberOfSensor])
        if nameSensor[NumberOfSensor] == "":
            NameOfSensor.insert(0, dNameSensor[NumberOfSensor])
        else:
            NameOfSensor.insert(0, nameSensor[NumberOfSensor])
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

        productType[NumberOfSensor] = ProductType.get()
        ProductType.delete(0, END)
        sensorBatch[NumberOfSensor] = SensorBatch.get()
        SensorBatch.delete(0, END)
        sensorWafer[NumberOfSensor] = SensorWafer.get()
        SensorWafer.delete(0, END)
        nameSensor[NumberOfSensor] = NameOfSensor.get()
        NameOfSensor.delete(0, END)  # Clear textbox for new name of next sensor.
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
            # ↑ Write label of menu according to type of sensor.

            ProductType.insert(0, productType[NumberOfSensor])
            SensorBatch.insert(0, sensorBatch[NumberOfSensor])
            SensorWafer.insert(0, sensorWafer[NumberOfSensor])
            if nameSensor[NumberOfSensor] == "":
                NameOfSensor.insert(0, dNameSensor[NumberOfSensor])
            else:
                NameOfSensor.insert(0, nameSensor[NumberOfSensor])
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
            # ↑ Write label of menu according to type of sensor.

            LSensor3["image"] = getattr(Img, "p" + str(NumberOfSensor))
            ProductType.insert(0, productType[NumberOfSensor])
            SensorBatch.insert(0, sensorBatch[NumberOfSensor])
            SensorWafer.insert(0, sensorWafer[NumberOfSensor])
            if nameSensor[NumberOfSensor] == "":
                NameOfSensor.insert(0, dNameSensor[NumberOfSensor])
            else:
                NameOfSensor.insert(0, nameSensor[NumberOfSensor])
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
                                                           "Humidity in the laboratory", default=str(LabPar.Humidity)))
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
                                                           "Humidity in the laboratory", default=str(LabPar.Humidity)))
                except TypeError:
                    pass

            start()  # Start program.


    def pre_start():
        global NumberOfSensor

        if mSensor[NumberOfSensor] == 0 and sSensor[NumberOfSensor] == 0 \
                and sType[NumberOfSensor] != "E":
            pag.alert("You must choice at least one possibility!", "Message")
        elif sType[NumberOfSensor] == "":
            pag.alert("You must choice type of sensor!", "Message")
        elif NameOfSensor.get() == dNameSensor[NumberOfSensor] and sType[NumberOfSensor] != "E":
            pag.alert("You must unique serial number of sensor!", "Message")
        # ↑ Conditions for last sensor.
        else:
            productType[NumberOfSensor] = ProductType.get()
            ProductType.delete(0, END)
            sensorBatch[NumberOfSensor] = SensorBatch.get()
            SensorBatch.delete(0, END)
            sensorWafer[NumberOfSensor] = SensorWafer.get()
            SensorWafer.delete(0, END)
            nameSensor[NumberOfSensor] = NameOfSensor.get()
            NameOfSensor.delete(0, END)  # Clear textbox for new name of next sensor.
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
                # ↑ Write label of menu according to type of sensor.

                ProductType.insert(0, productType[NumberOfSensor])
                SensorBatch.insert(0, sensorBatch[NumberOfSensor])
                SensorWafer.insert(0, sensorWafer[NumberOfSensor])
                if nameSensor[NumberOfSensor] == "":
                    NameOfSensor.insert(0, dNameSensor[NumberOfSensor])
                else:
                    NameOfSensor.insert(0, nameSensor[NumberOfSensor])
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
    frameTBTB = tkinter.Frame(frameTBT, bg="light gray", height=7, width=400)
    frameTBBT = tkinter.Frame(frameTBB)
    frameTBBB = tkinter.Frame(frameTBB, bg="light gray", height=7, width=400)
    LProductType = tkinter.Label(frameTTTT, text="Product type: ", height=1, width=20)
    ProductType = tkinter.Entry(frameTTTT, bd=3, width=36)
    LSensorBatch = tkinter.Label(frameTTTB, text="Sensor batch: ", height=1, width=20)
    SensorBatch = tkinter.Entry(frameTTTB, bd=3, width=36)
    LSensorWafer = tkinter.Label(frameTTBT, text="Sensor wafer: ", height=1, width=20)
    SensorWafer = tkinter.Entry(frameTTBT, bd=3, width=36)
    LSensorSerial = tkinter.Label(frameTBTT, text="Serial number: ", height=1, width=21)
    NameOfSensor = tkinter.Entry(frameTBTT, bd=3, width=36)
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
    LSensor2 = tkinter.Label(frameD1, text="  Sensor " + str(NumberOfSensor + 1))
    LSensor3 = tkinter.Label(frameD, image=Img.p0)
    ButtonNext = tkinter.Button(frameD, text=" Next sensor ", command=next_sensor, bg="light gray",
                                activebackground="gray", activeforeground="white")
    ButtonStart = tkinter.Button(frameD3, text="Start measuring", command=pre_start, bg="light gray",
                                 activebackground="dark red", activeforeground="white")
    ButtonBack = tkinter.Button(frameD1, text="Back to settings", command=back, bg="light gray",
                                activebackground="gray", activeforeground="white")
    # ↑ Set properties of window and objects(buttons, menu, etc...).

    if sType[NumberOfSensor] == "E" or sType[NumberOfSensor] == "":
        if sType[NumberOfSensor] == "E":
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
    else:
        TypeMenu = tkinter.Menubutton(SMS, text="Select type of sensor   -   " + str(sType[0]), relief=SUNKEN,
                                      bg="light gray", activebackground="gray", activeforeground="white")
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
    # ↑ Write label of menu according to type of sensor.
    # Conditionals for insert title on menu.

    TypeMenu.grid()
    TypeMenu.menu = Menu(TypeMenu, tearoff=1)
    TypeMenu["menu"] = TypeMenu.menu

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

    SMS.title("Sensors measurement and scanning")
    SMS.resizable(0, 0)
    try:
        SMS.iconbitmap(programPath + "screens\\SensorMeasurement.ico")
    except TclError:
        pass
    # ↑ Set options of GUI.

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
