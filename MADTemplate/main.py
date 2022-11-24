import kivy
from kivy.app import App
kivy.require('1.9.0') #version requirement

#every app basically starts with these top three things


from kivy.lang import Builder
from kivy.uix.screenmanager import (ScreenManager, Screen, NoTransition,
SlideTransition, CardTransition, SwapTransition,
FadeTransition, WipeTransition, FallOutTransition, RiseInTransition) #import all the transitions
#ways to go from one tab to another


from kivy.config import Config
Config.set('graphics', 'width', '441') #fixes the dimensions with the confic library
Config.set('graphics', 'height', '800')
Config.set('graphics', 'resizable', False) #makes the screen unsizable, cannot adjust size


from func import hi #how to import a func from a file (import hi from func.py)

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.text import LabelBase

from kivy.core.window import Window
Window.clearcolor = (0.588, 0.824, 0.929, 0.8) #sets color in rgba
#rgb to rgba decimal convert link: http://www.corecoding.com/utilities/rgb-or-hex-to-float.php
#this handles first three values, last value is absorbance
#values in kivy are all 0-1

#screenone is just a main page with a bunch of tabs, please find pngs and change the icons
#this is a way to have main code all in same file
Builder.load_string("""
<ScreenOne>:
    FloatLayout:
        Image:
            source: 'hello.png'
            pos_hint: {'center_x': 0.5, 'center_y': 0.75}
            size_hint: 0.9, 0.9
            #pos hint is where you want to put it in respect of the screen length
            #size hint is how much of old size you want to display

        Label:
			id: name_label
			text: "Hello!"
            font_name: "Squad"
            pos: 0, 0
			font_size: 25
            keep_ratio: False
            allow_stretch: True

    BoxLayout:


        Button: #you can put images in buttons and change the buttons colors
            background_normal: 'home.png'
            background_color: 1, 1, 1, 0.8
            size: 147, 147
            size_hint: 0.1, 0.2
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_two'
        Button:
            background_normal: 'search.png'
            background_color: 1, 1, 1, 0.8
            size: 147, 147
            size_hint: 0.1, 0.2
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_three'
        Button:
            background_normal: 'settings.png'
            background_color: 1, 1, 1, 0.8
            size: 147, 147
            size_hint: 0.1, 0.2
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_four'

<ScreenTwo>:
    FloatLayout:
        Button:
            background_normal: 'backbutton.png'
            pos: 0, 710
            size: 100, 100
            size_hint: None, None

            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_one'
        Label:
			text: "This is how to display text"
            font_name: "Squad"
            pos: 5, 100
			font_size: 22


<ScreenThree>:
    FloatLayout:
        Button:

            background_normal: 'backbutton.png'
            pos: 0, 710
            size: 100, 100
            size_hint: None, None
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_one'

        Button:
            text: "Print hello: This is a function"
            font_name: "Squad"
            pos: 75, 100
            size: 291, 75
            size_hint: None, None
            background_color: 1, 1, 1, 1
            on_press:
                root.run()


<ScreenFour>:
    FloatLayout:
        Button:
            background_normal: 'backbutton.png'
            pos: 0, 710
            size: 100, 100
            size_hint: None, None
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_one'
        Button:
            text: "this is a button. You can control its size and color" #chang in the kv file
            text_size: self.width-50, None
            height: self.texture_size[1]
            width: 450
            font_name: "Squad"
            pos: 100, 100
            size: 241, 50
            background_color: 1, 1, 1, 1
            size_hint: None, None


		Label:
			id: name_label
			text: "Now try to make your own app introducing yourself"
            font_name: "Squad"
            pos: 5, 100
			font_size: 16


""")

#TO USE A FONT YOU MUST DOWNLOAD IT AND PUT IT IN THE FOLDER, SAME FOR IMAGES
LabelBase.register(name='Squad',
                   fn_regular='Squad.ttf') #this is labelbase, it controls your font_name
                   #squad is a font a found feel frere to research other ones



# Create a class for all screens in which you can include
# helpful methods specific to that screen
class ScreenOne(Screen):
    pass
#if you don't want to write any code and only want to display stuff than pass

class ScreenTwo(Screen):
    pass



class ScreenThree(Screen):
    def run(self): #I call the hi function in this function bc in the kv code you can only call the roots(screens) func
        hi() #put func inside this ScreenTwo func


class ScreenFour(Screen):
    pass


class ScreenFive(Screen):
    pass



screen_manager = ScreenManager() #this manages the screens

#this creates each screen with a class
screen_manager.add_widget(ScreenOne(name ="screen_one"))
screen_manager.add_widget(ScreenTwo(name ="screen_two"))
screen_manager.add_widget(ScreenThree(name ="screen_three"))
screen_manager.add_widget(ScreenFour(name ="screen_four"))
screen_manager.add_widget(ScreenFive(name ="screen_five"))


#screen_manager.current = "School Fed"

class ScreenApp(App): #name of class of app

    def build(self): #must return screen manager for it to work and run

        return screen_manager



# run the app, must always be present
sample_app = ScreenApp() #screenapp is the name of class of the app
sample_app.run()
