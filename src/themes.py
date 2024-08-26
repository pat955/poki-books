"""
-- themes.py --
Creates themes
"""
import tkinter
from functools import partial
from defaults import *  # pylint: disable=W0401


class Theme:
    """
    TODO: add one more public method
    Theme, name not optional.
    """

    def __init__(
            self,
            name: str,
            color: str = COLOR,             # background color
            font_color: str = FONT_COLOR,        # font color for all text
            button_color: str = BUTTON_COLOR,      #
            active_background: str = ACTIVE_BACKGROUND,
            active_font: str = ACTIVE_FONT,       #
            font: str = FONT,              # font used for everything
            font_size: int = FONT_SIZE,         # main font size for book text
            heading_size: int = HEADING_SIZE       # font size for heading and titles
    ) -> None:
        """
        TODO: add docs
        """
        self.name = name              # str
        self.color = color             # str
        self.font_color = font_color        # str
        self.button_color = button_color      # str
        self.active_background = active_background  # str
        self.active_font = active_font       # str
        self.font = font              # str
        self.font_size = font_size         # int
        self.heading_size = heading_size      # int

    def add(self, window: tkinter.Frame, index: int) -> None:
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
    """
    Collection of all themes
    TODO: Add one more public method
    """

    def __init__(self) -> None:
        self.themes = []

    def __make_themes(self) -> None:
        """
        Makes themes form themes.txt
        """
        starter_themes = [
            {'name': 'Default',
             'color': 'white',
             'font_color': 'black',
             'button_color': 'lavender',
             'active_background': 'white',
             'active_font': 'black'},
            {'name': 'Dark',
             'color': 'gray11',
             'font_color': 'white',
             'button_color': 'steel blue',
             'active_background': 'skyblue3',
             'active_font': 'white',
             'font': 'Times New Roman',
             'font_size': 20,
             'heading_size': 30},
            {'name': 'Cute',
             'color': '#E4F1EE',
             'font_color': 'black',
             'button_color': '#DEDAF4',
             'active_background': 'pink',
             'active_font': 'black'},
            {'name': 'Latte',
             'color': '#fdf7e4',
             'font_color': '#75543d',
             'button_color': '#dfcbae',
             'active_background': '#e6dac7',
             'active_font': '#432411'},
            {'name': 'Froggy',
             'color': 'ivory2',
             'font_color': '#667b68',
             'button_color': '#dde6d5',
             'active_background': '#a3b899',
             'active_font': '#3a453b'},
            {'name': 'Discord',
             'color': '#2c2f33',
             'font_color': 'white',
             'button_color': '#7289da',
             'active_background': '#99aab5',
             'active_font': 'white'},
            {'name': 'Vintage',
             'color': '#e2d9b3',
             'font_color': 'black',
             'button_color': '#92b080',
             'active_background': '#c9dcaf',
             'active_font': 'black'}
        ]
        for theme in starter_themes:
            self.themes.append(Theme(**theme))

    def get_all_themes(self) -> list:
        """
        Returns all themes from themes.txt
        """
        if len(self.themes) == 0:
            self.__make_themes()
        return self.themes
