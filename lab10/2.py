import psycopg2

config = psycopg2.connect(
    host = 'localhost', 
    database = 'postgres',
    user = 'postgres',
    password = 'Dulat2005'
)

current = config.cursor()
#add values into table
id = 2
name = 'Dulat'
number = '+77079839500'

sql = '''
    INSERT INTO phonebook VALUES (%s, %s, %s); 
'''

current.execute(sql, (id, name, number))

current.close()
config.commit()
config.close()