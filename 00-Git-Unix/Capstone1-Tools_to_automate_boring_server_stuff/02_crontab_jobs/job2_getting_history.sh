#!/bin/bash

HISTFILE=~/.bash_history  # Set the history file.
HISTTIMEFORMAT='%F %T '   # Set the hitory time format.
set -o history            # Enable the history.

cd <PATH-OF-FOLDER-OF-TASKS>;

file=<PATH-OUT-FILE>


echo "########################################" >> $file
history >> $file          # Save the history.
history -cw               # Clears the history of the current session.
