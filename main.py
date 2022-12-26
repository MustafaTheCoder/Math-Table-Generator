"""
Author: MustafaXD (github.com/MustafaTheCoder)
MIT License: https://opensource.org/licenses/MIT
Github: github.com/MustafaTheCoder/Math-Equation-Calculator/blob/main/main.py
"""

# Importing essential modules
import tkinter
import customtkinter

# Configuring appearance mode and color theme
customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("blue")  

# Defining the main app variable 
app = customtkinter.CTk()

# Defining master root and app geometry
root_tk = app.geometry("900x600")

# Defining app title
app.title("Math Table Generator Using Python | github.com/MustafaTheCoder")

# Defining app header label value
heading_label_text_var = tkinter.StringVar(value="MATH TABLES")
# Defining app header label custom font size 
heading_label_font = customtkinter.CTkFont(size=50)

# Defining the text variable (label value) and font size variable of the app header label
heading_label = customtkinter.CTkLabel(master=root_tk, textvariable=heading_label_text_var, font=heading_label_font)
# Placing the app header label in the center anchor
heading_label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

# Defining app table number label value
table_num_label_text_var = tkinter.StringVar(value="Input your table number:")
# Defining app table number label custom font size 
table_num_font = customtkinter.CTkFont(size=25)

# Defining the text variable (label value) and font size variable of the app table number label
table_label = customtkinter.CTkLabel(master=root_tk, textvariable=table_num_label_text_var, font=table_num_font)
# Placing the app table number label in the center anchor
table_label.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

# Defining the main calculation function to generate a maths table upon the number inputted
def calculate_function():
    # Defining a try and exception statement
    try:
        # Getting the user input stored in a variable
        inp = table_input.get()
        # Typecasting the variable into an integer
        inp = int(inp)
        # Creating a file to write the maths table of the inputted number
        with open(f"table_of_{inp}.txt", "w") as f:
            # For loop to write the maths table of the number that ends on {number} x 10 = {answer}
            for i in range(1, 11):
                # Writing the generated maths table in the file created with a new line character to avoid overwriting
                f.write(f"{inp} x {i} = {i*inp}\n")
    # This is to handle if any exceptions occur such as user entering incorrect data
    except Exception as e:
        # To inform the user about the error I'm creating a file named just "table.txt" and writing the error message in it
        with open("table.txt", "w") as f:
            f.write(f"[ERROR OCCURED] | {e}")

# Defining the main app input textbox that will take the maths table number as an input
table_input = customtkinter.CTkEntry(master=root_tk, placeholder_text="Enter table number.")
# Placing the app input textbox in the center anchor
table_input.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

# Defining the main app button that will be clicked to generate the maths table as per the entered input
button = customtkinter.CTkButton(master=app, text="Calculate", command=calculate_function)
# Placing the app main calculate button in the center anchor
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# Executing the main app loop
app.mainloop()