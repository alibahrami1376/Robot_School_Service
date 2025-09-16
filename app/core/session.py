import time

from telebot.types import Message
from enum import Enum

class step(Enum):
    START= "Start"
    DRIVER= "DRIVER"
    DRIVER_RG_INPUT_NAME="DRIVER_RG_INPUT_NAME"
    STUDENT= "STUDENT"
    CONTACT_US= "CONTACT_US"
    STUDENT_RG="STUDENT_RG"
    ENTER_NAME = "2"
    ENTER_PHONE = "3"
    ENTER_EMAIL = "4"
    CONFIRM = "5"
    DONE = "6"




class SessionRegister:

    """
    expire_time: مدت اعتبار سشن (ثانیه)
    0 یعنی بدون محدودیت زمان
    """
            
    sessions = {}
    # {user_id: {"step": int, "data": dict, "last_update": timestamp}}
    expire_time = 0


    def start(self,message: Message):
        self.sessions[message.from_user.id] = {"step": step.START, "data": {},"last_update": time.time(),"Last_message":message.message_id,
                                            "from_user":{"first_name":message.from_user.first_name,"username":message.from_user.username,
                                                         'last_name': message.from_user.last_name}}



    def exists(self, user_id: int) -> bool:
        """بررسی وجود و انقضا"""
        if user_id not in self.sessions:
            return False
        if self.expire_time > 0 and time.time() - self.sessions[user_id]["last_update"] > self.expire_time:
            del self.sessions[user_id]
            return False
        return True

    def get_step(self, user_id: int) -> int:
        """مرحله فعلی کاربر"""
        return self.sessions.get(user_id, {}).get("step", 0)

    def set_step(self, user_id: int, step: str):
        """تغییر مرحله"""
        if self.exists(user_id):
            self.sessions[user_id]["step"] = step
            self.sessions[user_id]["last_update"] = time.time()

    def set_last_messageid(self,user_id: int,message_id: int):
        
        self.sessions[user_id]["Last_message"]= message_id


    def save_data(self, user_id: int, key: str, value: str):
        """ذخیره داده کاربر"""
        if self.exists(user_id):
            self.sessions[user_id]["data"][key] = value
            self.sessions[user_id]["last_update"] = time.time()

    def get_data(self, user_id: int) -> dict:
        """دریافت داده‌های کاربر"""
        return self.sessions.get(user_id, {}).get("data", {})
    
    def get_last_messageid(self,user_id:int):
        return self.sessions.get(user_id).get("Last_message")

    def clear(self, user_id: int):
        """پاک کردن سشن (پایان ثبت‌نام)"""
        if user_id in self.sessions:
            del self.sessions[user_id]




session = SessionRegister()