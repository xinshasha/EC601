import _mysql

def connect(server,user_name,password,database):
	db=_mysql.connect(host=server,user=user_name,
                  passwd=password,db=database)
	return db

def keyword_images(db,key):
    db.query("""SELECT * FROM pic_label;""")
    r=db.store_result()
    db_store=[]
    while True:
        tmp=r.fetch_row();
        if len(tmp)==0:
            break
        db_store.append(tmp[0])
    result=[]
    for i in range(len(db_store)):
        tmp=[]
        for j in range(len(db_store[i])):
            try :
                tmp.append(db_store[i][j].decode('UTF-8'))
            except:
                pass
        result.append(tmp)
    for i in result:
        if not (key in i):
            result.remove(i)
    result=[i[0] for i in result]
    return result

def keyword_frequency(db,key):
    db.query("""SELECT * FROM pic_label;""")
    r=db.store_result()
    db_store=[]
    while True:
        tmp=r.fetch_row();
        if len(tmp)==0:
            break
        db_store.append(tmp[0])
    result=[]
    for i in range(len(db_store)):
        result.append([db_store[i][0].decode('UTF-8'),int(db_store[i][-1])])
    return result