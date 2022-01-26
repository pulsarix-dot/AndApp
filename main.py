from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivymd.theming import ThemeManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem, MDList
from kivy.properties import StringProperty, ListProperty
import webbrowser
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

Window.size = (360, 800)

KV = '''

# Menu item in the DrawerList list.

<Content>
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"

    MDTextField:
        
        id: t1
        hint_text: "Meno"

    MDTextField:
        id: t2
        hint_text: "Výkon"
        

<ItemDrawer>:
    theme_text_color: "Custom"
    on_press:
        app.root.ids.nav_drawer.set_state("close")
        app.root.ids.screen_manager.current = self.text.lower()

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color


<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "data/logo/kivy-icon-256.png"

    MDLabel:
        text: "Telocvikársky program"
        font_style: "Button"
        adaptive_height: True
        height: self.texture_size[1]

    MDLabel:
        text: "infoteloprogram@gmail.com"
        font_style: "Caption"
        adaptive_height: True
        height: self.texture_size[1]

    ScrollView:

        DrawerList:
            id: md_list

<NavigationDrawer>:
    orientation: 'vertical'

    MDToolbar:
        title: "Telocvikársky program"
        elevation: 10
        left_action_items: [["menu", lambda x: app.root.ids.nav_drawer.set_state("open")]]

    Widget:

MDScreen:

    MDNavigationLayout:

        ScreenManager:
            id: screen_manager

            MDScreen:
                name: "domov"
                NavigationDrawer:

                MDBoxLayout:
                    MDLabel:
                        text: "Telocvikársky program"
                        halign: "center"
                        font_size: '45sp'
                        color: 0, 0, 0, 1

                MDFloatLayout:
                    MDLabel:
                        text: "Program na pomoc učiteľom Telesnej výchovy"
                        halign: "center"
                        font_size: '25sp'
                        color: "FF6D00"
                        pos_hint: {"center_x": .5, "center_y": .30}


        
            MDScreen:
                name: "vkladanie disciplín"
                NavigationDrawer:



                MDFloatLayout:


                    MDRoundFlatButton:
                        text: "     Hod medicimbálom     "
                        pos_hint: {"center_x": .5, "center_y": .88}  
                        text_color: 0, 0, 0, 1
                        line_color: 0, 0, 0, 1 
                        font_size: 0.46 * self.height
                        on_release: app.show_first_dialog()

                    MDRoundFlatButton:
                        text: "          Výdrž v zhybe          "
                        pos_hint: {"center_x": .5, "center_y": .81}  
                        text_color: 0, 0, 0, 1
                        line_color: 0, 0, 0, 1 
                        font_size: 0.46 * self.height
                        on_release: app.show_first_dialog()

                    MDRoundFlatButton:
                        text: "                 Zhyby                 "
                        pos_hint: {"center_x": .5, "center_y": .74}  
                        text_color: 0, 0, 0, 1
                        line_color: 0, 0, 0, 1 
                        font_size: 0.46 * self.height
                        on_release: app.show_first_dialog()

                    MDRoundFlatButton:
                        text: "           Člnkový beh           "
                        pos_hint: {"center_x": .5, "center_y": .67}  
                        text_color: 0, 0, 0, 1
                        line_color: 0, 0, 0, 1 
                        font_size: 0.46 * self.height
                        on_release: app.show_first_dialog()

                    MDRoundFlatButton:
                        text: "                 50m                 "
                        pos_hint: {"center_x": .5, "center_y": .60}  
                        text_color: 0, 0, 0, 1
                        line_color: 0, 0, 0, 1 
                        font_size: 0.46 * self.height
                        on_release: app.show_first_dialog()

                    MDRoundFlatButton:
                        text: "               1000m               "
                        pos_hint: {"center_x": .5, "center_y": .53}  
                        text_color: 0, 0, 0, 1
                        line_color: 0, 0, 0, 1 
                        font_size: 0.46 * self.height
                        on_release: app.show_first_dialog()

                    MDRoundFlatButton:
                        text: "                3000m                "
                        pos_hint: {"center_x": .5, "center_y": .46}  
                        text_color: 0, 0, 0, 1
                        line_color: 0, 0, 0, 1 
                        font_size: 0.46 * self.height
                        on_release: app.show_first_dialog()

                    MDRoundFlatButton:
                        text: "          Hod granatom          "
                        pos_hint: {"center_x": .5, "center_y": .40}  
                        text_color: 0, 0, 0, 1
                        line_color: 0, 0, 0, 1 
                        font_size: 0.46 * self.height
                        on_release: app.show_first_dialog()

                    MDRoundFlatButton:
                        text: "         Skok do piesku         "
                        pos_hint: {"center_x": .5, "center_y": .34}  
                        text_color: 0, 0, 0, 1
                        line_color: 0, 0, 0, 1 
                        font_size: 0.46 * self.height
                        on_release: app.show_first_dialog()

                    MDRoundFlatButton:
                        text: "               Sed-ľah               "
                        pos_hint: {"center_x": .5, "center_y": .28}  
                        text_color: 0, 0, 0, 1
                        line_color: 0, 0, 0, 1 
                        font_size: 0.46 * self.height
                        on_release: app.show_first_dialog()

                    MDRoundFlatButton:
                        text: "   Veslovanie 500 metrov   "
                        pos_hint: {"center_x": .5, "center_y": .22}  
                        text_color: 0, 0, 0, 1
                        line_color: 0, 0, 0, 1 
                        font_size: 0.46 * self.height
                        on_release: app.show_first_dialog()

                    MDRoundFlatButton:
                        text: "                  Kľuky                  "
                        pos_hint: {"center_x": .5, "center_y": .16}  
                        text_color: 0, 0, 0, 1
                        line_color: 0, 0, 0, 1 
                        font_size: 0.46 * self.height
                        on_release: app.show_first_dialog()

                    MDRoundFlatButton:
                        text: "      Preskoky cez lavičku     "
                        pos_hint: {"center_x": .5, "center_y": .10}  
                        text_color: 0, 0, 0, 1
                        line_color: 0, 0, 0, 1 
                        font_size: 0.46 * self.height
                        on_release: app.show_first_dialog()

                    MDRoundFlatButton:
                        text: "           Skok do diaľky           "
                        pos_hint: {"center_x": .5, "center_y": .04}  
                        text_color: 0, 0, 0, 1
                        line_color: 0, 0, 0, 1 
                        font_size: 0.46 * self.height
                        on_release: app.show_first_dialog()


            MDScreen:
                name: "štatistika"
                NavigationDrawer:

                BoxLayout:
                    MDLabel:
                        text: "Štatistika"
                        halign: "center"

            MDScreen:
                name: "zobraziť hodnotenia"
                NavigationDrawer:

                BoxLayout:
                    MDLabel:
                        text: "Štatistika"
                        halign: "center"

            MDScreen:
                name: "ukážka cvikov"
                NavigationDrawer:


                MDFloatLayout:


                    MDRoundFlatButton:
                        pos_hint: {"center_x": .5, "center_y": .88}
                        text_color: 0, 0, 0, 1
                        line_color: 0, 0, 0, 1
                        font_size: 0.46 * self.height
                        width: 90
                        height: 59
                        text:"   Hod medicimbálom   "
                        on_release:
                            import webbrowser
                            webbrowser.open("https://www.sportujeme.sk/medicinbal-odhody-na-rozvoj-vybusnej-sily-video/")

                    MDRoundFlatButton:
                        pos_hint: {"center_x": .5, "center_y": .81}
                        text_color: 0, 0, 0, 1
                        line_color: 0, 0, 0, 1   
                        font_size: 0.46 * self.height
                        width: 90
                        height: 59           
                        text:"        Výdrž v zhybe        "
                        on_release:
                            import webbrowser
                            webbrowser.open("https://workout4u.eu/ako-spravne-cvicit-vydrz-v-zhybe") 

                    MDRoundFlatButton:
                        pos_hint: {"center_x": .5, "center_y": .74}
                        text_color: 0, 0, 0, 1
                        line_color: 0, 0, 0, 1
                        font_size: 0.46 * self.height
                        width: 90
                        height: 59 
                        text:"            Zhyby - ch            "
                        on_release:
                            import webbrowser
                            webbrowser.open("https://www.youtube.com/watch?v=QUaxOQCxb9c")

                    MDRoundFlatButton:
                        pos_hint: {"center_x": .5, "center_y": .67}
                        text_color: 0, 0, 0, 1
                        line_color: 0, 0, 0, 1
                        font_size: 0.46 * self.height
                        width: 90
                        height: 59 
                        text:"             Člnk. beh             "
                        on_release:
                            import webbrowser
                            webbrowser.open("https://www.youtube.com/watch?v=3Mkora5mHH8")

                    MDRoundFlatButton:
                        pos_hint: {"center_x": .5, "center_y": .60}
                        text_color: 0, 0, 0, 1
                        line_color: 0, 0, 0, 1
                        font_size: 0.46 * self.height
                        width: 90
                        height: 59 
                        text:"                50m                  "
                        on_release:
                            import webbrowser
                            webbrowser.open("https://www.rogelli.sk/technika-behu/")

                    MDRoundFlatButton:
                        pos_hint: {"center_x": .5, "center_y": .53}
                        text_color: 0, 0, 0, 1
                        line_color: 0, 0, 0, 1
                        font_size: 0.46 * self.height
                        width: 90
                        height: 59 
                        text:"              1500m               "
                        on_release:
                            import webbrowser
                            webbrowser.open("https://beh.sk/poradna/casto-sa-vyskytujuce-chyby-pri-bezeckom-treningu/")

                    MDRoundFlatButton:
                        pos_hint: {"center_x": .5, "center_y": .46}
                        text_color: 0, 0, 0, 1
                        line_color: 0, 0, 0, 1
                        font_size: 0.46 * self.height
                        width: 90
                        height: 59 
                        text:"              3000m               "
                        on_release:
                            import webbrowser
                            webbrowser.open("https://cs.wikipedia.org/wiki/B%C4%9Bh_na_3000_metr%C5%AF")

                    MDRoundFlatButton:
                        pos_hint: {"center_x": .5, "center_y": .40}
                        text_color: 0, 0, 0, 1
                        line_color: 0, 0, 0, 1
                        font_size: 0.46 * self.height
                        width: 90
                        height: 59 
                        text:"        Hod granatom        "
                        on_release:
                            import webbrowser
                            webbrowser.open("https://www.youtube.com/watch?v=YAX8wmyrpQU")

                    MDRoundFlatButton:
                        pos_hint: {"center_x": .5, "center_y": .34}
                        text_color: 0, 0, 0, 1
                        line_color: 0, 0, 0, 1
                        font_size: 0.46 * self.height
                        width: 90
                        height: 59 
                        text:"        Skok do piesku        "
                        on_release:
                            import webbrowser
                            webbrowser.open("https://www.youtube.com/watch?v=0AKixhpPVAk")

                    MDRoundFlatButton:
                        pos_hint: {"center_x": .5, "center_y": .28}
                        text_color: 0, 0, 0, 1
                        line_color: 0, 0, 0, 1
                        font_size: 0.46 * self.height
                        width: 90
                        height: 59 
                        text:"               Sed-ľah               "
                        on_release:
                            import webbrowser
                            webbrowser.open("https://www.youtube.com/watch?v=yJbpOrt3itA")

                    MDRoundFlatButton:
                        pos_hint: {"center_x": .5, "center_y": .22}
                        text_color: 0, 0, 0, 1
                        line_color: 0, 0, 0, 1
                        font_size: 0.46 * self.height
                        width: 90
                        height: 59 
                        text:"    Veslovanie do 500m    "
                        on_release:
                            import webbrowser
                            webbrowser.open("https://www.youtube.com/watch?v=zQ82RYIFLN8")

                    MDRoundFlatButton:
                        pos_hint: {"center_x": .5, "center_y": .16}
                        text_color: 0, 0, 0, 1
                        line_color: 0, 0, 0, 1
                        font_size: 0.46 * self.height
                        width: 90
                        height: 59 
                        text:"                 Kľuky                 "
                        on_release:
                            import webbrowser
                            webbrowser.open("https://www.youtube.com/watch?v=IODxDxX7oi4")

                    MDRoundFlatButton:
                        pos_hint: {"center_x": .5, "center_y": .10}
                        text_color: 0, 0, 0, 1
                        line_color: 0, 0, 0, 1
                        font_size: 0.46 * self.height
                        width: 90
                        height: 59 
                        text:"     Preskok cez lavičku     "
                        on_release:
                            import webbrowser
                            webbrowser.open("https://www.youtube.com/watch?v=3wDLcHQb3vQ")

                    MDRoundFlatButton:
                        pos_hint: {"center_x": .5, "center_y": .04}
                        text_color: 0, 0, 0, 1
                        line_color: 0, 0, 0, 1
                        font_size: 0.46 * self.height
                        width: 90
                        height: 59 
                        text:"          Skok do diaľky          "
                        on_release:
                            import webbrowser
                            webbrowser.open("https://www.youtube.com/watch?v=9kONQrcrZdc")

            MDScreen:
            
                name: "ukaž výsledky"
                
                NavigationDrawer:
                
                    MDBoxLayout:
                    
                        MDLabel:
                            id: med_label
                            text: "   "
                            halign: "center"
                            font_size: '30sp'
                            color: 0, 0, 0, 1
                                   

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer
'''

