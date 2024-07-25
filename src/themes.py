from defaults import *
import json
from functools import partial

class Theme:
    def __init__(self, name, color, font_color, button_color, active_background, active_font, font, font_size, heading_size):
        self.name               = name              # str
        self.color              = COLOR             # str
        self.font_color         = FONT_COLOR        # str
        self.button_color       = BUTTON_COLOR      # str
        self.active_background  = ACTIVE_BACKGROUND # str
        self.active_font        = ACTIVE_FONT       # str
        self.font               = FONT              # str
        self.font_size          = FONT_SIZE         # int
        self.heading_size       = HEADING_SIZE      # int
    

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
                print(theme_dict)
                self.themes.append(from_dict_to_theme(theme_dict))
                break
            file.close()
    
    def get_all_themes(self):
        self.make_themes()
        return self.themes

def from_dict_to_theme(d):
    return Theme(
        name=d['name'], 
        color=d['color'], 
        font_color=d['font_color'], 
        button_color=d['button_color'], 
        active_background=d['active_background'], 
        active_font=d['active_font'], 
        font=d['font'], 
        font_size=d['font_size'], 
        heading_size=d['heading_size']
        )