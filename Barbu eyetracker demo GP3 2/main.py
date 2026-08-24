#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 14:05:31 2021
 
@author: Barbu
"""
 
from psychopy import prefs
prefs.hardware['audioLib'] = ['PTB']
 
import os, sys, time
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from psychopy import visual, sound, constants
from psychopy import core
from ImageClass import ViennaFestival
from psychopy.hardware import keyboard
 
# =============================================================================
# PRELIMINARIES
# =============================================================================
# Eyetracker monitor resolution
# Auto-detected from the actual connected display (screen index 1, matching
# the `screen = 1` used for psychopyWindow below) instead of hardcoding
# 1920x1080, so this works correctly on whatever monitor it's run on.
import pyglet
_display = pyglet.canvas.get_display()
_screens = _display.get_screens()
_screenIndex = 1 if len(_screens) > 1 else 0  # fall back to the only screen if a second monitor isn't connected
resolution = (_screens[_screenIndex].width, _screens[_screenIndex].height)
print(f"DEBUG: auto-detected resolution for screen {_screenIndex}: {resolution}")
 
# Open main window
psychopyWindow = visual.Window(size = resolution, 
                               screen = 1, fullscr = True,
                               units = 'height', 
                               color = 'black', 
                               colorSpace = "rgb", 
                               winType = "pyglet", 
                               waitBlanking = False, 
                               allowGUI = False)
 
 
# # Open window where experimenter can track gaze data
experimenterWindow = visual.Window(size = (480, 270), 
                                    pos = (50, 50),
                                    screen = 0, 
                                    fullscr = False, units = 'height',
                                    color = 'white', winType = "pyglet", 
                                    waitBlanking = False, allowGUI = True)
 
 
# =============================================================================
# INFORMATION ON CURRENTLY TESTED SUBJECT
# =============================================================================
usingEyetracker = True
calibrated = False
 
# =============================================================================
# INITIALIZE EXPERIMENT
# =============================================================================
exp = ViennaFestival(psychopyWindow, 
                    experimenterWindow, 
                    usingEyetracker = usingEyetracker)
 
# =============================================================================
# CALIBRATION
# =============================================================================
if usingEyetracker:
    #exp.adjustPosition()
    numPoints = 5
    exp.calibrate(numPoints = numPoints)
 
print("--------------------")
print("Calibration over.")
print("--------------------")
 
while True:
    task = exp.chooseNextTask()
    if not task:
        break
 
 
# =============================================================================
# CLOSE
# =============================================================================
psychopyWindow.close()
experimenterWindow.close()
core.quit()