from sqlalchemy import Column, String, DateTime, Numeric, Date
from sqlalchemy.ext.declarative import declarative_base
import datetime
import uuid

Base = declarative_base()

class Account(Base):
    __tablename__ = 'accounts'
    account_name = Column(String(20), primary_key=True)
    accounting_region = Column(String(10))
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

class Transaction(Base):
    __tablename__ = 'transactions'
    transaction_id = Column(String(100), primary_key=True, default=lambda: str(uuid.uuid4()))
    account_name = Column(String(20))
    amount = Column(Numeric(12, 2))
    trade_date = Column(Date)
    settlement_date = Column(Date)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
