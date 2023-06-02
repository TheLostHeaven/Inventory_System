from sqlalchemy import Column, Integer, Float, ForeignKey
from config.database import Base
from sqlalchemy.orm import relationship

class Supplies(Base):


    __tablename__ ="supplies"


    id = Column(Integer, primary_key = True)
    product_id = Column(Integer)
    supplier_id = Column(Integer )
    purchase_price = Column(Float)


    #product = relationship("Product", back_populates="supplies")
    #supplier = relationship("Supplier", back_populates="supplies")