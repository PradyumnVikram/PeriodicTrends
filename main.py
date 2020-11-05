__author__ = "Pradyumn Vikram"
#all logic is in this file, for the UI please refer to NavigationHelper.py (kv code)
# Imports required for the app

import random

import pandas as pd
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel

#importing variables from the other file needed for the app like the UI and some helper variables
from NavigationHelper import navigation_helper, button_helper, help_content


# App class (Inherits from the MDApp class)
class PeriodicTrendsApp(MDApp):
    def draw(self, obj, val):
        for j in self.df['name']:
            if self.down_group_elements[4 - int(val - 1)] == j.lower():
                self.root.ids.main_img.source = "Assets/compressed_elements/{}-min-removebg-preview.png".format(
                    j.lower())
                self.root.ids.main_img.size_hint = (1, 1)
                self.root.ids.element_name.text = j

    # build function - runs when app is compiled
    def build(self):
        # some app attributes declared here along with the color code for each series
        # files used in the app also declared here
        self.sound = SoundLoader.load('Assets/table_song.wav')
        self.color_code = {
            'Nonmetals': (217 / 255, 83 / 255, 79 / 255, 1),
            'Noble gases': (255 / 255, 221 / 255, 60 / 255, 1),
            'Alkali metals': (15 / 255, 79 / 255, 52 / 255, 1),
            'Alkaline earth metals': (126 / 255, 126 / 255, 126 / 255, 1),
            'Metalloids': (40 / 255, 10 / 255, 92 / 255, 1),
            'Halogens': (0.6, 0, 0.9, 1),
            'Poor metals': (1, 140 / 255, 0, 1),
            'Transition metals': (0, 0.5, 0.75, 1),
            'Lanthanides': (0.7, 0.2, 0, 1),
            'Actinides': (80 / 255, 200 / 255, 120 / 255, 1)
        }
        self.df = pd.read_csv('Assets/elements.csv')
        self.question_df = pd.read_csv('Assets/questions_quiz.csv')
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "800"
        self.array_imageid = []
        # loads the UI for the app (declared in NavigationHelper.py)
        screen = Builder.load_string(navigation_helper)
        return screen

    # Common function to change screens in app
    def change_screen(self, name):
        self.root.ids.screen_manager.current = name

    # Helper functions for some buttons included in MDDialogs
    def close_d(self, obj):
        self.sound.stop()
        self.d.dismiss()

    def play_music(self, obj):  # plays the music in song section - called when button is pressed
        self.sound.play()

    def stop_music(self, obj):  # stops the music - called when button is pressed
        self.sound.stop()

    def play_song(self):  # dialog for the Song section in app

        close_button = MDRectangleFlatButton(text='Close', on_release=self.close_d)
        play_button = MDRectangleFlatButton(text='Play', on_release=lambda x: self.play_music(x))
        self.d = MDDialog(title="Periodic Table Song!", size_hint=(0.9, 1),
                          buttons=[play_button, close_button])

        self.d.text = "By - ASAPScience (A YouTube channel)"
        self.d.open()

    def draw_periodic(self):  # Function to draw the periodic table
        # some variable declarations
        ind = 1
        table = []
        count = 0
        row_num = 1

        # Adds the group headings in the forms of labels on top of the table
        for d in range(19):
            if d == 0:
                id_label = MDLabel(text=' ', halign="center")
            else:
                id_label = MDLabel(text=str(d), halign="center")
            self.root.ids.layout_screen.add_widget(id_label)
        # iterates through all 118 elements in the periodic table to print them on the screen
        for i, j in zip(self.df['symbol'], self.df['series']):
            # Adds the period headings before respective elements in the form of MDLabels
            if i in ['H', 'Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']:
                id_label2 = MDLabel(text=str(row_num), halign="center")
                self.root.ids.layout_screen.add_widget(id_label2)
                row_num += 1
            # Appends the elements from 56 - 72 and 88 - 104 to a list for adding to the layout at the end
            if 56 < ind < 72 or 88 < ind < 104:
                table.append([i, j])
                ind += 1
                continue
            # button bg color changed according to series of element
            self.background_color = self.color_code[j]
            btn = Builder.load_string(button_helper)
            # button text is set
            btn.text = i
            # adds the button to the screen
            self.root.ids.layout_screen.add_widget(btn)
            # conditions for formatting the grid layout
            if ind == 1:

                for i in range(16):
                    self.root.ids.layout_screen.add_widget(MDLabel())
            if ind == 4 or ind == 12:
                for i in range(10):
                    self.root.ids.layout_screen.add_widget(MDLabel())
            if ind == 56:
                self.root.ids.layout_screen.add_widget(MDLabel(text='57-71'))
            if ind == 88:
                self.root.ids.layout_screen.add_widget(MDLabel(text='89-103'))
            ind += 1
            count += 1
        for i in range(22):
            self.root.ids.layout_screen.add_widget(MDLabel())
        self.root.ids.layout_screen.add_widget(MDLabel(text="6 "))
        # adding the elements which were stored in an array from earlier
        id = 0
        for element in table:
            self.background_color = self.color_code[element[1]]
            self.text = element[0]
            btn = Builder.load_string(button_helper)
            btn.text = element[0]
            self.root.ids.layout_screen.add_widget(btn)
            if id == 14:
                for i in range(3):
                    self.root.ids.layout_screen.add_widget(MDLabel())
                self.root.ids.layout_screen.add_widget(MDLabel(text='7 '))
            id += 1

    # Function for simulating the atomic slider for across the period
    def draw_across(self, obj, value):
        for i, j in zip(self.df['atomic_number'], self.df['name']):

            if int(value) == i:
                if i != 18:
                    # loads the atomic configuration simulation image
                    self.root.ids.main_img.source = "Assets/compressed_elements/{}-min-removebg-preview.png".format(
                        j.lower())
                    # statement for decreasing the size of elements as we go across the table
                    self.root.ids.main_img.size_hint = (
                        1 - 3 * float('0.{}'.format(i)), 3 * 1 - float('0.{}'.format(i)))
                    self.root.ids.element_name.text = j
                else:
                    # we print normal size for argon since it is an exception to decreasing size
                    self.root.ids.main_img.source = "Assets/compressed_elements/{}-min-removebg-preview.png".format(
                        j.lower())
                    self.root.ids.main_img.size_hint = (1, 1)
                    self.root.ids.element_name.text = j

    # function which runs when the app starts everytime - all variables declared here
    def on_start(self):
        # changes current screen to periodic table screen
        self.change_screen("screen2")
        self.q = 1
        self.background_color = (1, 1, 1, 1)
        # binding default values to slider and setting some default values
        self.root.ids.element_slider_table.bind(value=self.data_table)
        self.root.ids.element_slider_table.value = 1
        self.root.ids.name_element.text = self.df['name'][0]
        self.root.ids.number_element.text = str(self.df['atomic_number'][0])
        self.root.ids.Description.text = self.df['description'][0]
        self.root.ids.radius_element.text = 'Atomic radius: ' + str(self.df['atomic_radius'][0]) + ' pm'
        self.down_group_elements = ['hydrogen', 'lithium', 'sodium', 'potassium', 'rubidium']
        self.root.ids.heading_conf.text = "ATOMIC SIZE"
        self.correct = 0
        self.attempted = 0
        self.root.ids.slider_element.bind(value=self.draw)
        self.root.ids.slider_element_2.bind(value=self.draw_across)
        self.root.ids.slider_element.value = 5
        self.root.ids.correct_score.text = '\n\n{}/{}'.format(self.correct, self.attempted)
        self.id = random.choice(self.question_df['Id'])
        self.root.ids.question_text.text = self.question_df['Question'][self.id - 1]
        self.root.ids.option_1.text = 'A) ' + self.question_df['Option1'][self.id - 1]
        self.root.ids.option_2.text = 'B) ' + self.question_df['Option2'][self.id - 1]
        self.root.ids.option_3.text = 'C) ' + self.question_df['Option3'][self.id - 1]
        self.root.ids.option_4.text = 'D) ' + self.question_df['Option4'][self.id - 1]
        self.root.ids.question_number.text = "\n\n           Question {}".format(self.q)
        self.root.ids.question_text.text = '\n\n' + self.question_df['Question'][self.id - 1]
        self.root.ids.title_text.text = "PERIODIC TABLE OF ELEMENTS"
        # drawing the periodic table by calling the function written above
        self.draw_periodic()

    # function for the MDDialog opened by elements in the periodic table - called in the self.draw_periodic() function
    def print_data(self, args):
        description = ''
        # retrieving values and adding them to the final content of the dialog
        for i, j, k, m, l, n, o, p in zip(self.df['name'], self.df['description'], self.df['mass'], self.df['symbol'],
                                          self.df['density'], self.df['atomic_radius'], self.df['boiling_point'],
                                          self.df['melting_point']):
            if m == args:
                if p == 'none':
                    p = 'Unknown'
                else:
                    p += ' K'

                if o == 'none':
                    o = 'Unknown'
                else:
                    o += ' K'
                description = '\n\n' + 'Denstiy: ' + str(round(l, 2)) + '\n\n' + 'Atomic Mass: ' + str(
                    k) + ' amu' + '\n\n' + 'Atomic Radius: ' + str(n) + ' pm' + '\n\n' + 'Boiling Point: ' + str(
                    o) + '\n\n' + 'Melting Point: ' + str(p)
                title = i
        # adding the close button
        close_button = MDRectangleFlatButton(text='Close', on_release=self.close_dialog)
        self.dialog = MDDialog(size_hint=(0.7, 1),
                               buttons=[close_button])
        self.dialog.title = title
        self.dialog.text = description

        self.dialog.open()

    # helper functions for closing some dialogs
    def close_dialog(self, obj):
        self.dialog.dismiss()

    def close_dialog_atomic_size(self, obj):
        self.atomic_dialog.dismiss()

    def help_dialog_atomic_size(self):  # dialog which opens when you open the help section in atomic size
        close_button = MDRectangleFlatButton(text='Close', on_release=self.close_dialog_atomic_size)
        self.atomic_dialog = MDDialog(size_hint=(0.7, 1), title="Help", buttons=[close_button], text=help_content)
        self.atomic_dialog.open()

    # some helper functions for closing dialogs
    def close_dialog_correct(self, obj):
        self.dialog_correct.dismiss()

    def close_dialog_elements(self, obj):
        self.dialog_element.dismiss()

    def go_to_element_group(self, obj, group):
        self.dialog_element.dismiss()
        self.change_screen("screen2")

    # function for content in the dialog which opens when you press series in the key for elements section of the periodic table
    def dialog_elements(self, group):
        to_print = '\n\n'
        count = 0
        # retrieving all elements of the series button clicked from the elements.csv file and adding to final content
        for i, j in zip(self.df['name'], self.df['series']):
            if j == group:
                if j == 'Transition metals':
                    if count == 1:
                        to_print += '  * ' + i + ' \n'
                        count = 0
                    else:
                        to_print += ' * ' + i
                        count += 1
                else:
                    to_print += ' * ' + i + '\n'
        # creating go to elements button and close button helper functions for which have been declared above
        close_button = MDRectangleFlatButton(text='Close', on_release=self.close_dialog_elements)
        el_button = MDRectangleFlatButton(text='Go to elements',
                                          on_release=lambda args: self.go_to_element_group(args, group))
        # creating, adding content and opening the dialog
        self.dialog_element = MDDialog(buttons=[el_button, close_button], size_hint=(0.7, 1))
        self.dialog_element.title = group
        self.dialog_element.text = to_print
        self.dialog_element.open()

    # function which checks if answer entered in quiz is correct or wrong
    def check_answer(self, option):
        # retrieving question and the correct answer from question_quiz.csv
        for answer, question in zip(self.question_df['CorrectAnswer'], self.question_df['Question']):
            if self.root.ids.question_text.text == '\n\n' + question:
                # dialog to be shown when answer is correct
                if answer == option:

                    close_button = MDRectangleFlatButton(text='Next Question', on_release=self.close_dialog_correct)
                    self.dialog_correct = MDDialog(size_hint=(0.7, 1),
                                                   buttons=[close_button])
                    self.dialog_correct.title = 'Correct Answer!'
                    self.dialog_correct.text = "\n\nGood Job!\n\nYou got it right!\n\nReady for the next one?"
                    self.dialog_correct.open()
                    self.correct += 1
                # Dialog to be shown when answer is wrong
                else:

                    close_button = MDRectangleFlatButton(text='Next Question', on_release=self.close_dialog_correct)
                    self.dialog_correct = MDDialog(size_hint=(0.7, 1),
                                                   buttons=[close_button])
                    self.dialog_correct.title = 'Wrong Answer!'
                    self.dialog_correct.text = "\n\nAww better luck next time!\n\nThe correct answer was: {}".format(
                        answer)
                    self.dialog_correct.open()
        # changing UI Variables with formatting for next question
        self.id = random.choice(self.question_df['Id'])
        self.attempted += 1
        self.root.ids.correct_score.text = '\n\n{}/{}'.format(self.correct, self.attempted)
        self.root.ids.question_text.text = '\n\n' + self.question_df['Question'][self.id - 1]
        self.root.ids.option_1.text = 'A) ' + self.question_df['Option1'][self.id - 1]
        self.root.ids.option_2.text = 'B) ' + self.question_df['Option2'][self.id - 1]
        self.root.ids.option_3.text = 'C) ' + self.question_df['Option3'][self.id - 1]
        self.root.ids.option_4.text = 'D) ' + self.question_df['Option4'][self.id - 1]
        self.q += 1
        self.root.ids.question_number.text = "\n\n           Question {}".format(self.q)

    # function called when the 'Explore' feature is used
    def data_table(self, obj, value):
        # retrieving data for element based on slider value
        for i, j, k, l in zip(self.df['atomic_number'], self.df['name'], self.df['description'],
                              self.df['atomic_radius']):
            if int(i) == int(value):
                # changing the label values for the screen
                self.root.ids.name_element.text = j
                self.root.ids.number_element.text = str(i)
                self.root.ids.Description.text = k
                self.root.ids.radius_element.text = 'Atomic Radius: ' + str(l) + ' pm'


# Running the app
PeriodicTrendsApp().run()
