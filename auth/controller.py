import tkinter as tk
import ttkbootstrap as ttk
import re
import hashlib

# local
from .views import SignUpView, SignInView, SignOutView, MenuBarView, NotificationView
from .models import User
from .base.models import Session


class Controller(tk.Tk):
    """
    creates a controller window
    """

    def __init__(self, *args, **kwargs):
        """initialize superclass and attributes"""
        super().__init__(*args, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.geometry("500x350")
        self.style = ttk.Style()
        self.style.theme_use("cyborg")

        self.user = None
        self.create_frames()
        self.create_dynamics()

    def create_frames(self):
        """creates frames"""
        # big frame
        self.BigFrame = ttk.Frame(self)
        self.BigFrame.grid(row=0, column=0, sticky="nsew")
        self.BigFrame.grid_columnconfigure(0, weight=1)
        self.BigFrame.grid_rowconfigure(1, weight=1)
        # notification frame
        self.notify = NotificationView(self.BigFrame)
        self.notify.grid(row=0, column=0)

    def create_dynamics(self):
        """creates views that change periodically"""
        self.menubar = MenuBarView(self)
        self.config(menu=self.menubar)
        self.signin = SignInView
        if self.user == None:
            self.menubar.add_command(label="SignUp", command=self.signup_window)
            self.menubar.add_command(label="SignIn", command=self.signin_window)
        else:
            self.menubar.add_command(label="SignOut", command=self.signout_window)
        # mainframe
        self.mainframe = ttk.Frame(self.BigFrame)
        self.mainframe.grid(row=1, column=0, sticky="nsew")
        if self.user == None:
            ttk.Label(self.mainframe, text="Logged Out!").grid()
        else:
            ttk.Label(self.mainframe, text=f"You are in {self.user}!").grid()

    def signup_window(self):
        # signup view
        self.signup = SignUpView(self)

        def user_add():
            """
            handles user registration logic
            We will use 'self.signup' view
            """
            # collect input from forms
            # intialize empty list
            raw_inputs = []
            # append all inputs to the list
            for i in self.signup.inputs:
                raw_inputs.append(self.signup.inputs[i].get())
                # appends in the order of how you assigned the keys to the inputs
                # look at the SignUpView in views.py to see the order

            # check if there is an empty string in the list and raise an error
            if "" in raw_inputs:
                message = "Kindly, All fields are required!"
                self.signup.show_message(message)
            else:
                # check if username exists
                username = raw_inputs[0]
                session = Session()
                query_user = session.query(User.username).all()
                query_user = [i for j in query_user for i in j]
                session.close()
                if username in query_user:
                    message = "Username exists!!"
                    self.signup.show_message(message)
                else:
                    # check if email is in correct format
                    email = raw_inputs[1]
                    regex_em = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
                    if re.fullmatch(regex_em, email):
                        # check if email exists
                        session = Session()
                        query_email = session.query(User.email).all()
                        query_email = [i for j in query_email for i in j]
                        session.close()
                        if email in query_email:
                            message = "Email exists!!"
                            self.signup.show_message(message)
                        else:
                            # check if two passwords match
                            password = raw_inputs[4]
                            password2 = raw_inputs[5]
                            if password != password2:
                                message = "Passwords do not match!!"
                                self.signup.show_message(message)
                            else:
                                # hash the password
                                password = hashlib.sha512(password.encode()).hexdigest()
                                # update other inputs
                                firstname = raw_inputs[2]
                                lastname = raw_inputs[3]
                                # add user
                                session = Session()
                                user = User(
                                    username=username,
                                    email=email,
                                    first_name=firstname,
                                    last_name=lastname,
                                    password=password,
                                )
                                session.add(user)
                                session.commit()
                                session.close()
                                message = "Succesfuly registered! Proceed to Login"
                                self.notify.show_message(message)
                                self.signup.destroy()
                    else:
                        message = "Invalid email format!!!"
                        self.signup.show_message(message)

        self.signup.button.configure(command=user_add)

    def signin_window(self):
        # signin view
        self.signin = SignInView(self)

        def user_login():
            """
            handles user login logic
            We will use 'self.signin' view
            """
            # collect input from forms
            email = self.signin.inputs["login"].get()
            password = self.signin.inputs["password"].get()
            # check if fields are empty
            if email == "" or password == "":
                message = "Kindly, All fields are required!"
                self.signin.show_message(message)
            else:
                # check if email not exists
                session = Session()
                query_email = session.query(User.email).all()
                query_email = [i for j in query_email for i in j]
                session.close()
                if email not in query_email:
                    message = "Email does not exist!!"
                    self.signin.show_message(message)
                else:
                    # hash password
                    password = hashlib.sha512(password.encode()).hexdigest()
                    # match password and email
                    session = Session()
                    match = session.query(User).filter(
                        User.email == email, User.password == password
                    )
                    match = match.first()
                    session.close()
                    if match is None:
                        message = "Incorrect password!!"
                        self.signin.show_message(message)
                    else:
                        # get username
                        user = session.query(User.username).filter(User.email == email)
                        user = [i for j in user for i in j]
                        user = user[0]
                        message = "Login Succesfull!"
                        self.notify.show_message(message)
                        self.signin.destroy()
                        self.update_user(user)
                        self.refresh()

        self.signin.button.configure(command=user_login)

    def signout_window(self):
        # signout view
        self.signout = SignOutView(self)

        def user_logout():
            # update user and exist
            message = "Logout Succesfull!"
            self.notify.show_message(message)
            self.signout.destroy()
            self.update_user(None)
            self.refresh()

        self.signout.button_ok.configure(command=user_logout)

    def update_user(self, user):
        """returns user"""
        self.user = user

    def refresh(self):
        """refresh"""
        self.create_dynamics()
