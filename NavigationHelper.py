navigation_helper = """
#: import MDRoundImageButton kivymd.uix.button.MDRoundImageButton

        
<LineEllipse1>:
    canvas:
        Color:
            rgba: 0, 0, 0, .9
        Line:
            width: 2.
            circle:
                (self.center_x, self.center_y, min(self.width, self.height)
                / 6)
<LineEllipse2>:
    canvas:
        Color:
            rgba: 0, 0, 0, .9
        Line:
            width: 2.
            circle:
                (self.center_x, self.center_y, min(self.width, self.height)
                / 4)

<LineEllipse3>:
    canvas:
        Color:
            rgba: 0, 0, 0, .9
        Line:
            width: 2.
            circle:
                (self.center_x, self.center_y, min(self.width, self.height)
                / 3)
NavigationLayout:
    ScreenManager:
        id: screen_manager
        
        Screen:
            name: "screen1"
            Image:
                source: "Assets/nucleus.png"                
                halign: 'center'
                pos_hint: {'center_x':0.5, 'center_y':0.5}
                size_hint: (0.15, 0.15)
            BoxLayout:
                orientation: 'vertical'
                MDToolbar:
                    title: 'PeriodicTrends'
                    left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                MDLabel:
                    id: itsjustthere2
                MDLabel:
                    id: itsjustthere4
                

                MDLabel:
                    id: itsjustthere3
                MDLabel:
                    id: itsjustthere5
                MDLabel:
                    id: itsjustthere6
                MDLabel:
                    id: itsjustthere7
                MDLabel:
                    id: itsjustthere8
                MDLabel:
                    id: itsjustthere9
                MDLabel:
                    id: itsjustthere10
                    
                MDTextField:
                    id: text_thing
                MDRectangleFlatButton:
                    id: buttonS
                    on_press: app.draw()
                    text:"submit"
                MDLabel:
                    id: itsjustthere
                MDLabel:
                    id: element_name
                    pos_hint: {'center_x':0.5, 'center_y':0.5}
                    valign: "center"
                    halign: "center"
                    
                MDLabel:
                    id: idk
                    
                    
            LineEllipse1:
            LineEllipse2:
            LineEllipse3:
            
                
        Screen:
        
            name: "screen2"
            BoxLayout:
                orientation: 'vertical'
                
                MDToolbar:
                    title: 'PeriodicTrends'
                    left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                    right_action_items: [["help", lambda x: app.change_screen("help_screen")]]
                MDLabel:
                
                    font_style: "H6"
                    size_hint: (None, None)
                    size_hint_x: 1
                    id: title_text
                    halign: "center"
                    valign: "center"
                
                ScrollView:
                    size_hint: (1, 1)
                    MDGridLayout:
                        padding: "8dp"
                        spacing: "8dp"
                        adaptive_height: True
                        adaptive_width: True
                        id: layout_screen    
                        cols: 18
                
        Screen:
            name: "screen3"
            ScrollView:  
                MDBoxLayout:    
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'PeriodicTrends - QUIZ!'
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                    GridLayout:
                        rows: 1
                        MDLabel:
                            text: "Question 1"
                            valign: "top"
                            halign: "left"
                            id: question_number
                            size_hint: (None, None)
                            height: 10
                            size_hint_x: 0.7
                        
                        MDLabel:
                            valign: "top"
                            halign: "center"
                            size_hint: (None, None)
                            height: 10
                            size_hint_x: 0.7
                            id: correct_score
                    
                    
                    MDBoxLayout:
                        adaptive_height: True
                        orientation: "vertical"
                        padding: "32dp"
                        size_hint_y: 1.0 - self.height/root.height
                        MDLabel:
                            id: question_text
                            halign: "center"
                            size_hint_y: None
                            height: self.texture_size[1]
                        #MDLabel:
                        #
                         #   halign: "center"
                          #  size_hint: (None, None)
                           # size_hint_x: 1
                            #height: 10
                        MDLabel:
                            id: option_1
                            
                            halign: "center"
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDLabel:
                            id: option_2
                            halign: "center"
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDLabel:
                            id: option_3
                            halign: "center"
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDLabel:
                            id: option_4
                            halign: "center"
                            size_hint_y: None
                            height: self.texture_size[1]
                        
                        MDLabel:
                            halign: "center"
                            size_hint: (None, None)
                            height: 50
                            size_hint_x: 1
                    

                        GridLayout:
                            rows: 1
                            spacing: "16dp"
                            valign: "center"
                            MDLabel:
                                size_hint_x: None
                                width: self.texture_size[0]
                            
                            MDRectangleFlatButton:
                                valign: "center"
                                id: answer_1
                                halign: "center"
                                text: "A"
                                on_press: app.check_answer('a')
                            

                            
                            MDRectangleFlatButton:
                                id: answer_2
                                valign: "center"
                                halign: "center"
                                text: "B"
                                on_press: app.check_answer('b')

                                
                            MDRectangleFlatButton:
                                id: answer_3
                                valign: "center"
                                halign: "center"
                                text: "C"
                                on_press: app.check_answer('c')

                                
                            MDRectangleFlatButton:
                                id: answer_4
                                valign: "center"
                                halign: "center"
                                text: "D"
                                on_press: app.check_answer('d')
                
                
                
                    Widget:#Over
        Screen:
            name: "screen4"
            BoxLayout:
                orientation: 'vertical'
                MDToolbar:
                    title: 'Demo Application'
                    left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                
                MDLabel:
                    text: 'screen4'
                Widget:
        Screen:
            name: "help_screen"
            BoxLayout:
                orientation: 'vertical'
                MDToolbar:
                    title: 'PeriodicTrends - Help Periodic Table'
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
        id: nav_drawer
        BoxLayout:
            orientation: 'vertical'
            spacing: '8dp'
            padding: '8dp'
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
                        on_release: screen_manager.current = "screen1"
                        text: 'Electronic configurations'
                        IconLeftWidget:
                            icon: 'chemical-weapon'
                    OneLineIconListItem:
                        on_release: screen_manager.current = "screen2"
                        text: 'Periodic Table'
                        IconLeftWidget:
                            icon: 'periodic-table'
                    OneLineIconListItem:
                        on_release: screen_manager.current = "screen3"
                        text: 'Quiz'
                        
                        IconLeftWidget:
                            icon: 'test-tube'
            
"""

button_helper = """
MDFillRoundFlatButton:
    theme: "custom"
    on_press: app.print_data(self.text)
    md_bg_color: app.background_color
"""
