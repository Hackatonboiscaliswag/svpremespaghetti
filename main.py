import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox

alimentos = ["maiz", "frijoles", "cebolla", "tortillas", "limon", "tomate", "carne de vaca", "carne de puerco"]
recetas = ["pozole", "tacos de puerco"]
enfermedades = ["Enfermedades del Corazon", "Diabetes", "Cancer", "Enfermedades Cerebrovasculares", "Enfermedades del Higado", "Influenza"]

#------------------------Homiepage---------------------------------------------
class ScreenOne(Screen):

    def __init__ (self,**kwargs):
        super (ScreenOne, self).__init__(**kwargs)

        box1 = BoxLayout(orientation='vertical')
        box2 = BoxLayout(orientation='horizontal')

        my_label1 = Label(text="Nutriopolis", font_size='24dp')
        my_button1 = Button(text="Home",size_hint_y=None, size_y=100)
        #my_button1.bind(on_press=self.changer)
        my_button4 = Button(text="Informacion \nGeneral",size_hint_y=None, size_y=100)
        my_button2 = Button(text="Ingredientes",size_hint_y=None, size_y=100)
        my_button2.bind(on_press=self.changer)
        my_button3 = Button(text="Enfermedades",size_hint_y=None, size_y=100)
        my_button3.bind(on_press=self.changer2)

        box1.add_widget(my_label1)
        box2.add_widget(my_button1)
        box2.add_widget(my_button4)
        box2.add_widget(my_button2)
        box2.add_widget(my_button3)

        self.add_widget(box1)
        self.add_widget(box2)

    def changer(self,*args):
        self.manager.current = 'screen2'
    def changer2(self,*args):
        self.manager.current = 'screen3'

#--------------------------Ingredientes----------------------------------------
class ScreenTwo(Screen):

    def __init__(self,**kwargs):
        super (ScreenTwo,self).__init__(**kwargs)

        box1 = GridLayout()
        box1.cols = 2
        box2 = BoxLayout(orientation='horizontal')

        my_label1 = Label(text="Ingredientes", font_size='24dp')
        box1.add_widget(my_label1)
        box1.add_widget(Label(text=" "))
        for x in range(0, len(alimentos)):
            box1.add_widget(Label(text=alimentos[x]))
            box1.add_widget(CheckBox())
        box1.add_widget(Label(text=" "))
        box1.add_widget(Button(text="Ver recetas",on_press=self.changerR))
        box1.add_widget(Label(text=" "))
        box1.add_widget(Label(text=" "))
        box1.add_widget(Label(text=" "))
        box1.add_widget(Label(text=" "))
        box1.add_widget(Label(text=" "))
        box1.add_widget(Label(text=" "))

        my_button1 = Button(text="Home",size_hint_y=None, size_y=100)
        my_button1.bind(on_press=self.changer)
        my_button4 = Button(text="Informacion \nGeneral",size_hint_y=None, size_y=100)
        my_button2 = Button(text="Ingredientes",size_hint_y=None, size_y=100)
        #my_button2.bind(on_press=self.changer)
        my_button3 = Button(text="Enfermedades",size_hint_y=None, size_y=100)
        my_button3.bind(on_press=self.changer2)

        box2.add_widget(my_button1)
        box2.add_widget(my_button4)
        box2.add_widget(my_button2)
        box2.add_widget(my_button3)

        self.add_widget(box1)
        self.add_widget(box2)

    def changer(self,*args):
        self.manager.current = 'screen1'
    def changer2(self,*args):
        self.manager.current = 'screen3'
    def changerR(self,*args):
        self.manager.current = 'screenR'

#--------------------------Enfermedades----------------------------------------
class ScreenThree(Screen):

    def __init__(self,**kwargs):
        super (ScreenThree,self).__init__(**kwargs)

        box1 = GridLayout()
        box1.cols = 2
        box2 = BoxLayout(orientation='horizontal')

        my_label1 = Label(text="Enfermedades", font_size='24dp')
        box1.add_widget(my_label1)
        box1.add_widget(Label(text=" "))
        for x in range(0, len(enfermedades)):
            box1.add_widget(Label(text=enfermedades[x]))
            box1.add_widget(Button(text="Ver Mas Informacion", on_press=self.changerH))
        box1.add_widget(Label(text=" "))
        box1.add_widget(Label(text=" "))
        box1.add_widget(Label(text=" "))
        box1.add_widget(Label(text=" "))
        box1.add_widget(Label(text=" "))
        box1.add_widget(Label(text=" "))

        my_button1 = Button(text="Home",size_hint_y=None, size_y=100)
        my_button1.bind(on_press=self.changer)
        my_button4 = Button(text="Informacion \nGeneral",size_hint_y=None, size_y=100)
        my_button2 = Button(text="Ingredientes",size_hint_y=None, size_y=100)
        my_button2.bind(on_press=self.changer2)
        my_button3 = Button(text="Enfermedades",size_hint_y=None, size_y=100)
        #my_button3.bind(on_press=self.changer2)

        box2.add_widget(my_button1)
        box2.add_widget(my_button4)
        box2.add_widget(my_button2)
        box2.add_widget(my_button3)

        self.add_widget(box1)
        self.add_widget(box2)

    def changer(self,*args):
        self.manager.current = 'screen1'
    def changer2(self,*args):
        self.manager.current = 'screen2'
    def changerH(self,*args):
        self.manager.current = 'screenH'

