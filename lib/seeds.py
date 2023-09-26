from Models.classes import Food_Truck, Customer, Base, Session
from sqlalchemy import create_engine
from sqlalchemy.orm import Session



if __name__ == "__main__":
   
    engine = create_engine('sqlite:///food_truck.db')
    Food_Truck.__table__.drop(engine)
    Base.metadata.create_all(engine)
    
    with Session(engine) as session:
       
        session.commit()
      