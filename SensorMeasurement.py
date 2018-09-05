import time
import pyautogui as pag
from tkinter import*
import tkinter

m = 1
s = 1
sType = "R0"
path = "C:\\Partrtn\\"
SM = tkinter.Tk()
SM.title("Sensor measurement and scanning")
# ↑ Declaration variables and tkinter object.

class p:
    # Positions of objects.
    file = [10, 30]
    open = [20, 80]
    start = [800, 100]
    confirmStart = [720, 500]
    resetRoutine = [680, 100]
    resetAngle = [50, 950]
    desktop = [1915, 1050]
    mm3d = [340, 1050]
    save = [[1450, 800]]
    # Positions of 'mm3d' and 'save' will overwrite.

def M():
   global m
   if m == 1:
      m = 0
   else:
      m = 1
# ↑ switch function of Measurement.
def S():
   global s
   if s == 1:
      s = 0
   else:
      s = 1
# ↑ switch function of Scanning.

def R0select():
    global sType
    sType = "R0"

def R1select():
    global sType
    sType = "R1"

def R2select():
    global sType
    sType = "R2"

def R3select():
    global sType
    sType = "R3"

def R4select():
    global sType
    sType = "R4"

def R5select():
    global sType
    sType = "R5"
# ↑ 6 Switches for variable 'sType'. It performing if you click to button in GUI.

def openCmd():
    pag.hotkey('win', 'q')  # Finding function of windows.
    time.sleep(0.5)
    pag.typewrite("cmd")
    pag.typewrite(["enter"])
    time.sleep(0.5)
# ↑ Open search function of windows and start cmd.

def closeCmd():
    pag.typewrite(["enter"])
    time.sleep(0.1)
    pag.typewrite("exit")
    time.sleep(0.1)
    pag.typewrite(["enter"])
    time.sleep(1)
# ↑ Close cmd.

def OpenRoutine():
    pag.click(p.file)  # Click to "File".
    time.sleep(0.3)
    pag.click(p.open)  # Open routine.
    time.sleep(0.2)

def SearchFile():
    pag.hotkey("f4")  # Mark searching textbox.
    time.sleep(0.2)
    pag.hotkey("ctrl", "a")
    time.sleep(0.2)

def StartRoutine(routine):
    time.sleep(1)
    OpenRoutine()
    SearchFile()
    pag.typewrite(path + "Routines")  # Search place in pc.
    time.sleep(0.8)
    pag.typewrite(["enter"])
    time.sleep(0.1)
    pag.hotkey("alt", "n")  # Switch to textbox of 'Name file'.
    time.sleep(0.1)
    pag.typewrite(routine)  # Write name of routine.
    time.sleep(0.3)
    pag.typewrite(["enter"])
    time.sleep(0.5)
    pag.click(p.start)  # Start routine.
    time.sleep(0.2)
    pag.click(p.confirmStart)  # Confirming start.

def SaveFile():
    pag.typewrite(path + sType + "\\" + NameOfSensor1.get())
    # ↑ Search sensor folder.
    time.sleep(0.8)
    pag.typewrite(["enter"])
    time.sleep(0.1)
    pag.click(p.save)  # Save.
    time.sleep(0.5)
    pag.moveTo(900, 0)  # Move cursor from 'save' button.

def wait(fuse):
    try:
        if fuse == True:
            img = pag.locateCenterOnScreen("C:\\Program Files\\MetrologyAndScanning"\
                                           + "\\c1.png")
            # ↑ Finding image on screen.
            d = list(img)
            p.save = d  # Overwrite position of save button.
        else:
            img2 = pag.locateCenterOnScreen("C:\\Program Files\\MetrologyAndScanning"\
                                           + "\\c2.png")
            # ↑ Finding image on screen.
            d2 = list(img2)
            pag.typewrite(["enter"])  # Confirm end of routine.
    except:
        wait(fuse)  # Repeat code until it executed commands in 'try'.
# ↑ Waiting system, if on screen will appear required image, loop will end.

