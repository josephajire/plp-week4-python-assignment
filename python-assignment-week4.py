# Step 1: Creation of an original file with 'agriculture_note.txt' as file name
with open("agriculture_note.txt", "w") as file:
    file.write("Agriculture is the backbone of many economies.\n")
    file.write("It provides food, raw materials, and employment opportunities.\n")
print("File named 'agriculture_note.txt' created successfully.")


# Step 2: Asking the user for filename
filename = input("Enter the filename to read (e.g., agriculture_note.txt): ")


# Step 3: Reading the file (e.g., agriculture_note.txt) and writing a 
# modified version to a new file named 'updated_agriculture_note.txt'
# with error handling.

try:
    # Reading the content of the file
    with open(filename, "r") as file:
        content = file.readlines()
        print(content)

    # The modification to the file is the addition of another statement
    content.append("Modern agriculture uses technology to increase productivity.\n")

    # Saving updated content to a new file
    with open("updated_agriculture_note.txt", "w") as new_file:
        new_file.writelines(content)

    print("File modified and saved as 'updated_agriculture_note.txt'.")

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except IOError:
    print(f"Error: Could not read the file '{filename}'.")
