input_path = "/home/filedir/text.txt"
output_path = "/home/otherfiledir/text.txt"

with open(input_path, "r") as f:
    content = f.read()

with open(output_path, "w") as f:
    f.write(content)

print(f"Content copied from {input_path} to {output_path}")
