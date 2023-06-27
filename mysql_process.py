from sqlalchemy import create_engine, text
import configparser

config = configparser.ConfigParser()
config.read("settings.conf")

host = config['MYSQL']['hostname']
user_name = config['MYSQL']['user_name']
password = config['MYSQL']['password']
port = config['MYSQL']['port']

CONNECTION_STRING = f"mysql+pymysql://{user_name}:{password}@{host}:{port}"

def show_databases():
    conn = create_engine(CONNECTION_STRING).connect()
    statement_execute = conn.execute(text("Show Databases"))
    conn.close()
    
    databases = [x[0] for x in statement_execute.fetchall()]
    return {"databases":databases}
    
def create_database(db_name):
    conn = create_engine(CONNECTION_STRING).connect()
    try:
        statement_execute = conn.execute(text(f"CREATE Database {db_name}"))
        conn.close()
        return {"success":True,"msg":f"Database {db_name} Created!."}
    except Exception as e:
        return {"success":False,"reason":str(e)}
    
def drop_database(db_name):
    conn = create_engine(CONNECTION_STRING).connect()
    try:
        statement_execute = conn.execute(text(f"DROP Database {db_name}"))
        conn.close()
        return {"success":True,"msg":f"Database {db_name} Deleted!."}
    except Exception as e:
        return {"success":False,"reason":str(e)}
    
def list_tables(db_name):
    conn = create_engine(CONNECTION_STRING).connect()
    try:
        statement_execute = conn.execute(text(f"SHOW TABLES IN {db_name}"))
        conn.close()
        tables = [x[0] for x in statement_execute.fetchall()]
        return {"success":True,"tables":tables}
    except Exception as e:
        return {"success":False,"reason":str(e)}
    
def execute_query(query):
    conn = create_engine(CONNECTION_STRING).connect()
    if "select" in query.splitlines()[0].split(" ")[0].lower():
        try:
            statement_execute = conn.execute(text(query))
            conn.close()

            columns = [x for x in statement_execute.keys()]
            data = statement_execute.fetchall()

            result = list()
            for datum in data:
                temp_dict = dict()
                for i, datum_ in enumerate(datum):
                    temp_dict[columns[i]] = datum_
                result.append(temp_dict)

            return {"success":True,"result":result}
        except Exception as e:
            return {"success":False,"reason":str(e)}
    
    else:
        try:
            statement_execute = conn.execute(text(query))
            conn.commit()
            conn.close()
            return {"success":True,"result":"Statement Executed Successfully"}
        except Exception as e:
            return {"success":False,"reason":str(e)}

