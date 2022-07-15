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
import json, sys, os, importlib
from time import sleep as wait

if os.path.isfile("plugins/plugins.json"):

    with open("plugins/plugins.json") as f:

        plugin_load_list = json.load(f)
        print("\nGot Plugins to load:")
        print(plugin_load_list)
        print("\n")

    for plugin in plugin_load_list:

        import_plugin = importlib.import_module("plugins." + plugin)