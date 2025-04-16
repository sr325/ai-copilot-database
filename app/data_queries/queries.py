# from sqlalchemy.orm import sessionmaker
# from app.database.models import Account, Transaction
# from sqlalchemy import create_engine
#
# def get_session():
#     engine = create_engine("sqlite:///finance.db")  # Use PostgreSQL in production
#     Session = sessionmaker(bind=engine)
#     return Session()
#
# def get_recent_transactions(limit=10):
#     print("get_recent_transactions")
#     session = get_session()
#     txs = session.query(Transaction).order_by(Transaction.trade_date.desc()).limit(limit).all()
#     session.close()
#     return txs
#
# def get_accounts():
#     print("get_accounts")
#     session = get_session()
#     accounts = session.query(Account).all()
#     session.close()
#     return accounts
