file_path = "/home/filedir/text.txt"
with open(file_path, "r") as f:
    content = f.read()
print("File content: ", content)
