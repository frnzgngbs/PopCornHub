import tkinter as tk
from tkinter import ttk

def submit_review():
    # Handle the form submission logic here
    rating = star_rating.get()
    review = review_text.get("1.0", tk.END)
    print(f"Rating: {rating}")
    print(f"Review: {review}")

# Create the main window
window = tk.Tk()
window.title("Add Review")

# Create a label for the star rating
rating_label = ttk.Label(window, text="Rating:")
rating_label.grid(row=0, column=0)

# Create a variable to store the selected rating
star_rating = tk.IntVar()

# Create the star rating Radiobuttons
for i in range(5):
    rating_button = ttk.Radiobutton(window, text=str(i + 1), variable=star_rating, value=i + 1)
    rating_button.grid(row=0, column=i + 1)

# Create a label for the review text
review_label = ttk.Label(window, text="Review:")
review_label.grid(row=1, column=0, sticky="W")

# Create a text area for the review text
review_text = tk.Text(window, height=5, width=30)
review_text.grid(row=2, column=0, columnspan=6, padx=10, pady=5)

# Create a submit button
submit_button = ttk.Button(window, text="Submit", command=submit_review)
submit_button.grid(row=3, column=0, columnspan=6, pady=10)

# Start the main event loop
window.mainloop()