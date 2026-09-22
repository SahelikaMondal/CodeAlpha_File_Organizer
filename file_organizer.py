import os
import shutil


def organize_files():
    source_folder = "MyFiles"
    destination_folder = os.path.join(source_folder, "Image_Files")

    print("\n" + "=" * 45)
    print("           IMAGE FILE ORGANIZER")
    print("=" * 45)

    # Check if source folder exists
    if not os.path.exists(source_folder):
        print("Source folder 'MyFiles' was not found.")
        return

    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print("Created folder: Image_Files")

    moved_count = 0

    # Check all items in the source folder
    for filename in os.listdir(source_folder):

        source_path = os.path.join(source_folder, filename)

        # Make sure it is a file
        if os.path.isfile(source_path):

            # Check for JPG, JPEG and JFIF images
            if filename.lower().endswith((".jpg", ".jpeg", ".jfif")):

                destination_path = os.path.join(
                    destination_folder,
                    filename
                )

                shutil.move(source_path, destination_path)

                print(f"Moved: {filename}")
                moved_count += 1

    print("-" * 45)

    if moved_count == 0:
        print("No JPG, JPEG or JFIF files were found.")
    else:
        print(f"Successfully moved {moved_count} image file(s).")

    print("=" * 45)


if __name__ == "__main__":
    organize_files()