class Content(BoxLayout):
    pass


class NavigationDrawer(BoxLayout):
    pass


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class Telocvikársky_Program(MDApp):
    dialog = None

    def __init__(self, pk=None, **kwargs):
        super().__init__(**kwargs)
        # state a pk which we shall use link the list items with the database primary keys
        self.pk = pk

    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.primary_hue = "200"
        return Builder.load_string(KV)

    def on_start(self):
        icons_item = {
            "home": "Domov",
            "folder": "Vkladanie disciplín",
            "account-multiple": "Štatistika",
            "star": "Zobraziť hodnotenia",
            "history": "Ukážka cvikov",
            "checkbox-marked": "Ukaž výsledky",
            "upload": "Uložiť",
        }
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )



    def show_first_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Zadaj výkon:",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDRectangleFlatButton(
                        text="Exit", text_color=self.theme_cls.primary_color, on_release=self.close_dialog
                    ),
                    MDRectangleFlatButton(
                        text="Pridať", text_color=self.theme_cls.primary_color, on_release=self.net_dialog
                    ),

                ],
            )

        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def net_dialog(self, obj):
        print("Exercise: "+ self.dialog.content_cls.ids.t1.text)
        print("Value: "+ self.dialog.content_cls.ids.t2.text)
        self.ids.med_label.text = name





Telocvikársky_Program().run()