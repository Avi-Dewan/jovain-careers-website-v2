from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_all = result.all()
    column_names = result.keys()
    jobs = []
    for row in result_all:
      job_dict = dict(zip(column_names, row))
      jobs.append(job_dict)
    return jobs


print(load_jobs_from_db())
