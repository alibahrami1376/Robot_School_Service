from telebot import types



class ReplyKeyboard:
    def __init__(self, resize_keyboard: bool = True, list_name_buttons: list = None,row_key: int =0,Column: int =0):
        self.row= row_key
        self.column = Column
        self.markup = types.ReplyKeyboardMarkup(resize_keyboard=resize_keyboard)
        if list_name_buttons:
            self.create_button(self.row,self.column,list_name_buttons)
        
            
    def get_markup(self):
        return self.markup
    
    def create_button(self,row :int,column :int,list_name_buttons :list):
        if column == 0 or row == 0:
            for text in list_name_buttons:
                self.markup.add(types.KeyboardButton(text))
                self.markup.row()
        else:
            # چیدن دکمه‌ها بر اساس ستون‌ها
            buttons = [types.KeyboardButton(text) for text in list_name_buttons]
            for i in range(0, len(buttons), column):
                self.markup.row(*buttons[i:i + column])
        


class InlineKeyboard:
    def __init__(self, list_buttons: list = None, row_key: int = 0, column: int = 0):
        self.row = row_key
        self.column = column
        self.markup = types.InlineKeyboardMarkup()
        if list_buttons:
            self.create_button(self.row, self.column, list_buttons)

    def get_markup(self):
        return self.markup

    def create_button(self, row: int, column: int, list_buttons: list):
        if column == 0 or row == 0:
            # هر دکمه در یک ردیف
            for text, cb in list_buttons:
                self.markup.add(types.InlineKeyboardButton(text, callback_data=cb))
        else:
            # دکمه‌ها بر اساس تعداد ستون‌ها
            buttons = [types.InlineKeyboardButton(text, callback_data=cb) for text, cb in list_buttons]
            for i in range(0, len(buttons), column):
                self.markup.row(*buttons[i:i + column])

main = InlineKeyboard([
    ("رانندگان","Driver"),
    ("دانش آموزان", "Student"),
    ("ارتباط با ما ", "Contact_us")
], column=2)


student = InlineKeyboard([
    ("ثبت نام ","reg_ST"),
    ("اطلاعات دانش آموز ", "info_ST"),
    ("جزییات مالی ", "Financial_ST")
], column=2)


driver = InlineKeyboard([
    ("ثبت نام ","reg_DR"),
    ("اطلاعات دانش اموزان  ", "info_DR"),
    (" جزییات مالی ", "Financial_DR")
], column=2)


main_mark =main.get_markup()
student_mark =student.get_markup()
driver_mark =driver.get_markup() 


 
