from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

alimentos = ["maiz", "frijoles", "cebolla", "tortillas", "limon", "tomate", "carne de vaca", "carne de puerco"]
recetas = ["pozole", "tacos de puerco"]

'''
class Recetas(GridLayout):

    def __init__(self):
        super(Recetas, self).__init__()
        self.cols = 2



class MainScreen(GridLayout):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.cols = 2

        #self.add_widget(Label(text="Pesto Pasta"))
        #self.add_widget(Label(text=" "))

        self.add_widget(Label(text="Alimentos (Escoge los que tengas disponibles): "))
        self.add_widget(Label(text=" "))

        for x in range(0, len(alimentos)):
            self.add_widget(Label(text=alimentos[x]))
            self.add_widget(CheckBox())

        self.add_widget(Label(text=" "))
        btn = Button(text="Aceptar")
        btn.bind(on_release=self.recetas)
        self.add_widget(btn)

    def recetas(self):
        return Recetas()
'''
#-------------------------------------------------

Builder.load_string("""
<MenuScreen>:
    GridLayout:
        cols: 2
        Label:
            text:"Alimentos (Escoge los que tengas disponibles): "
        Label:
            text:" "

        Label:
            text:" "
        Button:
            text: 'Aceptar'
            on_press: root.manager.current = 'recipes'

<RecetasScreen>:
    BoxLayout:
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
""")

# Declare both screens
class MenuScreen(Screen):
    pass

class RecetasScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(RecetasScreen(name='recipes'))


class MyApp(App):

    def build(self):
        return sm

MyApp().run()
