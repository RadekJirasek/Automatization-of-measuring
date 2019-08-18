#  SCRIPT WITH FUNCTIONS CALL BY GUI AND SETTINGS OF GUI.
import pyautogui as pag
import traceback

try:
    from SMS_Process import*
    # Import script with declaring all of functions those using error system and other scripts.


    def measurement_select():
        global mSensor
        if mSensor[NumberOfSensor] == 1:
            mSensor[NumberOfSensor] = 0
        else:
            mSensor[NumberOfSensor] = 1
    # ↑ Switch function of Measurement.


    def scanning_select():
        global sSensor
        if sSensor[NumberOfSensor] == 1:
            sSensor[NumberOfSensor] = 0
        else:
            sSensor[NumberOfSensor] = 1
    # ↑ Switch function of Scanning.


    def aps_select():
        global pSensor
        if pSensor[NumberOfSensor] == 1:
            pSensor[NumberOfSensor] = 0
        else:
            pSensor[NumberOfSensor] = 1
    # ↑ Switch function of automatic position system.


    def r0_select():
        global sType
        sType[NumberOfSensor] = "R0"
        TypeMenu["text"] = "Select type of sensor   -   " + sType[NumberOfSensor]
    # ↑ Switch function of type of sensor. It will select type R0.


    def r1_select():
        global sType
        sType[NumberOfSensor] = "R1"
        TypeMenu["text"] = "Select type of sensor   -   " + sType[NumberOfSensor]
    # ↑ Switch function of type of sensor. It will select type R1.


    def r2_select():
        global sType
        sType[NumberOfSensor] = "R2"
        TypeMenu["text"] = "Select type of sensor   -   " + sType[NumberOfSensor]
    # ↑ Switch function of type of sensor. It will select type R2.


    def r3_select():
        global sType
        sType[NumberOfSensor] = "R3"
        TypeMenu["text"] = "Select type of sensor   -   " + sType[NumberOfSensor]
    # ↑ Switch function of type of sensor. It will select type R3.


    def r4_select():
        global sType
        sType[NumberOfSensor] = "R4"
        TypeMenu["text"] = "Select type of sensor   -   " + sType[NumberOfSensor]
    # ↑ Switch function of type of sensor. It will select type R4.


    def r5_select():
        global sType
        sType[NumberOfSensor] = "R5"
        TypeMenu["text"] = "Select type of sensor   -   " + sType[NumberOfSensor]
    # ↑ Switch function of type of sensor. It will select type R5.


    def b_select():
        global sType
        sType[NumberOfSensor] = "B"
        TypeMenu["text"] = "Select type of sensor   -   " + sType[NumberOfSensor]
    # ↑ Switch function of type of sensor. It will select type B.


    def e_select():
        global sType
        sType[NumberOfSensor] = "E"
        TypeMenu["text"] = "Select type of sensor   -   empty"
    # ↑ Switch function of type of sensor. It will select empty position.
    # ↑ 7 Switches for variable 'sType'. It performing if you click to button in GUI.


    def previous_sensor():
        global NumberOfSensor
        if NumberOfSensor > 0:
            if mSensor[NumberOfSensor] == 0 and sSensor[NumberOfSensor] == 0 \
                 and sType[NumberOfSensor] != "E":
                pag.alert("You must choice at least one possibility!")
            elif NameOfSensor.get() == dNameSensor[NumberOfSensor] and sType[NumberOfSensor] != "E":
                pag.alert("You must write name of sensor!")
            # ↑ Conditions for actual sensor.

            elif sType[NumberOfSensor] != "":
                nameSensor[NumberOfSensor] = NameOfSensor.get()
                NameOfSensor.delete(0, END)  # Clear textbox for new name of previous sensor.

                NumberOfSensor = NumberOfSensor - 1  # It decrease number of sensor.
                LSensor2["text"] = "  Sensor " + str(NumberOfSensor + 1)  # Edit label of number of sensor.
                if NumberOfSensor == 0:
                    LSensor3["image"] = Img.p0
                elif NumberOfSensor == 1:
                    LSensor3["image"] = Img.p1
                elif NumberOfSensor == 2:
                    LSensor3["image"] = Img.p2
                elif NumberOfSensor == 3:
                    LSensor3["image"] = Img.p3
                elif NumberOfSensor == 4:
                    LSensor3["image"] = Img.p4
                elif NumberOfSensor == 5:
                    LSensor3["image"] = Img.p5
                elif NumberOfSensor == 6:
                    LSensor3["image"] = Img.p6
                elif NumberOfSensor == 7:
                    LSensor3["image"] = Img.p7
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
                TypeMenu.menu.add_command(command=e_select, image=Img.E)
                # ↑ Set buttons in menu.

                if sType[NumberOfSensor] == "E":
                    TypeMenu["text"] = "Select type of sensor   -   empty"
                else:
                    TypeMenu["text"] = "Select type of sensor   -   " + sType[NumberOfSensor]
                # ↑ Write label of menu according to type of sensor.

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
                pag.alert("You must write name of sensor!")
            # ↑ Conditions for actual sensor.

            elif sType[NumberOfSensor] != "":
                nameSensor[NumberOfSensor] = NameOfSensor.get()
                NameOfSensor.delete(0, END)  # Clear textbox for new name of next sensor.

                NumberOfSensor = NumberOfSensor + 1  # It increase number of sensor.
                LSensor2["text"] = "  Sensor " + str(NumberOfSensor + 1)  # Edit label of number of sensor.
                if NumberOfSensor == 1:
                    LSensor3["image"] = Img.p1
                elif NumberOfSensor == 2:
                    LSensor3["image"] = Img.p2
                elif NumberOfSensor == 3:
                    LSensor3["image"] = Img.p3
                elif NumberOfSensor == 4:
                    LSensor3["image"] = Img.p4
                elif NumberOfSensor == 5:
                    LSensor3["image"] = Img.p5
                elif NumberOfSensor == 6:
                    LSensor3["image"] = Img.p6
                elif NumberOfSensor == 7:
                    LSensor3["image"] = Img.p7
                elif NumberOfSensor == 8:
                    LSensor3["image"] = Img.p8
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
                TypeMenu.menu.add_command(command=e_select, image=Img.E)
                # ↑ Set buttons in menu.

                if sType[NumberOfSensor] == "":
                    TypeMenu["text"] = "Select type of sensor"
                elif sType[NumberOfSensor] == "E":
                    TypeMenu["text"] = "Select type of sensor   -   empty"
                else:
                    TypeMenu["text"] = "Select type of sensor   -   " + sType[NumberOfSensor]

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
                else:
                    CheckP.deselect()
                # ↑ Selecting or deselecting of checkbox buttons.

            else:
                pag.alert("You must choice type of sensor.")
        else:
            pag.alert("Only sensors between 0 and 9")


    def pre_start():
        global NumberOfSensor

        if mSensor[NumberOfSensor] == 0 and sSensor[NumberOfSensor] == 0 \
                and sType[NumberOfSensor] != "E":
            pag.alert("You must choice at least one possibility!", "Message")
        elif sType[NumberOfSensor] == "":
            pag.alert("You must choice type of sensor!", "Message")
        elif NameOfSensor.get() == dNameSensor[NumberOfSensor] and sType[NumberOfSensor] != "E":
            pag.alert("You must write name of sensor!", "Message")
        # ↑ Conditions for last sensor.
        else:
            nameSensor[NumberOfSensor] = NameOfSensor.get()
            start()  # Start program.


    if sType[0] == "":
        TypeMenu = tkinter.Menubutton(SMS, text="Select type of sensor", relief=SUNKEN,
                                      bg="light gray", activebackground="gray", activeforeground="white")
    elif sType[0] == "E":
        TypeMenu = tkinter.Menubutton(SMS, text="Select type of sensor   -   empty", relief=SUNKEN,
                                      bg="light gray", activebackground="gray", activeforeground="white")
    else:
        TypeMenu = tkinter.Menubutton(SMS, text="Select type of sensor   -   " + str(sType[0]), relief=SUNKEN,
                                      bg="light gray", activebackground="gray", activeforeground="white")
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
    TypeMenu.menu.add_command(command=e_select, image=Img.E)
    # Insert images to submenu.

    frameTop = tkinter.Frame(SMS)
    frameDown = tkinter.Frame(SMS)
    frameT1 = tkinter.Frame(frameTop)
    frameT2 = tkinter.Frame(frameTop)
    LSensor1 = tkinter.Label(frameT1, text="Name of sensor: ", height=2, width=18)
    NameOfSensor = tkinter.Entry(frameT1, bd=3, width=32)
    CheckP = tkinter.Checkbutton(frameT2, text="Automatic position system", width=20, command=aps_select)
    CheckM = tkinter.Checkbutton(frameT2, text="Measuring", width=10, command=measurement_select)
    CheckS = tkinter.Checkbutton(frameT2, text="Scanning", width=10, command=scanning_select)
    frameD1 = tkinter.Frame(frameDown)
    frameD2 = tkinter.Frame(frameDown)
    frameD3 = tkinter.Frame(frameDown)
    ButtonPrevious = tkinter.Button(frameD1, text="Previous sensor", command=previous_sensor, bg="light gray",
                                    activebackground="gray", activeforeground="white")
    LSensor2 = tkinter.Label(frameD1, text="  Sensor " + str(NumberOfSensor + 1))
    LSensor3 = tkinter.Label(frameDown, image=Img.p0)
    ButtonNext = tkinter.Button(frameDown, text=" Next sensor ", command=next_sensor, bg="light gray",
                                activebackground="gray", activeforeground="white")
    ButtonStart = tkinter.Button(frameD3, text="Start measuring", command=pre_start, bg="light gray",
                                 activebackground="dark red", activeforeground="white")
    # ↑ Set properties of window and objects(buttons, menu, etc...).

    if mSensor[0] == 1:
        CheckM.select()
    if sSensor[0] == 1:
        CheckS.select()
    if pSensor[0] == 1:
        CheckP.select()
    # ↑ Set Checkbox to correct position.

    NameOfSensor.insert(0, dNameSensor[0])
    # Write default name of first sensor to textbox.

    TypeMenu.pack(side=TOP, fill=BOTH)
    LSensor1.pack(side=LEFT)
    NameOfSensor.pack(side=LEFT)
    frameTop.pack(side=TOP, fill=BOTH)
    frameT1.pack(side=TOP, fill=BOTH)
    frameT2.pack(side=BOTTOM, fill=BOTH)
    frameDown.pack(side=BOTTOM, fill=BOTH)
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
