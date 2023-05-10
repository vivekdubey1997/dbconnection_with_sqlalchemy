from  flask import Flask
from sqlalchemy import create_engine,column,String,Boolean,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app=Flask(__name__)

engine=create_engine("postgres://nfgstbdk:orKxnebERCNueGzxrN2pQ6PPnU-8SxST@tiny.db.elephantsql.com/nfgstbdk",echo=False)

session = sessionmaker(bind=engine)

session= session()

Base = declarative_base()

class student(Base):
    __tablename__ = 'students'
    id=column(Integer,primery_key=True)
    name=column(String(50))
    age=column(Integer)
    grade=column(String(50))

Base.metadata.create_all(engine)   


if __name__ =="__main":
    app.run(debug=True)