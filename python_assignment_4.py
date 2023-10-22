import os
import shutil
from datetime import datetime

def backup_files(source_dir, dest_dir)
    try
        # Check if the source directory exists
        if not os.path.exists(source_dir)
            print(fSource directory '{source_dir}' does not exist.)
            return

        # Create the destination directory if it doesn't exist
        if not os.path.exists(dest_dir)
            os.makedirs(dest_dir)

        # Iterate over the files in the source directory
        for filename in os.listdir(source_dir)
            source_path = os.path.join(source_dir, filename)
            dest_path = os.path.join(dest_dir, filename)

            # Check if the destination file already exists
            while os.path.exists(dest_path)
                # Append a timestamp to ensure a unique filename
                timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
                name, ext = os.path.splitext(filename)
                filename = f{name}_{timestamp}{ext}
                dest_path = os.path.join(dest_dir, filename)

            # Copy the file from the source to the destination
            shutil.copy2(source_path, dest_path)
            print(fCopied {filename})

        print(Backup completed successfully.)

    except Exception as e
        print(fAn error occurred {e})

if __name__ == __main__
    import sys

    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3
        print(Usage python backup.py source_directory destination_directory)
    else
        source_dir = sys.argv[1]
        dest_dir = sys.argv[2]
        # Call the backup_files function with the source and destination directories
        backup_files(source_dir, dest_dir)
