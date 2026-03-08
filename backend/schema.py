from pydantic import BaseModel


class Employee(BaseModel):

    city: str

    city_development_index: float

    gender: str

    relevent_experience: str

    enrolled_university: str

    education_level: str

    experience: str

    company_size: str

    last_new_job: str

    training_hours: int