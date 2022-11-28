#!/usr/bin/env python
# coding: utf-8

# In[23]:


import PySimpleGUI as sg
import os.path
import sys


sg.theme('Dark Grey 9')
layout = [[sg.Text("Pick an option:")], 
          [sg.Button("User Info"), sg.Button("Logs")], 
          [sg.Button("Exit")]]

UILayout = [[sg.Text("User Information")],
            [sg.Text("Enter Name:"), sg.InputText(), sg.Button("Save Name")],
            [sg.Text("Enter Phone Number: "), sg.InputText(), sg.Button("Save Number")],
            [sg.Button("Exit")]]

LogsLayout = [[sg.Text('File to open')],
              [sg.In(), sg.FileBrowse()],
              [sg.Button("Open"), sg.Button("Exit")]]

app = sg.Window("Motion Alarm", layout)

def openUI(layout):
    UIWindow = sg.Window("Info",layout)
    while True:
        event, values = UIWindow.read()
        
        
        if event == "Save Name":
            strValue = str(values[0])
            with open('ProjName.txt', 'a') as name:
                name.write(strValue)
                name.write('\n')
                name.close
                
        if event == "Save Number":
            strValue = str(values[1])
            with open('ProjNum.txt', 'a') as num:
                num.write(strValue)
                num.write('\n')
                num.close

                
        if event == "Exit":
            break
    UIWindow.close()

def openLogs(layout):
    LogsWindow = sg.Window("Logs", layout)
    while True:
        event, values = LogsWindow.read()
        if event == "Open":
            with open(values[0],'r') as log:
                contents = log.read()
                print(contents)
                log.close()
        
        if event == "Exit":
            break
    LogsWindow.close()
          
        
        
        
##### MAIN BRANCH ######
while True:
    event, values = app.read()
    if event == "User Info":
        openUI(UILayout)

    if event == "Logs":
        openLogs(LogsLayout)
        
    if event == "Exit":
        break
app.close()


# In[ ]:




