import os
from replit import db
from art import *

os.system("./setup.sh")
os.system("clear")

if "currentLesson" not in db:
  tprint("Python")
  print("**************************************")
  print("Hello and welcome to the Harrow School\nIntro to Python course!")
  print("**************************************")
  input("\nPress return to continue...")
  db["currentLesson"] = 1
  os.system("clear")

currentLesson = db["currentLesson"]
path = f"./lesson{currentLesson}/intro.py"
exec(open(path).read())

