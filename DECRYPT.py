import os
from cryptography.fernet import Fernet


def decrypt(file):
	try:
		with open(file, "rb") as murgi:
			data = murgi.read()
			if data.startswith(b"gAAAAAB"):
				key = open("symetric.key").read()
				fernet = Fernet(key)
				decrypted = fernet.decrypt(data)
				with open(file, "wb") as dec:
					dec.write(decrypted)
				dec.close()
				file.replace(".ak", "")
	except Exception:
		return


for file in os.listdir():
	files = [os.path.basename(__file__), "symetric.key", "icon.ico", "LICENSE", "README.md",
		 "inf.ico", "bg_movie.jpg", "requirements.txt", "dec.py"]
	if file in files:
		continue
	elif os.path.isfile(file):
		decrypt(file)
