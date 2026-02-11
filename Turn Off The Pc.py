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
        self.geometry(f'511x360+{width}+{height}') #320x240 #511x305
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
                f.write('600LТМОfГолубой')



        file = open('config.txt', 'r', encoding = 'utf-8')
        text = file.read()

        L_index = int(text.index('L'))

        self.f_theme = text[L_index + 1]
        self.f_otk = text[L_index + 2]
        self.f_act = text[L_index + 3]
        self.f_cpu = text[L_index + 4]

        self.f_time = text[0:L_index]

        self.color = text[L_index + 5:]
        file.close()
        print(self.f_theme)
        print(self.f_otk)
        print(self.f_act)
        print(self.f_cpu)
        print(self.f_time)
        print(self.color)

        self.otkq = 60000

        def quit(event):
            self.destroy()
        self.bind('<Alt_L>', quit)



        def delay():
            
            if self.otk_var.get()[0] == 'М':
                if self.time_sum < 5993:

                    self.time_sum += 5
                    hour = str(self.time_sum // 60)
                    minut = str(self.time_sum % 60)


                    if len(hour) == 1 and len(minut) == 1:
                        self.time_out_h.configure(text = f'0{hour}')
                        self.time_out_m.configure(text = f'0{minut}')
                    elif len(hour) == 1 and len(minut) != 1:
                        self.time_out_h.configure(text = f'0{hour}')
                        self.time_out_m.configure(text = minut)
                    elif len(hour) != 1 and len(minut) == 1:
                        self.time_out_h.configure(text = hour)
                        self.time_out_m.configure(text = f'0{minut}')
                    else:
                        self.time_out_h.configure(text = hour)
                        self.time_out_m.configure(text = minut)


                    plus_minut = int(self.entry_minut.get()) + 6

                    if int(self.entry_minut.get()) < 55:

                        self.entry_minut.delete(0, 25)
                        self.entry_minut.insert(0, plus_minut - 1)

                        self.en_m.delete(0, 25)
                        self.en_m.insert(0, plus_minut - 1)
                        tm.sleep(0.2)
                    
                    elif int(self.entry_minut.get()) > 55:
                        
                        delay_h = int(self.entry_hour.get()) + 1
                        delay_m = 60 - int(self.entry_minut.get()) 

                        if len(str(delay_h)) == 1:
                            self.entry_hour.delete(0, 25)
                            self.entry_hour.insert(0, delay_h)
                            self.entry_minut.delete(0, 25)
                            self.entry_minut.insert(0, delay_m)
                        elif len(str(delay_h)) != 1:
                            self.entry_hour.delete(0, 25)
                            self.entry_hour.insert(0, delay_h)
                            self.entry_minut.deelte(0, 25)
                            self.entry_minut.insert(0, delay_m)

                    elif int(self.entry_minut.get()) == 55:

                        delay_h = int(self.entry_hour.get())
                        self.entry_hour.delete(0, 25)
                        self.entry_hour.insert(0, delay_h + 1)
                        self.entry_minut.delete(0, 25)
                        self.entry_minut.insert(0, '0')




            elif self.otk_var.get()[0] == 'С':
                if self.time_sum < 5699:
                    
                    self.time_sum += 300
                    plus_second = int(self.entry_hour.get()) + 5
                    self.entry_hour.delete(0, 25)
                    self.entry_hour.insert(0, plus_second)

                    self.en_h.delete(0, 25)
                    self.en_h.insert(0, plus_second)
                    tm.sleep(0.2)

        def clear():
            self.entry_hour.delete(0, 25)
            self.entry_minut.delete(0 ,25)
            self.entry_hour.insert(0, 0)
            self.entry_minut.insert(0, 0)
            self.time_out_h.configure(text = '00')
            self.time_out_m.configure(text = '00')

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
            self.clear.place(x = 600, y = 600)
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

            self.act.place(x = 260, y = 130)
            self.label_act.place(x = 40, y = 130)
            self.check_cpu.place(x = 385, y = 170)

            self.delay.place(x = 700, y = 100)
            self.check_entry.place(x = 310, y = 210)

            self.check_cpu_label.place(x = 40, y = 170)
            self.entry_count_label.place(x = 40, y = 210)

            self.frame_3.place(x = 700, y = 600)
            self.frame_4.place(x = 0, y = 0)
            self.frame_5.place(x = 426, y = 0)            
            self.frame_6.place(x = 455, y = 0)
            self.under_delay.place(x = 700, y = 100)
            

        def close():
            self.clear.place(x = 15, y = 300)
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
            self.act.place(x = 700, y = 100)
            self.label_act.place(x = 700, y = 100)
            self.delay.place(x = 265, y = 300)
            self.under_delay.place(x = 250, y = 290)
            self.check_cpu.place(x = 700, y = 100)

            self.check_entry.place(x = 700, y = 100)

            self.check_cpu_label.place(x = 700, y = 100)
            self.entry_count_label.place(x = 700, y = 100)

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
                self.under_delay.configure(fg_color = '#2E2E2E')


            elif value == 'Светлая':
                customtkinter.set_appearance_mode('Light')
                self.frame_1.configure(fg_color = '#D6D6D6')
                self.frame_2.configure(fg_color = '#D6D6D6')
                self.frame_3.configure(fg_color = '#D6D6D6')
                self.frame_4.configure(fg_color = '#D6D6D6')
                self.frame_5.configure(fg_color = '#D6D6D6')
                self.hour_text.configure(fg_color = '#D6D6D6')
                self.minut_text.configure(fg_color = '#D6D6D6')
                self.under_delay.configure(fg_color = '#D6D6D6')


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

                self.check_cpu.configure(fg_color = '#346EBA', 
                                     hover_color = '#3A5B87')
                self.delay.configure(fg_color = '#346EBA',
                                     hover_color = '#3A5B87')
                self.clear.configure(fg_color = '#346EBA',
                                     hover_color = '#3A5B87')
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
                self.act.configure(fg_color = '#346EBA', 
                    button_color = '#346EBA', button_hover_color = '#3A5B87')
                
            elif value == 'Красный':
                # красный: #D65656  #B04C4C  #723131

                self.check_cpu.configure(fg_color = '#D65656',
                                     hover_color = '#B04C4C')
                self.delay.configure(fg_color = '#D65656',
                                     hover_color = '#B04C4C')
                self.clear.configure(fg_color = '#D65656',
                                     hover_color = '#B04C4C')
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
                self.act.configure(fg_color = '#D65656', 
                    button_color = '#D65656', button_hover_color = '#B04C4C')

            elif value == 'Зеленый':
                # зеленый: #41904B  #407347  #315A37

                self.check_cpu.configure(fg_color = '#41904B',
                                     hover_color = '#407347')
                self.delay.configure(fg_color = '#41904B',
                                     hover_color = '#407347')
                self.clear.configure(fg_color = '#41904B',
                                     hover_color = '#407347')
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
                self.act.configure(fg_color = '#41904B', 
                    button_color = '#41904B', button_hover_color = '#407347')

            elif value == 'Оранжевый':
                # оранжевый: #C4834D  #8F623C  #61432A

                self.check_cpu.configure(fg_color = '#C4834D',
                                     hover_color = '#8F623C')
                self.delay.configure(fg_color = '#C4834D',
                                     hover_color = '#8F623C')
                self.clear.configure(fg_color = '#C4834D',
                                     hover_color = '#8F623C')
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
                self.act.configure(fg_color = '#C4834D', 
                    button_color = '#C4834D', button_hover_color = '#8F623C')

            elif value == 'Фиолетовый':
                # фиолетовый: #9250DE  #5B3982  #462B64

                self.check_cpu.configure(fg_color = '#9250DE',
                                     hover_color = '#5B3982')
                self.delay.configure(fg_color = '#9250DE',
                                     hover_color = '#5B3982')
                self.clear.configure(fg_color = '#9250DE',
                                     hover_color = '#5B3982')
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
                self.act.configure(fg_color = '#9250DE', 
                    button_color = '#9250DE', button_hover_color = '#5B3982')


        def otk_value(value):
            print('Выбран режим:', value)

            if value == 'Минутам':
                self.hour_text.configure(text = 'Часы:')
                self.minut_text.configure(text = 'Минуты:')

                self.hour_t.configure(text = 'H')
                self.minut_t.configure(text = 'M')
                self.otkq = 60000
            elif value == 'Секундам':
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
            
# Тема + Режим отсчета + Действие + Цвет            

            theme = self.theme_var.get()[0]
            otk = self.otk_var.get()[0]
            act = self.choise_act.get()[0]
            cpu = self.check_var.get()[-1]
            time = self.check_entry.get()
            color = self.color_var.get()
            

            print('theme:', theme)  # Работает
            print('otk:', otk)  # Работает
            print('act:', act)  # 
            print('cpu:', cpu)  #
            print('time the load:', time) #
            print('color:', color)  # Работает
            

            content = time + 'L' + str(theme) + str(otk) + str(act) + str(cpu) + str(color)

            filepath('config.txt', content)

        def act(value):
            if value == 'Гибернация':
                self.command = 'shutdown /h'
            elif value == 'Выключение':
                self.command = 'shutdown /s /t 0'
            elif value == 'Перезагрузка':
                self.command = 'shutdown /r /t 0'


        settings_image = Image.open(resource_path('settings.png'))
        settings_photo = ImageTk.PhotoImage(settings_image)

        close_image = Image.open(resource_path('close.png'))
        close_photo = ImageTk.PhotoImage(close_image)

        save_image = Image.open(resource_path('save.png'))
        save_photo = ImageTk.PhotoImage(save_image)

  
# напиши свитч с функцией автовыключения пк исходя из нагрузки пк на цп




        self.check_var = customtkinter.StringVar(value = 'off')
        self.check_cpu = customtkinter.CTkCheckBox(self,
            corner_radius = 0, text = '',
            onvalue = 'on', offvalue = 'off',
            variable = self.check_var, 
            command = self.check_values)
        self.check_cpu.place(x = 700, y = 100)


        self.check_cpu_label = customtkinter.CTkLabel(self,
            text = 'Авто-гибернация:',
            font = ('Arial', 19))
        self.check_cpu_label.place(x = 700, y = 100)

        self.entry_count_label = customtkinter.CTkLabel(self,
            text = 'Секунд до авто-гибернации:',
            font = ('Arial', 19))
        self.check_cpu_label.place(x = 700, y = 100)


        self.label_act = customtkinter.CTkLabel(self,
            text = 'Действие:', 
            font = ('Arial', 19))
        self.label_act.place(x = 700, y = 100)

        self.choise_act = customtkinter.StringVar()

        self.act = customtkinter.CTkOptionMenu(self,
            width = 150, height = 30,
            font = ('Arial', 16), corner_radius = 0,
            fg_color = '#346EBA', button_color = '#346EBA',
            button_hover_color = '#3A5B87',
            values = ['Гибернация', 'Отключение', 'Перезагрузка'],
            variable = self.choise_act,
            command = act)
        self.act.place(x = 700, y = 100)

        if self.f_act == 'Г':
            self.act.set('Гибернация')
        elif self.f_act == 'О':
            self.act.set('Отключение')
        elif self.f_act == 'П':
            self.act.set('Перезагрузка')

        

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
            width = 30, height = 370,
            fg_color = '#2E2E2E', corner_radius = 0)
        self.frame_4.place(x = 700, y = 600)

        self.frame_5 = customtkinter.CTkFrame(self,
            width = 30, height = 370,
            fg_color = '#2E2E2E', corner_radius = 0)
        self.frame_5.place(x = 700, y = 600)

        self.frame_6 = customtkinter.CTkFrame(self,
            width = 58, height = 370,
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
        if self.f_theme == 'С':
            self.option_themes.set('Светлая')
        elif self.f_theme == 'Т':
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
            button_hover_color = '#3A5B87', state = 'normal',
            values = ['Минутам', 'Секундам'],
            variable = self.otk_var,
            command = otk_value)
        self.otk.place(x = 700, y = 100)
        

        if self.f_otk == 'М':
            self.otk.set('Минутам')
        else:
            self.otk.set('Секундам')

        self.otk_text = customtkinter.CTkLabel(self,
            text = 'Отсчет по:',
            font = ('Arial', 19))
        self.otk_text.place(x = 700, y = 100)

        #vision time out --- Label()
        self.time_out_m = customtkinter.CTkLabel(self,
            text = '00', font = ('Arial', 140, 'bold'))
        self.time_out_m.place(x = 279, y = 145)

        self.time_out_h = customtkinter.CTkLabel(self,
            text = '00', font = ('Arial', 140, 'bold'))
        self.time_out_h.place(x = 279, y = 10)

        self.under_delay = customtkinter.CTkFrame(self,
            width = 210, height = 85,
            fg_color = '#2E2E2E', corner_radius = 0)
        self.under_delay.place(x = 250, y = 290)

        self.delay = customtkinter.CTkButton(self,
            text = 'Отложить время', width = 185, height = 50,
            font = ('Arial', 19), corner_radius = 0,
            fg_color = '#346EBA', hover_color = '#3A5B87',
            command = delay,
            state = 'disabled')
        self.delay.place(x = 265, y = 300)

        self.clear = customtkinter.CTkButton(self,
            text = 'Очистить', width = 230, height = 50,
            font = ('Arial', 23), corner_radius = 0,
            fg_color = '#346EBA', hover_color = '#3A5B87',
            command = clear,
            state = 'disabled')
        self.clear.place(x = 15, y = 300)

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


        self.check_entry = customtkinter.CTkEntry(self,
            corner_radius = 0, justify = 'right',
            width = 100, font = ('Arial', 23),
            validate = 'key',
            validatecommand = valid)
        self.check_entry.place(x = 700, y = 100)
        self.check_entry.insert(0, self.f_time)



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

        #time will run ot in --- Label()
        self.time = customtkinter.CTkLabel(self,
            text = 'Время закончится через:',
            font = ('Arial', 15))
        self.time.place(x = 272, y = 0)


        #invisible Entry() to stoping time
        self.vis_entry = customtkinter.CTkEntry(self, width = 50)
        self.vis_entry.place(x = 10, y = 450)

        #invisible Entry() to stoping time
        self.vis_entry_2 = customtkinter.CTkEntry(self, width = 50)
        self.vis_entry_2.place(x = 10, y = 485)

        #designation hours
        self.vis_hour = customtkinter.CTkLabel(self, 
            text = 'vis hour', font = ('Arial', 14))
        self.vis_hour.place(x = 65, y = 450)

        #designation minuts
        self.vis_minut = customtkinter.CTkLabel(self,
            text = 'vis minut', font = ('Arial', 14))
        self.vis_minut.place(x = 65, y = 485)


        self.en_h = customtkinter.CTkEntry(self, width = 50)
        self.en_h.place(x = 150, y = 450)

        self.en_m = customtkinter.CTkEntry(self, width = 50)
        self.en_m.place(x = 150, y = 485)

        self.vis_hour = customtkinter.CTkLabel(self, 
            text = 'en h', font = ('Arial', 14))
        self.vis_hour.place(x = 205, y = 450)

        #designation minuts
        self.vis_minut = customtkinter.CTkLabel(self,
            text = 'en m', font = ('Arial', 14))
        self.vis_minut.place(x = 205, y = 485)


        if self.color == 'Голубой':
                # голубой: #346EBA  #3A5B87  #283F5E
            self.check_cpu.configure(fg_color = '#346EBA', 
                                     hover_color = '#3A5B87')
            self.delay.configure(fg_color = '#346EBA',
                                     hover_color = '#3A5B87')
            self.clear.configure(fg_color = '#346EBA',
                                     hover_color = '#3A5B87')
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
            self.act.configure(fg_color = '#346EBA', 
                    button_color = '#346EBA', button_hover_color = '#3A5B87')            

        elif self.color == 'Красный':
                # красный: #D65656  #B04C4C

            self.check_cpu.configure(fg_color = '#D65656',
                                     hover_color = '#B04C4C')
            self.delay.configure(fg_color = '#D65656',
                                     hover_color = '#B04C4C')
            self.clear.configure(fg_color = '#D65656',
                                     hover_color = '#B04C4C')
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
            self.act.configure(fg_color = '#D65656', 
                    button_color = '#D65656', button_hover_color = '#B04C4C')

        elif self.color == 'Зеленый':
                # зеленый: #41904B  #407347  #315A37

            self.check_cpu.configure(fg_color = '#41904B',
                                     hover_color = '#407347')
            self.delay.configure(fg_color = '#41904B',
                                     hover_color = '#407347')
            self.clear.configure(fg_color = '#41904B',
                                     hover_color = '#407347')
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
            self.act.configure(fg_color = '#41904B', 
                    button_color = '#41904B', button_hover_color = '#407347')
                

        elif self.color == 'Оранжевый':
                # оранжевый: #C4834D  #8F623C  #61432A

            self.check_cpu.configure(fg_color = '#C4834D',
                                     hover_color = '#8F623C')
            self.delay.configure(fg_color = '#C4834D',
                                     hover_color = '#8F623C')
            self.clear.configure(fg_color = '#C4834D',
                                     hover_color = '#8F623C')
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
            self.act.configure(fg_color = '#C4834D', 
                    button_color = '#C4834D', button_hover_color = '#8F623C')
                

        elif self.color == 'Фиолетовый':
                # фиолетовый: #9250DE  #5B3982  #462B64

            self.check_cpu.configure(fg_color = '#9250DE',
                                     hover_color = '#5B3982')
            self.delay.configure(fg_color = '#9250DE',
                                     hover_color = '#5B3982')
            self.clear.configure(fg_color = '#9250DE',
                                     hover_color = '#5B3982')
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
            self.act.configure(fg_color = '#9250DE', 
                    button_color = '#9250DE', button_hover_color = '#5B3982')
                

        if self.f_theme == 'Т':
            customtkinter.set_appearance_mode('Dark')
            self.frame_1.configure(fg_color = '#2E2E2E')
            self.frame_2.configure(fg_color = '#2E2E2E')
            self.frame_3.configure(fg_color = '#2E2E2E')
            self.frame_4.configure(fg_color = '#2E2E2E')
            self.frame_5.configure(fg_color = '#2E2E2E')
            self.hour_text.configure(fg_color = '#2E2E2E')
            self.minut_text.configure(fg_color = '#2E2E2E')
            self.under_delay.configure(fg_color = '#2E2E2E')


        elif self.f_theme == 'С':
            customtkinter.set_appearance_mode('Light')
            self.frame_1.configure(fg_color = '#D6D6D6')
            self.frame_2.configure(fg_color = '#D6D6D6')
            self.frame_3.configure(fg_color = '#D6D6D6')
            self.frame_4.configure(fg_color = '#D6D6D6')
            self.frame_5.configure(fg_color = '#D6D6D6')
            self.hour_text.configure(fg_color = '#D6D6D6')
            self.minut_text.configure(fg_color = '#D6D6D6')
            self.under_delay.configure(fg_color = '#D6D6D6')


        if self.f_otk == 'М':
            self.hour_text.configure(text = 'Часы:')
            self.minut_text.configure(text = 'Минуты:')

            self.hour_t.configure(text = 'H')
            self.minut_t.configure(text = 'M')

            self.hour_text.place(x = 104, y = 2)
            self.minut_text.place(x = 92, y = 72)
        elif self.f_otk == 'С':
            self.hour_text.configure(text = 'Минуты:')
            self.minut_text.configure(text = 'Секунды:')

            self.hour_t.configure(text = 'M')
            self.minut_t.configure(text = 'S')

            self.hour_text.place(x = 92, y = 2)
            self.minut_text.place(x = 89, y = 72)


        if self.otk_var.get()[0] == 'М':
            self.otkq = 60000
        elif self.otk_var.get()[0] == 'С':
            self.otkq = 1000


        if self.choise_act.get()[0] == 'Г':
            self.command = 'shutdown /h'
        elif self.choise_act.get()[0] == 'О':
            self.command = 'shutdown /s /t 0'
        elif self.choise_act.get()[0] == 'П':
            self.command = 'shutdown /r /t 0'

        
        if self.f_cpu == 'n':
            self.check_var.set('on')
            self.check_values()
        elif self.f_cpu == 'f':
            self.check_var.set('off')


        self.hour = 0
        self.minut = 0
        self.star_time = False
        self.stop = 1

        self.stop_time_count = 0


    def start_monitoring(self):
        try:
            time_value = int(self.check_entry.get())
            if time_value < 60:
                msbox.showwarning('Предупреждение', 'Минимальное время - 60 секунд')
                self.check_var.set('off')
                return
        except ValueError:
            msbox.showwarning('Ошибка', 'Введите число')
            self.check_var.set('off')
            return

        self.check_entry.configure(state = 'disabled')
        if self.check_var.get() == 'on':
            self.monitor_cpu = True
            self.count_time = int(self.check_entry.get())
            self.time_now = 0
            self.cpu_check_start()

        else:
            self.stop_monitoring()

    def stop_monitoring(self):
        self.check_entry.configure(state = 'normal')
        self.minitor_cpu = False
        self.after_cancel(self.cpu_act)
        self.cpu_act = None

    def cpu_check_start(self):
        cpu_load = psutil.cpu_percent()
        if cpu_load < 13:
            self.time_now += 1
            print(f'Cpu load: {cpu_load}% | {self.time_now} seconds left')


            if self.time_now == self.count_time:
                self.monitor_cpu = False
                self.cpu_act = None
                self.time_now = 0
                self.shutdown()

        else:
            if self.time_now > 0:
                self.time_now = 0

        self.cpu_act = self.after(1000, self.cpu_check_start)

    def shutdown(self):
        print('Гибернация')
        os.system('shutdown /h')

    def check_values(self):
        if self.check_var.get() == 'on':
            print(f'Turn {self.check_var.get()} the processor load check')
        else:
            print(f'Disabling {self.check_var.get()} the processor load check')

        if self.check_var.get() == 'on':
            self.start_monitoring()
        else:
                self.stop_monitoring()





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


        if self.stop % 2 == 1:
            self.stop += 1
            self.star_time = False

            self.stop_b.configure(text = 'Возобновить')
            self.check_cpu.configure(state = 'normal')
            self.clear.configure(state = 'normal')
            self.otk.configure(state = 'normal')
            self.entry_hour.configure(state = 'normal')
            self.entry_minut.configure(state = 'normal')
            self.hour_minus_button.configure(state = 'normal')
            self.hour_plus_button.configure(state = 'normal')
            self.minut_minus_button.configure(state = 'normal')
            self.minut_plus_button.configure(state = 'normal')

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
                        self.star_time = False
                        self.entry_hour.delete(0, 25)
                        self.entry_minut.delete(0 ,25)
                        self.entry_hour.insert(0, 0)
                        self.entry_minut.insert(0, 0)
                        self.time_out_h.configure(text = '00')
                        self.time_out_m.configure(text = '00')
                        print('1) The input field "entry_hour" and "entry_minut" is cleared')



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
                        if self.time_sum == 60:
                            msbox.showinfo('Оповещение', 'Осталась 1 минута!')

                        elif self.time_sum == 30:
                            msbox.showinfo('Оповещение', 'Осталось 30 секунд!')

                        elif self.time_sum == 10:
                            msbox.showinfo('Оповещение', 'Осталось 10 секунд!')
                            
                        elif self.time_sum == 5:
                            msbox.showinfo('Оповещение', 'Осталось 5 секунд!')


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
                        self.star_time = False
                        self.entry_hour.delete(0, 25)
                        self.entry_minut.delete(0 ,25)
                        self.entry_hour.insert(0, 0)
                        self.entry_minut.insert(0, 0)
                        self.time_out_h.configure(text = '00')
                        self.time_out_m.configure(text = '00')
                        print('2) The input field "entry_hour" and "entry_minut" is cleared')

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
                        if self.time_sum == 60:
                            msbox.showinfo('Оповещение', 'Осталась 1 минута!')

                        elif self.time_sum == 30:
                            msbox.showinfo('Оповещение', 'Осталось 30 секунд!')

                        elif self.time_sum == 10:
                            msbox.showinfo('Оповещение', 'Осталось 10 секунд!')
                            
                        elif self.time_sum == 5:
                            msbox.showinfo('Оповещение', 'Осталось 5 секунд!')


        elif self.stop % 2 == 0:
            self.stop -= 1
            self.star_time = True

            self.stop_b.configure(text = 'Остановить')

            if self.check_var.get() == 'on':
                self.stop_monitoring()
                self.check_var.set('off')
            else:
                pass
            self.check_cpu.configure(state = 'disabled')

            self.delay.configure(state = 'normal')
            self.clear.configure(state = 'disabled')
            self.otk.configure(state = 'disabled')
            self.hour_minus_button.configure(state = 'disabled')
            self.hour_plus_button.configure(state = 'disabled')
            self.minut_minus_button.configure(state = 'disabled')
            self.minut_plus_button.configure(state = 'disabled')

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
                        self.star_time = True
                        self.entry_hour.delete(0, 25)
                        self.entry_minut.delete(0 ,25)
                        self.entry_hour.insert(0, 0)
                        self.entry_minut.insert(0, 0)
                        self.time_out_h.configure(text = '00')
                        self.time_out_m.configure(text = '00')
                        self.stop_b.configure(text = 'Возобновить')
                        self.check_cpu.configure(state = 'normal')
                        self.delay.configure(state = 'disabled')
                        self.otk.configure(state = 'normal')
                        self.entry_hour.configure(state = 'normal')
                        self.entry_minut.configure(state = 'normal')
                        self.hour_minus_button.configure(state = 'normal')
                        self.hour_plus_button.configure(state = 'normal')
                        self.minut_minus_button.configure(state = 'normal')
                        self.minut_plus_button.configure(state = 'normal')
                        self.setings_b.configure(state = 'normal')
                        print('3) The input field "entry_hour" and "entry_minut" is cleared')



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
                        if self.time_sum == 60:
                            msbox.showinfo('Оповещение', 'Осталась 1 минута!')

                        elif self.time_sum == 30:
                            msbox.showinfo('Оповещение', 'Осталось 30 секунд!')

                        elif self.time_sum == 10:
                            msbox.showinfo('Оповещение', 'Осталось 10 секунд!')
                            
                        elif self.time_sum == 5:
                            msbox.showinfo('Оповещение', 'Осталось 5 секунд!')


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
                        self.star_time = True
                        self.entry_hour.delete(0, 25)
                        self.entry_minut.delete(0 ,25)
                        self.entry_hour.insert(0, 0)
                        self.entry_minut.insert(0, 0)
                        self.time_out_h.configure(text = '00')
                        self.time_out_m.configure(text = '00')
                        self.stop_b.configure(text = 'Возобновить')
                        self.check_cpu.configure(state = 'normal')
                        self.otk.configure(state = 'normal')
                        self.entry_hour.configure(state = 'normal')
                        self.entry_minut.configure(state = 'normal')
                        self.hour_minus_button.configure(state = 'normal')
                        self.hour_plus_button.configure(state = 'normal')
                        self.minut_minus_button.configure(state = 'normal')
                        self.minut_plus_button.configure(state = 'normal')
                        self.setings_b.configure(state = 'normal')
                        print('4) The input field "entry_hour" and "entry_minut" is cleared')



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
                        if self.time_sum == 60:
                            msbox.showinfo('Оповещение', 'Осталась 1 минута!')

                        elif self.time_sum == 30:
                            msbox.showinfo('Оповещение', 'Осталось 30 секунд!')

                        elif self.time_sum == 10:
                            msbox.showinfo('Оповещение', 'Осталось 10 секунд!')
                            
                        elif self.time_sum == 5:
                            msbox.showinfo('Оповещение', 'Осталось 5 секунд!')

        


    # def start_but(self):

