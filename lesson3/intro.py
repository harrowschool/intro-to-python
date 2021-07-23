subtitle = '''
Welcome to Lesson 3. In this lesson you will learn about selection. 

👈 On the sidebar on the left you will see folder called lesson 3. In this folder you will find one file for each task.
Read the instructions and edit the code accordingly.
When you are ready to run your code, enter the number of the task below.
'''

menu = CursesMenu("Lesson 3", subtitle)

topLevel = SelectionMenu([f"Task {i}" for i in range(1, 6)])
menu.append(topLevel)

for i in range(1,6):
  submenu = SelectionMenu(["Run Code", "Mark as Complete"])
  submenu_item = SubmenuItem(f"Task {i}", submenu, menu)
  menu.append(submenu_item)




# A FunctionItem runs a Python function when selected
function_item = FunctionItem("Call a Python function", input, ["Enter an input"])

# A CommandItem runs a console command
command_item = CommandItem("Run a console command",  "touch hello.txt")

# A SelectionMenu constructs a menu from a list of strings
selection_menu = SelectionMenu(["item1", "item2", "item3"])

# A SubmenuItem lets you add a menu (the selection_menu above, for example)
# as a submenu of another menu
submenu_item = SubmenuItem("Submenu item", selection_menu, menu)


# Finally, we call show to show the menu and allow the user to interact
menu.show()