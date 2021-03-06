tprint("Lesson 3")
print("Welcome to Lesson 3. In this lesson you will learn about selection.")
print("\nš On the sidebar on the left you will see folder called lesson 3.")
print("In this folder you will find one file for each task.")
print("Read the instructions and edit the code accordingly.")
print("When you are ready to run your code, enter the number of the task below.")

choice = input("\nEnter the number of the task you would like to run: ")

if choice in [String(n) for n in range(1,6)]:
    currentLesson = db["currentLesson"]
    path = f"./lesson{currentLesson}/task{choice}.py"
    exec(open(path).read())
else:
    print("ERROR: Invalid task number. Please try again.")  