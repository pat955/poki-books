from defaults import *
import json
from functools import partial

class Theme:
    def __init__(self, name, color=COLOR, font_color=FONT_COLOR, button_color=BUTTON_COLOR, active_background=ACTIVE_BACKGROUND, active_font=ACTIVE_FONT, font=FONT, font_size=FONT_SIZE, heading_size=HEADING_SIZE):
        self.name               = name              # str
        self.color              = color             # str
        self.font_color         = font_color        # str
        self.button_color       = button_color      # str
        self.active_background  = active_background # str
        self.active_font        = active_font       # str
        self.font               = font              # str
        self.font_size          = font_size         # int
        self.heading_size       = heading_size      # int
    

    def add(self, window, index):
        window.themes_button.add_radiobutton(
            label=self.name, 
            command=partial(
                window.change_theme, 
                self.color, 
                self.font_color, 
                self.button_color, 
                self.active_background, 
                self.active_font, 
                self.font, 
                self.font_size, 
                self.heading_size
                ), value=index, indicator=0)

class AllThemes:
    def __init__(self):
        self.themes = []

    def make_themes(self):
        with open('themes.txt', 'r') as file:
            for theme in file:
                theme_dict = eval(theme)
                self.themes.append(Theme(**theme_dict))
            file.close()
    
    def get_all_themes(self):
        self.make_themes()
        return self.themes