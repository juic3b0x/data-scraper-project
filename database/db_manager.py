# data-scraper-project/database/db_manager.py

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///promo_codes.db"
Base = declarative_base()

class PromoCode(Base):
    __tablename__ = 'promo_codes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(50), nullable=False)
    promo = Column(String(255), nullable=False)

# Set up the engine and session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def initialize_database():
    Base.metadata.create_all(engine)

def add_promo_codes(promo_codes):
    session = Session()
    for code, promo in promo_codes:
        promo_code_instance = PromoCode(code=code, promo=promo)
        session.add(promo_code_instance)
    session.commit()
    session.close()

def search_promo_codes(search_term):
    session = Session()
    query = session.query(PromoCode).filter(PromoCode.code.contains(search_term))
    results = query.all()
    session.close()
    return results
