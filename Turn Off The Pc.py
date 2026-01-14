import os
import sys
import psutil

def resource_path(rel_path):
    try:
        base_path =  sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')

    return os.path.join(base_path, rel_path)

import customtkinter
from PIL import Image, ImageTk
import time as tm
import tkinter.messagebox as msbox

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('ShutPC')
        width = (int(self.winfo_screenwidth()) // 2) - 255
        height = (int(self.winfo_screenheight()) // 2) - 200
        self.geometry(f'511x305+{width}+{height}') #320x240 #511x305
        self.resizable(False, False)
        icon = resource_path('timer.ico')
        self.iconbitmap(icon)
  

        
        if getattr(sys, 'frozen', False):
            applic_path = os.path.dirname(sys.executable)

        else:
            applic_path = os.path.dirname(os.path.abspath(__file__))

        config_path = os.path.join(applic_path, 'config.txt')

        if not os.path.exists(config_path):
            with open(config_path, 'w', encoding = 'utf-8') as f:
                f.write('МГолубойТ')



        file = open('config.txt', 'r', encoding = 'utf-8')
        text = file.read()
        self.color = text[1:int(len(text)) - 1]
        self.themeq = text[-1]
        self.otktext = text[0]
        file.close()
        print(self.color)
        print(self.themeq)
        print(self.otktext)


        self.otkq = 60000

        
        print('otk:', self.otktext)
        print('pered:', self.color)
        print('pered:', self.themeq)

        def quit(event):
            self.destroy()
        self.bind('<Alt_L>', quit)


        def hour_minus():
            hour_m = int(self.entry_hour.get()) - 1
            if 0 <= hour_m < 100:
                self.entry_hour.delete(0, 20)
                self.entry_hour.insert(0, hour_m)
            else:
                self.entry_hour.insert(0, '')

        def hour_plus():
            hour_p  = int(self.entry_hour.get()) + 1
            if 0 < hour_p <= 99:
                self.entry_hour.delete(0, 20)
                self.entry_hour.insert(0, hour_p)
            else:
                self.entry_hour.insert(0, '')

        def minut_minus():
            minut_m = int(self.entry_minut.get()) - 1
            if 0 <= minut_m < 100:
                self.entry_minut.delete(0, 20)
                self.entry_minut.insert(0, minut_m)
            else:
                self.entry_minut.insert(0, '')

        def minut_plus():
            minut_p = int(self.entry_minut.get()) + 1
            sum = int(self.entry_hour.get()) + int(self.entry_minut.get())

            if int(self.entry_hour.get()) >= 99 and minut_p == 61:
                self.entry_minut.insert(0, '')
            elif int(self.entry_hour.get()) <= 99 and 0 < minut_p <= 99:
                self.entry_minut.delete(0, 20)
                self.entry_minut.insert(0, minut_p) 
            else:
                self.entry_minut.insert(0, '')

        def validate(text):
            if text.isdigit() or text == '':
                return True
            else:
                return False

        def sett():
            self.setings_b.place(x = 600, y = 600) # 455 0
            self.close.place(x = 455, y = 0) # 700 100
            self.save.place(x = 455, y = 56) # 700 100

            self.str_b.place(x = 600, y = 600) # 15 155
            self.stop_b.place(x = 600, y = 600) # 15 240
            self.hour_minus_button.place(x = 600, y = 600) # 15 30
            self.hour_plus_button.place(x = 600, y = 600) # 205 30
            self.minut_minus_button.place(x = 600, y = 600) # 15 100
            self.minut_plus_button.place(x = 600, y = 600) # 205 100
            self.entry_hour.place(x = 600, y = 600) # 55 30
            self.entry_minut.place(x = 600, y = 600) # 55 100
            self.hour_text.place(x = 600, y = 600) # 104 2
            self.minut_text.place(x = 600, y = 600) # 92 72 
            self.time_out_h.place(x = 600, y = 600) # 279 10
            self.time_out_m.place(x = 600, y = 600) # 279 145
            self.time.place(x = 600, y = 600) # 272 0
            self.hour_t.place(x = 700, y = 700) # 435 119
            self.minut_t.place(x = 600,  y = 600) # 435 254
            self.frame_2.place(x = 600, y = 600) # 0 0
            self.frame_1.place(x = 600, y = 600)

            self.option_themes.place(x = 260, y = 10) # 700 100
            self.themes.place(x = 40, y = 10) # 700 100

            self.option_colors.place(x = 260, y = 50) # 700 100
            self.colors.place(x = 40, y = 50)

            self.otk.place(x = 260, y = 90)
            self.otk_text.place(x = 40, y = 90)


            self.frame_3.place(x = 700, y = 600)
            self.frame_4.place(x = 0, y = 0)
            self.frame_5.place(x = 426, y = 0)            
            self.frame_6.place(x = 455, y = 0)
            

        def close():
            self.setings_b.place(x = 455, y = 0)
            self.close.place(x = 700, y = 100)
            self.save.place(x = 700, y = 100)

            self.str_b.place(x = 15, y = 155)
            self.stop_b.place(x = 15, y = 240)
            self.hour_minus_button.place(x = 15, y = 30)
            self.hour_plus_button.place(x = 205, y = 30)
            self.minut_minus_button.place(x = 15, y = 100)
            self.minut_plus_button.place(x = 205, y = 100)
            self.entry_hour.place(x = 55, y = 30)
            self.entry_minut.place(x = 55, y = 100)
            self.hour_text.place(x = 104, y = 2)
            self.minut_text.place(x = 92, y = 72)
            self.time_out_h.place(x = 279, y = 10)
            self.time_out_m.place(x = 279, y = 145)
            self.time.place(x = 272, y = 0)
            self.hour_t.place(x = 435, y = 119)
            self.minut_t.place(x = 435, y = 254)
            self.frame_2.place(x = 0, y = 0)

            self.themes.place(x = 700, y = 100)
            self.option_themes.place(x = 700, y = 100)
            self.colors.place(x = 700, y = 100)
            self.option_colors.place(x = 700, y = 100)
            self.otk.place(x = 700, y = 100)
            self.otk_text.place(x = 700, y = 100)
            self.frame_1.place(x = 455, y = 0)
            self.frame_3.place(x = 700, y = 100)
            self.frame_4.place(x = 700, y = 600)
            self.frame_6.place(x = 700, y = 600)
            self.frame_5.place(x = 700, y = 600)

            if self.otk_var.get() == 'Минутам':
                self.hour_text.place(x = 104, y = 2)
                self.minut_text.place(x = 92, y = 72)
            else:
                self.hour_text.place(x = 92, y = 2)
                self.minut_text.place(x = 89, y = 72)

        def option_themes(value):
            print('value:', value)

            if value == 'Темная':
                customtkinter.set_appearance_mode('Dark')
                self.frame_1.configure(fg_color = '#2E2E2E')
                self.frame_2.configure(fg_color = '#2E2E2E')
                self.frame_3.configure(fg_color = '#2E2E2E')
                self.frame_4.configure(fg_color = '#2E2E2E')
                self.frame_5.configure(fg_color = '#2E2E2E')
                self.hour_text.configure(fg_color = '#2E2E2E')
                self.minut_text.configure(fg_color = '#2E2E2E')


            elif value == 'Светлая':
                customtkinter.set_appearance_mode('Light')
                self.frame_1.configure(fg_color = '#D6D6D6')
                self.frame_2.configure(fg_color = '#D6D6D6')
                self.frame_3.configure(fg_color = '#D6D6D6')
                self.frame_4.configure(fg_color = '#D6D6D6')
                self.frame_5.configure(fg_color = '#D6D6D6')
                self.hour_text.configure(fg_color = '#D6D6D6')
                self.minut_text.configure(fg_color = '#D6D6D6')


        def option_colors(value):
            print('value:', value)

# голубой: #346EBA  #3A5B87  #283F5E
# голубой: #346EBA  #3A5B87  
# красный: #FF4242  #B04C4C
# зеленый: #52D163  #4E9158
# оранжевый: #DB9960  #8F623C
# фиолетовый: #5B3982  #9250DE

            if value == 'Голубой':
                # голубой: #346EBA  #3A5B87  #283F5E

                self.frame_6.configure(fg_color = '#283F5E')
                self.str_b.configure(fg_color = '#346EBA',    # цвет в целом
                                     hover_color = '#3A5B87') # цвет при наведении
                
                self.stop_b.configure(fg_color = '#346EBA',
                                     hover_color = '#3A5B87')
                self.hour_minus_button.configure(fg_color = '#346EBA',
                                     hover_color = '#3A5B87')
                self.hour_plus_button.configure(fg_color = '#346EBA',
                                     hover_color = '#3A5B87')
                self.minut_minus_button.configure(fg_color = '#346EBA',
                                     hover_color = '#3A5B87')
                self.minut_plus_button.configure(fg_color = '#346EBA',
                                     hover_color = '#3A5B87')
                self.setings_b.configure(fg_color = '#346EBA',
                                     hover_color = '#3A5B87')
                self.close.configure(fg_color = '#346EBA',
                                     hover_color = '#3A5B87')
                self.save.configure(fg_color = '#346EBA',
                                     hover_color = '#3A5B87')
                self.option_themes.configure(fg_color = '#346EBA', 
                    button_color = '#346EBA', button_hover_color = '#3A5B87')
                self.option_colors.configure(fg_color = '#346EBA', 
                    button_color = '#346EBA', button_hover_color = '#3A5B87')
                self.otk.configure(fg_color = '#346EBA', 
                    button_color = '#346EBA', button_hover_color = '#3A5B87')
                
            elif value == 'Красный':
                # красный: #D65656  #B04C4C  #723131

                self.frame_6.configure(fg_color = '#723131')
                self.str_b.configure(fg_color = '#D65656',    # цвет в целом
                                     hover_color = '#B04C4C') # цвет при наведении
                
                self.stop_b.configure(fg_color = '#D65656',
                                     hover_color = '#B04C4C')
                self.hour_minus_button.configure(fg_color = '#D65656',
                                     hover_color = '#B04C4C')
                self.hour_plus_button.configure(fg_color = '#D65656',
                                     hover_color = '#B04C4C')
                self.minut_minus_button.configure(fg_color = '#D65656',
                                     hover_color = '#B04C4C')
                self.minut_plus_button.configure(fg_color = '#D65656',
                                     hover_color = '#B04C4C')
                self.setings_b.configure(fg_color = '#D65656',
                                     hover_color = '#B04C4C')
                self.close.configure(fg_color = '#D65656',
                                     hover_color = '#B04C4C')
                self.save.configure(fg_color = '#D65656',
                                     hover_color = '#B04C4C')
                self.option_themes.configure(fg_color = '#D65656', 
                    button_color = '#D65656', button_hover_color = '#B04C4C')
                self.option_colors.configure(fg_color = '#D65656', 
                    button_color = '#D65656', button_hover_color = '#B04C4C')
                self.otk.configure(fg_color = '#D65656', 
                    button_color = '#D65656', button_hover_color = '#B04C4C')

            elif value == 'Зеленый':
                # зеленый: #41904B  #407347  #315A37

                self.frame_6.configure(fg_color = '#315A37')
                self.str_b.configure(fg_color = '#41904B',    # цвет в целом
                                     hover_color = '#407347') # цвет при наведении
  
                self.stop_b.configure(fg_color = '#41904B',
                                     hover_color = '#407347')
                self.hour_minus_button.configure(fg_color = '#41904B',
                                     hover_color = '#407347')
                self.hour_plus_button.configure(fg_color = '#41904B',
                                     hover_color = '#407347')
                self.minut_minus_button.configure(fg_color = '#41904B',
                                     hover_color = '#407347')
                self.minut_plus_button.configure(fg_color = '#41904B',
                                     hover_color = '#407347')
                self.setings_b.configure(fg_color = '#41904B',
                                     hover_color = '#407347')
                self.close.configure(fg_color = '#41904B',
                                     hover_color = '#407347')
                self.save.configure(fg_color = '#41904B',
                                     hover_color = '#407347')
                self.option_themes.configure(fg_color = '#41904B', 
                    button_color = '#41904B', button_hover_color = '#407347')
                self.option_colors.configure(fg_color = '#41904B', 
                    button_color = '#41904B', button_hover_color = '#407347')
                self.otk.configure(fg_color = '#41904B', 
                    button_color = '#41904B', button_hover_color = '#407347')

            elif value == 'Оранжевый':
                # оранжевый: #C4834D  #8F623C  #61432A

                self.frame_6.configure(fg_color = '#61432A')
                self.str_b.configure(fg_color = '#C4834D',    # цвет в целом
                                     hover_color = '#8F623C') # цвет при наведении
                
                self.stop_b.configure(fg_color = '#C4834D',
                                     hover_color = '#8F623C')
                self.hour_minus_button.configure(fg_color = '#C4834D',
                                     hover_color = '#8F623C')
                self.hour_plus_button.configure(fg_color = '#C4834D',
                                     hover_color = '#8F623C')
                self.minut_minus_button.configure(fg_color = '#C4834D',
                                     hover_color = '#8F623C')
                self.minut_plus_button.configure(fg_color = '#C4834D',
                                     hover_color = '#8F623C')
                self.setings_b.configure(fg_color = '#C4834D',
                                     hover_color = '#8F623C')
                self.close.configure(fg_color = '#C4834D',
                                     hover_color = '#8F623C')
                self.save.configure(fg_color = '#C4834D',
                                     hover_color = '#8F623C')
                self.option_themes.configure(fg_color = '#C4834D', 
                    button_color = '#C4834D', button_hover_color = '#8F623C')
                self.option_colors.configure(fg_color = '#C4834D', 
                    button_color = '#C4834D', button_hover_color = '#8F623C')
                self.otk.configure(fg_color = '#C4834D', 
                    button_color = '#C4834D', button_hover_color = '#8F623C')

            elif value == 'Фиолетовый':
                # фиолетовый: #9250DE  #5B3982  #462B64

                self.frame_6.configure(fg_color = '#462B64')
                self.str_b.configure(fg_color = '#9250DE',    # цвет в целом
                                     hover_color = "#462B64") # цвет при наведении
                
                self.stop_b.configure(fg_color = '#9250DE',
                                     hover_color = '#5B3982')
                self.hour_minus_button.configure(fg_color = '#9250DE',
                                     hover_color = '#5B3982')
                self.hour_plus_button.configure(fg_color = '#9250DE',
                                     hover_color = '#5B3982')
                self.minut_minus_button.configure(fg_color = '#9250DE',
                                     hover_color = '#5B3982')
                self.minut_plus_button.configure(fg_color = '#9250DE',
                                     hover_color = '#5B3982')
                self.setings_b.configure(fg_color = '#9250DE',
                                     hover_color = '#5B3982')
                self.close.configure(fg_color = '#9250DE',
                                     hover_color = '#5B3982')
                self.save.configure(fg_color = '#9250DE',
                                     hover_color = '#5B3982')
                self.option_themes.configure(fg_color = '#9250DE', 
                    button_color = '#9250DE', button_hover_color = '#5B3982')
                self.option_colors.configure(fg_color = '#9250DE', 
                    button_color = '#9250DE', button_hover_color = '#5B3982')
                self.otk.configure(fg_color = '#9250DE', 
                    button_color = '#9250DE', button_hover_color = '#5B3982')


        def otk_value(value):
            print('Выбран режим:', value)

            if value == 'Минутам':
                print('M')
                self.hour_text.configure(text = 'Часы:')
                self.minut_text.configure(text = 'Минуты:')

                self.hour_t.configure(text = 'H')
                self.minut_t.configure(text = 'M')
                self.otkq = 60000
            elif value == 'Секундам':
                print('S')
                self.hour_text.configure(text = 'Минуты:')
                self.minut_text.configure(text = 'Секунды:')

                self.hour_t.configure(text = 'M')
                self.minut_t.configure(text = 'S')
                self.otkq = 1000

        def filepath(file_path, content):
            with open(file_path, 'w', encoding = 'utf-8') as f:
                f.write(content)
            print('saved')

        def save():
            color = self.color_var.get()
            theme = self.theme_var.get()[0]
            otk = self.otk_var.get()[0]
            print('color:', color)  # Работает
            print('theme:', theme)  # Работает
            print('otk:', otk)  # Работает

            
            content = str(otk) + str(color) + str(theme)

            
            filepath('config.txt', content)


        settings_image = Image.open(resource_path('settings.png'))
        settings_photo = ImageTk.PhotoImage(settings_image)

        close_image = Image.open(resource_path('close.png'))
        close_photo = ImageTk.PhotoImage(close_image)

        save_image = Image.open(resource_path('save.png'))
        save_photo = ImageTk.PhotoImage(save_image)

  
# напиши свитч с функцией автовыключения пк исходя из нагрузки пк на цп

        self.frame_1 = customtkinter.CTkFrame(self, 
            width = 58, height = 440,
            fg_color = '#2E2E2E', corner_radius = 0)
        self.frame_1.place(x = 455, y = 0)

        self.frame_2 = customtkinter.CTkFrame(self,
            width = 260, height = 440, 
            fg_color = '#2E2E2E', corner_radius = 0)
        self.frame_2.place(x = 0, y = 0)

        self.frame_3 = customtkinter.CTkFrame(self,
            width = 230, height = 310,
            fg_color = '#2E2E2E', corner_radius = 0)
        self.frame_3.place(x = 700, y = 100)

        self.frame_4 = customtkinter.CTkFrame(self,
            width = 30, height = 310,
            fg_color = '#2E2E2E', corner_radius = 0)
        self.frame_4.place(x = 700, y = 600)

        self.frame_5 = customtkinter.CTkFrame(self,
            width = 30, height = 310,
            fg_color = '#2E2E2E', corner_radius = 0)
        self.frame_5.place(x = 700, y = 600)

        self.frame_6 = customtkinter.CTkFrame(self,
            width = 58, height = 310,
            fg_color = "#315A37", corner_radius = 0)
        self.frame_6.place(x = 700, y = 600)

        self.setings_b = customtkinter.CTkButton(self,
            image = settings_photo, width = 56, height = 56, 
            corner_radius = 0, text = '', 
            fg_color = '#346EBA', hover_color = '#3A5B87',
            command = sett)
        self.setings_b.place(x = 455, y = 0)

        self.close = customtkinter.CTkButton(self,
            image = close_photo, width = 56, height = 56,
            corner_radius = 0, text = '',
            fg_color = '#346EBA', hover_color = '#3A5B87',
            command = close)
        self.close.place(x = 700, y = 100)

        self.save = customtkinter.CTkButton(self,
            image = save_photo, text = '',
            width = 56, height = 56, corner_radius = 0,
            fg_color = '#346EBA', hover_color = '#3A5B87',
            command = save)
        self.save.place(x = 700, y = 100)


        self.themes = customtkinter.CTkLabel(self,
            text = 'Тема приложения:', 
            font = ('Arial', 19))
        self.themes.place(x = 700, y = 100)

        self.theme_var = customtkinter.StringVar()

        self.option_themes = customtkinter.CTkOptionMenu(self,
            width = 150, height = 30,
            font = ('Arial', 16), corner_radius = 0,
            fg_color = '#346EBA', button_color = '#346EBA',
            button_hover_color = '#3A5B87',
            values = ['Темная', 'Светлая'],
            variable = self.theme_var,
            command = option_themes)
        self.option_themes.place(x = 700, y = 100)
        if self.themeq == 'С':
            self.option_themes.set('Светлая')
        elif self.themeq == 'Т':
            self.option_themes.set('Темная')

        self.colors = customtkinter.CTkLabel(self,
            text = 'Цвет приложения:',
            font = ('Arial', 19))
        self.colors.place(x = 700, y = 100)

        self.color_var = customtkinter.StringVar()

        self.option_colors = customtkinter.CTkOptionMenu(self,
            width = 150, height = 30,
            font = ('Arial', 16), corner_radius = 0,
            fg_color = '#346EBA', button_color = '#346EBA',
            button_hover_color = '#3A5B87',
            values = ['Голубой', 'Красный', 'Зеленый', 'Оранжевый', 'Фиолетовый'],
            variable = self.color_var,
            command = option_colors)
        self.option_colors.place(x = 700, y = 100)
        self.option_colors.set(self.color)

        self.otk_var = customtkinter.StringVar()

        self.otk = customtkinter.CTkOptionMenu(self,
            width = 150, height = 30,
            font = ('Arial', 16),corner_radius = 0,
            fg_color = '#346EBA', button_color = '#346EBA',
            button_hover_color = '#3A5B87',
            values = ['Минутам', 'Секундам'],
            variable = self.otk_var,
            command = otk_value)
        self.otk.place(x = 700, y = 100)
        

        if self.otktext == 'М':
            self.otk.set('Минутам')
        else:
            self.otk.set('Секундам')

        self.otk_text = customtkinter.CTkLabel(self,
            text = 'Отсчет по:',
            font = ('Arial', 19))
        self.otk_text.place(x = 700, y = 100)

        #start turn off pc --- Button()
        self.str_b = customtkinter.CTkButton(self, 
            text = 'Запустить', width = 230, height = 75,
            font = ('Arial', 23), corner_radius = 0,
            fg_color = '#346EBA', hover_color = '#3A5B87',
            command = self.start_time)
        self.str_b.place(x = 15, y = 155)      

        #stop turn off pc --- Button()
        self.stop_b = customtkinter.CTkButton(self,
            text = 'Остановить', width = 230, height = 50,
            font = ('Arial', 23), corner_radius = 0,
            fg_color = '#346EBA', hover_color = '#3A5B87',
            command = self.stoped,
            state = 'disabled')
        self.stop_b.place(x = 15, y = 240)

        #hours --- Entry()
        valid = (self.register(validate), '%P')
        self.entry_hour = customtkinter.CTkEntry(self,
            width = 150, height = 40, corner_radius = 0, 
            justify = 'center', font = ('Arial', 23), 
            validate = 'key',
            validatecommand = valid)
        self.entry_hour.place(x = 55, y = 30)
        self.entry_hour.insert(0, '0')

        #hours --- Button()
        self.hour_minus_button = customtkinter.CTkButton(self,
            text = '-', font = ('Arial', 24), corner_radius = 0,  
            fg_color = '#346EBA', hover_color = '#3A5B87',                   
            width = 40, height = 40, command = hour_minus)
        self.hour_minus_button.place(x = 15, y = 30)

        self.hour_plus_button = customtkinter.CTkButton(self,
            text = '+', font = ('Arial', 24), corner_radius = 0,
            fg_color = '#346EBA', hover_color = '#3A5B87',                             
            width = 40, height = 40, command = hour_plus)
        self.hour_plus_button.place(x = 205, y = 30)

        #hours --- Label()
        self.hour_text = customtkinter.CTkLabel(self,
            text = 'Часы:', font = ('Arial', 20),
            fg_color = '#2E2E2E')
        self.hour_text.place(x = 104, y = 2)


        #minuts --- Entry()
        self.entry_minut = customtkinter.CTkEntry(self,
            width = 150, height = 40, corner_radius = 0, 
            justify = 'center',font = ('Arial', 23), 
            validate = 'key',
            validatecommand = valid)
        self.entry_minut.place(x = 55, y = 100)
        self.entry_minut.insert(0, '0')

        #minuts --- Button() 
        self.minut_minus_button = customtkinter.CTkButton(self,
            text = '-', font = ('Arial', 24), corner_radius = 0,
            fg_color = '#346EBA', hover_color = '#3A5B87',
            width = 40, height = 40, command = minut_minus)
        self.minut_minus_button.place(x = 15, y = 100)

        self.minut_plus_button = customtkinter.CTkButton(self,
            text = '+', font = ('Arial', 24), corner_radius = 0,
            fg_color = '#346EBA', hover_color = '#3A5B87',
            width = 40, height = 40, command = minut_plus)
        self.minut_plus_button.place(x = 205, y = 100)

        #minuts --- Label()
        self.minut_text = customtkinter.CTkLabel(self,
            text = 'Минуты:', font = ('Arial', 20),
            fg_color = '#2E2E2E')
        self.minut_text.place(x = 92, y = 72)


        #letter of the hour --- Label()
        self.hour_t = customtkinter.CTkLabel(self,
            text = 'H', font = ('Arial', 18))
        self.hour_t.place(x = 435, y = 119)

        #letter of the minut --- Label()
        self.minut_t = customtkinter.CTkLabel(self,
            text = 'M', font = ('Arial', 18))
        self.minut_t.place(x = 435, y = 254)

        #vision time out --- Label()
        self.time_out_m = customtkinter.CTkLabel(self,
            text = '00', font = ('Arial', 140, 'bold'))
        self.time_out_m.place(x = 279, y = 145)


        self.time_out_h = customtkinter.CTkLabel(self,
            text = '00', font = ('Arial', 140, 'bold'))
        self.time_out_h.place(x = 279, y = 10)

        #time will run ot in --- Label()
        self.time = customtkinter.CTkLabel(self,
            text = 'Время закончится через:',
            font = ('Arial', 15))
        self.time.place(x = 272, y = 0)


        #invisible Entry() to stoping time
        self.vis_entry = customtkinter.CTkEntry(self)
        self.vis_entry.place(x = 10, y = 650)

        #invisible Entry() to stoping time
        self.vis_entry_2 = customtkinter.CTkEntry(self)
        self.vis_entry_2.place(x = 10, y = 690)

        #designation hours
        self.vis_hour = customtkinter.CTkLabel(self, 
            text = 'hour', font = ('Arial', 14))
        self.vis_hour.place(x = 160, y = 650)

        #designation minuts
        self.vis_minut = customtkinter.CTkLabel(self,
            text = 'minut', font = ('Arial', 14))
        self.vis_minut.place(x = 160, y = 690)

        self.en_h = customtkinter.CTkEntry(self)
        self.en_h.place(x = 10, y = 630)

        self.en_m = customtkinter.CTkEntry(self)
        self.en_m.place(x = 10, y = 670)


# 3 блока кода для 

        if self.color == 'Голубой':
                # голубой: #346EBA  #3A5B87  #283F5E

            self.frame_6.configure(fg_color = '#283F5E')
            self.str_b.configure(fg_color = '#346EBA',    # цвет в целом
                                     hover_color = '#3A5B87') # цвет при наведении
                
            self.stop_b.configure(fg_color = '#346EBA',
                                     hover_color = '#3A5B87')
            self.hour_minus_button.configure(fg_color = '#346EBA',
                                     hover_color = '#3A5B87')
            self.hour_plus_button.configure(fg_color = '#346EBA',
                                     hover_color = '#3A5B87')
            self.minut_minus_button.configure(fg_color = '#346EBA',
                                     hover_color = '#3A5B87')
            self.minut_plus_button.configure(fg_color = '#346EBA',
                                     hover_color = '#3A5B87')
            self.setings_b.configure(fg_color = '#346EBA',
                                     hover_color = '#3A5B87')
            self.close.configure(fg_color = '#346EBA',
                                     hover_color = '#3A5B87')
            self.save.configure(fg_color = '#346EBA',
                                     hover_color = '#3A5B87')
            self.option_themes.configure(fg_color = '#346EBA', 
                    button_color = '#346EBA', button_hover_color = '#3A5B87')
            self.option_colors.configure(fg_color = '#346EBA', 
                    button_color = '#346EBA', button_hover_color = '#3A5B87')
            self.otk.configure(fg_color = '#346EBA', 
                    button_color = '#346EBA', button_hover_color = '#3A5B87')                

        elif self.color == 'Красный':
                # красный: #D65656  #B04C4C

            self.frame_6.configure(fg_color = '#723131')   
            self.str_b.configure(fg_color = '#D65656',    # цвет в целом
                                     hover_color = '#B04C4C') # цвет при наведении
                
            self.stop_b.configure(fg_color = '#D65656',
                                     hover_color = '#B04C4C')
            self.hour_minus_button.configure(fg_color = '#D65656',
                                     hover_color = '#B04C4C')
            self.hour_plus_button.configure(fg_color = '#D65656',
                                     hover_color = '#B04C4C')
            self.minut_minus_button.configure(fg_color = '#D65656',
                                     hover_color = '#B04C4C')
            self.minut_plus_button.configure(fg_color = '#D65656',
                                     hover_color = '#B04C4C')
            self.setings_b.configure(fg_color = '#D65656',
                                     hover_color = '#B04C4C')
            self.close.configure(fg_color = '#D65656',
                                     hover_color = '#B04C4C')
            self.save.configure(fg_color = '#D65656',
                                     hover_color = '#B04C4C')
            self.option_themes.configure(fg_color = '#D65656', 
                    button_color = '#D65656', button_hover_color = '#B04C4C')
            self.option_colors.configure(fg_color = '#D65656', 
                    button_color = '#D65656', button_hover_color = '#B04C4C')
            self.otk.configure(fg_color = '#D65656', 
                    button_color = '#D65656', button_hover_color = '#B04C4C')

        elif self.color == 'Зеленый':
                # зеленый: #41904B  #407347  #315A37

            self.frame_6.configure(fg_color = '#315A37')
            self.str_b.configure(fg_color = '#41904B',    # цвет в целом
                                     hover_color = '#407347') # цвет при наведении
                
            self.stop_b.configure(fg_color = '#41904B',
                                     hover_color = '#407347')
            self.hour_minus_button.configure(fg_color = '#41904B',
                                     hover_color = '#407347')
            self.hour_plus_button.configure(fg_color = '#41904B',
                                     hover_color = '#407347')
            self.minut_minus_button.configure(fg_color = '#41904B',
                                     hover_color = '#407347')
            self.minut_plus_button.configure(fg_color = '#41904B',
                                     hover_color = '#407347')
            self.setings_b.configure(fg_color = '#41904B',
                                     hover_color = '#407347')
            self.close.configure(fg_color = '#41904B',
                                     hover_color = '#407347')
            self.save.configure(fg_color = '#41904B',
                                     hover_color = '#407347')
            self.option_themes.configure(fg_color = '#41904B', 
                    button_color = '#41904B', button_hover_color = '#407347')
            self.option_colors.configure(fg_color = '#41904B', 
                    button_color = '#41904B', button_hover_color = '#407347')
            self.otk.configure(fg_color = '#41904B', 
                    button_color = '#41904B', button_hover_color = '#407347')
                

        elif self.color == 'Оранжевый':
                # оранжевый: #C4834D  #8F623C  #61432A

            self.frame_6.configure(fg_color = '#61432A')
            self.str_b.configure(fg_color = '#C4834D',    # цвет в целом
                                     hover_color = '#8F623C') # цвет при наведении
                
            self.stop_b.configure(fg_color = '#C4834D',
                                     hover_color = '#8F623C')
            self.hour_minus_button.configure(fg_color = '#C4834D',
                                     hover_color = '#8F623C')
            self.hour_plus_button.configure(fg_color = '#C4834D',
                                     hover_color = '#8F623C')
            self.minut_minus_button.configure(fg_color = '#C4834D',
                                     hover_color = '#8F623C')
            self.minut_plus_button.configure(fg_color = '#C4834D',
                                     hover_color = '#8F623C')
            self.setings_b.configure(fg_color = '#C4834D',
                                     hover_color = '#8F623C')
            self.close.configure(fg_color = '#C4834D',
                                     hover_color = '#8F623C')
            self.save.configure(fg_color = '#C4834D',
                                     hover_color = '#8F623C')
            self.option_themes.configure(fg_color = '#C4834D', 
                    button_color = '#C4834D', button_hover_color = '#8F623C')
            self.option_colors.configure(fg_color = '#C4834D', 
                    button_color = '#C4834D', button_hover_color = '#8F623C')
            self.otk.configure(fg_color = '#C4834D', 
                    button_color = '#C4834D', button_hover_color = '#8F623C')
                

        elif self.color == 'Фиолетовый':
                # фиолетовый: #9250DE  #5B3982  #462B64

            self.frame_6.configure(fg_color = '#462B64')
            self.str_b.configure(fg_color = '#9250DE',    # цвет в целом
                                     hover_color = '#5B3982') # цвет при наведении
                
                
            self.stop_b.configure(fg_color = '#9250DE',
                                     hover_color = '#5B3982')
            self.hour_minus_button.configure(fg_color = '#9250DE',
                                     hover_color = '#5B3982')
            self.hour_plus_button.configure(fg_color = '#9250DE',
                                     hover_color = '#5B3982')
            self.minut_minus_button.configure(fg_color = '#9250DE',
                                     hover_color = '#5B3982')
            self.minut_plus_button.configure(fg_color = '#9250DE',
                                     hover_color = '#5B3982')
            self.setings_b.configure(fg_color = '#9250DE',
                                     hover_color = '#5B3982')
            self.close.configure(fg_color = '#9250DE',
                                     hover_color = '#5B3982')
            self.save.configure(fg_color = '#9250DE',
                                     hover_color = '#5B3982')
            self.option_themes.configure(fg_color = '#9250DE', 
                    button_color = '#9250DE', button_hover_color = '#5B3982')
            self.option_colors.configure(fg_color = '#9250DE', 
                    button_color = '#9250DE', button_hover_color = '#5B3982')
            self.otk.configure(fg_color = '#9250DE', 
                    button_color = '#9250DE', button_hover_color = '#5B3982')
                

        if self.themeq == 'Т':
            customtkinter.set_appearance_mode('Dark')
            self.frame_1.configure(fg_color = '#2E2E2E')
            self.frame_2.configure(fg_color = '#2E2E2E')
            self.frame_3.configure(fg_color = '#2E2E2E')
            self.frame_4.configure(fg_color = '#2E2E2E')
            self.frame_5.configure(fg_color = '#2E2E2E')
            self.hour_text.configure(fg_color = '#2E2E2E')
            self.minut_text.configure(fg_color = '#2E2E2E')


        elif self.themeq == 'С':
            customtkinter.set_appearance_mode('Light')
            self.frame_1.configure(fg_color = '#D6D6D6')
            self.frame_2.configure(fg_color = '#D6D6D6')
            self.frame_3.configure(fg_color = '#D6D6D6')
            self.frame_4.configure(fg_color = '#D6D6D6')
            self.frame_5.configure(fg_color = '#D6D6D6')
            self.hour_text.configure(fg_color = '#D6D6D6')
            self.minut_text.configure(fg_color = '#D6D6D6')



        if self.otktext == 'М':
            self.hour_text.configure(text = 'Часы:')
            self.minut_text.configure(text = 'Минуты:')

            self.hour_t.configure(text = 'H')
            self.minut_t.configure(text = 'M')
        elif self.otktext == 'С':
            self.hour_text.configure(text = 'Минуты:')
            self.minut_text.configure(text = 'Секунды:')

            self.hour_t.configure(text = 'M')
            self.minut_t.configure(text = 'S')


        if self.otktext == 'М':
            self.hour_text.place(x = 104, y = 2)
            self.minut_text.place(x = 92, y = 72)
        else:
            self.hour_text.place(x = 92, y = 2)
            self.minut_text.place(x = 89, y = 72)
            
        print(self.otk_var)


        if self.otk_var.get()[0] == 'М':
            print('get')
            self.otkq = 60000
        elif self.otk_var.get()[0] == 'С':
            print('get sec')
            self.otkq = 1000


        self.hour = 0
        self.minut = 0
        self.star_time = False
        self.stop = 1

        

# Функция для оставноки времени.Содержится 4 почти одинаковых блока кода,
# каждый из которых нужен для воизбеждания багов и проблем в целом в работе
# Например, отключаются кнопки интерфейса, когда время идет, 
# тк при взаимодействии с ними могут время может остановиться, перетать идти и
# и подобные проблемы. чтобы время продолжало идти после оставноки, использовалась
# функция number(), которая просто ведет счет времени на экране
  
    def stoped(self):
        if self.otk_var.get() == 'Минутам':
            self.otkq = 60000
        elif self.otk_var.get() == 'Секундам':
            self.otkq = 1000
        print('otk:', self.otktext)
        print('pered:', self.color)
        print('pered:', self.themeq)
        tm.sleep(0.2)
        if self.stop % 2 == 1:
            self.stop += 1
            self.stop_b.configure(text = 'Возобновить')
            self.star_time = False

            self.entry_hour.configure(state = 'normal')
            self.entry_minut.configure(state = 'normal')
            self.hour_minus_button.configure(state = 'normal')
            self.hour_plus_button.configure(state = 'normal')
            self.minut_minus_button.configure(state = 'normal')
            self.minut_plus_button.configure(state = 'normal')
            self.setings_b.configure(state = 'normal')

            h = int(self.en_h.get())
            m = int(self.en_m.get())

            entry_h = int(self.entry_hour.get())
            entry_m = int(self.entry_minut.get())


            if int(self.entry_hour.get()) != h or int(self.entry_minut.get()) != m:
                
                self.h = int(self.entry_hour.get()) * 60
                self.m = int(self.entry_minut.get())
                self.time_sum = self.h + self.m

                self.en_h.delete(0, 25)
                self.en_m.delete(0, 25)
                self.en_h.insert(0, entry_h)
                self.en_m.insert(0, entry_m)
                
                if self.star_time:
                    if 0 < self.time_sum < 6001:
                        self.time_sum -= 1
                        self.hour = str(self.time_sum // 60)
                        self.minut = str(self.time_sum % 60)

                        self.vis_entry.delete(0, 25)
                        self.vis_entry_2.delete(0, 25)
                        self.vis_entry.insert(0, self.hour)
                        self.vis_entry_2.insert(0, self.minut)

                        if len(self.hour) == 1 and len(self.minut) == 1:
                            self.time_out_h.configure(text = f'0{self.hour}')
                            self.time_out_m.configure(text = f'0{self.minut}')
                        elif len(self.hour) == 1 and len(self.minut) != 1:
                            self.time_out_h.configure(text = f'0{self.hour}')
                            self.time_out_m.configure(text = self.minut)
                        elif len(self.hour) != 1 and len(self.minut) == 1:
                            self.time_out_h.configure(text = self.hour)
                            self.time_out_m.configure(text = f'0{self.minut}')
                        else:
                            self.time_out_h.configure(text = self.hour)
                            self.time_out_m.configure(text = self.minut)
                        self.after(self.otkq, self.number)
                
                    elif self.time_sum >= 6001:
                        self.entry_hour.delete(0, 25)
                        self.entry_minut.delete(0 ,25)
                        print('deleted')
                    
            elif int(self.entry_hour.get()) == h or int(self.entry_minut.get()) == m:

                self.en_h.delete(0, 25)
                self.en_m.delete(0, 25)
                self.en_h.insert(0, entry_h)
                self.en_m.insert(0, entry_m)

                if self.star_time:
                    if 0 < self.time_sum < 6001:
                        self.time_sum -= 1
                        self.hour = str(self.time_sum // 60)
                        self.minut = str(self.time_sum % 60)

                        self.vis_entry.delete(0, 25)
                        self.vis_entry_2.delete(0, 25)
                        self.vis_entry.insert(0, self.hour)
                        self.vis_entry_2.insert(0, self.minut)

                        if len(self.hour) == 1 and len(self.minut) == 1:
                            self.time_out_h.configure(text = f'0{self.hour}')
                            self.time_out_m.configure(text = f'0{self.minut}')
                        elif len(self.hour) == 1 and len(self.minut) != 1:
                            self.time_out_h.configure(text = f'0{self.hour}')
                            self.time_out_m.configure(text = self.minut)
                        elif len(self.hour) != 1 and len(self.minut) == 1:
                            self.time_out_h.configure(text = self.hour)
                            self.time_out_m.configure(text = f'0{self.minut}')
                        else:
                            self.time_out_h.configure(text = self.hour)
                            self.time_out_m.configure(text = self.minut)
                        self.after(self.otkq, self.number)

                    elif self.time_sum >= 6001:
                        self.entry_hour.delete(0, 25)
                        self.entry_minut.delete(0 ,25)
                        print('deleted')

        elif self.stop % 2 == 0:
            self.stop -= 1
            self.stop_b.configure(text = 'Остановить')
            self.star_time = True

            self.entry_hour.configure(state = 'disabled')
            self.entry_minut.configure(state = 'disabled')
            self.hour_minus_button.configure(state = 'disabled')
            self.hour_plus_button.configure(state = 'disabled')
            self.minut_minus_button.configure(state = 'disabled')
            self.minut_plus_button.configure(state = 'disabled')
            self.setings_b.configure(state = 'disabled')

            h = int(self.en_h.get())
            m = int(self.en_m.get())

            entry_h = int(self.entry_hour.get())
            entry_m = int(self.entry_minut.get())


            if int(self.entry_hour.get()) != h or int(self.entry_minut.get()) != m:

                self.h = int(self.entry_hour.get()) * 60
                self.m = int(self.entry_minut.get())
                self.time_sum = self.h + self.m

                self.en_h.delete(0, 25)
                self.en_m.delete(0, 25)
                self.en_h.insert(0, entry_h)
                self.en_m.insert(0, entry_m)

                if self.star_time:
                    if 0 < self.time_sum < 6001:
                        self.time_sum -= 1
                        self.hour = str(self.time_sum // 60)
                        self.minut = str(self.time_sum % 60)

                        self.vis_entry.delete(0, 25)
                        self.vis_entry_2.delete(0, 25)
                        self.vis_entry.insert(0, self.hour)
                        self.vis_entry_2.insert(0, self.minut)

                        if len(self.hour) == 1 and len(self.minut) == 1:
                            self.time_out_h.configure(text = f'0{self.hour}')
                            self.time_out_m.configure(text = f'0{self.minut}')
                        elif len(self.hour) == 1 and len(self.minut) != 1:
                            self.time_out_h.configure(text = f'0{self.hour}')
                            self.time_out_m.configure(text = self.minut)
                        elif len(self.hour) != 1 and len(self.minut) == 1:
                            self.time_out_h.configure(text = self.hour)
                            self.time_out_m.configure(text = f'0{self.minut}')
                        else:
                            self.time_out_h.configure(text = self.hour)
                            self.time_out_m.configure(text = self.minut)
                        self.after(self.otkq, self.number)
                    
                    elif self.time_sum >= 6001:
                        self.entry_hour.delete(0, 25)
                        self.entry_minut.delete(0 ,25)
                        print('deleted')

            elif int(self.entry_hour.get()) == h or int(self.entry_minut.get()) == m:

                self.en_h.delete(0, 25)
                self.en_m.delete(0, 25)
                self.en_h.insert(0, entry_h)
                self.en_m.insert(0, entry_m)

                if self.star_time:
                    if 0 < self.time_sum < 6001:
                        self.time_sum -= 1
                        self.hour = str(self.time_sum // 60)
                        self.minut = str(self.time_sum % 60)

                        self.vis_entry.delete(0, 25)
                        self.vis_entry_2.delete(0, 25)
                        self.vis_entry.insert(0, self.hour)
                        self.vis_entry_2.insert(0, self.minut)

                        if len(self.hour) == 1 and len(self.minut) == 1:
                            self.time_out_h.configure(text = f'0{self.hour}')
                            self.time_out_m.configure(text = f'0{self.minut}')
                        elif len(self.hour) == 1 and len(self.minut) != 1:
                            self.time_out_h.configure(text = f'0{self.hour}')
                            self.time_out_m.configure(text = self.minut)
                        elif len(self.hour) != 1 and len(self.minut) == 1:
                            self.time_out_h.configure(text = self.hour)
                            self.time_out_m.configure(text = f'0{self.minut}')
                        else:
                            self.time_out_h.configure(text = self.hour)
                            self.time_out_m.configure(text = self.minut)
                        self.after(self.otkq, self.number)
    
                    elif self.time_sum >= 6001:
                        self.entry_hour.delete(0, 25)
                        self.entry_minut.delete(0 ,25)
                        print('deleted')

# Функция служит для передачи времени из полей ввода Часов и Минут, также 
# требуется для отключений виджетов интерфейса для воизбежания багов
# Функция принимает на вход часы и минуты, переводит в минуты и дальше 
# используется для подсчета времени до окончания работы программы




    def start_time(self):
        text = self.entry_hour.get() + self.entry_minut.get()
        if not self.star_time:
            


            self.str_b.configure(state = 'disabled')
            self.stop_b.configure(state = 'normal')

            self.entry_hour.configure(state = 'disabled')
            self.entry_minut.configure(state = 'disabled')
            self.hour_minus_button.configure(state = 'disabled')
            self.hour_plus_button.configure(state = 'disabled')
            self.minut_minus_button.configure(state = 'disabled')
            self.minut_plus_button.configure(state = 'disabled')
            self.setings_b.configure(state = 'disabled')

            self.en_h.delete(0, 25)
            self.en_m.delete(0, 25)
            self.en_h.insert(0, self.entry_hour.get())
            self.en_m.insert(0, self.entry_minut.get())

            try:
                time_hour = int(self.entry_hour.get()) * 60
                print('try hour', time_hour)
                time_minut = int(self.entry_minut.get()) 
                self.time_sums = time_minut + time_hour
                if self.time_sums > 0:
                    self.time_sum = self.time_sums
                    self.star_time = True
                    self.number()
            except ValueError:
                print('error')
        else:
            print(f't:  {self.star_time}')

# принимает сумму часов и минут в минутах, отображает на экране
# далее отправляет отдельными окнами уведомления об окончании времени
# и завершает работу компьютера

    def number(self):
            if self.star_time:
                if 0 < self.time_sum < 6001:
                    print(self.time_sum)
                    self.time_sum -= 1
                    self.hour = str(self.time_sum // 60)
                    self.minut = str(self.time_sum % 60)

                    self.vis_entry.delete(0, 25)
                    self.vis_entry_2.delete(0, 25)
                    self.vis_entry.insert(0, self.hour)
                    self.vis_entry_2.insert(0, self.minut)

                    if len(self.hour) == 1 and len(self.minut) == 1:
                        self.time_out_h.configure(text = f'0{self.hour}')
                        self.time_out_m.configure(text = f'0{self.minut}')
                    elif len(self.hour) == 1 and len(self.minut) != 1:
                        self.time_out_h.configure(text = f'0{self.hour}')
                        self.time_out_m.configure(text = self.minut)
                    elif len(self.hour) != 1 and len(self.minut) == 1:
                        self.time_out_h.configure(text = self.hour)
                        self.time_out_m.configure(text = f'0{self.minut}')
                    else:
                        self.time_out_h.configure(text = self.hour)
                        self.time_out_m.configure(text = self.minut)
                    self.after(self.otkq, self.number)
            
                elif self.time_sum > 6000:
                    print('deleted')

                else:
                    self.star_time = False
                    if sys.platform == 'win32':
                        command = 'shutdown /s /t 0'
                    try:
                        os.system(command)
                    except Exception as e:
                        print(f'Error: {e}')

                if self.otk_var.get() == 'Минутам':
                    if self.time_sum == 30:
                        msbox.showinfo('Оповещение', 'Осталось 30 минут!')

                    elif self.time_sum == 10:
                        msbox.showinfo('Оповещение', 'Осталось 10 минут!')
                        
                    elif self.time_sum == 5:
                        msbox.showinfo('Оповещение', 'Осталось 5 минут!')

                    elif self.time_sum == 1:
                        msbox.showinfo('Оповещение', 'Осталось 1 минута!')

                elif self.otk_var.get() == 'Секундам':
                    if self.time_sum == 30:
                        msbox.showinfo('Оповещение', 'Осталось 30 секунд!')

                    elif self.time_sum == 10:
                        msbox.showinfo('Оповещение', 'Осталось 10 секунд!')
                        
                    elif self.time_sum == 5:
                        msbox.showinfo('Оповещение', 'Осталось 5 секунд!')

app = App()
app.mainloop()

