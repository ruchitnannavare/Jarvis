from logging import error
import os
from sys import path
import time
from pywinauto import backend
from pywinauto.application import Application 
import win32api

#Variable Data
CiscoLocate = "C:/Program Files (x86)/Cisco/Cisco AnyConnect Secure Mobility Client/vpnui.exe"
Title = "Cisco AnyConnect Secure Mobility Client"
Title2 = "Cisco AnyConnect | Civica India"
Password = ""
CiscoApp = Application(backend="win32").start(CiscoLocate)
time.sleep(2)
CiscoApp = Application(backend="win32").connect(title=Title, visible_only=True)
CiscoApp.Dialog.Connect.click()
CiscoApp = Application(backend="win32").connect(title=Title2, visible_only=True, timeout=100)
CiscoApp.Dialog["Password:Edit"].type_keys(Password)
CiscoApp.Dialog.Ok.click()


