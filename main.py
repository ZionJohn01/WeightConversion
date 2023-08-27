import tkinter as tk
from tkinter import ttk

# Conversion constants
CONVERSION_FACTORS = {
    "Grams": 453.592,
    "Milligrams": 453592.0,
    "Ounces": 16.0
}

# Function to perform the conversion
def convertWeight():
    try:
        input_weight = float(entry_weight.get())
        to_unit = combo_to.get()

        conversion_factor = CONVERSION_FACTORS.get(to_unit, 1.0)
        converted_weight = input_weight * conversion_factor
        result.config(text=f"Converted Weight: {converted_weight:.4f} {to_unit}")
    except ValueError:
        result.config(text="Invalid input")

# Create the main window
root = tk.Tk()
root.title("Weight Conversion App")

# Entry for user input
label_entry = tk.Label(root, text="Enter Weight in Pounds:")
label_entry.pack()

entry_weight = tk.Entry(root)
entry_weight.pack()

# Dropdown for to unit
label_to = tk.Label(root, text="Convert To:")
label_to.pack()

options = list(CONVERSION_FACTORS.keys())
combo_to = ttk.Combobox(root, values=options)
combo_to.pack()

# Convert button
convert_button = tk.Button(root, text="Convert", command=convertWeight)
convert_button.pack()

# Result label
result = tk.Label(root, text="")
result.pack()

# Start the GUI event loop
root.mainloop()