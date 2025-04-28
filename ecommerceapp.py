import tkinter as tk
from tkinter import font

# Create main window
root = tk.Tk()
root.title("Shopsy")
root.geometry("1000x700")
root.configure(bg="white")

# Custom Fonts
poppins_font = ("Poppins", 14)
heading_font = ("Poppins", 24, "bold", "italic")
price_font = ("Poppins", 16, "bold")

# Header
header = tk.Frame(root, bg="lightgray", padx=30, pady=10)
header.pack(fill=tk.X)

name_label = tk.Label(header, text="Shopsy", font=heading_font, bg="lightgray", fg="black")
name_label.pack(side=tk.LEFT)

cart_button = tk.Button(header, text="🛒", font=("Poppins", 20), bg="white", fg="black", width=5, height=1, relief="ridge", bd=2)
cart_button.pack(side=tk.RIGHT, padx=10)

# Subheading
sub_heading = tk.Label(root, text="Products", font=("Poppins", 20, "underline"), fg="black", bg="white")
sub_heading.pack(pady=20)

# Products Section
products_frame = tk.Frame(root, bg="white")
products_frame.pack(padx=20, pady=10)

# Sample Product List
products = [
    {"name": "Ear pots", "price": 754},
    {"name": "Headset", "price": 867},
    {"name": "Blueetooth", "price": 375},
    {"name": "Shoe", "price": 450},
    {"name": "Art", "price": 1200},
    {"name": "Wall Stickers", "price": 650},
    {"name": "Trees", "price": 600},
    {"name": "Paintings", "price": 300},
]

# Grid settings: 3 columns
columns = 3

def create_product(frame, name, price, row, col):
    product_frame = tk.Frame(frame, bg="white", highlightbackground="gray", highlightthickness=1, width=250, height=250)
    product_frame.grid(row=row, column=col, padx=10, pady=10)
    product_frame.grid_propagate(False)

    img_placeholder = tk.Label(product_frame, text="🖼️", font=("Arial", 50), bg="white")
    img_placeholder.pack(pady=10)

    name_label = tk.Label(product_frame, text=name, font=poppins_font, bg="white")
    name_label.pack()

    price_label = tk.Label(product_frame, text=f"₹{price}", font=price_font, fg="green", bg="white")
    price_label.pack()

    add_button = tk.Button(product_frame, text="Add to Cart", bg="orange", fg="white", font=("Poppins", 10), width=12, height=1)
    add_button.pack(pady=10)

# Display products
for idx, product in enumerate(products):
    row = idx // columns
    col = idx % columns
    create_product(products_frame, product["name"], product["price"], row, col)

# Start the Tkinter event loop
root.mainloop()
