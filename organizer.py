import os
import shutil
import json

FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Python": [".py"],
    "Java": [".java", ".class", ".jar"],
    "Web": [".html", ".css", ".js"],
    "Executables": [".exe"]
}


def organize_files(folder, progress, status):

    if not os.path.exists(folder):
        raise Exception("Selected folder does not exist.")

    files = [
        file for file in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, file))
    ]

    if len(files) == 0:
        raise Exception("Selected folder is empty.")

    stats = {
        "Images": 0,
        "Documents": 0,
        "Videos": 0,
        "Music": 0,
        "Archives": 0,
        "Python": 0,
        "Java": 0,
        "Web": 0,
        "Executables": 0,
        "Others": 0
    }
    
    history = []

    total_files = len(files)
    progress["value"] = 0

    for index, file in enumerate(files):

        source = os.path.join(folder, file)
        extension = os.path.splitext(file)[1].lower()

        moved = False

        status.config(text=f"Moving: {file}")
        status.update_idletasks()

        for category, extensions in FILE_TYPES.items():

            if extension in extensions:

                destination_folder = os.path.join(folder, category)
                os.makedirs(destination_folder, exist_ok=True)

                destination = os.path.join(destination_folder, file)

                if os.path.exists(destination):

                    name, ext = os.path.splitext(file)
                    counter = 1

                    while os.path.exists(destination):
                        new_name = f"{name}({counter}){ext}"
                        destination = os.path.join(destination_folder, new_name)
                        counter += 1

                shutil.move(source, destination)

                history.append({
                      "source": source,
                      "destination": destination
                  })

                stats[category] += 1
                moved = True
                break

        if not moved:

            other_folder = os.path.join(folder, "Others")
            os.makedirs(other_folder, exist_ok=True)

            destination = os.path.join(other_folder, file)

            if os.path.exists(destination):

                name, ext = os.path.splitext(file)
                counter = 1

                while os.path.exists(destination):
                    new_name = f"{name}({counter}){ext}"
                    destination = os.path.join(other_folder, new_name)
                    counter += 1

            shutil.move(source, destination)

            history.append({
                "source": source,
                "destination": destination
            })

            stats["Others"] += 1

        progress["value"] = ((index + 1) / total_files) * 100
        progress.update_idletasks()

    status.config(text=f"✅ Successfully organized {total_files} files.")

    with open("history.json", "w") as file:
        json.dump(history, file, indent=4)

    return stats