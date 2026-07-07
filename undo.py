import os
import json
import shutil


HISTORY_FILE = "history.json"


def undo_last_operation():

    if not os.path.exists(HISTORY_FILE):
        return False

    with open(HISTORY_FILE, "r") as file:
        history = json.load(file)

    if len(history) == 0:
        return False

    # Move files back in reverse order
    for move in reversed(history):

        source = move["destination"]
        destination = move["source"]

        if os.path.exists(source):

            os.makedirs(os.path.dirname(destination), exist_ok=True)

            shutil.move(source, destination)

            # Remove empty folder if possible
            parent = os.path.dirname(source)

            try:
                if len(os.listdir(parent)) == 0:
                    os.rmdir(parent)
            except:
                pass

    # Clear history
    with open(HISTORY_FILE, "w") as file:
        json.dump([], file, indent=4)

    return True