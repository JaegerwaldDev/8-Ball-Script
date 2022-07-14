import sys
final_file_content = ""
script_content = open(sys.argv[1], 'r').read()
print(script_content)
seperated_sequence = script_content.split(";")
print(seperated_sequence)
for item in seperated_sequence:
    seperated_characters = item.split(",")
    print(seperated_characters)
    for item in seperated_characters:
        print(item)
        if item == ":8ball:":
            final_file_content = final_file_content + "0"
        elif item == ":8ball::8ball:":
            final_file_content = final_file_content + "1"
    final_file_content = final_file_content + " "
    print(final_file_content)
with open("8ball_script.bin", "w") as f:
    f.write(final_file_content)
