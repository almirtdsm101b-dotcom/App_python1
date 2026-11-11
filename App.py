from kivy.app import App
from kivy.uix.label import Label

class AppTeste(App):
  def build(self):
    return Label(text="Ola Almir")

if __name__ == '__main__':
    AppTeste().run()

    
    
      