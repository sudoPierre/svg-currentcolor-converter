import re
import os

def rewrite_svg_files(file_path):
    for file in os.listdir(file_path):
        completePath = os.path.join(file_path, file)
        # Make sure it's an SVG file
        if file[-4:] == (".svg"):
            content = open(completePath, 'r')
            
            # Read the content of the file
            innerContent = content.read()
            
            # Replace the fill and stroke color with currentColor
            updated_content = re.sub(r'fill="#?[a-zA-Z0-9]{1,20}"', 'fill="currentColor"', innerContent)
            updated_content = re.sub(r'stroke="#?[a-zA-Z0-9]{1,20}"', 'stroke="currentColor"', updated_content)
            # Close the file
            content.close()

            # Open the file in write mode

            # Write the updated content back to the file
            if updated_content != innerContent:
                content = open(completePath, 'w')
                content.write(updated_content)
                print(f'Changes made to the file: "{file}"')

                # Close the file
                content.close()
            else:
                print(f'No changes made to the file: "{file}"')

            # Erasing any blank space in the file name and capitalize the first letter of each word
            reName = ' '.join([word.capitalize() for word in file.split()])
            reName = reName.replace(" ", "")
            
            # if the file name has a space, it will be removed
            if reName != file:
                newPath = os.path.join(file_path, reName)
                os.rename(completePath, newPath)
                print(f'Renamed : "{file}" -> "{reName}"')

# Path to the folder containing the SVG files
file_path = './'
rewrite_svg_files(file_path)