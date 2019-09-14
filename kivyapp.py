import os
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
kivy.require("1.11.1")

# u"\u20A6"
class Controller(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.n = '\u20A6'
        
        self.add_widget(Label(text = f'Inflow ({self.n}): '))
        self.inflow = TextInput(multiline=False)
        self.add_widget(self.inflow)
        # validate\
                
        self.divide_btn = Button(text="Divide")
        self.divide_btn.bind(on_release=self.divide_button)
        self.add_widget(Label())
        self.add_widget(self.divide_btn)  


        # divideBtn END


    def divide_button(self, instance):
        # self.na = '\u20A6'
        inflow = int(self.inflow.text)
        self.inflow.text = ""
        if not inflow:
            self.add_widget(Label(text="Please, put an appropriate amount!"))
        else:
            
            self.tithe = str(inflow * 0.1)
            self.family = str(inflow * 0.1)
            self.preserve = str(inflow * 0.15)
            self.seeds = str(inflow * 0.2)
            self.misc = str(inflow * 0.2)
            self.major = str(inflow * 0.25)
            # self.add_widget(Label())   

        with open(f"Division details for {self.n}{inflow}.docx", "w", encoding='utf-8') as d:
            d.write(f"Tithe - 10%: {self.n}{self.tithe}")  
            
        # self.add_widget(Label(text=f"Division for {self.n}{inflow}"))     
        

class FinAppApp(App):
    def build(self):
        return Controller()


if __name__ == "__main__":
   div_app = FinAppApp()
   div_app.run()