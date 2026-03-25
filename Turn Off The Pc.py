import os
import sys
import psutil
import time as tm
import customtkinter
import tkinter.messagebox as msbox
from PIL import Image, ImageTk


def resource_path(rel_path):
    try:
        base_path =  sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')

    return os.path.join(base_path, rel_path)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Название, размеры, иконка
        self.title('ShutPC')
        
        width = (int(self.winfo_screenwidth()) // 2) - 255
        height = (int(self.winfo_screenheight()) // 2) - 200
        
        self.geometry(f'511x360+{width}+{height}') #320x240 #511x305
        self.resizable(False, False)
        
        icon = resource_path('timer.ico')
        self.iconbitmap(icon)
  

        # Автоматическое создание конфига в случае отсутствия
        if getattr(sys, 'frozen', False):
            applic_path = os.path.dirname(sys.executable)

        else:
            applic_path = os.path.dirname(os.path.abspath(__file__))

        config_path = os.path.join(applic_path, 'config.txt')

        if not os.path.exists(config_path):
            with open(config_path, 'w', encoding = 'utf-8') as f:
                f.write('600LТМОfГолубой')


        # Открытие файла для извлечения настроек
        file = open('config.txt', 'r', encoding = 'utf-8')
        text = file.read()

        # Знак разделителя для извлечения настроек 
        L_index = int(text.index('L'))


        self.open_file_optionmenu_mode_themes_ui = text[L_index + 1]
        self.open_file_optionmenu_mode_color_ui = text[L_index + 5:]
        self.open_file_optionmenu_mode_countdown_time = text[L_index + 2]
        
        self.open_file_optionmenu_mode_act = text[L_index + 3]
        self.open_file_checkbox_mode_auto_hibernation = text[L_index + 4]
        self.open_file_entry_time_for_auto_hibernation = text[0:L_index]

        file.close()
        
        print(self.open_file_optionmenu_mode_themes_ui)
        print(self.open_file_optionmenu_mode_color_ui)
        print(self.open_file_optionmenu_mode_countdown_time)
        print(self.open_file_optionmenu_mode_act)
        print(self.open_file_checkbox_mode_auto_hibernation)
        print(self.open_file_entry_time_for_auto_hibernation)

        self.value_for_countwond_times = 60000


        open_image_for_open_settings = Image.open(resource_path('settings.png'))
        image_open_settings = ImageTk.PhotoImage(open_image_for_open_settings)

        open_image_for_shut_settings = Image.open(resource_path('close.png'))
        image_shut_settings = ImageTk.PhotoImage(open_image_for_shut_settings)

        open_image_for_save_settings = Image.open(resource_path('save.png'))
        image_save_settigs = ImageTk.PhotoImage(open_image_for_save_settings)


        # Функция для закрытия приложения через сочетание клавиш "Ctrl + Q"
        def quit(event):
            self.destroy()
        self.bind('<Control-Key-q>', quit)


        def function_delay_time():
            
            if self.value_optionmenu_mode_countdown_time.get()[0] == 'М':
                
                if self.summa_hours_and_minuts_for_convetison_in_minuts < 5993:

                    self.summa_hours_and_minuts_for_convetison_in_minuts += 5
                    
                    hours = str(self.summa_hours_and_minuts_for_convetison_in_minuts // 60)
                    minuts= str(self.summa_hours_and_minuts_for_convetison_in_minuts % 60)


                    if len(hours) == 1 and len(minuts) == 1:
                        self.label_title_count_time_hours.configure(text = f'0{hours}')
                        self.label_title_count_time_minuts.configure(text = f'0{minuts}')
                        
                    elif len(hours) == 1 and len(minuts) != 1:
                        self.label_title_count_time_hours.configure(text = f'0{hours}')
                        self.label_title_count_time_minuts.configure(text = minuts)
                        
                    elif len(hours) != 1 and len(minuts) == 1:
                        self.label_title_count_time_hours.configure(text = hours)
                        self.label_title_count_time_minuts.configure(text = f'0{minuts}')
                        
                    else:
                        self.label_title_count_time_hours.configure(text = hours)
                        self.label_title_count_time_minuts.configure(text = minuts)

                    plus_minuts = int(self.entry_title_accept_minuts.get()) + 6


                    if int(self.entry_title_accept_minuts.get()) < 55:

                        self.entry_title_accept_minuts.delete(0, 25)
                        self.entry_title_accept_minuts.insert(0, plus_minuts - 1)

                        self.entry_under_title_for_function_stop_time_minuts.delete(0, 25)
                        self.entry_under_title_for_function_stop_time_minuts.insert(0, plus_minuts - 1)
                        tm.sleep(0.2)
                    
                    
                    elif int(self.entry_title_accept_minuts.get()) > 55:
                        
                        delay_h = int(self.entry_title_accept_hours.get()) + 1
                        delay_m = 60 - int(self.entry_title_accept_minuts.get()) 

                        if len(str(delay_h)) == 1:
                            self.entry_title_accept_hours.delete(0, 25)
                            self.entry_title_accept_hours.insert(0, delay_h)
                            self.entry_title_accept_minuts.delete(0, 25)
                            self.entry_title_accept_minuts.insert(0, delay_m)
                            
                        elif len(str(delay_h)) != 1:
                            self.entry_title_accept_hours.delete(0, 25)
                            self.entry_title_accept_hours.insert(0, delay_h)
                            self.entry_title_accept_minuts.deelte(0, 25)
                            self.entry_title_accept_minuts.insert(0, delay_m)


                    elif int(self.entry_title_accept_minuts.get()) == 55:

                        delay_h = int(self.entry_title_accept_hours.get())
                        
                        self.entry_title_accept_hours.delete(0, 25)
                        self.entry_title_accept_hours.insert(0, delay_h + 1)
                        self.entry_title_accept_minuts.delete(0, 25)
                        self.entry_title_accept_minuts.insert(0, '0')




            elif self.value_optionmenu_mode_countdown_time.get()[0] == 'С':
                
                if self.summa_hours_and_minuts_for_convetison_in_minuts < 5699:
                    
                    self.summa_hours_and_minuts_for_convetison_in_minuts += 300
                    plus_seconds = int(self.entry_title_accept_hours.get()) + 5
                    
                    self.entry_title_accept_hours.delete(0, 25)
                    self.entry_title_accept_hours.insert(0, plus_seconds)
                    self.entry_under_title_for_function_stop_time_hours.delete(0, 25)
                    self.entry_under_title_for_function_stop_time_hours.insert(0, plus_seconds)
                    
                    tm.sleep(0.2)


        def function_clear_time():
            self.entry_title_accept_hours.delete(0, 25)
            self.entry_title_accept_minuts.delete(0 ,25)
            self.entry_title_accept_hours.insert(0, 0)
            self.entry_title_accept_minuts.insert(0, 0)
            self.label_title_count_time_hours.configure(text = '00')
            self.label_title_count_time_minuts.configure(text = '00')


        def hour_minus():
            hours_minus = int(self.entry_title_accept_hours.get()) - 1
            
            if 0 <= hours_minus < 100:
                self.entry_title_accept_hours.delete(0, 20)
                self.entry_title_accept_hours.insert(0, hours_minus)
                
            else:
                self.entry_title_accept_hours.insert(0, '')


        def hour_plus():
            hours_plus  = int(self.entry_title_accept_hours.get()) + 1
            
            if 0 < hours_plus < 100:
                self.entry_title_accept_hours.delete(0, 20)
                self.entry_title_accept_hours.insert(0, hours_plus)
                
            else:
                self.entry_title_accept_hours.insert(0, '')


        def minut_minus():
            minuts_minus = int(self.entry_title_accept_minuts.get()) - 1
            
            if 0 <= minuts_minus < 100:
                self.entry_title_accept_minuts.delete(0, 20)
                self.entry_title_accept_minuts.insert(0, minuts_minus)
                
            else:
                self.entry_title_accept_minuts.insert(0, '')


        def minut_plus():
            minusts_plus = int(self.entry_title_accept_minuts.get()) + 1
            sum = int(self.entry_title_accept_hours.get()) + int(self.entry_title_accept_minuts.get())

            if int(self.entry_title_accept_hours.get()) == 99 and minusts_plus == 61:
                self.entry_title_accept_minuts.insert(0, '')
                
            elif int(self.entry_title_accept_hours.get()) <= 99 and 0 < minusts_plus <= 99:
                self.entry_title_accept_minuts.delete(0, 20)
                self.entry_title_accept_minuts.insert(0, minusts_plus)
                
            else:
                self.entry_title_accept_minuts.insert(0, '')


        def validate(text):
            if text.isdigit() or text == '':
                return True
            else:
                return False


        def function_open_settings():
            self.frame_title_background_left_side.place(x = 600, y = 600)
            self.frame_title_background_delay.place(x = 700, y = 100)
            self.frame_settings_background_under_button_settings.place(x = 600, y = 600)
            self.frame_settings_background_left_side.place(x = 0, y = 0)
            self.frame_settings_background_right_side.place(x = 426, y = 0)    
            self.frame_settins_background_under_button_settings.place(x = 455, y = 0)      


            self.label_title_designation_hours.place(x = 600, y = 600)
            self.label_title_designaton_minuts.place(x = 600, y = 600)
            self.label_title_time_out_through.place(x = 600, y = 600)
            self.label_title_count_time_hours.place(x = 600, y = 600)
            self.label_title_count_time_minuts.place(x = 600, y = 600)
            self.label_title_unit_time_hours.place(x = 700, y = 700)
            self.label_title_unit_time_minuts.place(x = 600,  y = 600)
            self.label_settings_choise_themes_ui.place(x = 40, y = 10)
            self.label_settings_choise_color_ui.place(x = 40, y = 50)
            self.label_settings_choise_countdown_time.place(x = 40, y = 90)
            # self.label_settings_choise_font_ui.place(x = 40, y = 250)
            self.label_settings_time_for_auto_hibernation.place(x = 40, y = 210)
            self.label_settings_choise_act_after_time.place(x = 40, y = 130)
            self.label_settings_state_auto_hibernation.place(x = 40, y = 170)


            self.button_title_start_time.place(x = 600, y = 600)
            self.button_title_stop_time.place(x = 600, y = 600)
            self.button_title_minus_hour.place(x = 600, y = 600)
            self.button_title_plus_hour.place(x = 600, y = 600)
            self.button_title_minus_minut.place(x = 600, y = 600)
            self.button_title_plus_minut.place(x = 600, y = 600)
            self.button_title_delay_time.place(x = 700, y = 100)
            self.button_title_clear_time.place(x = 600, y = 600)
            self.button_settings_open_page_settings.place(x = 600, y = 600)
            self.button_settings_shut_page_settings.place(x = 455, y = 0)
            self.button_settings_save_settings.place(x = 455, y = 56)


            self.entry_title_accept_hours.place(x = 600, y = 600)
            self.entry_title_accept_minuts.place(x = 600, y = 600)
            self.entry_settings_auto_shutdown.place(x = 310, y = 210)


            self.optionmenu_settings_mode_themes_ui.place(x = 260, y = 10)
            self.optionmenu_settings_mode_color_ui.place(x = 260, y = 50)
            self.optionmenu_settings_mode_countdown_time.place(x = 260, y = 90)
            self.optionmenu_settings_mode_act_after_time.place(x = 260, y = 130)


            self.checkbox_settings_mode_auto_hibernation.place(x = 385, y = 170)


        def function_shut_settings():
            self.frame_title_background_left_side.place(x = 0, y = 0)
            self.frame_title_background_delay.place(x = 250, y = 290)
            self.frame_settings_background_under_button_settings.place(x = 455, y = 0)
            self.frame_settings_background_left_side.place(x = 1150, y = 10)
            self.frame_settings_background_right_side.place(x = 1200, y = 10)
            self.frame_settins_background_under_button_settings.place(x = 1250, y = 10)


            self.label_title_designation_hours.place(x = 104, y = 2)
            self.label_title_designaton_minuts.place(x = 92, y = 72)
            self.label_title_time_out_through.place(x = 272, y = 0)
            self.label_title_count_time_hours.place(x = 279, y = 10)
            self.label_title_count_time_minuts.place(x = 279, y = 145)
            self.label_title_unit_time_hours.place(x = 435, y = 119)
            self.label_title_unit_time_minuts.place(x = 435, y = 254)
            self.label_settings_choise_themes_ui.place(x = 700, y = 100)
            self.label_settings_choise_color_ui.place(x = 700, y = 170)
            self.label_settings_choise_countdown_time.place(x = 700, y = 130)
            # self.label_settings_choise_font_ui.place(x = 700, y = 100)
            self.label_settings_time_for_auto_hibernation.place(x = 700, y = 40)
            self.label_settings_choise_act_after_time.place(x = 700, y = 70)
            self.label_settings_state_auto_hibernation.place(x = 700, y = 10)


            self.button_title_start_time.place(x = 15, y = 155)
            self.button_title_stop_time.place(x = 15, y = 240)
            self.button_title_minus_hour.place(x = 15, y = 30)
            self.button_title_plus_hour.place(x = 205, y = 30)
            self.button_title_minus_minut.place(x = 15, y = 100)
            self.button_title_plus_minut.place(x = 205, y = 100)
            self.button_title_delay_time.place(x = 265, y = 300)
            self.button_title_clear_time.place(x = 15, y = 300)
            self.button_settings_open_page_settings.place(x = 455, y = 0)
            self.button_settings_shut_page_settings.place(x = 1350, y = 10)
            self.button_settings_save_settings.place(x = 1350, y = 80)


            self.entry_title_accept_hours.place(x = 55, y = 30)
            self.entry_title_accept_minuts.place(x = 55, y = 100)
            self.entry_settings_auto_shutdown.place(x = 1000, y = 10)


            self.optionmenu_settings_mode_themes_ui.place(x = 700, y = 250)
            self.optionmenu_settings_mode_color_ui.place(x = 700, y = 300)
            self.optionmenu_settings_mode_countdown_time.place(x = 700, y = 350)
            self.optionmenu_settings_mode_act_after_time.place(x = 700, y = 400)


            self.checkbox_settings_mode_auto_hibernation.place(x = 600, y = 10)


            if self.value_optionmenu_mode_countdown_time.get() == 'Минутам':
                self.label_title_designation_hours.place(x = 104, y = 2)
                self.label_title_designaton_minuts.place(x = 92, y = 72)
            else:
                self.label_title_designation_hours.place(x = 92, y = 2)
                self.label_title_designaton_minuts.place(x = 89, y = 72)


        def function_choise_themes_ui(value):
            if value == 'Темная':
                customtkinter.set_appearance_mode('Dark')

                self.frame_title_background_left_side.configure(fg_color = '#2E2E2E')
                self.frame_title_background_delay.configure(fg_color = '#2E2E2E')
                self.frame_settings_background_under_button_settings.configure(fg_color = '#2E2E2E')
                self.frame_settings_background_left_side.configure(fg_color = '#2E2E2E')
                self.frame_settings_background_right_side.configure(fg_color = '#2E2E2E')

                self.label_title_designation_hours.configure(fg_color = '#2E2E2E')
                self.label_title_designaton_minuts.configure(fg_color = '#2E2E2E')

            elif value == 'Светлая':
                customtkinter.set_appearance_mode('Light')

                self.frame_title_background_delay.configure(fg_color = '#D6D6D6')
                self.frame_title_background_left_side.configure(fg_color = '#D6D6D6')
                self.frame_settings_background_under_button_settings.configure(fg_color = '#D6D6D6')
                self.frame_settings_background_left_side.configure(fg_color = '#D6D6D6')
                self.frame_settings_background_right_side.configure(fg_color = '#D6D6D6')

                self.label_title_designation_hours.configure(fg_color = '#D6D6D6')
                self.label_title_designaton_minuts.configure(fg_color = '#D6D6D6')


        def function_choise_color_ui(value):
            # голубой:    #346EBA  #3A5B87  #283F5E
            # красный:    #FF4242  #B04C4C  #723131
            # зеленый:    #52D163  #4E9158  #315A37
            # оранжевый:  #DB9960  #8F623C  #61432A
            # фиолетовый: #5B3982  #9250DE  #462B64

            # fg_color - отображаемый цвет
            # hover_color - цвет при наведении
            if value == 'Голубой':

                self.checkbox_settings_mode_auto_hibernation.configure(fg_color = '#346EBA', hover_color = '#3A5B87')

                self.button_title_delay_time.configure(fg_color = '#346EBA', hover_color = '#3A5B87')

                self.button_title_clear_time.configure(fg_color = '#346EBA', hover_color = '#3A5B87')

                self.frame_settins_background_under_button_settings.configure(fg_color = '#283F5E')

                self.button_title_start.configure(fg_color = '#346EBA', hover_color = '#3A5B87')

                self.button_title_stop.configure(fg_color = '#346EBA', hover_color = '#3A5B87')

                self.button_title_minus_hour.configure(fg_color = '#346EBA', hover_color = '#3A5B87')

                self.button_title_plus_hour.configure(fg_color = '#346EBA', hover_color = '#3A5B87')

                self.button_title_minus_minut.configure(fg_color = '#346EBA', hover_color = '#3A5B87')

                self.button_title_plus_minut.configure(fg_color = '#346EBA', hover_color = '#3A5B87')

                self.button_settings_open_page_settings.configure(fg_color = '#346EBA', hover_color = '#3A5B87')

                self.button_settings_shut_page_settings.configure(fg_color = '#346EBA', hover_color = '#3A5B87')

                self.button_settings_save_settings.configure(fg_color = '#346EBA', hover_color = '#3A5B87')

                self.optionmenu_settings_mode_themes_ui.configure(fg_color = '#346EBA', button_color = '#346EBA', button_hover_color = '#3A5B87')

                self.optionmenu_settings_mode_color_ui.configure(fg_color = '#346EBA', button_color = '#346EBA', button_hover_color = '#3A5B87')

                self.optionmenu_settings_mode_countdown_time.configure(fg_color = '#346EBA', button_color = '#346EBA', button_hover_color = '#3A5B87')

                self.optionmenu_settings_mode_act_after_time.configure(fg_color = '#346EBA', button_color = '#346EBA', button_hover_color = '#3A5B87')            


            elif value == 'Красный':

                self.checkbox_settings_mode_auto_hibernation.configure(fg_color = '#D65656', hover_color = '#B04C4C')

                self.button_title_delay_time.configure(fg_color = '#D65656', hover_color = '#B04C4C')

                self.button_title_clear_time.configure(fg_color = '#D65656', hover_color = '#B04C4C')

                self.frame_settins_background_under_button_settings.configure(fg_color = '#723131')

                self.button_title_start.configure(fg_color = '#D65656', hover_color = '#B04C4C')

                self.button_title_stop.configure(fg_color = '#D65656', hover_color = '#B04C4C')

                self.button_title_minus_hour.configure(fg_color = '#D65656', hover_color = '#B04C4C')

                self.button_title_plus_hour.configure(fg_color = '#D65656', hover_color = '#B04C4C')

                self.button_title_minus_minut.configure(fg_color = '#D65656', hover_color = '#B04C4C')

                self.button_title_plus_minut.configure(fg_color = '#D65656', hover_color = '#B04C4C')

                self.button_settings_open_page_settings.configure(fg_color = '#D65656', hover_color = '#B04C4C')

                self.button_settings_shut_page_settings.configure(fg_color = '#D65656', hover_color = '#B04C4C')

                self.button_settings_save_settings.configure(fg_color = '#D65656', hover_color = '#B04C4C')

                self.optionmenu_settings_mode_themes_ui.configure(fg_color = '#D65656', button_color = '#D65656', button_hover_color = '#B04C4C')

                self.optionmenu_settings_mode_color_ui.configure(fg_color = '#D65656', button_color = '#D65656', button_hover_color = '#B04C4C')

                self.optionmenu_settings_mode_countdown_time.configure(fg_color = '#D65656', button_color = '#D65656', button_hover_color = '#B04C4C')

                self.optionmenu_settings_mode_act_after_time.configure(fg_color = '#D65656', button_color = '#D65656', button_hover_color = '#B04C4C')


            elif value == 'Зеленый':
                # зеленый: #41904B  #407347  #315A37

                self.checkbox_settings_mode_auto_hibernation.configure(fg_color = '#41904B', hover_color = '#407347')

                self.button_title_delay_time.configure(fg_color = '#41904B', hover_color = '#407347')

                self.button_title_clear_time.configure(fg_color = '#41904B', hover_color = '#407347')

                self.frame_settins_background_under_button_settings.configure(fg_color = '#315A37')

                self.button_title_start.configure(fg_color = '#41904B', hover_color = '#407347')

                self.button_title_stop.configure(fg_color = '#41904B', hover_color = '#407347')

                self.button_title_minus_hour.configure(fg_color = '#41904B', hover_color = '#407347')

                self.button_title_plus_hour.configure(fg_color = '#41904B', hover_color = '#407347')

                self.button_title_minus_minut.configure(fg_color = '#41904B', hover_color = '#407347')

                self.button_title_plus_minut.configure(fg_color = '#41904B', hover_color = '#407347')

                self.button_settings_open_page_settings.configure(fg_color = '#41904B', hover_color = '#407347')

                self.button_settings_shut_page_settings.configure(fg_color = '#41904B', hover_color = '#407347')

                self.button_settings_save_settings.configure(fg_color = '#41904B', hover_color = '#407347')

                self.optionmenu_settings_mode_themes_ui.configure(fg_color = '#41904B', button_color = '#41904B', button_hover_color = '#407347')

                self.optionmenu_settings_mode_color_ui.configure(fg_color = '#41904B', button_color = '#41904B', button_hover_color = '#407347')

                self.optionmenu_settings_mode_countdown_time.configure(fg_color = '#41904B', button_color = '#41904B', button_hover_color = '#407347')

                self.optionmenu_settings_mode_act_after_time.configure(fg_color = '#41904B', button_color = '#41904B', button_hover_color = '#407347')
                    
    
            elif value == 'Оранжевый':
                # оранжевый: #C4834D  #8F623C  #61432A

                self.checkbox_settings_mode_auto_hibernation.configure(fg_color = '#C4834D', hover_color = '#8F623C')

                self.button_title_delay_time.configure(fg_color = '#C4834D', hover_color = '#8F623C')

                self.button_title_clear_time.configure(fg_color = '#C4834D', hover_color = '#8F623C')

                self.frame_settins_background_under_button_settings.configure(fg_color = '#61432A')

                self.button_title_start.configure(fg_color = '#C4834D', hover_color = '#8F623C')

                self.button_title_stop.configure(fg_color = '#C4834D', hover_color = '#8F623C')

                self.button_title_minus_hour.configure(fg_color = '#C4834D', hover_color = '#8F623C')

                self.button_title_plus_hour.configure(fg_color = '#C4834D', hover_color = '#8F623C')

                self.button_title_minus_minut.configure(fg_color = '#C4834D', hover_color = '#8F623C')

                self.button_title_plus_minut.configure(fg_color = '#C4834D', hover_color = '#8F623C')
                
                self.button_settings_open_page_settings.configure(fg_color = '#C4834D', hover_color = '#8F623C')

                self.button_settings_shut_page_settings.configure(fg_color = '#C4834D', hover_color = '#8F623C')

                self.button_settings_save_settings.configure(fg_color = '#C4834D', hover_color = '#8F623C')

                self.optionmenu_settings_mode_themes_ui.configure(fg_color = '#C4834D', button_color = '#C4834D', button_hover_color = '#8F623C')

                self.optionmenu_settings_mode_color_ui.configure(fg_color = '#C4834D', button_color = '#C4834D', button_hover_color = '#8F623C')

                self.optionmenu_settings_mode_countdown_time.configure(fg_color = '#C4834D', button_color = '#C4834D', button_hover_color = '#8F623C')

                self.optionmenu_settings_mode_act_after_time.configure(fg_color = '#C4834D', button_color = '#C4834D', button_hover_color = '#8F623C')
                    

            elif value == 'Фиолетовый':
                # фиолетовый: #9250DE  #5B3982  #462B64

                self.checkbox_settings_mode_auto_hibernation.configure(fg_color = '#9250DE', hover_color = '#5B3982')

                self.button_title_delay_time.configure(fg_color = '#9250DE', hover_color = '#5B3982')

                self.button_title_clear_time.configure(fg_color = '#9250DE', hover_color = '#5B3982')

                self.frame_settins_background_under_button_settings.configure(fg_color = '#462B64')

                self.button_title_start.configure(fg_color = '#9250DE', hover_color = '#5B3982')

                self.button_title_stop.configure(fg_color = '#9250DE', hover_color = '#5B3982')

                self.button_title_minus_hour.configure(fg_color = '#9250DE', hover_color = '#5B3982')

                self.button_title_plus_hour.configure(fg_color = '#9250DE', hover_color = '#5B3982')

                self.button_title_minus_minut.configure(fg_color = '#9250DE', hover_color = '#5B3982')

                self.button_title_plus_minut.configure(fg_color = '#9250DE',hover_color = '#5B3982')

                self.button_settings_open_page_settings.configure(fg_color = '#9250DE',hover_color = '#5B3982')

                self.button_settings_shut_page_settings.configure(fg_color = '#9250DE',hover_color = '#5B3982')

                self.button_settings_save_settings.configure(fg_color = '#9250DE',hover_color = '#5B3982')

                self.optionmenu_settings_mode_themes_ui.configure(fg_color = '#9250DE', button_color = '#9250DE', button_hover_color = '#5B3982')

                self.optionmenu_settings_mode_color_ui.configure(fg_color = '#9250DE', button_color = '#9250DE', button_hover_color = '#5B3982')

                self.optionmenu_settings_mode_countdown_time.configure(fg_color = '#9250DE', button_color = '#9250DE', button_hover_color = '#5B3982')

                self.optionmenu_settings_mode_act_after_time.configure(fg_color = '#9250DE', button_color = '#9250DE', button_hover_color = '#5B3982')


        def function_choise_countdown_time(value):

            if value == 'Минутам':
                self.label_title_designation_hours.configure(text = 'Часы:')
                self.label_title_designaton_minuts.configure(text = 'Минуты:')

                self.label_title_unit_time_hours.configure(text = 'H')
                self.label_title_unit_time_minuts.configure(text = 'M')
                self.value_for_countwond_times = 60000

            elif value == 'Секундам':
                self.label_title_designation_hours.configure(text = 'Минуты:')
                self.label_title_designaton_minuts.configure(text = 'Секунды:')

                self.label_title_unit_time_hours.configure(text = 'M')
                self.label_title_unit_time_minuts.configure(text = 'S')
                self.value_for_countwond_times = 1000


        def filepath(file_path, content):
            with open(file_path, 'w', encoding = 'utf-8') as f:
                f.write(content)
            print('saved')


        def function_save_settings():
            # Время для автогибернации + Тема + Режим отсчета + Действие + Автогибернация + Цвет            

            theme = self.value_optionmenu_mode_themes_ui.get()[0]
            otk = self.value_optionmenu_mode_countdown_time.get()[0]
            act = self.value_optionmenu_mode_act_after_time.get()[0]
            cpu = self.value_checkbox_mode_auto_hibernation.get()[-1]
            time = self.entry_settings_auto_shutdown.get()
            color = self.value_optionmenu_mode_color_ui.get()
            
            print('Theme ui:', theme)
            print('Counter the time:', otk)
            print('Act:', act) 
            print('Auto hibernation:', cpu)
            print('Time for auto hibernation:', time)
            print('Color ui:', color)
            
            content = time + 'L' + str(theme) + str(otk) + str(act) + str(cpu) + str(color)

            filepath('config.txt', content)


        def function_act_after_time(value):
            
            if value == 'Гибернация':
                self.command = 'shutdown /h'
            elif value == 'Выключение':
                self.command = 'shutdown /s /t 0'
            elif value == 'Перезагрузка':
                self.command = 'shutdown /r /t 0'


        # Экспорт значения из checkbox_settings_mode_auto_hibernation
        self.value_checkbox_mode_auto_hibernation = customtkinter.StringVar(value = 'off')

        # Чек бокс в настройках. служит для автоматической гибернации self.function_auto_hibernation
        self.checkbox_settings_mode_auto_hibernation = customtkinter.CTkCheckBox(self,
            corner_radius = 0, text = '',
            onvalue = 'on', offvalue = 'off',
            variable = self.value_checkbox_mode_auto_hibernation, 
            command = self.function_auto_hibernation)
        
        self.checkbox_settings_mode_auto_hibernation.place(x = 600, y = 10)

        # Лейбл в настройках. служит для обозначения состоянии функции авто-гибернация function_auto_hibernation
        self.label_settings_state_auto_hibernation = customtkinter.CTkLabel(self,
            font = ('Arial', 19),
            text = 'Авто-гибернация:')
        
        self.label_settings_state_auto_hibernation.place(x = 700, y = 10)

        # Лейбл в настройках. служит для обозначения количества секунд до авто-гибернации
        self.label_settings_time_for_auto_hibernation = customtkinter.CTkLabel(self,
            font = ('Arial', 19),
            text = 'Секунд до авто-гибернации:')

        self.label_settings_time_for_auto_hibernation.place(x = 700, y = 40)

        # Лейбл в настройках. служит для обозначения выбора действия после истечения времени optionmenu_settings_mode_act_after_time
        self.label_settings_choise_act_after_time = customtkinter.CTkLabel(self,
            font = ('Arial', 19),
            text = 'Действие:')
        
        self.label_settings_choise_act_after_time.place(x = 700, y = 70)

        # Лейбл в настройках. служит для обозначения выбора темы ui
        self.label_settings_choise_themes_ui = customtkinter.CTkLabel(self,
            font = ('Arial', 19),
            text = 'Тема приложения:')
        
        self.label_settings_choise_themes_ui.place(x = 700, y = 100)

        # Лейбл в настройках. служит для обозначения выбора отсчета времени
        self.label_settings_choise_countdown_time = customtkinter.CTkLabel(self,
            font = ('Arial', 19),
            text = 'Отсчет по:')
        self.label_settings_choise_countdown_time.place(x = 700, y = 130)

        # Лейбл в настройках. служит для обозначения выбора цвета ui
        self.label_settings_choise_color_ui = customtkinter.CTkLabel(self,
            font = ('Arial', 19),
            text = 'Цвет приложения:')
        
        self.label_settings_choise_color_ui.place(x = 700, y = 170)

        # Экспорт значения из optionmenu_settings_mode_auto_hibernation
        self.value_optionmenu_mode_act_after_time = customtkinter.StringVar()
        
        # Меню выбора в настройках. служит для выбора действия после окончания времени function_act_after_time
        self.optionmenu_settings_mode_act_after_time = customtkinter.CTkOptionMenu(self,
            font = ('Arial', 16),
            values = ['Гибернация', 'Отключение', 'Перезагрузка'],
            width = 150, height = 30, corner_radius = 0,
            fg_color = '#346EBA', button_color = '#346EBA', button_hover_color = '#3A5B87',
            variable = self.value_optionmenu_mode_act_after_time,
            command = function_act_after_time)
        
        self.optionmenu_settings_mode_act_after_time.place(x = 700, y = 400)

        # Импорт значения из файла настроек для optionmenu_settings_mode_act_after_time
        if self.open_file_optionmenu_mode_act == 'Г':
            self.optionmenu_settings_mode_act_after_time.set('Гибернация')

        elif self.open_file_optionmenu_mode_act == 'О':
            self.optionmenu_settings_mode_act_after_time.set('Отключение')

        elif self.open_file_optionmenu_mode_act == 'П':
            self.optionmenu_settings_mode_act_after_time.set('Перезагрузка')

        # Фрейм в главном окне, находится под полями ввода
        self.frame_title_background_left_side = customtkinter.CTkFrame(self,
            width = 260, height = 440, 
            fg_color = '#2E2E2E', corner_radius = 0)
        self.frame_title_background_left_side.place(x = 0, y = 0)

        # Фрейм в главном окне, находится под кнопкой "Настройки"
        self.frame_settings_background_under_button_settings = customtkinter.CTkFrame(self, 
            width = 58, height = 440,
            fg_color = '#2E2E2E', corner_radius = 0)
        self.frame_settings_background_under_button_settings.place(x = 455, y = 0)

        # Фрейм в настройках. служит задним планом для виджетов на левой стороне
        self.frame_settings_background_left_side = customtkinter.CTkFrame(self,
            width = 30, height = 370, corner_radius = 0,
            fg_color = '#2E2E2E')

        self.frame_settings_background_left_side.place(x = 1150, y = 10)

        # Фрейм в настройках. служит задним планом для виджетов в правой стороне
        self.frame_settings_background_right_side = customtkinter.CTkFrame(self,
            width = 30, height = 370, corner_radius = 0,
            fg_color = '#2E2E2E')
        
        self.frame_settings_background_right_side.place(x = 1200, y = 10)

        # Фрейм в настроках. служит задним планом для кнопки "Закрыть настройки"
        self.frame_settins_background_under_button_settings = customtkinter.CTkFrame(self,
            width = 58, height = 370, corner_radius = 0,
            fg_color = "#315A37")
        
        self.frame_settins_background_under_button_settings.place(x = 1250, y = 10)

        # # Лейбл в настроках. служит для обозначения выбора шрифта ui
        # self.label_settings_choise_font_ui = customtkinter.CTkLabel(self,
        #     font = ('Arial', 19),
        #     text = 'Шрифт:')

        # self.label_settings_choise_font_ui.place(x = 600, y = 260)

        # Кнопка на главном экране. служит для открытия страницы настроек function_open_settings
        self.button_settings_open_page_settings = customtkinter.CTkButton(self,
            text = '',
            image = image_open_settings, 
            width = 56, height = 56, corner_radius = 0, 
            fg_color = '#346EBA', hover_color = '#3A5B87',
            command = function_open_settings)
        
        self.button_settings_open_page_settings.place(x = 455, y = 0)

        # Кнопка в настройках. служит для закрытия страницы настроек function_shut_settings
        self.button_settings_shut_page_settings = customtkinter.CTkButton(self,
            text = '',
            image = image_shut_settings, 
            width = 56, height = 56, corner_radius = 0,
            fg_color = '#346EBA', hover_color = '#3A5B87',
            command = function_shut_settings)

        self.button_settings_shut_page_settings.place(x = 1350, y = 10)

        # Кнопка в настройках. служит для сохранения настроек function_save_settings
        self.button_settings_save_settings = customtkinter.CTkButton(self,
            text = '',
            image = image_save_settigs,
            width = 56, height = 56, corner_radius = 0,
            fg_color = '#346EBA', hover_color = '#3A5B87',
            command = function_save_settings)

        self.button_settings_save_settings.place(x = 1350, y = 80)

        # Экспорт значения из optionmenu_settings_mode_themes_ui
        self.value_optionmenu_mode_themes_ui = customtkinter.StringVar()

        # Меню выбора в настройках. служит для выбора темы ui
        self.optionmenu_settings_mode_themes_ui = customtkinter.CTkOptionMenu(self,
            font = ('Arial', 16),
            values = ['Темная', 'Светлая'],
            width = 150, height = 30, corner_radius = 0,
            fg_color = '#346EBA', button_color = '#346EBA', button_hover_color = '#3A5B87',
            variable = self.value_optionmenu_mode_themes_ui,
            command = function_choise_themes_ui)
        
        self.optionmenu_settings_mode_themes_ui.place(x = 700, y = 250)

        # Импорт значения из файла настроек для optionmenu_settings_mode_themes_ui
        if self.open_file_optionmenu_mode_themes_ui == 'С':
            self.optionmenu_settings_mode_themes_ui.set('Светлая')

        elif self.open_file_optionmenu_mode_themes_ui == 'Т':
            self.optionmenu_settings_mode_themes_ui.set('Темная')

        # Экспорт значения из optionmenu_settings_mode_color_ui
        self.value_optionmenu_mode_color_ui = customtkinter.StringVar()

        # Меню выбора в настройках. служит для выбора цвета ui
        self.optionmenu_settings_mode_color_ui = customtkinter.CTkOptionMenu(self,
            font = ('Arial', 16),
            values = ['Голубой', 'Красный', 'Зеленый', 'Оранжевый', 'Фиолетовый'],
            width = 150, height = 30, corner_radius = 0,
            fg_color = '#346EBA', button_color = '#346EBA', button_hover_color = '#3A5B87',
            variable = self.value_optionmenu_mode_color_ui,
            command = function_choise_color_ui)

        self.optionmenu_settings_mode_color_ui.place(x = 700, y = 300)
        self.optionmenu_settings_mode_color_ui.set(self.open_file_optionmenu_mode_color_ui)

        # Экспорт значения из optionmenu_settings_mode_countdown_time
        self.value_optionmenu_mode_countdown_time = customtkinter.StringVar()

        # Меню выбора в настройках. служит для выбора отсчета времени
        self.optionmenu_settings_mode_countdown_time = customtkinter.CTkOptionMenu(self,
            font = ('Arial', 16),
            values = ['Минутам', 'Секундам'],
            width = 150, height = 30, corner_radius = 0,
            fg_color = '#346EBA', button_color = '#346EBA', button_hover_color = '#3A5B87', 
            state = 'normal',
            variable = self.value_optionmenu_mode_countdown_time,
            command = function_choise_countdown_time)
        
        self.optionmenu_settings_mode_countdown_time.place(x = 700, y = 350)

        # Импорт значения из файла настроек для optionmenu_settings_mode_countdown_time
        if self.open_file_optionmenu_mode_countdown_time == 'М':
            self.optionmenu_settings_mode_countdown_time.set('Минутам')

        else:
            self.optionmenu_settings_mode_countdown_time.set('Секундам')

        # Лейбл на главном экране. служит счетчиком времени для пользователей, то есть показывает то, сколько минут осталось
        self.label_title_count_time_minuts = customtkinter.CTkLabel(self,
            font = ('Arial', 140, 'bold'),
            text = '00')
        
        self.label_title_count_time_minuts.place(x = 279, y = 145)

        # Лейбл на главном экране. служит счетчиком времени для пользователей, то есть показывает то, сколько часов осталось
        self.label_title_count_time_hours = customtkinter.CTkLabel(self,
            font = ('Arial', 140, 'bold'),
            text = '00')
        
        self.label_title_count_time_hours.place(x = 279, y = 10)

        # Лейбл на главном экране. служит задним планом для кнопки button_title_delay_time
        self.frame_title_background_delay = customtkinter.CTkFrame(self,
            width = 210, height = 85, corner_radius = 0,
            fg_color = '#2E2E2E')

        self.frame_title_background_delay.place(x = 250, y = 290)

        # Кнопка на главном экране. служит, чтобы откладывать время на 5 минут function_delay_time
        self.button_title_delay_time = customtkinter.CTkButton(self,
            font = ('Arial', 19),
            text = 'Отложить время',
            width = 185, height = 50, corner_radius = 0,
            fg_color = '#346EBA', hover_color = '#3A5B87',
            state = 'disabled',
            command = function_delay_time)

        self.button_title_delay_time.place(x = 265, y = 300)

        # Кнопка на главном экране. служит для очитски полей ввода, лейблов на главном экране function_clear_time
        self.button_title_clear_time = customtkinter.CTkButton(self,
            font = ('Arial', 23),
            text = 'Очистить',
            width = 230, height = 50, corner_radius = 0,
            fg_color = '#346EBA', hover_color = '#3A5B87',
            state = 'disabled',
            command = function_clear_time)
        
        self.button_title_clear_time.place(x = 15, y = 300)

        # Кнопка на главном экране. служит для запуска таймера function_start_time
        self.button_title_start_time = customtkinter.CTkButton(self,
            font = ('Arial', 23),
            text = 'Запустить', 
            width = 230, height = 75, corner_radius = 0,
            fg_color = '#346EBA', hover_color = '#3A5B87',
            command = self.function_start_time)
        
        self.button_title_start_time.place(x = 15, y = 155)      

        # Кнопка на главном экране. служит для оставновки таймера function_stop_time
        self.button_title_stop_time = customtkinter.CTkButton(self,
            font = ('Arial', 23),
            text = 'Остановить', 
            width = 230, height = 50, corner_radius = 0,
            fg_color = '#346EBA', hover_color = '#3A5B87',
            state = 'disabled',
            command = self.function_stop_time)
        
        self.button_title_stop_time.place(x = 15, y = 240)

        # Поле ввода на главном экране. служит для получения количества часов
        valid = (self.register(validate), '%P')

        self.entry_title_accept_hours = customtkinter.CTkEntry(self,
            font = ('Arial', 23),
            width = 150, height = 40, corner_radius = 0, 
            justify = 'center', 
            validate = 'key',
            validatecommand = valid)

        self.entry_title_accept_hours.place(x = 55, y = 30)
        self.entry_title_accept_hours.insert(0, '0')

        # Поле ввода в настройках. служит для получения количества секунд до авто гибернации
        self.entry_settings_auto_shutdown = customtkinter.CTkEntry(self,
            font = ('Arial', 23),
            width = 100, corner_radius = 0, 
            justify = 'right',
            validate = 'key',
            validatecommand = valid)

        self.entry_settings_auto_shutdown.place(x = 1000, y = 10)
        self.entry_settings_auto_shutdown.insert(0, self.open_file_entry_time_for_auto_hibernation)

        # Кнопа на главном экране. служит для уменьшения количества часов поля ввода entry_title_accept_hours
        self.button_title_minus_hour = customtkinter.CTkButton(self,
            font = ('Arial', 24),
            text = '-', 
            width = 40, height = 40, corner_radius = 0,  
            fg_color = '#346EBA', hover_color = '#3A5B87',                   
            command = hour_minus)
        
        self.button_title_minus_hour.place(x = 15, y = 30)

        # Кнопка на главном экране. служит для увеличения количества часов поля ввода entry_title_accept_hours
        self.button_title_plus_hour = customtkinter.CTkButton(self,
            font = ('Arial', 24),
            text = '+',
            width = 40, height = 40, corner_radius = 0,
            fg_color = '#346EBA', hover_color = '#3A5B87',                             
            command = hour_plus)
        
        self.button_title_plus_hour.place(x = 205, y = 30)

        # Лейбл на главном экране. служит для обозначния поля ввода entry_title_accept_hours "часами"
        self.label_title_designation_hours = customtkinter.CTkLabel(self,
            font = ('Arial', 20),
            text = 'Часы:',
            fg_color = '#2E2E2E')
        
        self.label_title_designation_hours.place(x = 104, y = 2)

        # Поле ввода на главном экране. служит для получения количества минут 
        self.entry_title_accept_minuts = customtkinter.CTkEntry(self,
            font = ('Arial', 23),
            width = 150, height = 40, corner_radius = 0, 
            justify = 'center', 
            validate = 'key',
            validatecommand = valid)
        
        self.entry_title_accept_minuts.place(x = 55, y = 100)
        self.entry_title_accept_minuts.insert(0, '0')

        # Кнопка на главном экране. служит для уменьшения количества минут поля ввода entry_title_accept_minuts
        self.button_title_minus_minut = customtkinter.CTkButton(self,
            font = ('Arial', 24),
            text = '-',
            width = 40, height = 40, corner_radius = 0,
            fg_color = '#346EBA', hover_color = '#3A5B87',
            command = minut_minus)
        
        self.button_title_minus_minut.place(x = 15, y = 100)

        # Кнопка на главном экране. служит для увелечения количества минут поля ввода entry_title_accept_minuts
        self.button_title_plus_minut = customtkinter.CTkButton(self,
            font = ('Arial', 24),
            text = '+', 
            width = 40, height = 40, corner_radius = 0,
            fg_color = '#346EBA', hover_color = '#3A5B87',
            command = minut_plus)
        
        self.button_title_plus_minut.place(x = 205, y = 100)

        # Лейбл на главном экране. служит для обозначния поля ввода entry_title_accept_minuts "минутами"
        self.label_title_designaton_minuts = customtkinter.CTkLabel(self,
            font = ('Arial', 20),
            text = 'Минуты:',
            fg_color = '#2E2E2E')
        
        self.label_title_designaton_minuts.place(x = 92, y = 72)

        # Лейбл на главном экране. служит для обозначения единицы времени таймера "часами"
        self.label_title_unit_time_hours = customtkinter.CTkLabel(self,
            font = ('Arial', 18),
            text = 'H')
        
        self.label_title_unit_time_hours.place(x = 435, y = 119)

        # Лейбл на главном экране. служит для обозначения единицы времени таймера "минутами"
        self.label_title_unit_time_minuts = customtkinter.CTkLabel(self,
            font = ('Arial', 18),
            text = 'M')
        
        self.label_title_unit_time_minuts.place(x = 435, y = 254)

        # Лейбл на главном экране. Служит для ориентировки пользователя во времени, то есть дает понимает того, сколько времени осталос до дейтсвия
        self.label_title_time_out_through = customtkinter.CTkLabel(self,
            font = ('Arial', 15), 
            text = 'Время закончится через:')
        
        self.label_title_time_out_through.place(x = 272, y = 0)

        # Поле ввода под главным экраном. служит для ориентировки во времени функции function_stop_time, то есть нужна для оставновки и возобновлении времени в нужной точке
        self.entry_under_title_for_function_stop_time_hours = customtkinter.CTkEntry(self, width = 50)
        self.entry_under_title_for_function_stop_time_hours.place(x = 10, y = 450)

        # Поле ввода под главным экраном. служит для ориентировки во времени функции function_stop_time, то есть нужна для оставновки и возобновлении времени в нужной точке
        self.entry_under_title_for_function_stop_time_minuts = customtkinter.CTkEntry(self, width = 50)
        self.entry_under_title_for_function_stop_time_minuts.place(x = 10, y = 485)

        # Лейбл под главным экраном. служит для определения поля ввода с единицей времени "часы"
        self.label_for_designation_hours_entry_under_title = customtkinter.CTkLabel(self, text = 'Hours', font = ('Arial', 16))
        self.label_for_designation_hours_entry_under_title.place(x = 70, y = 450)

        # Лейбл под главным экраном. служит для определения поля ввода с единицой времени "минуты"
        self.label_for_designation_minuts_entry_under_title = customtkinter.CTkLabel(self, text = 'Minuts', font = ('Arial', 16))
        self.label_for_designation_minuts_entry_under_title.place(x = 70, y = 485)


        # голубой:    #346EBA  #3A5B87  #283F5E
        # красный:    #FF4242  #B04C4C  #723131
        # зеленый:    #52D163  #4E9158  #315A37
        # оранжевый:  #DB9960  #8F623C  #61432A
        # фиолетовый: #5B3982  #9250DE  #462B64

        # fg_color - отображаемый цвет
        # hover_color - цвет при наведении
        if self.open_file_optionmenu_mode_color_ui == 'Голубой':

            self.checkbox_settings_mode_auto_hibernation.configure(fg_color = '#346EBA', hover_color = '#3A5B87')

            self.button_title_delay_time.configure(fg_color = '#346EBA', hover_color = '#3A5B87')

            self.button_title_clear_time.configure(fg_color = '#346EBA', hover_color = '#3A5B87')

            self.frame_settins_background_under_button_settings.configure(fg_color = '#283F5E')

            self.button_title_start_time.configure(fg_color = '#346EBA', hover_color = '#3A5B87')

            self.button_title_stop_time.configure(fg_color = '#346EBA', hover_color = '#3A5B87')

            self.button_title_minus_hour.configure(fg_color = '#346EBA', hover_color = '#3A5B87')

            self.button_title_plus_hour.configure(fg_color = '#346EBA', hover_color = '#3A5B87')

            self.button_title_minus_minut.configure(fg_color = '#346EBA', hover_color = '#3A5B87')

            self.button_title_plus_minut.configure(fg_color = '#346EBA', hover_color = '#3A5B87')

            self.button_settings_open_page_settings.configure(fg_color = '#346EBA', hover_color = '#3A5B87')

            self.button_settings_shut_page_settings.configure(fg_color = '#346EBA', hover_color = '#3A5B87')

            self.button_settings_save_settings.configure(fg_color = '#346EBA', hover_color = '#3A5B87')

            self.optionmenu_settings_mode_themes_ui.configure(fg_color = '#346EBA', button_color = '#346EBA', button_hover_color = '#3A5B87')

            self.optionmenu_settings_mode_color_ui.configure(fg_color = '#346EBA', button_color = '#346EBA', button_hover_color = '#3A5B87')

            self.optionmenu_settings_mode_countdown_time.configure(fg_color = '#346EBA', button_color = '#346EBA', button_hover_color = '#3A5B87')

            self.optionmenu_settings_mode_act_after_time.configure(fg_color = '#346EBA', button_color = '#346EBA', button_hover_color = '#3A5B87')            


        elif self.open_file_optionmenu_mode_color_ui == 'Красный':

            self.checkbox_settings_mode_auto_hibernation.configure(fg_color = '#D65656', hover_color = '#B04C4C')

            self.button_title_delay_time.configure(fg_color = '#D65656', hover_color = '#B04C4C')

            self.button_title_clear_time.configure(fg_color = '#D65656', hover_color = '#B04C4C')

            self.frame_settins_background_under_button_settings.configure(fg_color = '#723131')

            self.button_title_start_time.configure(fg_color = '#D65656', hover_color = '#B04C4C')

            self.button_title_stop_time.configure(fg_color = '#D65656', hover_color = '#B04C4C')

            self.button_title_minus_hour.configure(fg_color = '#D65656', hover_color = '#B04C4C')

            self.button_title_plus_hour.configure(fg_color = '#D65656', hover_color = '#B04C4C')

            self.button_title_minus_minut.configure(fg_color = '#D65656', hover_color = '#B04C4C')

            self.button_title_plus_minut.configure(fg_color = '#D65656', hover_color = '#B04C4C')

            self.button_settings_open_page_settings.configure(fg_color = '#D65656', hover_color = '#B04C4C')

            self.button_settings_shut_page_settings.configure(fg_color = '#D65656', hover_color = '#B04C4C')

            self.button_settings_save_settings.configure(fg_color = '#D65656', hover_color = '#B04C4C')

            self.optionmenu_settings_mode_themes_ui.configure(fg_color = '#D65656', button_color = '#D65656', button_hover_color = '#B04C4C')

            self.optionmenu_settings_mode_color_ui.configure(fg_color = '#D65656', button_color = '#D65656', button_hover_color = '#B04C4C')

            self.optionmenu_settings_mode_countdown_time.configure(fg_color = '#D65656', button_color = '#D65656', button_hover_color = '#B04C4C')

            self.optionmenu_settings_mode_act_after_time.configure(fg_color = '#D65656', button_color = '#D65656', button_hover_color = '#B04C4C')


        elif self.open_file_optionmenu_mode_color_ui == 'Зеленый':

            self.checkbox_settings_mode_auto_hibernation.configure(fg_color = '#41904B', hover_color = '#407347')

            self.button_title_delay_time.configure(fg_color = '#41904B', hover_color = '#407347')

            self.button_title_clear_time.configure(fg_color = '#41904B', hover_color = '#407347')

            self.frame_settins_background_under_button_settings.configure(fg_color = '#315A37')

            self.button_title_start_time.configure(fg_color = '#41904B', hover_color = '#407347')

            self.button_title_stop_time.configure(fg_color = '#41904B', hover_color = '#407347')

            self.button_title_minus_hour.configure(fg_color = '#41904B', hover_color = '#407347')

            self.button_title_plus_hour.configure(fg_color = '#41904B', hover_color = '#407347')

            self.button_title_minus_minut.configure(fg_color = '#41904B', hover_color = '#407347')

            self.button_title_plus_minut.configure(fg_color = '#41904B', hover_color = '#407347')

            self.button_settings_open_page_settings.configure(fg_color = '#41904B', hover_color = '#407347')

            self.button_settings_shut_page_settings.configure(fg_color = '#41904B', hover_color = '#407347')

            self.button_settings_save_settings.configure(fg_color = '#41904B', hover_color = '#407347')

            self.optionmenu_settings_mode_themes_ui.configure(fg_color = '#41904B', button_color = '#41904B', button_hover_color = '#407347')

            self.optionmenu_settings_mode_color_ui.configure(fg_color = '#41904B', button_color = '#41904B', button_hover_color = '#407347')

            self.optionmenu_settings_mode_countdown_time.configure(fg_color = '#41904B', button_color = '#41904B', button_hover_color = '#407347')

            self.optionmenu_settings_mode_act_after_time.configure(fg_color = '#41904B', button_color = '#41904B', button_hover_color = '#407347')
                
 
        elif self.open_file_optionmenu_mode_color_ui == 'Оранжевый':

            self.checkbox_settings_mode_auto_hibernation.configure(fg_color = '#C4834D', hover_color = '#8F623C')

            self.button_title_delay_time.configure(fg_color = '#C4834D', hover_color = '#8F623C')

            self.button_title_clear_time.configure(fg_color = '#C4834D', hover_color = '#8F623C')

            self.frame_settins_background_under_button_settings.configure(fg_color = '#61432A')

            self.button_title_start_time.configure(fg_color = '#C4834D', hover_color = '#8F623C')

            self.button_title_stop_time.configure(fg_color = '#C4834D', hover_color = '#8F623C')

            self.button_title_minus_hour.configure(fg_color = '#C4834D', hover_color = '#8F623C')

            self.button_title_plus_hour.configure(fg_color = '#C4834D', hover_color = '#8F623C')

            self.button_title_minus_minut.configure(fg_color = '#C4834D', hover_color = '#8F623C')

            self.button_title_plus_minut.configure(fg_color = '#C4834D', hover_color = '#8F623C')
            
            self.button_settings_open_page_settings.configure(fg_color = '#C4834D', hover_color = '#8F623C')

            self.button_settings_shut_page_settings.configure(fg_color = '#C4834D', hover_color = '#8F623C')

            self.button_settings_save_settings.configure(fg_color = '#C4834D', hover_color = '#8F623C')

            self.optionmenu_settings_mode_themes_ui.configure(fg_color = '#C4834D', button_color = '#C4834D', button_hover_color = '#8F623C')

            self.optionmenu_settings_mode_color_ui.configure(fg_color = '#C4834D', button_color = '#C4834D', button_hover_color = '#8F623C')

            self.optionmenu_settings_mode_countdown_time.configure(fg_color = '#C4834D', button_color = '#C4834D', button_hover_color = '#8F623C')

            self.optionmenu_settings_mode_act_after_time.configure(fg_color = '#C4834D', button_color = '#C4834D', button_hover_color = '#8F623C')
                

        elif self.open_file_optionmenu_mode_color_ui == 'Фиолетовый':

            self.checkbox_settings_mode_auto_hibernation.configure(fg_color = '#9250DE', hover_color = '#5B3982')

            self.button_title_delay_time.configure(fg_color = '#9250DE', hover_color = '#5B3982')

            self.button_title_clear_time.configure(fg_color = '#9250DE', hover_color = '#5B3982')

            self.frame_settins_background_under_button_settings.configure(fg_color = '#462B64')

            self.button_title_start_time.configure(fg_color = '#9250DE', hover_color = '#5B3982')

            self.button_title_stop_time.configure(fg_color = '#9250DE', hover_color = '#5B3982')

            self.button_title_minus_hour.configure(fg_color = '#9250DE', hover_color = '#5B3982')

            self.button_title_plus_hour.configure(fg_color = '#9250DE', hover_color = '#5B3982')

            self.button_title_minus_minut.configure(fg_color = '#9250DE', hover_color = '#5B3982')

            self.button_title_plus_minut.configure(fg_color = '#9250DE',hover_color = '#5B3982')

            self.button_settings_open_page_settings.configure(fg_color = '#9250DE',hover_color = '#5B3982')

            self.button_settings_shut_page_settings.configure(fg_color = '#9250DE',hover_color = '#5B3982')

            self.button_settings_save_settings.configure(fg_color = '#9250DE',hover_color = '#5B3982')

            self.optionmenu_settings_mode_themes_ui.configure(fg_color = '#9250DE', button_color = '#9250DE', button_hover_color = '#5B3982')

            self.optionmenu_settings_mode_color_ui.configure(fg_color = '#9250DE', button_color = '#9250DE', button_hover_color = '#5B3982')

            self.optionmenu_settings_mode_countdown_time.configure(fg_color = '#9250DE', button_color = '#9250DE', button_hover_color = '#5B3982')

            self.optionmenu_settings_mode_act_after_time.configure(fg_color = '#9250DE', button_color = '#9250DE', button_hover_color = '#5B3982')


        if self.open_file_optionmenu_mode_themes_ui == 'Т':
            customtkinter.set_appearance_mode('Dark')

            self.frame_title_background_left_side.configure(fg_color = '#2E2E2E')
            self.frame_title_background_delay.configure(fg_color = '#2E2E2E')
            self.frame_settings_background_under_button_settings.configure(fg_color = '#2E2E2E')
            self.frame_settings_background_left_side.configure(fg_color = '#2E2E2E')
            self.frame_settings_background_right_side.configure(fg_color = '#2E2E2E')

            self.label_title_designation_hours.configure(fg_color = '#2E2E2E')
            self.label_title_designaton_minuts.configure(fg_color = '#2E2E2E')


        elif self.open_file_optionmenu_mode_themes_ui == 'С':
            customtkinter.set_appearance_mode('Light')

            self.frame_title_background_delay.configure(fg_color = '#D6D6D6')
            self.frame_title_background_left_side.configure(fg_color = '#D6D6D6')
            self.frame_settings_background_under_button_settings.configure(fg_color = '#D6D6D6')
            self.frame_settings_background_left_side.configure(fg_color = '#D6D6D6')
            self.frame_settings_background_right_side.configure(fg_color = '#D6D6D6')

            self.label_title_designation_hours.configure(fg_color = '#D6D6D6')
            self.label_title_designaton_minuts.configure(fg_color = '#D6D6D6')
            

        if self.open_file_optionmenu_mode_countdown_time == 'М':

            self.label_title_designation_hours.configure(text = 'Часы:')
            self.label_title_designaton_minuts.configure(text = 'Минуты:')

            self.label_title_unit_time_hours.configure(text = 'H')
            self.label_title_unit_time_minuts.configure(text = 'M')

            self.label_title_designation_hours.place(x = 104, y = 2)
            self.label_title_designaton_minuts.place(x = 92, y = 72)

        elif self.open_file_optionmenu_mode_countdown_time == 'С':

            self.label_title_designation_hours.configure(text = 'Минуты:')
            self.label_title_designaton_minuts.configure(text = 'Секунды:')

            self.label_title_unit_time_hours.configure(text = 'M')
            self.label_title_unit_time_minuts.configure(text = 'S')

            self.label_title_designation_hours.place(x = 92, y = 2)
            self.label_title_designaton_minuts.place(x = 89, y = 72)


        if self.value_optionmenu_mode_countdown_time.get()[0] == 'М':
            self.value_for_countwond_times = 60000

        elif self.value_optionmenu_mode_countdown_time.get()[0] == 'С':
            self.value_for_countwond_times = 1000


        if self.value_optionmenu_mode_act_after_time.get()[0] == 'Г':
            self.command = 'shutdown /h'

        elif self.value_optionmenu_mode_act_after_time.get()[0] == 'О':
            self.command = 'shutdown /s /t 0'

        elif self.value_optionmenu_mode_act_after_time.get()[0] == 'П':
            self.command = 'shutdown /r /t 0'

        
        if self.open_file_checkbox_mode_auto_hibernation == 'n':
            self.value_checkbox_mode_auto_hibernation.set('on')
            self.function_auto_hibernation()

        elif self.open_file_checkbox_mode_auto_hibernation == 'f':
            self.value_checkbox_mode_auto_hibernation.set('off')


        self.amount_hours_out_of_entry = 0
        self.amount_minuts_out_of_entry = 0
        self.point_for_start_or_stop_times = False
        self.time_stop_counter = 1


    def start_monitoring(self):
        try:

            amount_the_time = int(self.entry_settings_auto_shutdown.get())

            if amount_the_time < 60:
                
                msbox.showwarning('Предупреждение', 'Минимальное время - 60 секунд')
                self.value_checkbox_mode_auto_hibernation.set('off')
                return
            
        except ValueError:

            msbox.showwarning('Ошибка', 'Введите число')
            self.value_checkbox_mode_auto_hibernation.set('off')
            return

        self.entry_settings_auto_shutdown.configure(state = 'disabled')

        if self.value_checkbox_mode_auto_hibernation.get() == 'on':

            self.giving_the_value_out_of_cpu = True
            self.amount_time_for_auto_shutdown = int(self.entry_settings_auto_shutdown.get())
            self.time_on_the_moment = 0
            self.cpu_check_start()

        else:
            self.stop_monitoring()


    def stop_monitoring(self):

        self.entry_settings_auto_shutdown.configure(state = 'normal')
        self.giving_the_value_out_of_cpu = False
        self.after_cancel(self.cpu_act)
        self.cpu_act = None


    def cpu_check_start(self):

        cpu_load = psutil.cpu_percent()

        if cpu_load < 15:

            self.time_on_the_moment += 1
            print(f'Cpu load: {cpu_load}% | {self.time_on_the_moment} seconds left')

            if self.time_on_the_moment == self.amount_time_for_auto_shutdown:

                self.giving_the_value_out_of_cpu = False
                self.cpu_act = None
                self.time_on_the_moment = 0
                self.shutdown()

        else:
            if self.time_on_the_moment > 0:
                self.time_on_the_moment = 0

        self.cpu_act = self.after(1000, self.cpu_check_start)


    def shutdown(self):
        os.system('shutdown /h')


    def function_auto_hibernation(self):

        if self.value_checkbox_mode_auto_hibernation.get() == 'on':
            print('Turn on the processor load check')
            self.start_monitoring()
        
        else:
            print('Disabling the processor load check')
            self.stop_monitoring()


# Функция для оставноки времени.Содержится 4 почти одинаковых блока кода,
# каждый из которых нужен для воизбеждания багов и проблем в целом в работе
# Например, отключаются кнопки интерфейса, когда время идет, 
# тк при взаимодействии с ними могут время может остановиться, перестать идти и
# и подобные проблемы. чтобы время продолжало идти после оставноки, использовалась
# функция function_count_time(), которая просто ведет счет времени на экране
    def function_stop_time(self):

        if self.value_optionmenu_mode_countdown_time.get() == 'Минутам':
            self.value_for_countwond_times = 60000
            
        elif self.value_optionmenu_mode_countdown_time.get() == 'Секундам':
            self.value_for_countwond_times = 1000


        if self.time_stop_counter % 2 == 1:


            self.time_stop_counter += 1
            self.point_for_start_or_stop_times = False

            self.button_title_stop_time.configure(text = 'Возобновить')
            self.button_title_plus_hour.configure(state = 'normal')
            self.button_title_minus_hour.configure(state = 'normal')
            self.button_title_plus_minut.configure(state = 'normal')
            self.button_title_minus_minut.configure(state = 'normal')
            self.button_title_clear_time.configure(state = 'normal')

            self.entry_title_accept_hours.configure(state = 'normal')
            self.entry_title_accept_minuts.configure(state = 'normal')

            self.checkbox_settings_mode_auto_hibernation.configure(state = 'normal')
            self.value_checkbox_mode_auto_hibernation.set('on')
            self.start_monitoring()

            self.optionmenu_settings_mode_countdown_time.configure(state = 'normal')


            hours_out_of_under_title = int(self.entry_under_title_for_function_stop_time_hours.get())
            minuts_out_of_under_title = int(self.entry_under_title_for_function_stop_time_minuts.get())

            got_the_hours_out_of_entry = int(self.entry_title_accept_hours.get())
            got_the_minuts_out_of_entry = int(self.entry_title_accept_minuts.get())


            if got_the_hours_out_of_entry != hours_out_of_under_title or got_the_minuts_out_of_entry != minuts_out_of_under_title:
                
                
                self.got_hours_in_minuts = got_the_hours_out_of_entry * 60
                self.got_minuts_in_minuts = got_the_minuts_out_of_entry
                
                self.summa_hours_and_minuts_for_convetison_in_minuts = self.got_hours_in_minuts + self.got_minuts_in_minuts

                self.entry_under_title_for_function_stop_time_hours.delete(0, 25)
                self.entry_under_title_for_function_stop_time_minuts.delete(0, 25)
                self.entry_under_title_for_function_stop_time_hours.insert(0, got_the_hours_out_of_entry)
                self.entry_under_title_for_function_stop_time_minuts.insert(0, got_the_minuts_out_of_entry)


                if self.point_for_start_or_stop_times:

                    if 0 < self.summa_hours_and_minuts_for_convetison_in_minuts < 6001:

                        self.summa_hours_and_minuts_for_convetison_in_minuts -= 1
                        
                        self.amount_hours_out_of_entry = str(self.summa_hours_and_minuts_for_convetison_in_minuts // 60)
                        self.amount_minuts_out_of_entry = str(self.summa_hours_and_minuts_for_convetison_in_minuts % 60)


                        if len(self.amount_hours_out_of_entry) == 1 and len(self.amount_minuts_out_of_entry) == 1:
                            self.label_title_count_time_hours.configure(text = f'0{self.amount_hours_out_of_entry}')
                            self.label_title_count_time_minuts.configure(text = f'0{self.amount_minuts_out_of_entry}')
                        
                        elif len(self.amount_hours_out_of_entry) == 1 and len(self.amount_minuts_out_of_entry) != 1:
                            self.label_title_count_time_hours.configure(text = f'0{self.amount_hours_out_of_entry}')
                            self.label_title_count_time_minuts.configure(text = self.amount_minuts_out_of_entry)
                        
                        elif len(self.amount_hours_out_of_entry) != 1 and len(self.amount_minuts_out_of_entry) == 1:
                            self.label_title_count_time_hours.configure(text = self.amount_hours_out_of_entry)
                            self.label_title_count_time_minuts.configure(text = f'0{self.amount_minuts_out_of_entry}')
                        
                        else:
                            self.label_title_count_time_hours.configure(text = self.amount_hours_out_of_entry)
                            self.label_title_count_time_minuts.configure(text = self.amount_minuts_out_of_entry)
                        
                        self.after(self.value_for_countwond_times, self.function_count_time)


                    elif self.summa_hours_and_minuts_for_convetison_in_minuts >= 6001:

                        self.point_for_start_or_stop_times = False
                        self.entry_title_accept_hours.delete(0, 25)
                        self.entry_title_accept_minuts.delete(0 ,25)
                        self.entry_title_accept_hours.insert(0, 0)
                        self.entry_title_accept_minuts.insert(0, 0)
                        self.label_title_count_time_hours.configure(text = '00')
                        self.label_title_count_time_minuts.configure(text = '00')
                        
                        print('1) The input field "entry_title_accept_hours" and "entry_title_accept_minuts" is button_title_clear_timeed')


            elif got_the_hours_out_of_entry == hours_out_of_under_title or got_the_minuts_out_of_entry == minuts_out_of_under_title:

                self.entry_under_title_for_function_stop_time_hours.delete(0, 25)
                self.entry_under_title_for_function_stop_time_minuts.delete(0, 25)
                self.entry_under_title_for_function_stop_time_hours.insert(0, got_the_hours_out_of_entry)
                self.entry_under_title_for_function_stop_time_minuts.insert(0, got_the_minuts_out_of_entry)


                if self.point_for_start_or_stop_times:
                    
                    if 0 < self.summa_hours_and_minuts_for_convetison_in_minuts < 6001:

                        self.summa_hours_and_minuts_for_convetison_in_minuts -= 1
                        
                        self.amount_hours_out_of_entry = str(self.summa_hours_and_minuts_for_convetison_in_minuts // 60)
                        self.amount_minuts_out_of_entry = str(self.summa_hours_and_minuts_for_convetison_in_minuts % 60)


                        if len(self.amount_hours_out_of_entry) == 1 and len(self.amount_minuts_out_of_entry) == 1:
                            self.label_title_count_time_hours.configure(text = f'0{self.amount_hours_out_of_entry}')
                            self.label_title_count_time_minuts.configure(text = f'0{self.amount_minuts_out_of_entry}')
                        
                        elif len(self.amount_hours_out_of_entry) == 1 and len(self.amount_minuts_out_of_entry) != 1:
                            self.label_title_count_time_hours.configure(text = f'0{self.amount_hours_out_of_entry}')
                            self.label_title_count_time_minuts.configure(text = self.amount_minuts_out_of_entry)
                        
                        elif len(self.amount_hours_out_of_entry) != 1 and len(self.amount_minuts_out_of_entry) == 1:
                            self.label_title_count_time_hours.configure(text = self.amount_hours_out_of_entry)
                            self.label_title_count_time_minuts.configure(text = f'0{self.amount_minuts_out_of_entry}')
                        
                        else:
                            self.label_title_count_time_hours.configure(text = self.amount_hours_out_of_entry)
                            self.label_title_count_time_minuts.configure(text = self.amount_minuts_out_of_entry)
                        
                        self.after(self.value_for_countwond_times, self.function_count_time)

                    elif self.summa_hours_and_minuts_for_convetison_in_minuts >= 6001:

                        self.point_for_start_or_stop_times = False
                        self.entry_title_accept_hours.delete(0, 25)
                        self.entry_title_accept_minuts.delete(0 ,25)
                        self.entry_title_accept_hours.insert(0, 0)
                        self.entry_title_accept_minuts.insert(0, 0)
                        self.label_title_count_time_hours.configure(text = '00')
                        self.label_title_count_time_minuts.configure(text = '00')
                        
                        print('2) The input field "entry_title_accept_hours" and "entry_title_accept_minuts" is button_title_clear_timeed')


        elif self.time_stop_counter % 2 == 0:

            self.time_stop_counter -= 1
            self.point_for_start_or_stop_times = True


            if self.value_checkbox_mode_auto_hibernation.get() == 'on':
                self.stop_monitoring()
                self.value_checkbox_mode_auto_hibernation.set('off')
            
            else:
                pass

            self.button_title_stop_time.configure(text = 'Остановить')
            self.button_title_plus_hour.configure(state = 'disabled')
            self.button_title_minus_hour.configure(state = 'disabled')
            self.button_title_plus_minut.configure(state = 'disabled')
            self.button_title_minus_minut.configure(state = 'disabled')
            self.button_title_clear_time.configure(state = 'disabled')
            self.button_title_delay_time.configure(state = 'normal')

            self.checkbox_settings_mode_auto_hibernation.configure(state = 'disabled')
            
            self.optionmenu_settings_mode_countdown_time.configure(state = 'disabled')
            

            hours_out_of_under_title = int(self.entry_under_title_for_function_stop_time_hours.get())
            minuts_out_of_under_title = int(self.entry_under_title_for_function_stop_time_minuts.get())

            got_the_hours_out_of_entry = int(self.entry_title_accept_hours.get())
            got_the_minuts_out_of_entry = int(self.entry_title_accept_minuts.get())


            if got_the_hours_out_of_entry != hours_out_of_under_title or got_the_minuts_out_of_entry != minuts_out_of_under_title:


                self.got_hours_in_minuts = got_the_hours_out_of_entry * 60
                self.got_minuts_in_minuts = got_the_minuts_out_of_entry
                
                self.summa_hours_and_minuts_for_convetison_in_minuts = self.got_hours_in_minuts + self.got_minuts_in_minuts

                self.entry_under_title_for_function_stop_time_hours.delete(0, 25)
                self.entry_under_title_for_function_stop_time_minuts.delete(0, 25)
                self.entry_under_title_for_function_stop_time_hours.insert(0, got_the_hours_out_of_entry)
                self.entry_under_title_for_function_stop_time_minuts.insert(0, got_the_minuts_out_of_entry)


                if self.point_for_start_or_stop_times:

                    if 0 < self.summa_hours_and_minuts_for_convetison_in_minuts < 6001:

                        self.summa_hours_and_minuts_for_convetison_in_minuts -= 1
                        
                        self.amount_hours_out_of_entry = str(self.summa_hours_and_minuts_for_convetison_in_minuts // 60)
                        self.amount_minuts_out_of_entry = str(self.summa_hours_and_minuts_for_convetison_in_minuts % 60)


                        if len(self.amount_hours_out_of_entry) == 1 and len(self.amount_minuts_out_of_entry) == 1:
                            self.label_title_count_time_hours.configure(text = f'0{self.amount_hours_out_of_entry}')
                            self.label_title_count_time_minuts.configure(text = f'0{self.amount_minuts_out_of_entry}')
                        
                        elif len(self.amount_hours_out_of_entry) == 1 and len(self.amount_minuts_out_of_entry) != 1:
                            self.label_title_count_time_hours.configure(text = f'0{self.amount_hours_out_of_entry}')
                            self.label_title_count_time_minuts.configure(text = self.amount_minuts_out_of_entry)
                        
                        elif len(self.amount_hours_out_of_entry) != 1 and len(self.amount_minuts_out_of_entry) == 1:
                            self.label_title_count_time_hours.configure(text = self.amount_hours_out_of_entry)
                            self.label_title_count_time_minuts.configure(text = f'0{self.amount_minuts_out_of_entry}')
                        
                        else:
                            self.label_title_count_time_hours.configure(text = self.amount_hours_out_of_entry)
                            self.label_title_count_time_minuts.configure(text = self.amount_minuts_out_of_entry)
                        
                        self.after(self.value_for_countwond_times, self.function_count_time)

                    elif self.summa_hours_and_minuts_for_convetison_in_minuts >= 6001:

                        self.point_for_start_or_stop_times = True
                        
                        self.button_title_stop_time.configure(text = 'Возобновить')
                        self.button_title_plus_hour.configure(state = 'normal')
                        self.button_title_minus_hour.configure(state = 'normal')
                        self.button_title_plus_minut.configure(state = 'normal')
                        self.button_title_minus_minut.configure(state = 'normal')
                        self.button_title_delay_time.configure(state = 'disabled')
                        
                        self.entry_title_accept_hours.configure(state = 'normal')
                        self.entry_title_accept_minuts.configure(state = 'normal')
                        
                        self.checkbox_settings_mode_auto_hibernation.configure(state = 'normal')
                        
                        self.optionmenu_settings_mode_countdown_time.configure(state = 'normal')
                        
                        self.label_title_count_time_hours.configure(text = '00')
                        self.label_title_count_time_minuts.configure(text = '00')
                        
                        self.entry_title_accept_hours.delete(0, 25)
                        self.entry_title_accept_minuts.delete(0 ,25)
                        self.entry_title_accept_hours.insert(0, 0)
                        self.entry_title_accept_minuts.insert(0, 0)
                        
                        print('3) The input field "entry_title_accept_hours" and "entry_title_accept_minuts" is button_title_clear_timeed')


                    if self.value_optionmenu_mode_countdown_time.get() == 'Минутам':
                        
                        if self.summa_hours_and_minuts_for_convetison_in_minuts == 30:
                            msbox.showinfo('Оповещение', 'Осталось 30 минут!')

                        elif self.summa_hours_and_minuts_for_convetison_in_minuts == 10:
                            msbox.showinfo('Оповещение', 'Осталось 10 минут!')
                            
                        elif self.summa_hours_and_minuts_for_convetison_in_minuts == 5:
                            msbox.showinfo('Оповещение', 'Осталось 5 минут!')

                        elif self.summa_hours_and_minuts_for_convetison_in_minuts == 1:
                            msbox.showinfo('Оповещение', 'Осталось 1 минута!')

                    elif self.value_optionmenu_mode_countdown_time.get() == 'Секундам':
                        
                        if self.summa_hours_and_minuts_for_convetison_in_minuts == 60:
                            msbox.showinfo('Оповещение', 'Осталась 1 минута!')

                        elif self.summa_hours_and_minuts_for_convetison_in_minuts == 30:
                            msbox.showinfo('Оповещение', 'Осталось 30 секунд!')

                        elif self.summa_hours_and_minuts_for_convetison_in_minuts == 10:
                            msbox.showinfo('Оповещение', 'Осталось 10 секунд!')
                            
                        elif self.summa_hours_and_minuts_for_convetison_in_minuts == 5:
                            msbox.showinfo('Оповещение', 'Осталось 5 секунд!')


            elif got_the_hours_out_of_entry == hours_out_of_under_title or got_the_minuts_out_of_entry == minuts_out_of_under_title:

                self.entry_under_title_for_function_stop_time_hours.delete(0, 25)
                self.entry_under_title_for_function_stop_time_minuts.delete(0, 25)
                self.entry_under_title_for_function_stop_time_hours.insert(0, got_the_hours_out_of_entry)
                self.entry_under_title_for_function_stop_time_minuts.insert(0, got_the_minuts_out_of_entry)


                if self.point_for_start_or_stop_times:
                    
                    if 0 < self.summa_hours_and_minuts_for_convetison_in_minuts < 6001:
                        
                        self.summa_hours_and_minuts_for_convetison_in_minuts -= 1
                        
                        self.amount_hours_out_of_entry = str(self.summa_hours_and_minuts_for_convetison_in_minuts // 60)
                        self.amount_minuts_out_of_entry = str(self.summa_hours_and_minuts_for_convetison_in_minuts % 60)


                        if len(self.amount_hours_out_of_entry) == 1 and len(self.amount_minuts_out_of_entry) == 1:
                            self.label_title_count_time_hours.configure(text = f'0{self.amount_hours_out_of_entry}')
                            self.label_title_count_time_minuts.configure(text = f'0{self.amount_minuts_out_of_entry}')
                        elif len(self.amount_hours_out_of_entry) == 1 and len(self.amount_minuts_out_of_entry) != 1:
                            self.label_title_count_time_hours.configure(text = f'0{self.amount_hours_out_of_entry}')
                            self.label_title_count_time_minuts.configure(text = self.amount_minuts_out_of_entry)
                        elif len(self.amount_hours_out_of_entry) != 1 and len(self.amount_minuts_out_of_entry) == 1:
                            self.label_title_count_time_hours.configure(text = self.amount_hours_out_of_entry)
                            self.label_title_count_time_minuts.configure(text = f'0{self.amount_minuts_out_of_entry}')
                        else:
                            self.label_title_count_time_hours.configure(text = self.amount_hours_out_of_entry)
                            self.label_title_count_time_minuts.configure(text = self.amount_minuts_out_of_entry)
                            
                        self.after(self.value_for_countwond_times, self.function_count_time)


                    elif self.summa_hours_and_minuts_for_convetison_in_minuts >= 6001:
                        
                        self.point_for_start_or_stop_times = True
                        
                        self.button_title_stop_time.configure(text = 'Возобновить')
                        self.button_title_plus_hour.configure(state = 'normal')
                        self.button_title_minus_hour.configure(state = 'normal')
                        self.button_title_plus_minut.configure(state = 'normal')
                        self.button_title_minus_minut.configure(state = 'normal')
                        self.button_title_delay_time.configure(state = 'disabled')
                        
                        self.entry_title_accept_hours.configure(state = 'normal')
                        self.entry_title_accept_minuts.configure(state = 'normal')
                        
                        self.checkbox_settings_mode_auto_hibernation.configure(state = 'normal')
                        
                        self.optionmenu_settings_mode_countdown_time.configure(state = 'normal')
                        
                        self.label_title_count_time_hours.configure(text = '00')
                        self.label_title_count_time_minuts.configure(text = '00')
                        
                        self.entry_title_accept_hours.delete(0, 25)
                        self.entry_title_accept_minuts.delete(0 ,25)
                        self.entry_title_accept_hours.insert(0, 0)
                        self.entry_title_accept_minuts.insert(0, 0)
                        
                        print('4) The input field "entry_title_accept_hours" and "entry_title_accept_minuts" is button_title_clear_timeed')



                    if self.value_optionmenu_mode_countdown_time.get() == 'Минутам':
                        
                        if self.summa_hours_and_minuts_for_convetison_in_minuts == 30:
                            msbox.showinfo('Оповещение', 'Осталось 30 минут!')

                        elif self.summa_hours_and_minuts_for_convetison_in_minuts == 10:
                            msbox.showinfo('Оповещение', 'Осталось 10 минут!')
                            
                        elif self.summa_hours_and_minuts_for_convetison_in_minuts == 5:
                            msbox.showinfo('Оповещение', 'Осталось 5 минут!')

                        elif self.summa_hours_and_minuts_for_convetison_in_minuts == 1:
                            msbox.showinfo('Оповещение', 'Осталось 1 минута!')

                    elif self.value_optionmenu_mode_countdown_time.get() == 'Секундам':
                        
                        if self.summa_hours_and_minuts_for_convetison_in_minuts == 60:
                            msbox.showinfo('Оповещение', 'Осталась 1 минута!')

                        elif self.summa_hours_and_minuts_for_convetison_in_minuts == 30:
                            msbox.showinfo('Оповещение', 'Осталось 30 секунд!')

                        elif self.summa_hours_and_minuts_for_convetison_in_minuts == 10:
                            msbox.showinfo('Оповещение', 'Осталось 10 секунд!')
                            
                        elif self.summa_hours_and_minuts_for_convetison_in_minuts == 5:
                            msbox.showinfo('Оповещение', 'Осталось 5 секунд!')


# Разбей функцию function_stop_time() на несколько других функций для более широкой настройки


# Функция служит для передачи времени из полей ввода Часов и Минут, также 
# требуется для отключений виджетов интерфейса для воизбежания багов
# Функция принимает на вход часы и минуты, переводит в минуты и дальше 
# используется для подсчета времени до окончания работы программы
    def function_start_time(self):
        
        amount_times_for_start = int(self.entry_title_accept_hours.get()) + int(self.entry_title_accept_minuts.get())

        if not self.point_for_start_or_stop_times:
            
            if 0 < amount_times_for_start < 6001:
                
                

                if self.value_checkbox_mode_auto_hibernation.get() == 'on':
                    self.stop_monitoring()
                    self.value_checkbox_mode_auto_hibernation.set('off')
                    
                elif self.value_checkbox_mode_auto_hibernation.get() == 'off':
                    pass

                self.button_title_start_time.configure(state = 'disabled')
                self.button_title_stop_time.configure(state = 'normal')
                self.button_title_delay_time.configure(state = 'normal')
                self.button_title_plus_hour.configure(state = 'disabled')
                self.button_title_minus_hour.configure(state = 'disabled')
                self.button_title_plus_minut.configure(state = 'disabled')
                self.button_title_minus_minut.configure(state = 'disabled')

                self.checkbox_settings_mode_auto_hibernation.configure(state = 'disabled')

                self.optionmenu_settings_mode_countdown_time.configure(state = 'disabled')

                self.entry_under_title_for_function_stop_time_hours.delete(0, 25)
                self.entry_under_title_for_function_stop_time_minuts.delete(0, 25)
                self.entry_under_title_for_function_stop_time_hours.insert(0, self.entry_title_accept_hours.get())
                self.entry_under_title_for_function_stop_time_minuts.insert(0, self.entry_title_accept_minuts.get())

                try:
                    
                    self.summa_the_time_fnc_start_time = (int(self.entry_title_accept_hours.get()) * 60) + int(self.entry_title_accept_minuts.get())
                    
                    if self.summa_the_time_fnc_start_time > 0:
                        
                        self.summa_hours_and_minuts_for_convetison_in_minuts = self.summa_the_time_fnc_start_time
                        self.point_for_start_or_stop_times = True
                        self.function_count_time()
                        
                except ValueError:
                    
                    print('Error')
                    self.entry_title_accept_hours.delete(0, 25)
                    self.entry_title_accept_minuts.delete(0 ,25)
                    self.entry_title_accept_hours.insert(0, 0)
                    self.entry_title_accept_minuts.insert(0, 0)
                    self.entry_title_accept_hours.configure(state = 'disabled')
                    self.entry_title_accept_minuts.configure(state = 'disabled')
            
            elif amount_times_for_start < 0 or amount_times_for_start > 6001:
                
                self.button_title_stop_time.configure(text = 'Возобновить')
                
                
                
                
                self.point_for_start_or_stop_times = False
                self.button_title_delay_time.configure(state = 'disabled')
                
                self.checkbox_settings_mode_auto_hibernation.configure(state = 'normal')

                self.optionmenu_settings_mode_countdown_time.configure(state = 'normal')

                self.entry_title_accept_hours.delete(0, 25)
                self.entry_title_accept_minuts.delete(0 ,25)
                self.entry_title_accept_hours.insert(0, 0)
                self.entry_title_accept_minuts.insert(0, 0)
                self.label_title_count_time_hours.configure(text = '00')
                self.label_title_count_time_minuts.configure(text = '00')
                
                print('fnc start time) The input field "entry_title_accept_hours" and "entry_title_accept_minuts" is button_title_clear_timeed')

        else:
            print(f'fnc start time:  {self.point_for_start_or_stop_times}')


# принимает сумму часов и минут в минутах, отображает на экране
# далее отправляет отдельными окнами уведомления об окончании времени
# и завершает работу компьютера
    def function_count_time(self):
        
            if self.point_for_start_or_stop_times:
                
                if 0 < self.summa_hours_and_minuts_for_convetison_in_minuts < 6001:
                    
                    self.summa_hours_and_minuts_for_convetison_in_minuts -= 1
                    
                    self.amount_hours_out_of_entry = str(self.summa_hours_and_minuts_for_convetison_in_minuts // 60)
                    self.amount_minuts_out_of_entry = str(self.summa_hours_and_minuts_for_convetison_in_minuts % 60)


                    if len(self.amount_hours_out_of_entry) == 1 and len(self.amount_minuts_out_of_entry) == 1:
                        self.label_title_count_time_hours.configure(text = f'0{self.amount_hours_out_of_entry}')
                        self.label_title_count_time_minuts.configure(text = f'0{self.amount_minuts_out_of_entry}')
                        
                    elif len(self.amount_hours_out_of_entry) == 1 and len(self.amount_minuts_out_of_entry) != 1:
                        self.label_title_count_time_hours.configure(text = f'0{self.amount_hours_out_of_entry}')
                        self.label_title_count_time_minuts.configure(text = self.amount_minuts_out_of_entry)
                        
                    elif len(self.amount_hours_out_of_entry) != 1 and len(self.amount_minuts_out_of_entry) == 1:
                        self.label_title_count_time_hours.configure(text = self.amount_hours_out_of_entry)
                        self.label_title_count_time_minuts.configure(text = f'0{self.amount_minuts_out_of_entry}')
                        
                    else:
                        self.label_title_count_time_hours.configure(text = self.amount_hours_out_of_entry)
                        self.label_title_count_time_minuts.configure(text = self.amount_minuts_out_of_entry)
                        
                    self.after(self.value_for_countwond_times, self.function_count_time)
            

                elif 0 > self.summa_hours_and_minuts_for_convetison_in_minuts or self.summa_hours_and_minuts_for_convetison_in_minuts > 6000:
                    
                    self.point_for_start_or_stop_times = False
                    
                    self.button_title_stop_time.configure(text = 'Возобновить')
                    self.button_title_plus_hour.configure(state = 'normal')
                    self.button_title_minus_hour.configure(state = 'normal')
                    self.button_title_plus_minut.configure(state = 'normal')
                    self.button_title_minus_minut.configure(state = 'normal')
                    self.button_title_delay_time.configure(state = 'disabled')
                    
                    self.entry_title_accept_hours.configure(state = 'normal')
                    self.entry_title_accept_minuts.configure(state = 'normal')
                    
                    self.checkbox_settings_mode_auto_hibernation.configure(state = 'normal')
                    
                    self.optionmenu_settings_mode_countdown_time.configure(state = 'normal')
                    
                    self.entry_title_accept_hours.delete(0, 25)
                    self.entry_title_accept_minuts.delete(0 ,25)
                    self.entry_title_accept_hours.insert(0, 0)
                    self.entry_title_accept_minuts.insert(0, 0)
                    self.label_title_count_time_hours.configure(text = '00')
                    self.label_title_count_time_minuts.configure(text = '00')
                    
                    print('function_count_time) The input field "entry_title_accept_hours" and "entry_title_accept_minuts" is button_title_clear_timeed')


                else:
                    
                    self.point_for_start_or_stop_times = False
                    self.button_title_delay_time.configure(state = 'disabled')
                    self.optionmenu_settings_mode_countdown_time.configure(state = 'normal')
                    self.function_stop_time()
                    
                    if sys.platform == 'win32':
                        
                        if self.value_optionmenu_mode_act_after_time.get()[0] == 'Г':
                            print('Гибернация')
                            self.command = 'shutdown /h'
                            
                        elif self.value_optionmenu_mode_act_after_time.get()[0] == 'О':
                            print('Отключение')
                            self.command = 'shutdown /s /t 0'
                            
                        elif self.value_optionmenu_mode_act_after_time.get()[0] == 'П':
                            print('Перезагрузка')
                            self.command = 'shutdown /r /t 0'
                            
                    try:
                        os.system(self.command)
                        
                    except Exception as e:
                        print(f'Error: {e}')

                if self.value_optionmenu_mode_countdown_time.get() == 'Минутам':
                    
                    if self.summa_hours_and_minuts_for_convetison_in_minuts == 30:
                        msbox.showinfo('Оповещение', 'Осталось 30 минут!')

                    elif self.summa_hours_and_minuts_for_convetison_in_minuts == 10:
                        msbox.showinfo('Оповещение', 'Осталось 10 минут!')
                        
                    elif self.summa_hours_and_minuts_for_convetison_in_minuts == 5:
                        msbox.showinfo('Оповещение', 'Осталось 5 минут!')

                    elif self.summa_hours_and_minuts_for_convetison_in_minuts == 1:
                        msbox.showinfo('Оповещение', 'Осталось 1 минута!')

                elif self.value_optionmenu_mode_countdown_time.get() == 'Секундам':
                    
                    if self.summa_hours_and_minuts_for_convetison_in_minuts == 60:
                        msbox.showinfo('Оповещение', 'Осталась 1 минута!')

                    elif self.summa_hours_and_minuts_for_convetison_in_minuts == 30:
                        msbox.showinfo('Оповещение', 'Осталось 30 секунд!')

                    elif self.summa_hours_and_minuts_for_convetison_in_minuts == 10:
                        msbox.showinfo('Оповещение', 'Осталось 10 секунд!')
                        
                    elif self.summa_hours_and_minuts_for_convetison_in_minuts == 5:
                        msbox.showinfo('Оповещение', 'Осталось 5 секунд!')

app = App()
app.mainloop()