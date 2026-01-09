import os
import re

def update_version_in_file(file_name, search_pattern):
    """
    Refactored to handle multiple files with one function to avoid code duplication.
    """
    # 1. Get environment variables
    # I'm using .get() to avoid crashing if the variables aren't set
    source_path = os.environ.get("SourcePath")
    build_num = os.environ.get("BuildNum")

    if not source_path or not build_num:
        print(f"Error: Environment variables not set for {file_name}")
        return

    # 2. Build the full path
    # Keeping the path structure requested in the original requirements
    target_dir = os.path.join(source_path, "develop", "global", "src")
    full_path = os.path.join(target_dir, file_name)

    if not os.path.exists(full_path):
        print(f"File not found: {full_path}")
        return

    # 3. Read and update the content
    # Using 'with' statements is best practice for safe file handling
    with open(full_path, 'r') as f:
        lines = f.readlines()

    updated_content = []
    for line in lines:
        # Regex replaces only the digits after the '=' 
        # based on the specific search_pattern passed in
        new_line = re.sub(search_pattern, r"\g<1>" + build_num, line)
        updated_content.append(new_line)

    # 4. Write the changes back to the file
    with open(full_path, 'w') as f:
        f.writelines(updated_content)
    
    print(f"Updated {file_name} successfully.")

def main():
    # Update SConstruct: matches 'point=' followed by digits
    update_version_in_file("SConstruct", r"(point=)\d+")
    
    # Update VERSION: matches 'ADLMSDK_VERSION_POINT=' followed by digits
    update_version_in_file("VERSION", r"(ADLMSDK_VERSION_POINT=)\d+")

if __name__ == "__main__":
    main()