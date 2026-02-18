from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout

from kivy.app import App


class ExpenseApp(App):
    def build(self):
        al = AnchorLayout()
        gl = GridLayout()
        al.add_widget(gl)
        
        return al
