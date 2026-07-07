from tkinter import *
from tkinterdnd2 import DND_FILES, TkinterDnD
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
from organizer import organize_files
from undo import undo_last_operation
from report import generate_report
import json
import os

# -------------------- Window -------------------- #

root = TkinterDnD.Tk()
root.title("📁 Smart File Organizer")
root.geometry("700x700")
root.resizable(False, False)
root.configure(bg="#1E1E2F")

folder_path = StringVar()
last_stats = None

# -------------------- Browse Folder -------------------- #

def browse():
    path = filedialog.askdirectory()

    if path:
        folder_path.set(path)
        status.config(
            text="Folder Selected",
            fg="lightgreen"
        )

def drop(event):

    folder = event.data.strip()

    # Remove curly braces added by Windows
    if folder.startswith("{") and folder.endswith("}"):
        folder = folder[1:-1]

    if os.path.isdir(folder):

        folder_path.set(folder)

        status.config(
            text="Folder dropped successfully!",
            fg="lightgreen"
        )

    else:

        messagebox.showerror(
            "Invalid Folder",
            "Please drop a folder, not a file."
        )
# -------------------- Organize Files -------------------- #

def organize():
    
    global last_stats
    if folder_path.get() == "":
        messagebox.showerror(
            "Error",
            "Please select a folder first."
        )
        return

    progress["value"] = 0
    root.update_idletasks()

    try:

        stats = organize_files(
            folder_path.get(),
            progress,
            status
        )
        last_stats = stats

        icons = {
            "Images": "🖼",
            "Documents": "📄",
            "Videos": "🎬",
            "Music": "🎵",
            "Archives": "📦",
            "Python": "🐍",
            "Java": "☕",
            "Web": "🌐",
            "Executables": "⚙",
            "Others": "📁"
        }

        summary = "📊 File Summary\n\n"

        for category, count in stats.items():
            summary += f"{icons[category]} {category:<12}: {count}\n"

        stats_label.config(text=summary)

        status.config(
            text="✅ Files organized successfully!",
            fg="lightgreen"
        )

        undo_button.config(state=NORMAL)

        messagebox.showinfo(
            "Success",
            "Files Organized Successfully!"
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )


# -------------------- Undo -------------------- #

def undo():

    success = undo_last_operation()

    if success:

        progress["value"] = 0

        status.config(
            text="Undo completed successfully.",
            fg="lightgreen"
        )

        stats_label.config(
            text="📊 No files organized yet."
        )

        undo_button.config(state=DISABLED)

        messagebox.showinfo(
            "Undo",
            "Last operation has been undone successfully!"
        )

    else:

        messagebox.showwarning(
            "Undo",
            "Nothing to undo."
        )

def export_report():

    global last_stats

    if last_stats is None:

        messagebox.showwarning(
            "Export Report",
            "Please organize files first."
        )

        return

    try:

        report_path = generate_report(
            folder_path.get(),
            last_stats
        )

        messagebox.showinfo(
            "Report Generated",
            f"Report saved successfully.\n\n{report_path}"
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )
# -------------------- Title -------------------- #

Label(
    root,
    text="📁 Smart File Organizer",
    font=("Segoe UI", 22, "bold"),
    bg="#1E1E2F",
    fg="white"
).pack(pady=20)


# -------------------- Folder Selection -------------------- #

frame = Frame(root, bg="#1E1E2F")
frame.pack(pady=10)

drop_frame = Frame(
    root,
    bg="#2B2D42",
    width=600,
    height=120,
    highlightbackground="#4CAF50",
    highlightthickness=2
)

drop_frame.pack(pady=20)

drop_frame.pack_propagate(False)

drop_label = Label(
    drop_frame,
    text="📂 Drag & Drop Folder Here",
    bg="#2B2D42",
    fg="white",
    font=("Segoe UI", 14, "bold")
)

drop_label.pack(expand=True)
drop_frame.drop_target_register(DND_FILES)
drop_frame.dnd_bind("<<Drop>>", drop)

drop_label.drop_target_register(DND_FILES)
drop_label.dnd_bind("<<Drop>>", drop)

Entry(
    frame,
    textvariable=folder_path,
    width=55,
    font=("Segoe UI", 11)
).grid(row=0, column=0, padx=10)

Button(
    frame,
    text="Browse",
    command=browse,
    bg="#4CAF50",
    fg="white",
    width=15,
    font=("Segoe UI", 10, "bold")
).grid(row=0, column=1)


# -------------------- Organize Button -------------------- #

Button(
    root,
    text="📂 Organize Files",
    command=organize,
    bg="#2196F3",
    fg="white",
    width=25,
    height=2,
    font=("Segoe UI", 11, "bold")
).pack(pady=15)


# -------------------- Undo Button -------------------- #

undo_button = Button(
    root,
    text="↩ Undo Last Operation",
    command=undo,
    bg="#FF9800",
    fg="white",
    width=25,
    height=2,
    font=("Segoe UI", 11, "bold"),
    state=DISABLED
)

undo_button.pack(pady=10)

report_button = Button(
    root,
    text="📄 Export Report",
    command=export_report,
    bg="#673AB7",
    fg="white",
    width=25,
    height=2,
    font=("Segoe UI", 11, "bold")
)

report_button.pack(pady=10)

# Enable Undo button if history exists

if os.path.exists("history.json"):

    try:

        with open("history.json", "r") as file:
            history = json.load(file)

        if len(history) > 0:
            undo_button.config(state=NORMAL)

    except:
        pass


# -------------------- Progress Bar -------------------- #

progress = Progressbar(
    root,
    orient="horizontal",
    mode="determinate",
    length=500
)

progress.pack(pady=20)


# -------------------- Status -------------------- #

status = Label(
    root,
    text="Select a folder to organize",
    font=("Segoe UI", 11),
    bg="#1E1E2F",
    fg="white"
)

status.pack(pady=10)


# -------------------- Statistics -------------------- #

stats_label = Label(
    root,
    text="📊 No files organized yet.",
    justify=LEFT,
    anchor="w",
    bg="#1E1E2F",
    fg="white",
    font=("Consolas", 11)
)

stats_label.pack(pady=20)


# -------------------- Footer -------------------- #

Label(
    root,
    text="Organize your files automatically by file type",
    bg="#1E1E2F",
    fg="gray",
    font=("Segoe UI", 9)
).pack(side=BOTTOM, pady=15)


# -------------------- Run -------------------- #

root.mainloop()