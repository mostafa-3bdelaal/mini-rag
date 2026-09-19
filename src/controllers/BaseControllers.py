# الاعدادات المشتركه هتبقي هنا


from helpers.config import get_settings
import os
import random
import string


class BaseControllers:
    def __init__(self):
        self.settings = get_settings()
        self.base_dir= os.path.dirname(os.path.dirname(__file__))
        self.file_dir = os.path.join(self.base_dir,'assets/files')
        
        
    def generate_random_file_name(self,length=12):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    