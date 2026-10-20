import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from pathlib import Path


class JPGOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CodeAlpha | JPG File Organizer")
        self.root.geometry("720x520")
        self.root.minsize(620, 460)
        self.root.configure(bg="#171923")

        self.folder_var = tk.StringVar()

        tk.Label(
            root, text="JPG FILE ORGANIZER", font=("Segoe UI", 20, "bold"),
            fg="#f7fafc", bg="#171923"
        ).pack(pady=(22, 4))
        tk.Label(
            root, text="Automatically collect .jpg and .jpeg files into one folder",
            font=("Segoe UI", 10), fg="#a0aec0", bg="#171923"
        ).pack(pady=(0, 18))

        controls = tk.Frame(root, bg="#171923")
        controls.pack(fill="x", padx=24)

        self.folder_entry = tk.Entry(
            controls, textvariable=self.folder_var, font=("Segoe UI", 10),
            bg="#2d3748", fg="#f7fafc", insertbackground="#f7fafc",
            relief="flat"
        )
        self.folder_entry.pack(side="left", fill="x", expand=True, ipady=9, padx=(0, 10))

        tk.Button(
            controls, text="Browse", command=self.browse_folder,
            bg="#4a5568", fg="white", activebackground="#718096",
            activeforeground="white", relief="flat", padx=14, pady=7,
            cursor="hand2"
        ).pack(side="left")

        actions = tk.Frame(root, bg="#171923")
        actions.pack(fill="x", padx=24, pady=14)

        tk.Button(
            actions, text="Organize JPG Files", command=self.organize_files,
            bg="#3182ce", fg="white", activebackground="#2b6cb0",
            activeforeground="white", relief="flat", padx=18, pady=10,
            cursor="hand2", font=("Segoe UI", 10, "bold")
        ).pack(side="left")

        tk.Button(
            actions, text="Reset Log", command=self.reset_log,
            bg="#4a5568", fg="white", activebackground="#718096",
            activeforeground="white", relief="flat", padx=18, pady=10,
            cursor="hand2"
        ).pack(side="left", padx=10)

        tk.Label(
            root, text="ACTIVITY LOG", font=("Segoe UI", 10, "bold"),
            fg="#cbd5e0", bg="#171923", anchor="w"
        ).pack(fill="x", padx=24, pady=(4, 7))

        self.log = scrolledtext.ScrolledText(
            root, height=13, font=("Consolas", 9), wrap="word",
            bg="#0d1117", fg="#cbd5e0", insertbackground="white",
            relief="flat", padx=10, pady=10
        )
        self.log.pack(fill="both", expand=True, padx=24, pady=(0, 18))
        self.write_log("Welcome! Choose a folder to begin.")
        self.write_log("Supported extensions: .jpg and .jpeg")

    def write_log(self, message):
        self.log.insert(tk.END, message + "\n")
        self.log.see(tk.END)

    def browse_folder(self):
        folder = filedialog.askdirectory(title="Select a folder")
        if folder:
            self.folder_var.set(folder)
            self.write_log(f"Selected folder: {folder}")

    def unique_destination(self, destination):
        """Return a non-existing path rather than overwrite a same-named file."""
        if not destination.exists():
            return destination
        stem, suffix = destination.stem, destination.suffix
        counter = 1
        while True:
            candidate = destination.with_name(f"{stem}_{counter}{suffix}")
            if not candidate.exists():
                return candidate
            counter += 1

    def organize_files(self):
        folder_text = self.folder_var.get().strip()
        if not folder_text:
            messagebox.showwarning("Folder required", "Please choose a folder first.")
            return

        source_dir = Path(folder_text)
        if not source_dir.is_dir():
            messagebox.showerror("Invalid folder", "The selected folder does not exist.")
            return

        target_dir = source_dir / "JPG_Files"
        try:
            # Only inspect files directly inside the selected folder, not subfolders.
            jpg_files = [
                item for item in source_dir.iterdir()
                if item.is_file() and item.suffix.lower() in (".jpg", ".jpeg")
            ]
            if not jpg_files:
                self.write_log("No JPG/JPEG files found in the selected folder.")
                messagebox.showinfo("Nothing to organize", "No JPG or JPEG files were found.")
                return

            target_dir.mkdir(exist_ok=True)
            moved = 0
            errors = 0
            self.write_log(f"Found {len(jpg_files)} JPG/JPEG file(s).")

            for source in jpg_files:
                try:
                    destination = self.unique_destination(target_dir / source.name)
                    shutil.move(str(source), str(destination))
                    self.write_log(f"Moved: {source.name} -> {destination.name}")
                    moved += 1
                except OSError as exc:
                    self.write_log(f"ERROR moving {source.name}: {exc}")
                    errors += 1

            summary = f"Finished. Moved: {moved}; errors: {errors}."
            self.write_log(summary)
            if errors:
                messagebox.showwarning("Completed with errors", summary)
            else:
                messagebox.showinfo("Success", summary)

        except OSError as exc:
            self.write_log(f"ERROR: {exc}")
            messagebox.showerror("File operation failed", str(exc))

    def reset_log(self):
        self.log.delete("1.0", tk.END)
        self.write_log("Log cleared.")


def main():
    root = tk.Tk()
    JPGOrganizerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
