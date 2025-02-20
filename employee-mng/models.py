from sqlalchemy import Column, Integer, String
from app.database import Base

class Employee(Base):
    _tablename_ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    date_of_birth = Column(String)
    address = Column(String)
    contact_number = Column(String)
    emergency_contact = Column(String)