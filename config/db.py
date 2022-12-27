from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://jimbo:.htatec.@localhost:3306/logincat")


meta_data = MetaData()