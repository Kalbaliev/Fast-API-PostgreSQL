
from pydantic import BaseModel
from typing import Optional

class Job(BaseModel):

    title:Optional[str]=None

    position:Optional[str]=None
    experience_years:Optional[str]=None
    description:Optional[str]=None
    requirements:Optional[str]=None
    work_type:Optional[str]=None
    salary:Optional[str]=None

    company_name:Optional[str]=None
    industry:Optional[str]=None
    location:Optional[str]=None
    phone_number:Optional[str]=None
    email:Optional[str]=None

    api_key:str

