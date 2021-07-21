choice = input("Which task would you like to run? ")

exec(open(f"task{choice}.py").read())