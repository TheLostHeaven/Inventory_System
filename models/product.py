from sqlalchemy import Column,Integer,String,Float
from config.database import Base
from sqlalchemy.orm import relationship


class Product(Base):
    
    __tablename__= "product"
    
    id = Column(Integer,primary_key =True)
    name = Column(String)
    brand = Column(String)
    description = Column(String)
    price = Column(Float)
    entry_date = Column(Integer)

    #supplies = relationship("Supplies", back_populates="product", foreign_keys='Supplies.product_id')