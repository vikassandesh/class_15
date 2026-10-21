file = open("student.txt", "a+")

file.write("Favourite Hobby: Football\n")
file.write("Favorite color: blue")
file.seek(0)


content1 = file.read()
print(content1)

file.close()