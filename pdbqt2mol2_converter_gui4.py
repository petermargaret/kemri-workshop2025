import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk  # Requires Pillow: pip install pillow
import subprocess
import os

input_file = ""
output_dir = ""

def select_input_file():
    global input_file
    input_file = filedialog.askopenfilename(filetypes=[("PDBQT files", "*.pdbqt")])
    if input_file:
        input_label.config(text=f"Input: {os.path.basename(input_file)}", fg="white")

def select_output_dir():
    global output_dir
    output_dir = filedialog.askdirectory()
    if output_dir:
        output_label.config(text=f"Output: {output_dir}", fg="black")

def convert_pdbqt_to_mol2():
    if not input_file or not output_dir:
        messagebox.showwarning("Missing Info", "Please select an input file and output folder.")
        return

    if not os.path.exists(input_file):
        messagebox.showerror("Error", f"Input file not found: {input_file}")
        return

    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_file = os.path.join(output_dir, base_name + ".mol2")

    try:
        subprocess.run(['obabel', '-ipdbqt', input_file, '-omol2', '-O', output_file], check=True)
        messagebox.showinfo("Success", f"Converted to: {output_file}")
    except FileNotFoundError:
        messagebox.showerror("Error", "Open Babel (obabel) not found. Make sure it’s installed and in your PATH.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Conversion failed:\n{e}")

# GUI setup
root = tk.Tk()
root.title("PDBQT to MOL2 Converter")
root.geometry("450x400")
root.configure(bg="black")

# 🖼️ Load and display logo
try:
    logo_img = Image.open("logo.png")  # Make sure logo.png is in the same folder
    logo_img = logo_img.resize((150, 150), Image.Resampling.LANCZOS)
    logo_photo = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(root, image=logo_photo, bg="black")
    logo_label.pack(pady=10)
except Exception as e:
    print(f"Logo not found or failed to load: {e}")

# 🔴 Red Title
tk.Label(root, text="PDBQT ➜ MOL2 Converter", fg="red", bg="black", font=("Helvetica", 16, "bold")).pack(pady=5)

# Input/output controls
tk.Button(root, text="Select .pdbqt File", command=select_input_file, width=30, bg="white").pack(pady=5)
input_label = tk.Label(root, text="Input: None selected", bg="black", fg="red")
input_label.pack()

tk.Button(root, text="Choose Output Directory", command=select_output_dir, width=30, bg="white").pack(pady=5)
output_label = tk.Label(root, text="Output: None selected", bg="black", fg="red")
output_label.pack()

# Convert button
tk.Button(root, text="Convert to .mol2", command=convert_pdbqt_to_mol2, width=25, bg="black", fg="red").pack(pady=20)

root.mainloop()
