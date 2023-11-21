from kivy.factory import Factory
from kivy.lang import Builder
from kivymd.app import MDApp
import sqlite3
import mysql.connector
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import re
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivymd.uix.card import MDCard
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

Window.size = (370, 600)







class Shoes(Screen):
    def on_button_press(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'billing'
class Shoes(Screen):
    def on_button_press(self):
        if self.manager.current != 'shoes':
            self.manager.transition = SlideTransition(direction='right')
            self.manager.current = 'shoes'
class Shoes(Screen):
    def on_button_press(self):
        if self.manager.current != 'kids':
            self.manager.transition = SlideTransition(direction='right')
            self.manager.current = 'kids'


class Shoes(Screen):
    def on_button_press(self):
        if self.manager.current != 'women':
            self.manager.transition = SlideTransition(direction='right')
            self.manager.current = 'women'
class TrendyApp(MDApp):

    def show_custom_bottom_sheet(self, image, price, rate):
        bottom_sheet = Factory.ContentCustomSheet()
        bottom_sheet.rate = rate
        bottom_sheet.image = image
        bottom_sheet.price = price
        self.custom_sheet = MDCustomBottomSheet(screen=bottom_sheet)
        self.custom_sheet.open()


    def switch_to_shoes_screen(self):
        self.root.current = 'shoes'

    def switch_to_women_screen(self):
        self.root.current = 'women'

    def switch_to_billing_screen(self):
        if self.custom_sheet:
            self.custom_sheet.dismiss()  # Close the bottom sheet if it's open
            self.root.current = "billing"

    def switch_to_kids_screen(self):
        self.root.current = 'kids'


    def build(self):
        self.title = 'Trendy Foot Wear'
        self.theme_cls.primary_palette = "Orange"
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("home.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        screen_manager.add_widget(Builder.load_file("shoes.kv"))
        screen_manager.add_widget(Builder.load_file("women.kv"))
        screen_manager.add_widget(Builder.load_file("kids.kv"))
        screen_manager.add_widget(Builder.load_file("billing.kv"))
        return screen_manager




TrendyApp().run()
