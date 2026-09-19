''' 
create function to search for the project by id and return the project data
and if the project is not found create a new project with the given id and return the project data
'''


from .BaseControllers import BaseControllers
from fastapi import UploadFile
from models import ResponseSignal
import os


class ProjectController(BaseControllers):
    def __init__(self):
        super().__init__()

    def get_project_path(self, project_id: str):
        project_path = os.path.join(
            self.file_dir,  
            project_id
            )
        
        if not os.path.exists(project_path):
            os.makedirs(project_path)
            
        return project_path
    