# SCRIPT DECLARING BOOKMARKS AND BASIC VARIABLES AND VARIABLES FROM TEXT FILES

import os
# Bookmark for using operating system.
import shutil
# Bookmark for work with files etc...
import subprocess
# Bookmark for calling programs etc...
import time
# Time bookmark.
import math
# Bookmark for mathematics operations.
import datetime
# Bookmark detecting actual time.
import pyautogui as pag
# Bookmark using keywords, mouse, etc...
from tkinter import*  #
# Bookmark creating GUI.
import tkinter
# Bookmark creating GUI.
from PIL import Image, ImageTk
# Bookmark working with images.

SM = tkinter.Tk()
# ↑ Declaration tkinter object.


path = "C:\\Partrtn\\"  # Path to folder with everything about measuring (routines, measured date).
logFile = ""  # Path to log file.
NumberOfSensor = 0  # Actual number of measured sensor.
error = 0  # Variable of error system (if error = 0, everything ok; error = 1, problem is in start segment;
# error = 2, problem is process loop.)
errorId0 = 0  # Variable for identification origin of error in start segment.
sType = ["", "", "", "", "", "", "", "", ""]  # Array of variables for types of sensors.
nameSensor = ["", "", "", "", "", "", "", "", ""]  # Array of variables for names of sensors.
dNameSensor = ["", "", "", "", "", "", "", "", ""]  # Array of variables for default names of sensors.
mSensor = [1, 1, 1, 1, 1, 1, 1, 1, 1]  # Array of variables for measurement of sensors (measurement (1) or not (0)).
sSensor = [1, 1, 1, 1, 1, 1, 1, 1, 1]  # Array of variables for scanning of sensors (scanning (1) or not (0)).
pSensor = [1, 1, 1, 1, 1, 1, 1, 1, 1]  # Array of variables for APS of sensors (APS on (1) or off (0)).
sensorPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # Array of variables for right or bad position of sensors (ok (1) or bad (0)).


class LimitDistance:
    Phi = 0.0  # Limit of automatic position system (APS) of sensor for angle phi.
    RightD = [0.0, 0.0]  # Limit of distance between corner of sensor and vertical edge of holder in APS.
    BottomD = [0.0, 0.0]  # Limit of distance between corner of sensor and horizontal edge of holder in APS.


class LimitSize:
    R0 = [0, 0, 0, 0]
    R1 = [0, 0, 0, 0]
    R2 = [0, 0, 0, 0]
    R3 = [0, 0, 0, 0]
    R4 = [0, 0, 0, 0]
    R5 = [0, 0, 0, 0]
    B = [0, 0, 0, 0]
# ↑ Array of variables for all types of sensors. It represents data size limits (Type int, [0] and [1] are upper and
# lower data boundaries for measuring, [2] and [3] are upper and lower data boundaries for scanning).


class ErrorId:
    createFolder = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    startMeasuring = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    completeMeasuring = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    editOutput = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    moveTrash = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    startScanning = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    completeScanning = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    moveScreens = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    startJoinScreens = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    completeJoinScreens = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    dataSizeTest = [0, 0, 0, 0, 0, 0, 0, 0, 0]


class Position:
    file = [10, 30]
    open = [20, 80]
    start = [800, 100]
    system = [0, 0]
    stop = [200, 950]
    resetSystem = [0, 0]
    resetRoutine = [680, 100]
    resetAngle = [50, 950]
    resetX = [0, 0]
    resetY = [0, 0]
    desktop = [1915, 1050]
    cross = [1000, 200]
    cmd = [100, 200]
    mm3d = [340, 1050]
    save = [[1450, 800]]
# ↑ Positions of objects.


class Img:
    R0 = ImageTk.PhotoImage(Image.open("D:\\Downloads\\R0_.png"))
    R1 = ImageTk.PhotoImage(Image.open("D:\\Downloads\\R1_.png"))
    R2 = ImageTk.PhotoImage(Image.open("D:\\Downloads\\R2_.png"))
    R3 = ImageTk.PhotoImage(Image.open("D:\\Downloads\\R3_.png"))
    R4 = ImageTk.PhotoImage(Image.open("D:\\Downloads\\R4_.png"))
    R5 = ImageTk.PhotoImage(Image.open("D:\\Downloads\\R5_.png"))
    B = ImageTk.PhotoImage(Image.open("D:\\Downloads\\B_.png"))
    E = ImageTk.PhotoImage(Image.open("D:\\Downloads\\E.png"))
    p0 = ImageTk.PhotoImage(Image.open("D:\\Downloads\\0.png"))
    p1 = ImageTk.PhotoImage(Image.open("D:\\Downloads\\1.png"))
    p2 = ImageTk.PhotoImage(Image.open("D:\\Downloads\\2.png"))
    p3 = ImageTk.PhotoImage(Image.open("D:\\Downloads\\3.png"))
    p4 = ImageTk.PhotoImage(Image.open("D:\\Downloads\\4.png"))
    p5 = ImageTk.PhotoImage(Image.open("D:\\Downloads\\5.png"))
    p6 = ImageTk.PhotoImage(Image.open("D:\\Downloads\\6.png"))
    p7 = ImageTk.PhotoImage(Image.open("D:\\Downloads\\7.png"))
    p8 = ImageTk.PhotoImage(Image.open("D:\\Downloads\\8.png"))
