"""
-- themes.py --

"""
import ast
from functools import partial
from defaults import * 

class Theme:
    """
    Theme, name not optional. 
    """
    def __init__(
            self,
            name,
            color=COLOR,                            # background color
            font_color=FONT_COLOR,                  # font color for all text
            button_color=BUTTON_COLOR,              # 
            active_background=ACTIVE_BACKGROUND,    # 
            active_font=ACTIVE_FONT,                #
            font=FONT,                              # font used for everything
            font_size=FONT_SIZE,                    # main font size for book text
            heading_size=HEADING_SIZE               # font size for heading and titles
            ):
        self.name               = name              # str
        self.color              = color             # str
        self.font_color         = font_color        # str
        self.button_color       = button_color      # str
        self.active_background  = active_background # str
        self.active_font        = active_font       # str
        self.font               = font              # str
        self.font_size          = font_size         # int
        self.heading_size       = heading_size      # int

    def add(self, window, index): # Returns: None
        """
        Adds radiobutton to window variable of the theme
        """
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
    """ Collection of all themes """
    def __init__(self):
        self.themes = []

    def __make_themes(self): # Returns: None
        """
        Makes themes form themes.txt
        """
        with open('themes.txt', 'r') as file:
            for theme in file:
                theme_dict = ast.literal_eval(theme)
                self.themes.append(Theme(**theme_dict))
            file.close()

    def get_all_themes(self): # Returns: [Theme]
        """
        Returns all themes from themes.txt
        """
        if len(self.themes) == 0:
            self.__make_themes()
        return self.themes
