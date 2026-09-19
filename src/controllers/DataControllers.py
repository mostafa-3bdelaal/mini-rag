# logic for Data 

from .BaseControllers import BaseControllers
from fastapi import UploadFile
from models import ResponseSignal
from .ProjectControllers import ProjectController
import re
import os


class DataController(BaseControllers):
    def __init__(self):
        super().__init__()
        self.size_scale= 1048576
    
    
    def validate_upload_file(self, file: UploadFile):
        if file.size > self.settings.FILE_MAX_SIZE * self.size_scale:
            return False, ResponseSignal.FILE_SIZE_EXCEEDED.value

        if file.content_type not in self.settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value

        return True, ResponseSignal.FILE_VALIDATED_SUCCESS.value
    
    def generate_unique_filepath(self, original_file_name: str, project_id: str):
        random_file_name = self.generate_random_file_name()
        project_path = ProjectController().get_project_path(project_id=project_id)
        
        cleaned_filename = self.get_clean_file_name(original_file_name=original_file_name)
        
        new_file_path= os.path.join(
            project_path,
            random_file_name + '_' + cleaned_filename
        )
        
        while os.path.exists(new_file_path):
            random_file_name = self.generate_random_file_name()
            new_file_path= os.path.join(
                project_path,
                random_file_name + '_' + cleaned_filename
            )
            
        return new_file_path,  random_file_name + '_' + cleaned_filename
        
        
    def get_clean_file_name(self, original_file_name: str):
        
        # Remove any special characters, except underscores and periods
        clean_file_name = re.sub(r'[^\w.-]', '', original_file_name.strip())
        
        # replace spaces with underscores
        clean_file_name = clean_file_name.replace(' ', '_')
        
        return clean_file_name