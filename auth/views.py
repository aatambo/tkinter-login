import tkinter as tk
import ttkbootstrap as ttk


class SignUpView(tk.Toplevel):
    """creates signup window"""

    def __init__(self, *args, **kwargs):
        """initialize super class and attributes"""
        super().__init__(*args, **kwargs)
        self.attributes("-topmost", "true")
        self.grab_set()
        self.labels = {}
        self.inputs = {}

        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)

        # title
        ttk.Label(self, text="Sign Up View").grid(row=0, column=0, columnspan=4)
        # username
        ttk.Label(self, text="Username").grid(row=1, column=0)
        username = tk.StringVar()
        self.inputs["username"] = ttk.Entry(self, textvariable=username)
        self.inputs["username"].grid(row=1, column=1)
        # email
        ttk.Label(self, text="Email").grid(row=1, column=2)
        email = tk.StringVar()
        self.inputs["email"] = ttk.Entry(self, textvariable=email)
        self.inputs["email"].grid(row=1, column=3)
        # first_name
        ttk.Label(self, text="First Name").grid(row=2, column=0)
        first_name = tk.StringVar()
        self.inputs["first_name"] = ttk.Entry(self, textvariable=first_name)
        self.inputs["first_name"].grid(row=2, column=1)
        # last_name
        ttk.Label(self, text="Last Name").grid(row=2, column=2)
        last_name = tk.StringVar()
        self.inputs["last_name"] = ttk.Entry(self, textvariable=last_name)
        self.inputs["last_name"].grid(row=2, column=3)
        # password
        ttk.Label(self, text="Password").grid(row=3, column=0)
        password = tk.StringVar()
        self.inputs["password"] = ttk.Entry(self, textvariable=password, show="*")
        self.inputs["password"].grid(row=3, column=1)
        # password 2
        ttk.Label(self, text="Password(again)").grid(row=3, column=2)
        password2 = tk.StringVar()
        self.inputs["password2"] = ttk.Entry(self, textvariable=password2, show="*")
        self.inputs["password2"].grid(row=3, column=3)
        # messages
        # displays error and success messages
        self.message = tk.StringVar()
        self.message_label = ttk.Label(self, textvariable=self.message)
        self.message_label.grid(row=5, column=0, columnspan=4)

        # button
        self.button = ttk.Button(self, text="SignUp")
        self.button.grid(row=4, column=0, columnspan=4)

        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)

    def show_message(self, message):
        """shows error message"""
        self.message.set(message)
        self.message_label.configure(bootstyle="danger")
        self.message_label.after(5000, self.clean_message)

    def clean_message(self):
        """clears messages"""
        self.message.set("")


class SignInView(tk.Toplevel):
    """creates signup window"""

    def __init__(self, *args, **kwargs):
        """initialize superclass and attributes"""
        super().__init__(*args, **kwargs)
        self.attributes("-topmost", "true")
        self.grab_set()
        self.inputs = {}

        for i in range(2):
            self.grid_columnconfigure(i, weight=1)
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)

        # title
        ttk.Label(self, text="Sign In View").grid(row=0, column=0, columnspan=2)
        # username
        ttk.Label(self, text="Email").grid(row=1, column=0)
        login = tk.StringVar()
        self.inputs["login"] = ttk.Entry(self, textvariable=login, width=30)
        self.inputs["login"].grid(row=1, column=1)
        # password
        ttk.Label(self, text="Password").grid(row=2, column=0)
        password = tk.StringVar()
        self.inputs["password"] = ttk.Entry(
            self, textvariable=password, show="*", width=30
        )
        self.inputs["password"].grid(row=2, column=1)
        # messages
        # displays error and success messages
        self.message = tk.StringVar()
        self.message_label = ttk.Label(self, textvariable=self.message)
        self.message_label.grid(row=4, column=0, columnspan=2)

        # button
        self.button = ttk.Button(self, text="SignIn")
        self.button.grid(row=3, column=0, columnspan=2)

        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)

    def show_message(self, message):
        """shows error message"""
        self.message.set(message)
        self.message_label.configure(bootstyle="danger")
        self.message_label.after(5000, self.clean_message)

    def clean_message(self):
        """clears messages"""
        self.message.set("")


class SignOutView(tk.Toplevel):
    """creates signup frame"""

    def __init__(self, *args, **kwargs):
        """initialize superclass and attributes"""
        super().__init__(*args, **kwargs)
        self.attributes("-topmost", "true")
        self.grab_set()

        for i in range(2):
            self.grid_columnconfigure(i, weight=1)
        for i in range(2):
            self.grid_rowconfigure(i, weight=1)

        # title
        ttk.Label(self, text="Sign In View").grid(row=0, column=0, columnspan=2)
        # label
        message = "Hello, Are You Sure You Wan't to Sign Out?"
        self.label = ttk.Label(self, text=message)
        self.label.grid(row=1, column=0, columnspan=2)
        # button - okay
        self.button_ok = ttk.Button(self, text="Yes, please!")
        self.button_ok.grid(row=2, column=0)
        # button - cancel
        self.button_no = ttk.Button(
            self,
            text="No, just exploring",
            command=self.destroy_self,
        )
        self.button_no.grid(row=2, column=1)

        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)

    def destroy_self(self):
        """destroys toplevel window"""
        self.destroy()


class MenuBarView(tk.Menu):
    """creates a menu view"""

    def __init__(self, *args, **kwarg):
        """initialize superclass and attributes"""
        super().__init__(*args, **kwarg)
        self.configure(tearoff=False)
        self.configure(background="orange")


class NotificationView(ttk.Frame):
    """creates a main view"""

    def __init__(self, *args, **kwargs):
        """initialize superclass and attributes"""
        super().__init__(*args, **kwargs)

        # messages
        # displays messages
        self.message = tk.StringVar()
        self.message_label = ttk.Label(self, textvariable=self.message)
        self.message_label.grid(row=0, column=0)

    def show_message(self, message):
        """shows message"""
        self.message.set(message)
        self.message_label.configure(bootstyle="success")
        self.message_label.after(5000, self.clean_message)

    def clean_message(self):
        """clears messages"""
        self.message.set("")
