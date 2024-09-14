import tkinter as tk

# root=tk.Tk()
# root.title("Login force")
# root.geometry('340x440')
# root.configure(bg='#333333')
# login_label=tk.Label(root,text="Login",font=("Arial",30),bg="#ff3399")
# username_label=tk.Label(root,text="Username")
# username_entry=tk.Entry(username_label)
# password_label=tk.Label(root,text="Password")
# password_entry=tk.Entry(password_label)
# login_button= tk.Button(root,text="login")
# # label.pack
# login_label.grid(row=0,column=0,sticky="n")
# username_label.grid(row=1,column=0)
# username_entry.grid(row=1,column=1)
# password_label.grid(row=2,column=0)
# password_entry.grid(row=2,column=1)
# login_button.grid(row=3,column=0,columnspan=2)
# def hello():
#     print("hello world")
# if _name_=='_main_':
root=tk.Tk()
root.title("Tkinter first app")
root.geometry('300x400')

frame=tk.Frame(root)
frame.pack()

label=tk.Label(root,text="Hello World")
label.pack()
# label1=tk.Label(root,text="Hello World")
# label1.pack()

button=tk.Button(root,text="Hello World")
button.pack()

root.mainloop()