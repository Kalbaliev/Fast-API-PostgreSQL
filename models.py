import datetime
from database import Base
from sqlalchemy import Column,Integer,String,Identity,DateTime,Text


class Job(Base):
    __tablename__='jobs'

    id=Column(Integer, Identity(start=100000, cycle=True), primary_key=True, index=True)
    title=Column(String(50),unique=True,nullable=False)

    position=Column(String(150),nullable=False)
    experience_years=Column(String(10),nullable=False)
    description=Column(Text)
    requirements=Column(Text)
    work_type=Column(String(50),nullable=False)
    salary=Column(String(50),nullable=False)

    company_name=Column(String(150),nullable=False)
    industry=Column(String(150))
    location=Column(String(150))
    phone_number=Column(String(50),nullable=False)
    email=Column(String(100),nullable=False)
    
    created_time=Column(DateTime(timezone=False),default=datetime.datetime.utcnow)
    updated_time=Column(DateTime(timezone=False),default=datetime.datetime.utcnow)









