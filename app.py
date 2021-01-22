# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 13:06:48 2021
@author: Asia
"""

import tkinter as app
from tkinter import filedialog
from PIL import Image, ImageTk


"""
Our libraries:
"""
import Watershed_library  as wtr
import CannyHough_library as ch
import Laplacian_library  as lap
import Skeletone_library  as ske

title = "Detection of Nanofibers in SEM Images"

root = app.Tk()
root.title(title)

imgs=[]
var = app.StringVar()
varYesNo = app.StringVar()
varYesNo.set(2)
varType = app.StringVar()
varType.set(1)
varSkel = app.StringVar()
varSkel.set(1)
varSkelType = app.StringVar()
varSkelType.set(1)


def openImage():
        imageName=filedialog.askopenfilename(initialdir="/", title="Select File",filetypes=(("image_files","*.jpg"),("all files", "*.*")))
        imgs.append(imageName)
                                            
        for images in imgs:
            load = Image.open(images)          
            resized = load.resize((int(img_width),int(img_height)),Image.ANTIALIAS)
            render = ImageTk.PhotoImage(resized)
            img = app.Label(frameInput, image=render)
            img.image = render
            img.place(x=0,y=0)
            
            label_img_nm =app.Label(frameImgName, textvariable=var_img_nm, bg="silver")
            label_img_nm.pack(side=app.RIGHT)
            var_img_nm.set(imageName)
            

def runAlgorithm():  #command to not only run script but also to show the output image
        
        if not imgs:
            app.messagebox.showinfo(title="Info", message="First you need to choose an input image (Use: Open Image)")
        else:
            selection = str(var.get())
            runType = varType.get()
            
            if (selection=='1'):  
                outputImg, directory, img2Hough = ch.runCannyAlgorithm(imgs[-1],runType)#remember to correct the name
  
            elif(selection=='2'):              
                outputImg, directory, img2Hough = wtr.runWatershedAlgorithm(imgs[-1],runType)
            
            elif(selection=='3'):
                outputImg, directory, img2Hough = lap.runLaplacianAlgorithm(imgs[-1],runType)

            else:
                app.messagebox.showinfo(title="Information", message="Choose one method you want to check")
            
            print(str(varYesNo.get()))
            
            if str(varYesNo.get()) == '1':
                print('Here we are')
                outputImg, directory = ch.runHoughAlgorithm(img2Hough,directory,runType)
            
            
            load = Image.open(directory)
            resized = load.resize((int(img_width),int(img_height)),Image.ANTIALIAS)
            render = ImageTk.PhotoImage(resized)
            
            img = app.Label(frameOutput, image=render)
            img.image = render#was render
            img.place(x=0,y=0)

def empty_function(*args):
    pass


def runSkeletone():
    if not imgs:
        app.messagebox.showinfo(title="Info", message="First you need to choose an input image (Use: Open Image)")
    
    else:
        selection = str(varSkel.get())
        runType = varSkelType.get()        
        
        if (selection=='1'):  
            outputImg, directory,_ = ske.runSkeletone(imgs[-1],runType)#remember to correct the name
                
        elif(selection=='2'):
            outputImg, directory = ske.runSegmSkeletone(imgs[-1],runType)#remember to add Hough to it
      
        load = Image.open(directory)
        resized = load.resize((int(img_width),int(img_height)),Image.ANTIALIAS)
        render = ImageTk.PhotoImage(resized)
                  
        img = app.Label(frameOutput, image=render)
        img.image = render#was render
        img.place(x=0,y=0)       
            
##################################### BLOCKS DEFINITIONS #####################################

#####################################      frames        #####################################
img_width = 1024*0.7
img_height = 600*0.7
margin = 8
canvas = app.Canvas(root, height=600, width=2*img_width+3*margin, bg="silver")
canvas.pack()

frameImgName = app.Frame(root, width=2*img_width+1.5*margin,height = 15, bg="silver")
frameImgName.place(relx=0.005, rely= 0.015)

frameInput = app.Frame(root, width=img_width, height=600*0.7, bg="white",highlightbackground="gray", highlightthickness=2)
frameInput.place(relx=0.005, rely= 0.05)

frameOutput = app.Frame(root, width=img_width, height=600*0.7, bg="white",highlightbackground="gray", highlightthickness=2)
frameOutput.place(relx=0.505, rely= 0.05)

frameOptions = app.Frame(root, bg="#9FC5C6", highlightbackground="gray", highlightthickness=2)
frameOptions.place(relwidth=0.99, relheight=0.2, relx=0.005, rely= 0.77)

frameRadioBtns = app.Frame(root, bg="#9FC5C6", highlightbackground="gray", highlightthickness=1)
frameRadioBtns.place(relwidth=0.1, relheight=0.16, relx=0.15, rely= 0.79)

frameRadioBtns1 = app.Frame(root, bg="#9FC5C6", highlightbackground="gray", highlightthickness=1)
frameRadioBtns1.place(relwidth=0.1, relheight=0.16, relx=0.26, rely= 0.79)

frameRadioBtns2 = app.Frame(root, bg="#9FC5C6", highlightbackground="gray", highlightthickness=1)
frameRadioBtns2.place(relwidth=0.1, relheight=0.16, relx=0.37, rely= 0.79)

frameRadioBtns3 = app.Frame(root, bg="#9FC5C6", highlightbackground="gray", highlightthickness=1)
frameRadioBtns3.place(relwidth=0.1, relheight=0.16, relx=0.62, rely= 0.79)

frameRadioBtns4 = app.Frame(root, bg="#9FC5C6", highlightbackground="gray", highlightthickness=1)
frameRadioBtns4.place(relwidth=0.1, relheight=0.16, relx=0.73, rely= 0.79)

#####################################        labels       #####################################
var_img_nm = app.StringVar()

var_met = app.StringVar()
label_met =app.Label(frameRadioBtns, textvariable=var_met,bg="#9FC5C6")
var_met.set("Fibers detection method:")
label_met.pack()

var_phl = app.StringVar()
label_phl =app.Label(frameRadioBtns1, textvariable=var_phl,bg="#9FC5C6")
#var_phl.set("+ Probabilistic")
var_phl.set("Hough Lines:")
label_phl.pack()

var_set = app.StringVar()
label_set =app.Label(frameRadioBtns2, textvariable=var_set,bg="#9FC5C6")
var_set.set("Detector settings:")
label_set.pack()

var_skel = app.StringVar()
label_skel =app.Label(frameRadioBtns3, textvariable=var_skel,bg="#9FC5C6")
var_skel.set("Skeleton type:")
label_skel.pack()

var_set2 = app.StringVar()
label_set2 =app.Label(frameRadioBtns4, textvariable=var_skel,bg="#9FC5C6")
var_set2.set("Skeleton settings:")
label_set2.pack()

#####################################    radio buttons    #####################################

method1 = app.Radiobutton(frameRadioBtns, bg="#9FC5C6", text='Canny Edge',variable=var, value=1)
method1.pack()
method3 = app.Radiobutton(frameRadioBtns, bg="#9FC5C6",text='Watershed', variable=var,value=2)
method3.pack()
method4 = app.Radiobutton(frameRadioBtns, bg="#9FC5C6",text='Laplacian Filter', variable=var,value=3)
method4.pack()

hough_yes = app.Radiobutton(frameRadioBtns1, bg="#9FC5C6",text='Yes', variable=varYesNo,value=1)
hough_yes.pack()
hough_no = app.Radiobutton(frameRadioBtns1, bg="#9FC5C6",text='No', variable=varYesNo,value=2)
hough_no.pack()

run_type1 = app.Radiobutton(frameRadioBtns2, bg="#9FC5C6",text='Default', variable=varType,value=1)
run_type1.pack()
run_type2 = app.Radiobutton(frameRadioBtns2, bg="#9FC5C6",text='Manual', variable=varType,value=2)
run_type2.pack()

skel1 = app.Radiobutton(frameRadioBtns3, bg="#9FC5C6",text='Basic', variable=varSkel,value=1)
skel1.pack()
skel2 = app.Radiobutton(frameRadioBtns3, bg="#9FC5C6",text='Segmenting', variable=varSkel,value=2)
skel2.pack()

run_skel_type1 = app.Radiobutton(frameRadioBtns4, bg="#9FC5C6",text='Default', variable=varSkelType,value=1)
run_skel_type1.pack()
run_skel_type2 = app.Radiobutton(frameRadioBtns4, bg="#9FC5C6",text='Manual', variable=varSkelType,value=2)
run_skel_type2.pack()

#####################################        buttons       #####################################

openFile = app.Button(frameOptions, text="Open Image", padx=10, pady=8,fg="white", bg="gray", command=openImage)
openFile.place(relx=0.04, rely=0.31)

runScript = app.Button(frameOptions, text="Run Detection" ,padx=10, pady=8, fg="white", bg="gray", command=runAlgorithm)
runScript.place(relx=0.5,rely=0.31)

runSkelet = app.Button(frameOptions, text="Run Skeletonization" ,padx=10, pady=8, fg="white", bg="gray", command=runSkeletone)
runSkelet.place(relx=0.86,rely=0.31)


root.resizable(width=False, height=False)

root.mainloop()
