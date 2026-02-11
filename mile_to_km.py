from tkinter import *

# -------------------- FUNCTION -------------------- #
def calculate():
    """
    This function gets the value entered by the user,
    converts miles to kilometers,
    and updates the result label.
    """
    try:
        # Get value from entry box and convert to float
        miles = float(miles_input.get())
        
        # Convert miles to kilometers
        converted_ans = miles * 1.60934
        
        # Update answer label (rounded to 2 decimal places)
        ans.config(text=round(converted_ans, 2))
        
    except ValueError:
        # If user enters invalid input (like letters)
        ans.config(text="Invalid Input")


# -------------------- WINDOW SETUP -------------------- #
window = Tk()
window.title('Mile to KM Converter')
window.minsize(width=500, height=300)

# Add padding around the window
window.config(padx=150, pady=100)


# -------------------- INPUT FIELD -------------------- #
# Entry box where user types miles value
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)


# -------------------- LABELS -------------------- #
# "Miles" text label
miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

# "is equal to" label
is_equal_to = Label(text='is equal to')
is_equal_to.grid(column=0, row=1)

# Label to display result
ans = Label(text=0)
ans.grid(column=1, row=1)

# "Km" label
km_label = Label(text='Km')
km_label.grid(column=2, row=1)


# -------------------- BUTTON -------------------- #
# Button to trigger calculation
button = Button(text='Calculate', command=calculate)
button.grid(column=1, row=2)


# -------------------- MAIN LOOP -------------------- #
# Keeps the window running
window.mainloop()
