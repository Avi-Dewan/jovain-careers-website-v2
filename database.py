from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://n0wn9vl5jwi452xov8i4:pscale_pw_iIEE1flK670Ql6fMaNVn3XMxKy2w3cx1hpqsmebV2Kd@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4"
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
