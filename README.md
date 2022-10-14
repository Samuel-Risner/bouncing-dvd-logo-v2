# bouncing dvd logo v2
Something to really annoy your friends!
Creates a dvd logo which continuously changes colour and moves around the screen.
# about the files
## /images
Contains the ".png" files which are used for changing the coulour of the logo. Aswell as the ".tif" files used for creating them.
## bouncing_dvd_logo.xml
Contains the data/stuff needed for creating a sheduled task.
## create_task.cmd
Creates a shedduled task using the above file. Needs administrator priviledges to run. Gets called from "deploy.cmd".
## deploy.cmd
Copys the important file into a new directory on the victims pc and runs the above file.
## last_name.txt
"main.exe" gets renamed by "launch.exe", because of this the current name of "main.exe" is saved here.
## launch.exe
Renames "main.exe" with a name from "valid_names.txt", saves the new name to "last_name.txt" and runs "main.exe".
## launch.py
The Python file for the above executable file.
## main.exe
Displays and moves the dvd logo and changes its colour.
## main.py
The Python file for the above executable file.
## valid_names.txt
The options to which "main.exe" can be renamed to.