import os
from datetime import datetime


import os
from datetime import datetime
import re

def process_content(content):
    # Replace {{without space with {{ with space
    return re.sub(r'\{\{(?!\s)', '{{ ', content)

def write_directory_contents(directories, specific_files, output_file, file_extensions=None, exclude_dirs=None, exclude_files=None):
    if exclude_dirs is None:
        exclude_dirs = ['.git', '__pycache__', 'venv', 'env']

    if exclude_files is None:
        exclude_files = ['.DS_Store']

    with open(output_file, 'w', encoding='utf-8') as f:
        # Write header with timestamp
        f.write(f"Directory Contents Export - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 80 + "\n\n")

        # Process specific files first
        for file_path in specific_files:
            abs_file_path = os.path.abspath(os.path.expanduser(file_path))

            if not os.path.exists(abs_file_path):
                f.write(f"File not found: {abs_file_path}\n\n")
                continue

            try:
                # Write full file path and contents
                f.write(f"File: {abs_file_path}\n")
                f.write("-" * len(f"File: {abs_file_path}") + "\n")

                # Write file contents
                with open(abs_file_path, 'r', encoding='utf-8') as file_content:
                    content = file_content.read()
                    processed_content = process_content(content)
                    f.write(processed_content)
                    f.write("\n\n")

            except Exception as e:
                f.write(f"Error reading file {abs_file_path}: {str(e)}\n\n")

        # Process directories
        for directory in directories:
            # Convert to absolute path
            abs_directory = os.path.abspath(os.path.expanduser(directory))

            if not os.path.exists(abs_directory):
                f.write(f"Directory not found: {abs_directory}\n\n")
                continue

            for root, dirs, files in os.walk(abs_directory):
                # Skip excluded directories
                dirs[:] = [d for d in dirs if d not in exclude_dirs]

                # Process files
                for file in sorted(files):
                    # Skip excluded files
                    if file in exclude_files:
                        continue

                    file_path = os.path.join(root, file)

                    # Check file extension if specified
                    if file_extensions:
                        if not any(file.lower().endswith(ext.lower()) for ext in file_extensions):
                            continue

                    try:
                        # Write full file path and contents
                        f.write(f"File: {file_path}\n")
                        f.write("-" * len(f"File: {file_path}") + "\n")

                        # Write file contents
                        with open(file_path, 'r', encoding='utf-8') as file_content:
                            content = file_content.read()
                            processed_content = process_content(content)
                            f.write(processed_content)
                            f.write("\n\n")

                    except Exception as e:
                        f.write(f"Error reading file {file_path}: {str(e)}\n\n")

def main():
    # Example usage - now you can use absolute paths, relative paths, or paths with ~
    directories = [
        '/Users/shawnveltman/code/health/resources/views/components/medical_record/fields',
        # '/Users/shawnveltman/code/health/app/Services/MedicalRecordComponent',
        # '/Users/shawnveltman/code/pod/resources/js',
    ]

    # Add specific files you want to include
    specific_files = [
        # '/Users/shawnveltman/code/health/resources/views/components/medical_record/fields/date.blade.php',
        # '/Users/shawnveltman/code/health/resources/views/components/medical_record/fields/radio.blade.php',
        # '/Users/shawnveltman/code/health/resources/views/components/medical_record/fields/date-inputs.blade.php',
        # '/Users/shawnveltman/code/health/app/Livewire/MedicalRecordComponent.php',
        # '/Users/shawnveltman/code/health/app/Services/MedicalRecordComponent/FrontEndSchemaService.php',
        # '/Users/shawnveltman/code/health/resources/views/livewire/medical-record-component.blade.php',
        '/Users/shawnveltman/code/health/resources/views/components/medical_record/fields/editing-field.blade.php',

    ]

    output_file = "combined_code.txt"

    # Optional: specify file extensions to include
    # file_extensions = ['.py', '.txt', '.md']  # Add or modify extensions as needed

    # Optional: specify additional directories to exclude
    # exclude_dirs = ['.git', '__pycache__', 'venv', 'env', 'node_modules']

    # Optional: specify files to exclude
    exclude_files = ['.DS_Store']

    write_directory_contents(
        directories,
        specific_files,
        output_file,
        exclude_dirs=None,
        exclude_files=exclude_files
    )

    print(f"Directory contents have been written to {output_file}")


if __name__ == "__main__":
    main()
