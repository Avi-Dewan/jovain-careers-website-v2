from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://e0k4zptr3g8dw4v97p57:pscale_pw_XhMzzZWgf6W20WOs6dREYNYkegIaCzbewwFSGTvYvy6@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4"
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
