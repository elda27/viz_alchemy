from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()


class Shop(Base):
    __tablename__ = 'shop'
    shop_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String())
    owner = relationship('Owner', uselist=False)
    stock = relationship('Stock', uselist=True)


class Owner(Base):
    __tablename__ = 'owener'
    owner_id = Column(Integer, primary_key=True, autoincrement=True)
    shop_id = Column(Integer, ForeignKey('shop.shop_id'))
    age = Column(Integer)


class Catalog(Base):
    __tablename__ = 'catalog'
    item_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String())
    price = Column(Float)
    description = Column(String())


class Stock(Base):
    __tablename__ = 'stock'
    stock_id = Column(Integer, primary_key=True, autoincrement=True)
    shop_id = Column(Integer, ForeignKey('shop.shop_id'))
    item_id = Column(Integer, ForeignKey('catalog.item_id'))
    remain_item = Column(Integer)
    max_item = Column(Integer)


def main():
    engine = create_engine("sqlite:///test.db")
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)

    session = Session()
    session.add(Shop(name='shop1'))
    session.add(Shop(name='shop2'))

    session.add(Owner(shop_id=1, age=25))
    session.add(Owner(shop_id=2, age=48))

    session.add(Catalog(name='Apple', price=1.4, description='Fruit'))
    session.add(Catalog(name='Orange', price=1.5,
                        description='Fruit'))
    session.add(Catalog(name='Croissant', price=4.2,
                        description='Bread'))
    session.add(Catalog(name='Baguette', price=5.0,
                        description='Bread'))
    session.add(Catalog(name='Bagel', price=3.1,
                        description='Bread'))

    session.add(Stock(shop_id=1, item_id=1, remain_item=150, max_item=200))
    session.add(Stock(shop_id=1, item_id=2, remain_item=100, max_item=200))
    session.add(Stock(shop_id=1, item_id=3, remain_item=150, max_item=200))
    session.add(Stock(shop_id=2, item_id=1, remain_item=1050, max_item=1200))
    session.add(Stock(shop_id=2, item_id=2, remain_item=450, max_item=1200))
    session.add(Stock(shop_id=2, item_id=3, remain_item=250, max_item=1800))
    session.add(Stock(shop_id=2, item_id=4, remain_item=180, max_item=200))
    session.add(Stock(shop_id=2, item_id=5, remain_item=150, max_item=400))

    session.commit()
    # session.remove()


if __name__ == "__main__":
    main()