#----------------------------Recetas-------------------------------------------
class ScreenRecetas(Screen):

    def __init__(self, **kwargs):
        super(ScreenRecetas, self).__init__(**kwargs)

        box1 = GridLayout()
        box1.cols = 2
        box2 = BoxLayout(orientation='horizontal')

        my_label1 = Label(text="Recetas", font_size='24dp')
        box1.add_widget(my_label1)
        box1.add_widget(Label(text=" "))
        for x in range(0, len(recetas)):
            box1.add_widget(Label(text=recetas[x]))
            box1.add_widget(Button(text="Ver Receta", on_press=self.changerP))
        box1.add_widget(Label(text=" "))
        box1.add_widget(Label(text=" "))

        my_button1 = Button(text="Home",size_hint_y=None, size_y=100)
        my_button1.bind(on_press=self.changer)
        my_button4 = Button(text="Informacion \nGeneral",size_hint_y=None, size_y=100)
        my_button2 = Button(text="Ingredientes",size_hint_y=None, size_y=100)
        my_button2.bind(on_press=self.changer2)
        my_button3 = Button(text="Enfermedades",size_hint_y=None, size_y=100)
        my_button3.bind(on_press=self.changer3)

        box2.add_widget(my_button1)
        box2.add_widget(my_button4)
        box2.add_widget(my_button2)
        box2.add_widget(my_button3)

        self.add_widget(box1)
        self.add_widget(box2)

    def changer(self,*args):
        self.manager.current = 'screen1'
    def changer2(self,*args):
        self.manager.current = 'screen2'
    def changer3(self,*args):
        self.manager.current = 'screen3'
    def changerP(self,*args):
        self.manager.current = 'screenP'

#----------------------------Pozole--------------------------------------------
class ScreenPozole(Screen):

    def __init__(self, **kwargs):
        super(ScreenPozole, self).__init__(**kwargs)

        box1 = BoxLayout(orientation='vertical', halign='left')
        box2 = BoxLayout(orientation='horizontal')

        box1.add_widget(Label(text="Pozole", font_size='28dp'))
        box1.add_widget(Label(text=" "))
        box1.add_widget(Label(text="Ingredientes:", font_size='20dp'))
        box1.add_widget(Label(text="1 kilo de maiz para pozole"))
        box1.add_widget(Label(text="Sal a gusto"))
        box1.add_widget(Label(text="1 kilo de carne de puerco, cortada en cubos"))
        box1.add_widget(Label(text="1 jitomate grande"))
        box1.add_widget(Label(text=" "))
        box1.add_widget(Label(text="Preparacion:", font_size='20dp'))
        box1.add_widget(Label(text="Coloca el maiz en una olla grande, cubre con agua, agrega sal al gusto y cocina a fuego medio durante 2 horas."))
        box1.add_widget(Label(text="Despues de ese tiempo, agrega la carne a la olla y cocina durante 1 hora o hasta que la carne este bien suave."))
        box1.add_widget(Label(text="Mientras, hierve el jitomate hasta que se haya ablandado. "))
        box1.add_widget(Label(text="Cuando ya esta suave la carne, sacala de la olla y deshebrala"))
        box1.add_widget(Label(text="Vierte la salsa del tomate dentro de la olla con el maiz y deja que suelte el hervor. Regresa la carne deshebrada a la olla, rectifica la sazon y deja que hierva unos minutos mas antes de servir."))
        box1.add_widget(Label(text="Si es posible, sirve con lechuga picada, cebolla picada y unas gotas de jugo de limon y acompana con tostadas."))
        box1.add_widget(Label(text=" "))
        box1.add_widget(Label(text="Informacion Nutrimental: (1 taza)", font_size='20dp'))
        box1.add_widget(Label(text=" "))
        box1.add_widget(Label(text="Calorias: 228"))
        box1.add_widget(Label(text="Grasa   : 11g"))
        box1.add_widget(Label(text="Carbh   : 15g"))
        box1.add_widget(Label(text="Proteina: 16g"))
        box1.add_widget(Label(text=" "))
        box1.add_widget(Label(text=" "))
        box1.add_widget(Label(text=" "))
        box1.add_widget(Label(text=" "))
        box1.add_widget(Label(text=" "))
        box1.add_widget(Label(text=" "))

        my_button1 = Button(text="Home",size_hint_y=None, size_y=100)
        my_button1.bind(on_press=self.changer)
        my_button4 = Button(text="Informacion \nGeneral",size_hint_y=None, size_y=100)
        my_button2 = Button(text="Ingredientes",size_hint_y=None, size_y=100)
        my_button2.bind(on_press=self.changer2)
        my_button3 = Button(text="Enfermedades",size_hint_y=None, size_y=100)
        my_button3.bind(on_press=self.changer3)

        box2.add_widget(my_button1)
        box2.add_widget(my_button4)
        box2.add_widget(my_button2)
        box2.add_widget(my_button3)

        self.add_widget(box1)
        self.add_widget(box2)

    def changer(self,*args):
        self.manager.current = 'screen1'
    def changer2(self,*args):
        self.manager.current = 'screen2'
    def changer3(self,*args):
        self.manager.current = 'screen3'