def EditOutput(file, fuse, k, start, gap):
    a = 0
    w = 0
    s = start
    tempfile = ""
    t = False
    # ↑ Declaration variables.
    with open(path + sType + "\\" + NameOfSensor1.get()\
              + "\\" + file, 'r') as f:  # Open file with data (for read).
        while a < 50000:
            f1 = f.read(1)  # For everyone execute read one character.
            if f1 == "+" or f1 == "-":
                t = True
                if a < fuse:
                    tempfile += "Actual_Width "
                elif a <= (fuse + 110):
                    if w == 0:
                        tempfile += "Nominal_Width "
                        w += 1
                    elif w == 1:
                        tempfile += " Actual_Width "
                        w += 1
                    elif w == 2:
                        tempfile += " Deviation_Width "
                        w += 1
                # ↑ Naming data of another types.
                else:
                    if s == 0:
                        tempfile += "X_Nominal "
                    elif s == 1:
                        tempfile += gap + "X_Actual "
                    elif s == 2:
                        tempfile += " X_Deviation "
                    elif s == 3:
                        tempfile += " Y_Nominal "
                    elif s == 4:
                        tempfile += " Y_Actual "
                    elif s == 5:
                        tempfile += " Y_Deviation "
                    elif s == 6:
                        tempfile += " Z_Nominal "
                    elif s == 7:
                        tempfile += " Z_Actual "
                    elif s == 8:
                        tempfile += " Z_Deviation "
                    s += k
                # ↑ Naming data of normal type.
            elif f1 == " ":
                if t == True:
                    if a < fuse:
                        tempfile += "\n"
                    elif a <= (fuse + 110) and w == 3:
                        tempfile += "\n"
                    elif s > 8:
                        s = start
                        tempfile += "\n"
                        if gap == "":
                            f0 = f.read(16)
                # Creating new lines and reset variables.
                t = False

            if t == True:
                if f1 == "0" or f1 == "1" or f1 == "2" or f1 == "3" or f1 == "4"\
                        or f1 == "5" or f1 == "6" or f1 == "7" or f1 == "8" or\
                        f1 == "9" or f1 == "." or f1 == "+" or f1 == "-":
                    tempfile += f1  # Write of data to memory.
            a += 1
    f.close()
    with open(path + sType + "\\" + NameOfSensor1.get()\
              + "\\" + file, 'w') as f:  # Open file with data (for write).
        f.write(tempfile)  # Write data to file.
    f.close()

def ok():
    if m == 0 and s == 0:
        pag.alert("You must choice at least one possibility!")
    elif NameOfSensor1.get() == "":
        pag.alert("You must write name of sensor!")
