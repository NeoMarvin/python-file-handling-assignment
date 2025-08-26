# file_read_write.py

# Open input file and read content
with open("input.txt", "r") as infile:
    content = infile.read()

# Modify content (example: convert to uppercase)
modified_content = content.upper()

# Write to a new file
with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print("File has been read and modified successfully!")


# error_handling.py

filename = input("Enter the filename to open: ")

try:
    with open(filename, "r") as f:
        content = f.read()
        print("File content:\n", content)
except FileNotFoundError:
    print("Error: File not found. Please check the filename and try again.")
except Exception as e:
    print("An unexpected error occurred:", e)
