tprint("Lesson  1")
print("Welcome to Lesson 1. In this lesson you will learn about input, output and variables.")
print("\n👈 On the sidebar on the left you will see folder called lesson 1.")
print("In this folder you will find one file for each task.")
print("Read the instructions and edit the code accordingly.")
print("When you are ready to run your code, enter the number of the task below.")

choice = input("\nEnter the number of the task you would like to run: ")

currentLesson = db["currentLesson"]
path = f"./lesson{currentLesson}/task{choice}.py"
exec(open(path).read())