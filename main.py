"""
This File was written by Jaegerwald under the GNU General Public License v3.

Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications,
which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved.
Contributors provide an express grant of patent rights.

Permissions:
- Commercial use
- Modification
- Distribution
- Patent use
- Private use

Limitations:
- Liability
- Warranty

Conditions:
- License and copyright notice
- State changes
- Disclose source
- Same license
"""

# Import the necessary librarys.
import sys
import plugin_handler
from time import sleep as wait

# Define an empty string variable, that resembles the final file.
final_file_content = ""

# Get the path of the file that was dropped onto the executable and read the content into a variable.
script_content = open(sys.argv[1], "r").read()

if sys.argv[1].endswith(".bin"):

    # Split the script content into a list at space.
    seperated_sequence = script_content.split(" ")

    # Repeat for each item in the created list.
    for item in seperated_sequence:

        # Split the sequence into a list at.
        seperated_characters = [char for char in item]

        # Repeat for each item in the created list.
        for item in seperated_characters:

            # Convert binary into ":8ball:".
            if item == "0":

                final_file_content = final_file_content + ":8ball:"

            elif item == "1":

                final_file_content = final_file_content + ":8ball::8ball:"

            final_file_content = final_file_content + ","

        if final_file_content.endswith(","):

            # Remove the last character.
            final_file_content = final_file_content[:-1]

        final_file_content = final_file_content + ";"

    # Remove the last two characters.
    final_file_content = final_file_content[:-2]

    # Open or create the final file and write the final file content into it.
    with open("binary_script.8ballbin", "w") as final_file:

        final_file.write(final_file_content)

else:

    # Split the script content into a list at ";".
    seperated_sequence = script_content.split(";")

    # Repeat for each item in the created list.
    for item in seperated_sequence:

        # Split the sequence into a list at ",".
        seperated_characters = item.split(",")

        # Repeat for each item in the created list.
        for item in seperated_characters:

            # Convert :8ball: into 0 or 1.
            if item == ":8ball:":

                final_file_content = final_file_content + "0"

            elif item == ":8ball::8ball:":

                final_file_content = final_file_content + "1"

        final_file_content = final_file_content + " "

    # Remove the last character.
    final_file_content = final_file_content[:-1]

    # Open or create the final file and write the final file content into it.
    with open("8ball_script.bin", "w") as final_file:

        final_file.write(final_file_content)
