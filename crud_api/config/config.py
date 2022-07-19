from sqlalchemy import create_engine
import os 

engine = create_engine("postgresql://{os.environ['USER']}@localhost:5432/some-postgres")

engine.connect()
