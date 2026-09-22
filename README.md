# CodeAlpha_File_Organizer

This is a simple Python program that organizes JPG, JPEG and JFIF image files into a separate folder.

This project was made as part of the CodeAlpha Python Programming Internship.



## About the Project

The program checks the MyFiles folder and finds JPG, JPEG and JFIF image files. It then moves these files into a folder called Image_Files.

If the Image_Files folder does not exist, the program creates it automatically.



## Features

- Checks whether the source folder exists
- Creates the destination folder automatically
- Finds JPG, JPEG and JFIF files
- Moves the image files to the Image_Files folder
- Shows the names of the files that were moved
- Shows the total number of files moved
- Displays a message if no matching files are found



## Technologies Used

- Python
- os module
- shutil module



## Concepts Used

- Functions
- File handling
- Folder paths
- Loops
- If-else statements
- Strings
- os module
- shutil module



## Folder Structure

CodeAlpha_File_Organizer/
    
    MyFiles/
    
    file_organizer.py
    
    README.md

The Image_Files folder is created automatically when the program runs.



## How to Run

1. Create a folder named MyFiles in the project folder.
2. Put some JPG, JPEG or JFIF files inside the MyFiles folder.
3. Run the following command:

python file_organizer.py

4. The image files will be moved to:

MyFiles/Image_Files/



## Internship Task

CodeAlpha Python Programming Internship - Task 3: Task Automation with Python Scripts
