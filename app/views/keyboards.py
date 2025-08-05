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
        
    



# class Keyboards:
#     @staticmethod
#     def main_menu_keyboard():
#         """Reply Keyboard: نمایش منوی اصلی"""
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         markup.add(
#             types.KeyboardButton("📋 لیست کارها"),
#             types.KeyboardButton("ℹ️ درباره ما")
#         )
#         return markup

#     @staticmethod
#     def inline_actions():
#         """Inline Keyboard: نمایش دکمه‌های اکشن"""
#         markup = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton("🌐 وبسایت", url="https://example.com")
#         btn2 = types.InlineKeyboardButton("➕ افزودن", callback_data="add_task")
#         markup.add(btn1, btn2)
#         return markup



# # ✅ Reply Keyboard
# def main_menu_keyboard():
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add(types.KeyboardButton("📋 لیست کارها"), types.KeyboardButton("ℹ️ درباره ما"))
#     return markup

# # ✅ Inline Keyboard
# def inline_actions():
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton("🌐 وبسایت", url="https://example.com")
#     btn2 = types.InlineKeyboardButton("➕ افزودن", callback_data="add_task")
#     markup.add(btn1, btn2)
#     return markup
