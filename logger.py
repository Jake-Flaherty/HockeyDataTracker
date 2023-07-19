import tkinter as tk
import csv

def log_data():
    data = {
        'Name': name_entry.get(),
        'Age': age_entry.get(),
        'Email': email_entry.get()
    }
    with open('data.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        writer.writerow(data)
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Data Logger")

# Create labels
name_label = tk.Label(window, text="Name:")
name_label.pack()
age_label = tk.Label(window, text="Age:")
age_label.pack()
email_label = tk.Label(window, text="Email:")
email_label.pack()

# Create entry fields
name_entry = tk.Entry(window)
name_entry.pack()
age_entry = tk.Entry(window)
age_entry.pack()
email_entry = tk.Entry(window)
email_entry.pack()

# Create log button
log_button = tk.Button(window, text="Log Data", command=log_data)
log_button.pack()

# Run the main window loop
window.mainloop()