# ↑ Declaration of paths for images.


# ↓ This code segment will take over values of variables from text document.
with open("C:\\Users\\Uzivatel\\Desktop\\config.txt", 'r') as f:
    a = 0
    b = ""
    c = 0
    d = False
    e = 0
    rPhiB = ""
    rD1B = ["", ""]
    rD2B = ["", ""]
    sR0B = ["", "", "", ""]
    sR1B = ["", "", "", ""]
    sR2B = ["", "", "", ""]
    sR3B = ["", "", "", ""]
    sR4B = ["", "", "", ""]
    sR5B = ["", "", "", ""]
    sBB = ["", "", "", ""]
    # ↑ Declaring local variables.
    v1 = ["", "", "", "", "", "", "", "", ""]
    v2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    v3 = ["", ""]
    v4 = ["", "", "", ""]
    # ↑ Declaring local variables (using in function info_from_txt).

    def info_from_txt(con):  # Local function for adding characters from text file.
        global b
        global e
        global v1
        global v2
        global v3
        global v4
        if b == ";":
            e += 1
        # After program detect ';' it saving next string to next variable in array.
        else:
            if con == 1:
                v1[e] += b
            elif con == 2:
                v2[e] = int(b)
            elif con == 3:
                v3[e] += b
            elif con == 4:
                v4[e] += b
            # ↑ It added characters to variable. Finally it will be complete string.
        if con == 1:
            return v1
        elif con == 2:
            return v2
        elif con == 3:
            return v3
        elif con == 4:
            return v4
        # Return variable that was been called.

    while a < 1000:

        b = f.read(1)  # Reading text one by one character.
        if b == " " or b == "\n":  # Deleting gabs and new line characters.
            continue
        if b == "=":  # If program detect '=', it prepare to save next string.
            c += 1
            d = True
            continue
        if b == "#":  # If program detect '#', it end reading string.
            e = 0
            v1 = ["", "", "", "", "", "", "", "", ""]
            v2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            v3 = ["", ""]
            v4 = ["", "", "", "", ""]
            d = False
            # Reset variables.
            continue
        if d:  # Saving data only after detect '=' and before '#'.
            if c == 1:
                path += b
            elif c == 2:
                sType = info_from_txt(1)
            elif c == 3:
                dNameSensor = info_from_txt(1)
            elif c == 4:
                mSensor = info_from_txt(2)
            elif c == 5:
                sSensor = info_from_txt(2)
            elif c == 6:
                pSensor = info_from_txt(2)
            elif c == 7:
                sR0B = info_from_txt(4)
            elif c == 8:
                sR1B = info_from_txt(4)
            elif c == 9:
                sR2B = info_from_txt(4)
            elif c == 10:
                sR3B = info_from_txt(4)
            elif c == 11:
                sR4B = info_from_txt(4)
            elif c == 12:
                sR5B = info_from_txt(4)
            elif c == 13:
                sBB = info_from_txt(4)
            elif c == 14:
                rPhiB += b
            elif c == 15:
                rD1B = info_from_txt(3)
            elif c == 16:
                rD2B = info_from_txt(3)
            # ↑ Different options of saving data according to sequence (variable 'c').

        a += 1
    LimitSize.R0[0] = int(sR0B[0])
    LimitSize.R0[1] = int(sR0B[1])
    LimitSize.R0[2] = int(sR0B[2])
    LimitSize.R0[3] = int(sR0B[3])
    LimitSize.R1[0] = int(sR1B[0])
    LimitSize.R1[1] = int(sR1B[1])
    LimitSize.R1[2] = int(sR1B[2])
    LimitSize.R1[3] = int(sR1B[3])
    LimitSize.R2[0] = int(sR2B[0])
    LimitSize.R2[1] = int(sR2B[1])
    LimitSize.R2[2] = int(sR2B[2])
    LimitSize.R2[3] = int(sR2B[3])
    LimitSize.R3[0] = int(sR3B[0])
    LimitSize.R3[1] = int(sR3B[1])
    LimitSize.R3[2] = int(sR3B[2])
    LimitSize.R3[3] = int(sR3B[3])
    LimitSize.R4[0] = int(sR4B[0])
    LimitSize.R4[1] = int(sR4B[1])
    LimitSize.R4[2] = int(sR4B[2])
    LimitSize.R4[3] = int(sR4B[3])
    LimitSize.R5[0] = int(sR5B[0])
    LimitSize.R5[1] = int(sR5B[1])
    LimitSize.R5[2] = int(sR5B[2])
    LimitSize.R5[3] = int(sR5B[3])
    LimitSize.B[0] = int(sBB[0])
    LimitSize.B[1] = int(sBB[1])
    LimitSize.B[2] = int(sBB[2])
    LimitSize.B[3] = int(sBB[3])
    LimitSize.Phi = float(rPhiB)
    LimitDistance.RightD[0] = float(rD1B[0])
    LimitDistance.RightD[1] = float(rD1B[1])
    LimitDistance.BottomD[0] = float(rD2B[0])
    LimitDistance.BottomD[1] = float(rD2B[1])
    # ↑ Converting string to correct data type.

    f.close()
