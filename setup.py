import kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock,mainthread
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

Builder.load_file("ui.kv")




class HomeScreen(Screen):
	
	def effect(self):
		
		self.side.background_color=(0,1,1,.5)
		Clock.schedule_once(self.back_to_default, .2)		
		
	def back_to_default(self,*args):
		self.side.background_color=(.878,1,1,.794)
	def show_effect_clr(self,*args):
		self.side.background_color=(0,1,1,.5)


class package_pyApp(App):
	def build(self):
		sm=ScreenManager()
		sm.add_widget(HomeScreen(name='home'))
		return sm
	
LabelBase.register(name='os', 
                   fn_regular='resources/fonts/OpenSans-bold.ttf')

if __name__ == "__main__":
	package_pyApp().run()