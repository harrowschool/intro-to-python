import os
#from replit import db
from art import *
from cursesmenu import *
from cursesmenu.items import *

lessons = [
  {"name": "lesson1", 
  "complete": False,
  "tasks": [{"name": f"task{i}", "complete": False} for i in range(1,6)]
  },
  {"name": "lesson2", 
  "complete": False,
  "tasks": [{"name": f"task{i}", "complete": False} for i in range(1,6)]
  },
  {"name": "lesson3", 
  "complete": False,
  "tasks": [{"name": f"task{i}", "complete": False} for i in range(1,6)]
  },
  {"name": "lesson4", 
  "complete": False,
  "tasks": [{"name": f"task{i}", "complete": False} for i in range(1,4)]
  },
  {"name": "lesson5", 
  "complete": False,
  "tasks": [{"name": f"task{i}", "complete": False} for i in range(1,6)]
  },
  {"name": "lesson6", 
  "complete": False,
  "tasks": [{"name": f"task{i}", "complete": False} for i in range(1,5)]
  },
]

#if "lessons" not in db:
#  db["lessons"] = lessons
#else:
#  lessons = db["lessons"]

db = {"firstRun": False}

os.system("clear")

if "firstRun" not in db:
  tprint("Python")
  print("**************************************")
  print("Hello and welcome to the Harrow School\nIntro to Python course!")
  print("**************************************")
  input("\nPress return to continue...")
  db["firstRun"] = False
  os.system("clear")
  
def checkmark(complete):
  return " ✔︎" if complete else ""
  
def isLessonComplete(lesson):
  return all(task["complete"] for task in lesson["tasks"])

menu = CursesMenu()
  
def initMenu():  
  global menu
  menu = CursesMenu("Intro to Python", "Please select a lesson")
  
  for lesson in lessons:
    submenu = CursesMenu(lesson["name"], "Please select a task")
    
    for task in lesson["tasks"]:
      subsubmenu = CursesMenu(task["name"])
      
      lessonName = lesson["name"]
      taskName = task["name"]
      runCode = CommandItem("Run Code", f"python3 {lessonName}/{taskName}.py; python3 success.py")
      
      def markTaskAsComplete(task):
        task["complete"] = True
        initMenu()
        
      completeTask = FunctionItem("Mark Task as Complete", markTaskAsComplete, [task])
      
      subsubmenu.append_item(runCode)
      subsubmenu.append_item(completeTask)
      
      subsubmenuItem = SubmenuItem(task["name"] + checkmark(task["complete"]), subsubmenu, submenu)
      submenu.append_item(subsubmenuItem)
    
    submenuItem = SubmenuItem(lesson["name"] + checkmark(isLessonComplete(lesson)), submenu, menu)
    menu.append_item(submenuItem)
    
    def markLessonAsComplete(lesson):
      lesson["complete"] = True
      initMenu()
    
    #completeLesson = FunctionItem("Mark Lesson as Complete", markLessonAsComplete, [lesson])
    #submenu.append_item(completeLesson)
  
  menu.show()
  
initMenu()
  


#path = f"./lesson{currentLesson}/intro.py"
#exec(open(path).read())

