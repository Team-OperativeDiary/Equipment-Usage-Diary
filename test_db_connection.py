from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

database_url = 'PLACE_CONNECTION_STRING_HERE'

try:
   
    engine = create_engine(database_url)


    with engine.connect() as connection:
        query = text('SELECT 1')

        result = connection.execute(query).scalar()

        print('Connected to the database successfully!')

except OperationalError as e:
    print('Failed to connect to the database:', e)
