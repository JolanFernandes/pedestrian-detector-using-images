#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import imutils
import tkinter as tk
from tkinter import filedialog

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
def open_image():
    # Ask the user to select an image file
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])

    if file_path:
        # Read the image using OpenCV
        image = cv2.imread(file_path)
        
        
        image = imutils.resize(image,
        width=min(400, image.shape[1]))

        (regions, _) = hog.detectMultiScale(image, 
        winStride=(4, 4),
        padding=(4, 4),
        scale=1.05)


        for (a, b, width, height) in regions:
            cv2.rectangle(image, (a, b), 
            (a + width, b + height), 
            (0, 255, 0), 2)
        cv2.imshow("Selected Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



# In[2]:


root = tk.Tk()
root.title("Pedestrian Recognition")
open_button = tk.Button(root, text="Select Image", command=open_image)
open_button.pack()
root.geometry("350x350")
root.mainloop()


# In[ ]:




