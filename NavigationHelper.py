#UI for the entire app is defined here, this involves the positioning of various elements all logic is in main.py file
navigation_helper = """
#: import MDRoundImageButton kivymd.uix.button.MDRoundImageButton

#putting the app in a navigation layout
NavigationLayout:
    ScreenManager:
        id: screen_manager
        #screen1 which is the atomic size simulator
        Screen:
        #adding all elements to this screen
            name: "screen1"
            Image:
                source: "Assets/nucleus.png"                
                halign: 'center'
                pos_hint: {'center_x':0.5, 'center_y':0.5}
                id: main_img
            MDSlider:
                max: 5
                min: 1
                id: slider_element
                orientation: "vertical"
                size_hint: (1, 0.7)
                pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                hint: False
            BoxLayout:
            #setting some default values
                theme: "custom"
                md_bg_color: (204/255,219/255,238/255,1)
                orientation: 'vertical'
                #adding the top toolbar
                MDToolbar:
                    title: 'Atomic Size Simulator'
                    left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                    right_action_items: [["help", lambda x: app.help_dialog_atomic_size()]]
                
                MDLabel:
                    id: heading_conf
                    valign: "center"
                    halign: "center"
                

                MDLabel:
                    id: itsjustthere3
                    text: "Down a group-                 "
                    halign: "right"
                #empty labels added for positioning the other elements
                MDLabel:
                    id: spacing
                MDLabel:    
                    id: spacing
                MDLabel:
                    id: spacing
                MDLabel:
                    id: spacing
                MDLabel:
                    id: spacing
                MDLabel:
                    id: spacing
                MDLabel:
                    id: spacing
                MDLabel:
                    id: spacing
                MDLabel:
                    id: spacing
                MDLabel:
                    id: spacing
                    text: "   Across a period - "
                MDSlider:
                    max: 18
                    min: 11
                    id: slider_element_2
                    size_hint: (0.8, 1)
                    hint: False
                    
                

                MDLabel:
                    id: element_name
                    pos_hint: {'center_x':0.5, 'center_y':0.5}
                    valign: "center"
                    halign: "center"
                
                    
                MDLabel:
                    id: spacing
                    
                    
                
            
                
        Screen:
            #screen2 which is the periodic table
            name: "screen2"
            BoxLayout:
                orientation: 'vertical'
                
                MDToolbar:
                    title: 'Periodic Table'
                    left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                    right_action_items: [["help", lambda x: app.change_screen("help_screen")]]
                MDLabel:
                
                    font_style: "H6"
                    size_hint: (None, None)
                    size_hint_x: 1
                    id: title_text
                    halign: "center"
                    valign: "center"
                #adding the grid layout in which the elements get added
                ScrollView:
                    size_hint: (1, 1)
                    MDGridLayout:
                        padding: "8dp"
                        spacing: "8dp"
                        adaptive_height: True
                        adaptive_width: True
                        id: layout_screen    
                        cols: 19
                
        Screen:
        #screen3 which is the quiz
            name: "screen3"
            ScrollView:  
                BoxLayout:    
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'QUIZ!'
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                    #grid layout for the above info on quiz
                    GridLayout:
                        rows: 1
                        MDLabel:
                            text: "Question 1"
                            valign: "top"
                            halign: "left"
                            id: question_number
                            size_hint: (None, None)
                            height: 2
                            size_hint_x: 0.7
                        
                        MDLabel:
                            valign: "top"
                            halign: "center"
                            size_hint: (None, None)
                            height: 2
                            size_hint_x: 0.7
                            id: correct_score
                    

                   #     adaptive_height: True
                   #     orientation: "vertical"
                  #      spacing: "32dp"
                   #     padding: "32dp"
                    #    size_hint_y: 1.0 - self.height/root.height
                    #spacing
                    MDLabel:
                    MDLabel:
                    #boxlayout for question text and the options the values are changed in main.py
                    BoxLayout:
                        spacing: "32dp"
                        orientation: "vertical"
                        MDLabel:
                            id: question_text
                            halign: "left"
                            size_hint_y: None
                            bold: True
                            height: self.texture_size[1]
                        MDLabel:
                            id: option_1
                            
                            halign: "left"
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDLabel:
                            id: option_2
                            halign: "left"
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDLabel:
                            id: option_3
                            halign: "left"
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDLabel:
                            id: option_4
                            halign: "left"
                            size_hint_y: None
                            height: self.texture_size[1]
                    
                    #grid layout for the option buttons
                    GridLayout:
                        rows: 1
                        spacing: "16dp"
                        valign: "center"
                        halign: "center"
                        MDLabel:
                            size_hint_x: None
                            width: self.texture_size[0]
                        
                        MDRaisedButton:
                            valign: "center"
                            id: answer_1
                            halign: "center"
                            theme: "custom"
                            md_bg_color: (104/255, 136/255, 190/255, 1)
                            text: "A"
                            on_press: app.check_answer('a')
                        

                        
                        MDRaisedButton:
                            id: answer_2
                            valign: "center"
                            halign: "center"
                            text: "B"
                            on_press: app.check_answer('b')
                            theme: "custom"
                            md_bg_color: (104/255, 136/255, 190/255, 1)

                            
                        MDRaisedButton:
                            id: answer_3
                            valign: "center"
                            halign: "center"
                            text: "C"
                            on_press: app.check_answer('c')
                            theme: "custom"
                            md_bg_color: (104/255, 136/255, 190/255, 1)

                            
                        MDRaisedButton:
                            id: answer_4
                            valign: "center"
                            halign: "center"
                            text: "D"
                            on_press: app.check_answer('d')
                            theme: "custom"
                            md_bg_color: (104/255, 136/255, 190/255, 1)
                
                
                
                    Widget:
        Screen:
            name: "screen4"
            #screen4 which is the Explore section
            BoxLayout:
                orientation: 'vertical'
                MDToolbar:
                    title: 'The Elements'
                    left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                #adding the elements
                MDLabel:
                    id: name_element
                    halign: "center"
                    font_style: "H3"
                    valign: "center"
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    id: spacing
                    size_hint_y: 0.3
                MDFillRoundFlatButton:
                    id: number_element
                    halign: "center"
                    disabled: True
                    valign: "center"
                    bold: True
                    md_bg_color: (255/255, 242/255, 204/255, 1)
                    pos_hint: {'center_x':0.5, 'center_y': 0.5}
                    style: "H6"
                    valign: "center"
                MDLabel:
                    id: radius_element
                    halign: "center"
                    style: "H6"
                    valign: "center"
                MDLabel:
                    size_hint_y: 0.2
                MDLabel:
                    text: "   Description - "
                    font_style: "H6"
                    theme: "custom"
                    halign: "left"
                    color: (35/255,60/255,103/255,1)
                MDLabel:
                    size_hint_y: None
                    height: self.texture_size[1]
                    id: Description
                    halign: "center"
                    style: "H6"
                    valign: "center"
                    size_hint_y: None
                MDLabel:
                    size_hint_y: 0.2
                MDLabel:
                    size_hint_y: 0.2
                MDSlider:
                    max: 118
                    min: 1
                    id: element_slider_table
                    thumb_color_down: app.theme_cls.accent_color
                Widget:
        Screen:
            name: "help_screen"
            BoxLayout:
                orientation: 'vertical'
                MDToolbar:
                    title: 'Help Periodic Table'
                    left_action_items: [["page-previous", lambda x: app.change_screen("screen2")]]
                
                MDLabel:
                    text: "   Key for elements"
                    font_style: "H6"
                    size_hint: (None, None)
                    size_hint_x: 1
                GridLayout:
                    rows: 5
                    padding: "6dp"
                    spacing: "6dp"
                    MDFillRoundFlatButton:
                
                        text: 'Nonmetals'
                        md_bg_color: app.color_code['Nonmetals']
                        on_press: app.dialog_elements('Nonmetals')
                    MDFillRoundFlatButton:
            
                        text: 'Noble gases'
                        md_bg_color: app.color_code['Noble gases']
                        on_press: app.dialog_elements('Noble gases')
                    MDFillRoundFlatButton:
            
                        text: 'Alkali metals'
                        md_bg_color: app.color_code['Alkali metals']
                        on_press: app.dialog_elements('Alkali metals')
                    MDFillRoundFlatButton:
            
                        text: 'Alkaline earth metals'
                        md_bg_color: app.color_code['Alkaline earth metals']
                        on_press: app.dialog_elements('Alkaline earth metals')
                    MDFillRoundFlatButton:
            
                        text: 'Metalloids'
                        md_bg_color: app.color_code['Metalloids']
                        on_press: app.dialog_elements('Metalloids')
                    MDFillRoundFlatButton:
            
                        text: 'Halogens'
                        md_bg_color: app.color_code['Halogens']
                        on_press: app.dialog_elements('Halogens')
                    MDFillRoundFlatButton:
            
                        text: 'Poor metals'
                        md_bg_color: app.color_code['Poor metals']
                        on_press: app.dialog_elements('Poor metals')
                    MDFillRoundFlatButton:
            
                        text: 'Transition metals'
                        md_bg_color: app.color_code['Transition metals']
                        on_press: app.dialog_elements('Transition metals')
                    MDFillRoundFlatButton:
            
                        text: 'Lanthanides'
                        md_bg_color: app.color_code['Lanthanides']
                        on_press: app.dialog_elements('Lanthanides')
                    MDFillRoundFlatButton:
            
                        text: 'Actinides'
                        md_bg_color: app.color_code['Actinides']
                        on_press: app.dialog_elements('Actinides')
                
                
                Widget:

    MDNavigationDrawer:
    #menu for the entire app
        id: nav_drawer
        BoxLayout:
            orientation: 'vertical'
            spacing: '8dp'
            padding: '8dp'
            
            #adding the app logo
            Image:
                source: 'Assets/logo.png'
            MDLabel:
                text: '   The world of atoms, at your fingertips'
                font_style: 'Subtitle1'
                size_hint_y: None
                height: self.texture_size[1]
            ScrollView:
                MDList:
                    OneLineIconListItem:
                        on_release: screen_manager.current = "screen2"
                        text: 'Periodic Table'
                        IconLeftWidget:
                            icon: 'periodic-table'
                    OneLineIconListItem:
                        on_release: screen_manager.current = "screen1"
                        text: 'Atomic Size'
                        IconLeftWidget:
                            icon: 'chemical-weapon'
                    OneLineIconListItem:
                        on_release: screen_manager.current = "screen3"
                        text: 'Quiz'
                        
                        IconLeftWidget:
                            icon: 'test-tube'
                    
                    OneLineIconListItem:
                        on_release: screen_manager.current = "screen4"
                        text: 'Explore'
                        
                        IconLeftWidget:
                            icon: 'atom'
                            
                    OneLineIconListItem:
                        on_release: app.play_song()
                        text: 'Song'
                        
                        IconLeftWidget:
                            icon: 'music'
    
"""
#variable for the button in periodic table (elements), added as they all have some common formatting which can be done here
button_helper = """
MDFillRoundFlatButton:
    theme: "custom"
    on_press: app.print_data(self.text)
    md_bg_color: app.background_color
"""

#content for the atomic size simulator help dialog - imported in main.py
help_content = """
The across slider is there for you to toggle and see how the elements of a period (in this case the third period from Sodium to Argon) vary in atomic size, you will notice how the size reduces but immediately increases when you reach argon which is an inert gas and has the Van der Waals radius which is larger than covalent and ionic radii 
\nThe down slider when toggled shows that how new shells are added as you go down a group (in this case group 1, from Hydrogen to Francium, for the sake of explanation we have only simulated from Hydrogen to Rubidium)
"""
