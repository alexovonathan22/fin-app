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
        inflow = float(self.inflow.text)
        self.inflow.text = ""
        if not inflow:
            self.add_widget(Label(text="Please, put an appropriate amount!"))
        else:
            self.per_10 = inflow * 0.1
            self.per_15 = inflow * 0.15
            self.per_20 = inflow * 0.2
            self.per_25 = inflow * 0.25
            
            self.tithe = str(self.per_10)
            self.family = str(self.per_10)
            self.preserve = str(self.per_15)
            self.seeds = str(self.per_20)
            self.misc = str(self.per_20)
            self.major = str(self.per_25)
            self.total = self.per_10 + self.per_10 + self.per_15 + self.per_20 + self.per_20 + self.per_25
            # self.add_widget(Label())   

        with open(f"Division details for {self.n}{inflow}.docx", "w", encoding='utf-8') as d:
            d.write(f"""Tithe(10%): {self.n}{self.tithe}
Family(10%): {self.n}{self.family}
Preserve(15%): {self.n}{self.preserve}
Seeds/Offerrings(20%): {self.n}{self.seeds}
Miscellaneous(20%): {self.n}{self.misc}
Major Project(25%): {self.n}{self.major}
Total(100%): {self.n}{self.total}""")  
            
        # self.add_widget(Label(text=f"Division for {self.n}{inflow}"))     
        

class FinAppApp(App):
    def build(self):
        return Controller()


if __name__ == "__main__":
   div_app = FinAppApp()
   div_app.run()