# ↑ Conditions for switching on.

    else:
        imgMM3D = pag.locateCenterOnScreen("C:\\Program Files\\"\
                                        + "MetrologyAndScanning\\icon.png")
        p.mm3d = list(imgMM3D)  # Overwrite position of MM3D icon.
        openCmd()
        pag.click(350, 350)
        time.sleep(0.1)
        pag.typewrite("cd " + path + sType)
        # ↑ In cmd write command "go to" folder.
        pag.typewrite(["enter"])
        time.sleep(0.1)
        pag.typewrite("mkdir " + NameOfSensor1.get())  # Create file with sensor name.
        time.sleep(0.2)
        closeCmd()

        if m == 1:
            pag.click(p.mm3d)  # Switch to MeasureMind3D (MM3D).

            if sType == "R0":
                StartRoutine("ATLAS12EC_routine.RTN")
            elif sType == "R1":
                StartRoutine("ATLAS12EC_routine.RTN")
            elif sType == "R2":
                StartRoutine("ATLAS12EC_routine.RTN")
            elif sType == "R3":
                StartRoutine("ATLAS12EC_routine.RTN")
            elif sType == "R4":
                StartRoutine("ATLAS12EC_routine.RTN")
            elif sType == "R5":
                StartRoutine("ATLAS12EC_routine.RTN")
            # ↑ Start routine for correct sensor type.

            wait(True)  # Wait to complete first measuring.
            SearchFile()
            SaveFile()

            wait(True)  # Wait to complete second measuring.
            SearchFile()
            SaveFile()

            wait(True)  # Wait to third measuring.
            SearchFile()
            SaveFile()

            wait(False)  # Wait to complete third measuring.

            if sType == "R0":
                EditOutput('tempfile.txt', 890, 1, 0, " ")
                EditOutput('data_stream.DAT', -80, 3, 1, "")
            elif sType == "R1":
                EditOutput('tempfile.txt', 890, 1, 0, " ")
                EditOutput('data_stream.DAT', -80, 3, 1, "")
            elif sType == "R2":
                EditOutput('tempfile.txt', 890, 1, 0, " ")
                EditOutput('data_stream.DAT', -80, 3, 1, "")
            elif sType == "R3":
                EditOutput('tempfile.txt', 890, 1, 0, " ")
                EditOutput('data_stream.DAT', -80, 3, 1, "")
            elif sType == "R4":
                EditOutput('tempfile.txt', 890, 1, 0, " ")
                EditOutput('data_stream.DAT', -80, 3, 1, "")
            elif sType == "R5":
                EditOutput('tempfile.txt', 890, 1, 0, " ")
                EditOutput('data_stream.DAT', -80, 3, 1, "")
            # ↑ Edit data output for correct sensor type.

        if s == 1:
            if m == 0:
                pag.click(p.mm3d)  # Switch to MeasureMind3D (MM3D).
            time.sleep(1)
            pag.doubleClick(p.resetRoutine)  # Click to reset routine.
            time.sleep(1)
            pag.click(p.resetAngle)  # Click to reset angle.
            time.sleep(0.5)

            if sType == "R0":
                StartRoutine("SensorScanning.RTN")
            elif sType == "R1":
                StartRoutine("SensorScanning.RTN")
            elif sType == "R2":
                StartRoutine("SensorScanning.RTN")
            elif sType == "R3":
                StartRoutine("SensorScanning.RTN")
            elif sType == "R4":
                StartRoutine("SensorScanning.RTN")
            elif sType == "R5":
                StartRoutine("SensorScanning.RTN")
            # ↑ Start routine for correct sensor type.

            wait(False)  # Waiting to end of scanning.

            time.sleep(0.1)
            openCmd()
            pag.typewrite("move " + path + "*.* " + path\
                          + sType + "\\" + NameOfSensor1.get())
            # ↑ Move screens to folder.
            time.sleep(0.4)
            closeCmd()

        pag.click(p.desktop)  # Switch to desktop.
        pag.alert("Everything done!")  # Alert end of program.

TypeMenu = tkinter.Menubutton(SM, text = "Select type of sensor", relief=SUNKEN,\
                              bg="light gray", activebackground="gray",\
                              activeforeground="white")
TypeMenu.grid()
TypeMenu.menu = Menu(TypeMenu, tearoff=0.2)
TypeMenu["menu"] = TypeMenu.menu
TypeMenu.menu.add_command(label="R0", command=R0select)
TypeMenu.menu.add_command(label="R1", command=R1select)
TypeMenu.menu.add_command(label="R2", command=R2select)
TypeMenu.menu.add_command(label="R3", command=R3select)
TypeMenu.menu.add_command(label="R4", command=R4select)
TypeMenu.menu.add_command(label="R5", command=R5select)

LSensor1 = tkinter.Label(SM, text="Name of sensor: ")
NameOfSensor1 = tkinter.Entry(SM, bd=3)
CheckM = tkinter.Checkbutton(SM, text="Measuring", height=2, width=10, command=M)
CheckS = tkinter.Checkbutton(SM, text="Scanning", height=2, width=10, command=S)
ButtonOK = tkinter.Button(SM, text="Start measuring", command=ok, bg="light gray",\
                          activebackground="gray", activeforeground="white")
# ↑ Set properties of window and objects(buttons, menu, etc...).

CheckM.select()
CheckS.select()
# ↑ Set Checkbox to select position.

TypeMenu.pack(side=TOP, fill=BOTH)
LSensor1.pack(side=LEFT)
NameOfSensor1.pack(side=LEFT)
ButtonOK.pack(side=BOTTOM, fill=BOTH)
CheckS.pack(side=RIGHT)
CheckM.pack(side=RIGHT)
# ↑ Set position of objects.

SM.mainloop()