from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

# Replace 'your_database_url' with the actual database URL
database_url = 'mysql://root:aDbGfCCd533Da-CHcfgdGf3-Cg1hH1FF@roundhouse.proxy.rlwy.net:49193/railway'

try:
    # Create an engine to connect to the database
    engine = create_engine(database_url)

    # Try to execute a simple query to test the connection
    with engine.connect() as connection:
        # Create a SQLAlchemy text object for the query
        query = text('SELECT 1')

        # Execute the query and get the result
        result = connection.execute(query).scalar()

        # If the query is successful, print a success message
        print('Connected to the database successfully!')

except OperationalError as e:
    # If an OperationalError occurs, print the error message
    print('Failed to connect to the database:', e)
