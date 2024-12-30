import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate a random password
def generate_password():
    try:
        # Get user inputs for length and complexity
        length = int(entry_length.get())
        complexity = complexity_var.get()
        
        if length < 6:
            messagebox.showwarning("Input Error", "Password length must be at least 6 characters.")
            return
        
        # Define character sets based on complexity level
        if complexity == 1:
            characters = string.ascii_letters  # Letters only
        elif complexity == 2:
            characters = string.ascii_letters + string.digits  # Letters + numbers
        elif complexity == 3:
            characters = string.ascii_letters + string.digits + string.punctuation  # Letters + numbers + symbols
        else:
            messagebox.showwarning( "Please select a valid complexity level.")
            return
        
        # Generate the password
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Display the generated password
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError:
        messagebox.showerror( "Please enter a valid number for password length.")

# Function to copy the generated password to clipboard
def copy_to_clipboard():
    password = entry_password.get()
    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        window.update()  # Ensure clipboard content is updated
        messagebox.showinfo("Copied")
    else:
        messagebox.showwarning("Copy Error", "No password to copy!")

# Create the main application window
window = tk.Tk()
window.title("Password Generator")
window.geometry("600x500")
window.resizable(False, False)
window.configure(bg="lightblue")

#importing background
background = tk.PhotoImage(file=r"C:\Users\Admin\Desktop\internship\dark-background-abstract-background-network-3d-background-7680x4320-8324.png")
background_label = tk.Label(window, image=background)
background_label.place(relwidth=1,relheight=1)


# Title label
label_title = tk.Label(window, text="Password Generator", font=("Arial", 16, "bold"), bg="lightblue", fg="darkblue")
label_title.pack(pady=10)

# Password length input
frame_length = tk.Frame(window, bg="lightblue")
frame_length.pack(pady=10)
label_length = tk.Label(frame_length, text="Password Length:", font=("Arial", 12), bg="lightblue")
label_length.pack(side=tk.LEFT, padx=5)
entry_length = tk.Entry(frame_length, font=("Arial", 12), width=10)
entry_length.pack(side=tk.LEFT, padx=5)

# Password complexity options
frame_complexity = tk.Frame(window, bg="lightblue")
frame_complexity.pack(pady=10)
label_complexity = tk.Label(frame_complexity, text="Complexity:", font=("Arial", 12), bg="lightblue")
label_complexity.pack(side=tk.LEFT, padx=5)

complexity_var = tk.IntVar(value=3)  # Default complexity is 3
radiobutton_letters = tk.Radiobutton(frame_complexity, text="Letters Only", variable=complexity_var, value=1, bg="lightblue")
radiobutton_letters.pack(side=tk.LEFT, padx=5)
radiobutton_letters_numbers = tk.Radiobutton(frame_complexity, text="Letters + Numbers", variable=complexity_var, value=2, bg="lightblue")
radiobutton_letters_numbers.pack(side=tk.LEFT, padx=5)
radiobutton_full = tk.Radiobutton(frame_complexity, text="Letters + Numbers + Symbols", variable=complexity_var, value=3, bg="lightblue")
radiobutton_full.pack(side=tk.LEFT, padx=5)

# Generate button
btn_generate = tk.Button(window, text="Generate Password", command=generate_password, font=("Arial", 12), bg="green", fg="white")
btn_generate.pack(pady=10)

# Display generated password
frame_password = tk.Frame(window, bg="lightblue")
frame_password.pack(pady=10)
label_password = tk.Label(frame_password, text="Generated Password:", font=("Arial", 12), bg="lightblue")
label_password.pack(side=tk.LEFT, padx=5)
entry_password = tk.Entry(frame_password, font=("Arial", 12), width=30)
entry_password.pack(side=tk.LEFT, padx=5)

# Copy to clipboard button
btn_copy = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 12), bg="blue", fg="white")
btn_copy.pack(pady=10)

# Run the application
window.mainloop()
