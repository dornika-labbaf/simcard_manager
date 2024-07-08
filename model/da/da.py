from sqlalchemy import create_engine, and_, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists
from model.entity.base import Base

connection_string = "mysql+pymysql://root:root123@localhost:3306/air_line"
if not database_exists(connection_string):
    create_database(connection_string)

engine = create_engine(connection_string)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


class DataAccess:
    def __init__(self, class_name):
        self.class_name = class_name

    def save(self, entity):
        session.add(entity)
        session.commit()
        session.refresh(entity)
        return entity

    def edit(self, entity):
        session.merge(entity)
        session.commit()
        session.refresh(entity)
        return entity
    #todo برای پاک کردن ارور میزنه از دیتا بیس
    def remove(self, entity):
        session.delete(entity)
        session.commit()
        session.refresh(entity)
        return entity

    def find_all(self):
        entity_list = session.query(self.class_name).all()
        return entity_list

    def find_by_id(self, id):
        entity = session.get(self.class_name, id)
        return entity

    def find_by(self, find_statement):
        entity = session.query(self.class_name).filter(find_statement).all()
        return entity

    def check_word_in_text(self, word):
        entity = session.query(self.class_name).filter(self.class_name._text.like(f'%{word}%')).all()
        return entity

    def find_by_date_range(self, start_date, end_date):
        entity = session.query(self.class_name).filter(self.class_name._date_time.between(start_date, end_date)).all()
        return entity
