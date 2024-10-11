from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [20, 20, 20, 20]
        self.spacing = 10

        # Title
        title_label = Label(text="Login", font_size=32, size_hint_y=None, height=50)
        self.add_widget(title_label)

        # Username field
        self.add_widget(Label(text="Username"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        # Password field
        self.add_widget(Label(text="Password"))
        self.password = TextInput(multiline=False, password=True)
        self.add_widget(self.password)

        # Login button
        login_button = Button(text="Login", size_hint_y=None, height=50, background_color=(0.1, 0.6, 0.8, 1))
        login_button.bind(on_press=self.validate_login)
        self.add_widget(login_button)

        # Forgot password button
        forgot_password_button = Button(text="Forgot Password?", size_hint_y=None, height=40, background_color=(0.8, 0.5, 0.2, 1))
        forgot_password_button.bind(on_press=self.show_forgot_password_popup)
        self.add_widget(forgot_password_button)

        # Sign-up button
        signup_button = Button(text="Sign Up", size_hint_y=None, height=50, background_color=(0.2, 0.6, 0.4, 1))
        signup_button.bind(on_press=self.show_signup_popup)
        self.add_widget(signup_button)

    def validate_login(self, instance):
        username = self.username.text
        password = self.password.text

        if username == "admin" and password == "password":
            popup = Popup(title="Login Success", content=Label(text="Welcome!"), size_hint=(0.6, 0.4))
            popup.open()
        else:
            popup = Popup(title="Login Failed", content=Label(text="Invalid credentials!"), size_hint=(0.6, 0.4))
            popup.open()

    def show_signup_popup(self, instance):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)

        content.add_widget(Label(text="Enter a new username"))
        new_username = TextInput(multiline=False)
        content.add_widget(new_username)

        content.add_widget(Label(text="Enter a new password"))
        new_password = TextInput(multiline=False, password=True)
        content.add_widget(new_password)

        signup_button = Button(text="Sign Up", size_hint_y=None, height=50, background_color=(0.2, 0.6, 0.4, 1))
        content.add_widget(signup_button)

        # Sign-up popup
        signup_popup = Popup(title="Sign Up", content=content, size_hint=(0.7, 0.7))

        def register_user(instance):
            # Registration logic (placeholder)
            signup_popup.dismiss()
            Popup(title="Sign Up Success", content=Label(text="Account created!"), size_hint=(0.6, 0.4)).open()

        signup_button.bind(on_press=register_user)
        signup_popup.open()

    def show_forgot_password_popup(self, instance):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)

        content.add_widget(Label(text="Enter your email"))
        email_input = TextInput(multiline=False)
        content.add_widget(email_input)

        reset_button = Button(text="Reset Password", size_hint_y=None, height=50, background_color=(0.8, 0.5, 0.2, 1))
        content.add_widget(reset_button)

        # Forgot Password popup
        forgot_popup = Popup(title="Forgot Password", content=content, size_hint=(0.7, 0.7))

        def reset_password(instance):
            # Password reset logic (placeholder)
            forgot_popup.dismiss()
            Popup(title="Password Reset", content=Label(text="Password reset link sent!"), size_hint=(0.6, 0.4)).open()

        reset_button.bind(on_press=reset_password)
        forgot_popup.open()

class LoginApp(App):
    def build(self):
        return LoginScreen()

if __name__ == "__main__":
    LoginApp().run()
