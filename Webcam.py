# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 16:05:39 2016

@author: SRINIVAS
"""
from pygame.locals import *
import pygame
import pygame.camera


pygame.camera.init()
pygame.camera.list_camera() #Camera detected or not
cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()
img = cam.get_image()
pygame.image.save(img,"filename.jpg")
