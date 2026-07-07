# 📁 Smart File Organizer

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-green?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)

A modern desktop application built with **Python** and **Tkinter** that automatically organizes files into categorized folders based on their extensions.

**Clean • Fast • Easy to Use**

</div>

---

# ✨ Features

* 📂 Browse and organize any folder
* 🖱️ Drag & Drop folder support
* 📁 Automatic file categorization
* 📊 Live progress bar
* 📈 File statistics summary
* ↩️ Undo last organization
* 📄 Export organization report
* 🛡️ Duplicate filename handling
* ⚠️ Error handling with pop-up notifications
* 🎨 Modern and user-friendly interface

---

# 📸 Application Preview

## 🏠 Home Screen

<p align="center">
<img src="assets/home.png" width="750">
</p>

---

## 🖱️ Drag & Drop Folder

<p align="center">
<img src="assets/drag_drop.png" width="750">
</p>

---

## 📊 File Organization Summary

<p align="center">
<img src="assets/organized.png" width="750">
</p>

---

## 📄 Generated Report

<p align="center">
<img src="assets/report.png" width="750">
</p>

---

## ↩️ Undo Operation

<p align="center">
<img src="assets/undo.png" width="750">
</p>

---

# 📂 Supported File Categories

| Category      | Extensions                                |
| ------------- | ----------------------------------------- |
| 🖼 Images     | png, jpg, jpeg, gif, bmp, webp            |
| 📄 Documents  | pdf, doc, docx, txt, ppt, pptx, xls, xlsx |
| 🎬 Videos     | mp4, mkv, avi, mov                        |
| 🎵 Music      | mp3, wav, flac                            |
| 📦 Archives   | zip, rar, 7z                              |
| 🐍 Python     | py                                        |
| ☕ Java        | java, class, jar                          |
| 🌐 Web        | html, css, js                             |
| ⚙ Executables | exe                                       |
| 📁 Others     | Unsupported extensions                    |

---

# 🏗️ Project Structure

```text
SmartFileOrganizer/
│
├── main.py
├── organizer.py
├── undo.py
├── report.py
├── theme.py
├── history.json
├── requirements.txt
├── README.md
├── .gitignore
└── assets/
```

---

# 🚀 Installation

## Clone the repository

```bash
git clone https://github.com/<your-username>/Smart-File-Organizer.git
```

## Navigate to the project

```bash
cd Smart-File-Organizer
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the application

```bash
python main.py
```

---

# 📊 How It Works

1. Select a folder using **Browse** or **Drag & Drop**.
2. Click **Organize Files**.
3. Files are automatically moved into categorized folders.
4. View the organization summary.
5. Export a report if needed.
6. Undo the last operation whenever required.

---

# 📄 Report Generation

The application generates an `organization_report.txt` containing:

* Date & Time
* Selected Folder
* Files organized in each category
* Total files processed

---

# ↩️ Undo Feature

Every file movement is stored in `history.json`.

If needed, clicking **Undo Last Operation** restores all files to their original locations.

---

# 🛠️ Tech Stack

* Python
* Tkinter
* tkinterdnd2
* JSON
* shutil
* os

---

# 📌 Key Highlights

* Modular architecture
* Desktop GUI application
* Automatic file categorization
* Progress tracking
* Duplicate file protection
* Report generation
* Undo functionality
* Drag & Drop support
* Clean and maintainable code

---

# 💡 Future Enhancements

* 🌙 Light/Dark Theme Toggle
* 📑 PDF Report Export
* ⚙️ Settings Panel
* 📂 Custom File Categories
* 🔍 File Search

---

# 👩‍💻 Author

**Krushnali Vikas Patil**

If you found this project useful, consider giving it a ⭐ on GitHub.

---
# **📚 Learning Project**

This project was developed as part of my Python learning journey to strengthen my understanding of GUI development, file handling, modular programming, and desktop application design. It is intended for educational purposes while following clean coding practices and real-world software organization.
