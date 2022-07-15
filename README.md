# 8 Ball Script
Why did I make this...
# How to Install 8 Ball Script
- Go to the Releases and Download the latest Release
- Create a New Folder or select an already existing one
- Copy the .exe into the Folder
- Done!
# How to use 8 Ball Script
Create a New File with the ending of .8ballbin and open it in your text editor of choice. This Language is a Binary Compiler, which means you need to know how to write Binary to use it. When you are done writing, drag and drop your .8ballbin file onto the .exe file. This will create a new file, "8ball_script.bin", which is the binary end result.

**Syntax:**

8 Ball Script is pretty simple, like in binary there are just ones and zeros, but instead its `:8ball:` for 0 and `:8ball::8ball:` for 1. Its seperated by `,` between 0 or 1 and `;` for the next sequence.

**Example:**

Hi:

:8ball:,:8ball::8ball:,:8ball:,:8ball:,:8ball::8ball:,:8ball:,:8ball:,:8ball:;:8ball:,:8ball::8ball:,:8ball::8ball:,:8ball:,:8ball::8ball:,:8ball:,:8ball:,:8ball::8ball:
```
:8ball:,:8ball::8ball:,:8ball:,:8ball:,:8ball::8ball:,:8ball:,:8ball:,:8ball:;:8ball:,:8ball::8ball:,:8ball::8ball:,:8ball:,:8ball::8ball:,:8ball:,:8ball:,:8ball::8ball:
```
<sub>This is a basic "Hi" sequence.</sub>
# (Build Deleted, Fix Will Release soon) How to use and make your own Plugins
Create a New Folder inside of your project folder called "plugins". In that folder create .json file named "plugins". Write the following code into the .json file:
```json
["your_plugin", "downloaded_plugin"]
```
<sub>Replace the items in the list with the plugin file names that you want to load.</sub>

To add or create a plugin, create or copy a Python File in the Plugins Folder and add the file name **without** the extension in the plugins.json file.
### How do Plugins work?
Plugins are Python files that run before or in the compile process. You can do pretty much anything you want.
