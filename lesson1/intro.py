tprint("Lesson  1")
print("Welcome to Lesson 1. In this lesson you will learn about input, output and variables.")
print("👈 On the sidebar on the left you will see the tasks under lesson 1. In each file, you will find instructions to read and code to edit. You can run the code in each task by entering its number below.")

choice = input("Enter the number of the task you would like to run: ")

currentLesson = db["currentLesson"]
path = f"./lesson{currentLesson}/task{choice}.py"
exec(open(path).read())