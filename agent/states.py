from pydantic import BaseModel, Field
class File(BaseModel):
    path:str=Field(description="The file path where the file should be created or modified")
    purpose:str=Field(description="The purpose of the file and what it should contain")

class Plan(BaseModel):
    name:str=Field(description="The name of the app to be built")
    description:str=Field(description="A short description of the app")
    techstack:str=Field(description="A list of technologies to be used in the app e.g  'python','react','flask','javascript'")
    features:list[str]=Field(description="A list of features the app should have e.g 'user authentication','data visualization'")
    files:list[File]=Field(description="A list of files to be created for the app each with a path and a purpose")