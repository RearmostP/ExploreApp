from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button

from kivy.app import App

<<<<<<< HEAD:app/ui/screens/main_screen.py
class ExpenseApp(App):
    def build(self):
=======
class ExpenseApp(App, GridLayout):
    def build(self): # כאן צריך להיות הבילד
>>>>>>> origin/main:ui/main_ui.py
        al = AnchorLayout()
        gl = GridLayout()
        al.add_widget(gl)

        return al
