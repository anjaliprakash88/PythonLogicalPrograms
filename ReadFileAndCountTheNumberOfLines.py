<<<<<<< HEAD
with open("count") as file:
    lines = file.readlines()
    lines = [line for line in lines if line.strip()]
    total_lines = len(lines)
=======
with open("count") as file:
    lines = file.readlines()
    lines = [line for line in lines if line.strip()]
    total_lines = len(lines)
>>>>>>> 7139c4579c85c35b896b6146dcf0799b485ae836
    print("Total: ", total_lines)