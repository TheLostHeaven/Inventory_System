from sqlalchemy import Column,Integer, String, Float
from config.database import Base
from sqlalchemy.orm import relationship

class Supplier(Base):
    
    __tablename__ = "supplier"


    id = Column(Integer,primary_key=True)
    sud_name = Column(String)
    address = Column(String)
    phone = Column(Integer)
    email = Column(String)

    #supplies = relationship("Supplies", foreign_keys="Supplies.suplier.id", back_populates="supplier")