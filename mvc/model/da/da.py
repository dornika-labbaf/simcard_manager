from sqlalchemy import create_engine, and_, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists
from mftplus.model.entity.base import Base
from mftplus.model.tools.decorators import log


class DataAccess:
    def __init__(self, class_name):
        connection_string = "mysql+pymysql://root:root123@localhost:3306/mft"
        if not database_exists(connection_string):
            create_database(connection_string)

        engine = create_engine(connection_string)
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.class_name = class_name

    def save(self, entity):
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity

    def edit(self, entity):
        self.session.merge(entity)
        self.session.commit()
        return entity

    def remove(self, entity):
        self.session.delete(entity)
        self.session.commit()
        return entity

    def find_all(self):
        entity_list = self.session.query(self.class_name).all()
        return entity_list

    def find_by_id(self, id):
        entity = self.session.get(self.class_name, id)
        return entity

    def find_by(self, find_statement):
        entity = self.session.query(self.class_name).filter(find_statement).all()
        return entity

    def check_word_in_text(self, word):
        entity = self.session.query(self.class_name).filter(self.class_name._text.like(f'%{word}%')).all()
        return entity

    def find_by_date_range(self, start_date, end_date):
        entity = self.session.query(self.class_name).filter(self.class_name._date_time.between(start_date, end_date)).all()
        return entity