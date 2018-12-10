import tkinter as tk
import ReadFile as rf

user_path ="Data/users.csv"
login = 'main'
class SharedPower(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Shared Power")
        self.geometry("200x100+%d+%d" % ((self.winfo_screenwidth()/2)-100, (self.winfo_screenheight()/2)-50))
        self.minsize('200','100')

        self._frame = None
        self.change_frame(StartPage)

    def log_in(self, u_log, u_pass):
        global login
        global user_path
        if u_log.get() in rf.search_values():

            if u_pass.get() == rf.search_value(u_log.get()):
                print('Logged in')

                login = u_log.get()
                self.change_frame(MainMenu)

            else:
                print('wrong password')

        else:
            print('user not exist')

    def log_out(self):
        global login
        login = 'main'
        self.change_frame(StartPage)

    def change_frame(self, f_class):
        """Destroys current frame and replaces it with a new one"""
        new_frame = f_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        u_login = tk.StringVar(self)
        u_password = tk.StringVar(self)

        lab_user = tk.Label(self ,text="username").grid(row=3,column=0)
        ent_user = tk.Entry(self, textvariable = u_login).grid(row=3,column=1)
        lab_pass = tk.Label(self ,text="password").grid(row=4,column=0)
        ent_pass = tk.Entry(self,show="*",textvariable = u_password).grid(row=4,column=1)

        b_login = tk.Button(self, text="Login",command=lambda : master.log_in(u_login, u_password)).grid(row=5,column=0)
        b_reg = tk.Button(self, text="Register",command=lambda : master.change_frame(RegisterPage)).grid(row=5,column=1)

class RegisterPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        master.geometry("280x270+%d+%d" % ((self.winfo_screenwidth()/2)-100, (self.winfo_screenheight()/2)-50))

        """I take stuff from Adam RegisterUiGrid and modify a bit"""
        master.title('Register')

        firstNameLabel = tk.Label(self ,text = "First Name").grid(row = 0, column = 0, sticky="E")
        lastNameLabel = tk.Label(self ,text = "Last Name").grid(row = 1, column = 0, sticky="E")
        userNameLabel = tk.Label(self ,text = "User Name").grid(row = 2, column = 0, sticky="E")
        postCodeLabel = tk.Label(self ,text = "Post Code").grid(row = 3, column = 0, sticky="E")
        streetNameLabel = tk.Label(self ,text = "Street Name").grid(row = 4, column = 0, sticky="E")
        houseNumberLabel = tk.Label(self ,text = "House Number").grid(row = 5, column = 0, sticky="E")
        emailLabel = tk.Label(self ,text = "Email").grid(row = 6, column = 0, sticky="E")
        emailConfirmLabel = tk.Label(self ,text = "Email Confirmation").grid(row = 7, column = 0, sticky="E")
        passwordLabel = tk.Label(self ,text = "Password").grid(row = 8, column = 0, sticky="E")
        passwordConfirmationLabel = tk.Label(self ,text = "Password Confirmation").grid(row = 9, column = 0)

        firstNameEntry = tk.Entry(self).grid(row = 0, column = 1)
        lastNameEntry = tk.Entry(self).grid(row = 1, column = 1)
        userNameEntry = tk.Entry(self).grid(row = 2, column = 1)
        postCodeEntry = tk.Entry(self).grid(row = 3, column = 1)
        streetNameEntry = tk.Entry(self).grid(row = 4, column = 1)
        houseNumberEntry = tk.Entry(self).grid(row = 5, column = 1)
        emailEntry = tk.Entry(self).grid(row = 6, column = 1)
        emailConfirmEntry = tk.Entry(self).grid(row = 7, column = 1)
        passwordEntry = tk.Entry(self, show = "*").grid(row = 8, column = 1)
        passwordConfirmationEntry = tk.Entry(self, show = "*").grid(row = 9, column = 1)

        createAccountButton = tk.Button (self, text = "Create Account").grid(row = 10, column =0, columnspan=2)

class MainMenu(tk.Frame):

    def __init__(self, master):
        global login

        tk.Frame.__init__(self, master)

        Label = tk.Label(self ,text = "Main menu for user: "+login).grid(row=1,column=0)
        b_logout = tk.Button(self, text="Log Out",command=lambda : master.log_out()).grid(row=2,column=0)

        """
        What we need in MainMenu?
        Your Tools and Hire tool only?
        """


"""Use:
class NAME OF FRAME(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

to create new frames

"""

app = SharedPower()
app.mainloop()