# Разбей функцию stoped() на несколько других функций для более широкой настройки



# Функция служит для передачи времени из полей ввода Часов и Минут, также 
# требуется для отключений виджетов интерфейса для воизбежания багов
# Функция принимает на вход часы и минуты, переводит в минуты и дальше 
# используется для подсчета времени до окончания работы программы




    def start_time(self):
        text = int(self.entry_hour.get()) + int(self.entry_minut.get())
        if not self.star_time:
            if 0 < int(text) < 6001:
                self.check_cpu.configure(state = 'disabled')

                if self.check_var.get() == 'on':
                    self.stop_monitoring()
                    self.check_var.set('off')
                elif self.check_var.get() == 'off':
                    pass

                self.str_b.configure(state = 'disabled')
                self.stop_b.configure(state = 'normal')
                self.delay.configure(state = 'normal')
                self.otk.configure(state = 'disabled')
                self.hour_minus_button.configure(state = 'disabled')
                self.hour_plus_button.configure(state = 'disabled')
                self.minut_minus_button.configure(state = 'disabled')
                self.minut_plus_button.configure(state = 'disabled')

                self.en_h.delete(0, 25)
                self.en_m.delete(0, 25)
                self.en_h.insert(0, self.entry_hour.get())
                self.en_m.insert(0, self.entry_minut.get())

                try:
                    time_hour = int(self.entry_hour.get()) * 60
                    time_minut = int(self.entry_minut.get()) 
                    self.time_sums = time_minut + time_hour
                    if self.time_sums > 0:
                        self.time_sum = self.time_sums
                        self.star_time = True
                        self.number()
                except ValueError:
                    print('error')
                    self.entry_hour.delete(0, 25)
                    self.entry_minut.delete(0 ,25)
                    self.entry_hour.insert(0, 0)
                    self.entry_minut.insert(0, 0)
                    self.entry_hour.configure(state = 'disabled')
                    self.entry_minut.configure(state = 'disabled')
            
            elif text < 0 or text > 6001:
                self.star_time = False
                self.entry_hour.delete(0, 25)
                self.entry_minut.delete(0 ,25)
                self.entry_hour.insert(0, 0)
                self.entry_minut.insert(0, 0)
                self.time_out_h.configure(text = '00')
                self.time_out_m.configure(text = '00')
                self.stop_b.configure(text = 'Возобновить')
                self.check_cpu.configure(state = 'normal')
                self.delay.configure(state = 'disabled')
                self.otk.configure(state = 'normal')
                print('st) The input field "entry_hour" and "entry_minut" is cleared')

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
            
                elif 0 > self.time_sum or self.time_sum > 6000:
                    self.star_time = False
                    self.entry_hour.delete(0, 25)
                    self.entry_minut.delete(0 ,25)
                    self.entry_hour.insert(0, 0)
                    self.entry_minut.insert(0, 0)
                    self.time_out_h.configure(text = '00')
                    self.time_out_m.configure(text = '00')
                    self.stop_b.configure(text = 'Возобновить')
                    self.check_cpu.configure(state = 'normal')
                    self.delay.configure(state = 'disabled')
                    self.otk.configure(state = 'normal')
                    self.entry_hour.configure(state = 'normal')
                    self.entry_minut.configure(state = 'normal')
                    self.hour_minus_button.configure(state = 'normal')
                    self.hour_plus_button.configure(state = 'normal')
                    self.minut_minus_button.configure(state = 'normal')
                    self.minut_plus_button.configure(state = 'normal')
                    self.setings_b.configure(state = 'normal')
                    print('number) The input field "entry_hour" and "entry_minut" is cleared')

                else:
                    self.star_time = False
                    self.delay.configure(state = 'disabled')
                    self.otk.configure(state = 'normal')
                    self.stoped()
                    if sys.platform == 'win32':
                        if self.choise_act.get()[0] == 'Г':
                            print('Гибернация')
                            self.command = 'shutdown /h'
                        elif self.choise_act.get()[0] == 'О':
                            print('Отключение')
                            self.command = 'shutdown /s /t 0'
                        elif self.choise_act.get()[0] == 'П':
                            print('Перезагрузка')
                            self.command = 'shutdown /r /t 0'
                    try:
                        os.system(self.command)
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
                    if self.time_sum == 60:
                        msbox.showinfo('Оповещение', 'Осталась 1 минута!')

                    elif self.time_sum == 30:
                        msbox.showinfo('Оповещение', 'Осталось 30 секунд!')

                    elif self.time_sum == 10:
                        msbox.showinfo('Оповещение', 'Осталось 10 секунд!')
                        
                    elif self.time_sum == 5:
                        msbox.showinfo('Оповещение', 'Осталось 5 секунд!')

app = App()
app.mainloop()