#------------------------Enfermedades del Higado-------------------------------
class ScreenHigado(Screen):

    def __init__(self, **kwargs):
        super(ScreenHigado, self).__init__(**kwargs)

        box1 = BoxLayout(orientation='vertical', halign='left')
        box2 = BoxLayout(orientation='horizontal')

        box1.add_widget(Label(text="Enfermedades del Higado", font_size='28dp'))
        box1.add_widget(Label(text=" "))
        box1.add_widget(Label(text="Que es?", font_size='20dp'))
        box1.add_widget(Label(text="Se refiere aualquier enfermedad o trastorno que impide\nal higado funcionar correctamente o que detiene su funcionamiento. \nLa enfermedad hepatica normalmente se descubre haciendo examenes o pruebas de \nla funcion del higado."))
        box1.add_widget(Label(text=" "))
        box1.add_widget(Label(text="Dieta Especial:", font_size='20dp'))
        box1.add_widget(Label(text=" - Restringir la cantidad de proteina que consume. \nEsto le ayudara a reducir la acumulacion de productos de desecho toxicos."))
        box1.add_widget(Label(text=" - Aumentar su ingesta de carbohidratos para que sea \nproporcional a la cantidad de proteina que consume."))
        box1.add_widget(Label(text=" - Reducir el consumo de sal. La sal en la alimentacion\n puede empeorar la acumulacion de liquidos y la hinchazon en el higado."))
        box1.add_widget(Label(text=" "))
        box1.add_widget(Label(text=" "))
        box1.add_widget(Label(text=" "))
        box1.add_widget(Label(text=" "))

        my_button1 = Button(text="Home",size_hint_y=None, size_y=100)
        my_button1.bind(on_press=self.changer)
        my_button4 = Button(text="Informacion \nGeneral",size_hint_y=None, size_y=100)
        my_button2 = Button(text="Ingredientes",size_hint_y=None, size_y=100)
        my_button2.bind(on_press=self.changer2)
        my_button3 = Button(text="Enfermedades",size_hint_y=None, size_y=100)
        my_button3.bind(on_press=self.changer3)

        box2.add_widget(my_button1)
        box2.add_widget(my_button4)
        box2.add_widget(my_button2)
        box2.add_widget(my_button3)

        self.add_widget(box1)
        self.add_widget(box2)

    def changer(self,*args):
        self.manager.current = 'screen1'
    def changer2(self,*args):
        self.manager.current = 'screen2'
    def changer3(self,*args):
        self.manager.current = 'screen3'


#-----------------------------Main------------------------

class MyApp(App):

        def build(self):
            my_screenmanager = ScreenManager()
            screen1 = ScreenOne(name='screen1')
            screen2 = ScreenTwo(name='screen2')
            screen3 = ScreenThree(name='screen3')
            screenR = ScreenRecetas(name='screenR')
            screenP = ScreenPozole(name='screenP')
            screenH = ScreenHigado(name='screenH')
            my_screenmanager.add_widget(screen1)
            my_screenmanager.add_widget(screen2)
            my_screenmanager.add_widget(screen3)
            my_screenmanager.add_widget(screenR)
            my_screenmanager.add_widget(screenP)
            my_screenmanager.add_widget(screenH)
            return my_screenmanager

if __name__ == '__main__':
    MyApp().run()
