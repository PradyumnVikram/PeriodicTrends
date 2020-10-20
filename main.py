import random

import pandas as pd
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivy.core.window import Window

from NavigationHelper import navigation_helper, button_helper


class LineEllipse1(Widget):
    pass


class LineEllipse2(Widget):
    pass


class LineEllipse3(Widget):
    pass

class SimulationScreen(Widget):
    pass

class PeriodicTrendsApp(MDApp):
    def draw(self):

        self.shell_order = {'k': 0, 'l': 0, 'm': 0}
        for i, j, k, l, m in zip(self.df['atomic_number'], self.df['name'], self.df['ElectronsK'],
                                 self.df['ElectronsL'], self.df['ElectronsM']):
            if int(self.root.ids.text_thing.text) == i:
                self.root.ids.element_name.text = j
                self.shell_order['k'] = int(k) + int(l) + int(m)


        # adding image id in the array

        if len(self.array_imageid) > 0:
                for i in self.array_imageid:
                    self.root.ids.screen_manager.get_screen('screen1').remove_widget(i)
                self.array_imageid = []

        for h in range(self.shell_order['k']):
            img = Image(source="Assets/electron.jpg")
            self.array_imageid.append(img)
            img.pos = self.get_pos(h)
            img.size_hint_x = 0.05
            img.size_hint_y = 0.05
            self.root.ids.screen_manager.get_screen("screen1").add_widget(img)

    def get_pos(self, number):
        if number == 0:
            #print(1)
            self.pos1 = 2.8
            self.pos2 = 2

        elif number == 1:
            self.pos1 = 3
            self.pos2 = 2
        elif number == 3:
            self.pos1 = 8
            self.pos2 = 16
        return Window.width // self.pos1, Window.height // self.pos2

    def build(self):
        self.group_dict = {}
        self.pos1 = 4
        self.pos2 = 2
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
        self.array_imageid= []
        screen = Builder.load_string(navigation_helper)
        return screen

    def change_screen(self, name):
        self.root.ids.screen_manager.current = name

    def draw_periodic(self, highlight=None):
        ind = 1
        table = []
        for i, j in zip(self.df['symbol'], self.df['series']):
            if 56 < ind < 72 or 88 < ind < 104:
                table.append([i, j])
                ind += 1
                continue
            self.background_color = self.color_code[j]
            btn = Builder.load_string(button_helper)
            btn.text = i
            if j in self.group_dict:
                self.group_dict[j].append(btn)
            else:
                self.group_dict[j] = [btn]
            self.root.ids.layout_screen.add_widget(btn)
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
        for i in range(19):
            self.root.ids.layout_screen.add_widget(MDLabel())
        self.root.ids.layout_screen.add_widget(MDLabel(text="57-71"))
        id = 0
        for element in table:
            self.background_color = self.color_code[element[1]]
            self.text = element[0]
            btn = Builder.load_string(button_helper)
            btn.text = element[0]
            self.root.ids.layout_screen.add_widget(btn)
            if id == 14:
                for i in range(2):
                    self.root.ids.layout_screen.add_widget(MDLabel())
                self.root.ids.layout_screen.add_widget(MDLabel(text='89-103'))
            id += 1

    def on_start(self):
        self.q = 1
        #self.correct_sound = SoundLoader.load('correct.wav')
        self.correct = 0
        self.attempted = 0
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
        self.draw_periodic()

    def print_data(self, args):
        description = ''

        for i, j, k, m, l, n in zip(self.df['name'], self.df['description'], self.df['mass'], self.df['symbol'],
                                    self.df['density'], self.df['atomic_radius']):
            if m == args:
                description = '\n\n' + 'Denstiy: ' + str(round(l, 2)) + '\n\n' + 'Atomic Mass: ' + str(
                    k) + '\n\n' + 'Atomic Radius: ' + str(n)
                title = i
        close_button = MDRectangleFlatButton(text='Close', on_release=self.close_dialog)
        self.dialog = MDDialog(size_hint=(0.7, 1),
                               buttons=[close_button])
        self.dialog.title = title
        self.dialog.text = description

        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def close_dialog_correct(self, obj):
        self.dialog_correct.dismiss()

    def close_dialog_elements(self, obj):
        self.dialog_element.dismiss()

    def go_to_element_group(self, obj, group):
        self.dialog_element.dismiss()
        self.root.ids.screen_manager.current = "screen2"

    def dialog_elements(self, group):

        close_button = MDRectangleFlatButton(text='Close', on_release=self.close_dialog_elements)
        el_button = MDRectangleFlatButton(text='Go to elements',
                                          on_release=lambda args: self.go_to_element_group(args, group))
        self.dialog_element = MDDialog(size_hint=(0.7, 1),
                                       buttons=[el_button, close_button])
        self.dialog_element.title = group
        self.dialog_element.open()

    def check_answer(self, option):
        for answer, question in zip(self.question_df['CorrectAnswer'], self.question_df['Question']):
            if self.root.ids.question_text.text == '\n\n' + question:
                if answer == option:

                    close_button = MDRectangleFlatButton(text='Next Question', on_release=self.close_dialog_correct)
                    self.dialog_correct = MDDialog(size_hint=(0.7, 1),
                                                   buttons=[close_button])
                    self.dialog_correct.title = 'Correct Answer!'
                    self.dialog_correct.text = "\n\nGood Job!\n\nYou got it right!\n\nReady for the next one?"
                    self.dialog_correct.open()
                    self.correct += 1
                else:

                    close_button = MDRectangleFlatButton(text='Next Question', on_release=self.close_dialog_correct)
                    self.dialog_correct = MDDialog(size_hint=(0.7, 1),
                                                   buttons=[close_button])
                    self.dialog_correct.title = 'Wrong Answer!'
                    self.dialog_correct.text = "\n\nAww better luck next time!\n\nThe correct answer was: {}".format(
                        answer)
                    self.dialog_correct.open()
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


# Running the app
PeriodicTrendsApp().run()
