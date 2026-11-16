# import os

# def cwd():
#     #Retrieves and displays the current working directory and its contents.
#     path = os.getcwd()
#     print(f"The current working directory is {path}")
#     print("The directory contains the following files:")
#     for file in os.listdir(path):
#         print(file)

# def run():
#     #Displays processing status and calls the cwd function.
#     print("Processing...")
#     cwd()

# if __name__ == "__main__":
#     run()

# Task 2.
# import os

# def display_chars(file_path, num_chars):
#     #Reads and displays the specified number of characters from the file.
#     print("The first 5 characters are:")
#     with open(file_path, 'r') as file:
#         content = file.read(num_chars)
#         print(content)
#     print()

# def display_line(file_path):
#     #Reads and displays the first line from the file.
#     print("The first line is:")
#     with open(file_path, 'r') as file:
#         line = file.readline().strip()
#         print(line)
#     print()

# def display_text(file_path):
#     #Reads and displays all the text contained in the file.
#     print("The full text is:")
#     with open(file_path, 'r') as file:
#         content = file.read()
#         print(content, end='')
#     print()

# def run_task2():
#     #Sets up the text file and calls the display functions.
#     # Ensure the week6 directory exists and create library.txt there
#     os.makedirs('week6', exist_ok=True)
#     file_content = (
#         "The Law Section\n"
#         "The Art Section\n"
#         "The Technology Section\n"
#         "The History Section"
#     )
    
#     # Save in week6/library.txt as requested
#     with open('week6/library.txt', 'w') as file:
#         file.write(file_content)
        
#     # Also create a local copy if running from the root directory referencing "library.txt"
#     with open('library.txt', 'w') as file:
#         file.write(file_content)

#     # Call each function with "library.txt" as the file path
#     display_chars("library.txt", 5)
#     display_line("library.txt")
#     display_text("library.txt")

# if __name__ == "__main__":
#     run_task2()


# Task 3.
# def search(filename):
#     print("Searching...")
#     with open(filename, 'r') as file:
#         for line in file:
#             # line.strip() removes any trailing newline characters from the file
#             print(f"Looked in {line.strip()}")
#     print("...Done!")

# def run_task3():
#     search("library.txt")

# # To run the program:
# run_task3()

# Task 4.
import os

def search_books(file_path):
    
    #Reads the book file, separates sections and book titles,
    #and returns them formatted.
    
    print("Searching...", end="")
    sections = ""
    books = "Books:\n"
    
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            # Ensure each line includes a newline character
            line_with_nl = line if line.endswith("\n") else line + "\n"
            
            if line.startswith("Section"):
                sections += line_with_nl
            else:
                books += line_with_nl
                
    print("Done!")
    return f"{sections}\n{books}"

def save(file_path, data):
    
    #Saves the provided data string to the specified file path.
    
    print("Saving...", end="")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(data)
    print("Done!")

def run_task4():
    
    #Coordinates reading from 'week6/books.txt' and saving to 'section-books.txt'.
    
    data = search_books("week6/books.txt")
    save("section-books.txt", data)

if __name__ == "__main__":
    # 1. Create the week6 directory if it doesn't exist
    os.makedirs("week6", exist_ok=True)
    
    # 2. Create and populate week6/books.txt with the required content
    with open("week6/books.txt", "w", encoding="utf-8") as f:
        f.write("Section: The Law Section\n")
        f.write("The Magna Carta\n")
        f.write("Section: The Technology Section\n")
        f.write("How to build a robot\n")
        f.write("How to build a flying car\n")
        f.write("Section: The History Section\n")
        f.write("The history of everything\n")
        
    # 3. Run the task
    run_task4()