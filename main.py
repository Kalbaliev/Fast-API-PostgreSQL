from fastapi import FastAPI, Depends
import datetime
from sqlalchemy.orm.session import Session
from decorator import check_api_key
import schema,models
from database import *



app=FastAPI()
fields=["title","position","experience_years","description","requirements","work_type","salary","company_name","industry","location","phone_number","email"]
Base.metadata.create_all(engine)


def get_db():
    db = LocalSession()
    try:
        yield db
    except:
        db.close()
        
# Post/Put 
def save(db, job):
    db.add(job)
    db.commit()
    db.refresh(job)



@app.get('/jobs/')
@check_api_key
def jobs(db:Session=Depends(get_db)):
    all_jobs = db.query(models.Job).all()
    return all_jobs


@app.get('/jobs/{id}')
@check_api_key
def job_detail(
    id,
    db:Session=Depends(get_db)
):
    job = db.query(models.Job).filter(models.Job.id == id).first()

    if job:
        return job
    else:
        return f"GET ERROR: Does not exist job detail with {id} ID"



@app.post('/jobs/create/')
@check_api_key
def add_job(request:schema.Job,db:Session=Depends(get_db)):
    try:
        new_job = models.Job(
            title = request.title,
            position = request.position,
            experience_years = request.experience_years,
            description = request.description,
            requirements = request.requirements,
            work_type = request.work_type,
            salary = request.salary,
            company_name = request.company_name,
            industry = request.industry,
            location = request.location,
            phone_number = request.phone_number,
            email = request.email
        )

        save(db, new_job)

        return new_job
    except:
        return "POST ERROR: Something is went wrong!"






@app.put('/jobs/update/{id}')
@check_api_key
def update_job(request:schema.Job,id,db:Session=Depends(get_db)):

    job = db.query(models.Job).filter(models.Job.id == id).first()
    global fields
    if job:

        for i in fields:
            val=getattr(request, f"{i}")
            if val!=None:
                setattr(job, f"{i}", val)
        job.updated_time=datetime.datetime.now()
        
        save(db, job)
        return job
    else:
        return f"UPDATE ERROR: Does not exist job detail with {id} ID"


@app.delete('/jobs/delete/{id}')
@check_api_key
def delete_job(id,db:Session=Depends(get_db)):
    try:
        db.query(models.Job).filter(models.Job.id == id).delete(synchronize_session=False)
        db.commit()
        return f"{id} element is deleted successfully"
    except:
        return "DELETE ERROR: Something is went wrong!"






