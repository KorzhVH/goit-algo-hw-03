import os
import shutil
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("dest", nargs='?', default="dist")
    return parser.parse_args()


def copy_and_sort_files(src, dest):
    # Create the destination directory if it does not exist
    if not os.path.exists(dest):
        os.makedirs(dest)
    # Iterate over all items in the source directory
    for item in os.listdir(src):
        src_item = os.path.join(src, item)
        if os.path.isdir(src_item):
            # Recursively process the directory
            copy_and_sort_files(src_item, dest)
        elif os.path.isfile(src_item):
            try:
                # Process the file
                file_extension = os.path.splitext(item)[1].lstrip(".").lower()
                if not file_extension:
                    file_extension = "no_extension"
                dest_path = os.path.join(dest, file_extension)

                # Create the subdirectory for the file extension if it does not exist
                if not os.path.exists(dest_path):
                    os.makedirs(dest_path)

                # Copy the file to the appropriate subdirectory
                shutil.copy2(src_item, dest_path)
            except Exception as e:
                print(f"Failed to copy {src_item}: {e}")


def main():
    # Parse the command-line arguments
    args = parse_arguments()
    source_dir = args.source
    destination_dir = args.dest

    # Check if the source directory exists
    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return

    # Start the file copying and sorting process
    copy_and_sort_files(source_dir, destination_dir)
    print(f"Files have been copied and sorted into '{destination_dir}'")


if __name__ == "__main__":
    main()