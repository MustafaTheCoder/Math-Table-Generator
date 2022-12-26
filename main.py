import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("blue")  

app = customtkinter.CTk()
root_tk = app.geometry("900x600")
app.title("Math Table Generator Using Python | github.com/MustafaTheCoder")

heading_label_text_var = tkinter.StringVar(value="MATH TABLES")
heading_label_font = customtkinter.CTkFont(size=50)

heading_label = customtkinter.CTkLabel(master=root_tk, textvariable=heading_label_text_var, font=heading_label_font)
heading_label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

table_num_label_text_var = tkinter.StringVar(value="Input your table number:")
table_num_font = customtkinter.CTkFont(size=25)

table_label = customtkinter.CTkLabel(master=root_tk, textvariable=table_num_label_text_var, font=table_num_font)
table_label.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

def calculate_function():
    try:
        inp = table_input.get()
        inp = int(inp)
        with open(f"table_of_{inp}.txt", "w") as f:
            for i in range(1, 11):
                f.write(f"{inp} x {i} = {i*inp}\n")
    except Exception as e:
        with open("table.txt", "w") as f:
            f.write(f"[ERROR OCCURED] | {e}")


table_input = customtkinter.CTkEntry(master=root_tk, placeholder_text="Enter table number.")
table_input.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Calculate", command=calculate_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()