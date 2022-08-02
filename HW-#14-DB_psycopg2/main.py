import psycopg2


def create_tables(cursor):
    '''Функция, создающая структуру БД (таблицы)
    '''
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS client (
	    id SERIAL PRIMARY KEY,
	    first_name 	VARCHAR(30) NOT NULL,
	    last_name 	VARCHAR(30) NOT NULL,
	    email 		VARCHAR(30) UNIQUE NOT NULL	
    );""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS phone (
	    id SERIAL PRIMARY KEY,
	    person_id 		INTEGER 	REFERENCES client(id),
	    phone_number 	VARCHAR(30) 
    );""")
    conn.commit()


def add_new_client(cursor, first_name: str, last_name: str, email: str, phone_number=None):
    '''Функция, позволяющая добавить нового клиента
    '''
    cursor.execute("""
    INSERT INTO client(first_name, last_name, email) 
    VALUES (%s, %s, %s) 
    RETURNING id;
    """, (first_name, last_name, email))
    person_id = cursor.fetchone()
    cursor.execute("""
    INSERT INTO phone(person_id, phone_number)
    VALUES (%s, %s);
    """, (person_id[0], phone_number))
    conn.commit()


def add_phone_number(cursor, person_id: int, phone_number: str):
    '''Функция, позволяющая добавить телефон для существующего клиента
    '''
    cursor.execute("""
    INSERT INTO phone(person_id, phone_number)
    VALUES (%s, %s);
    """, (person_id, phone_number))
    cursor.execute("""
    DELETE FROM phone
     WHERE person_id=%s
       AND phone_number IS NULL;
    """, (person_id, ))
    conn.commit()


def change_client_data(cursor, person_id, first_name=None, last_name=None, email=None, phone_number=None):
    '''Функция, позволяющая изменить данные о клиенте
    '''
    if first_name != None:
        cursor.execute("""
        UPDATE client 
           SET first_name=%s 
         WHERE id=%s;
        """, (first_name, person_id))
    if last_name != None:
        cursor.execute("""
        UPDATE client 
           SET last_name=%s 
         WHERE id=%s;
        """, (last_name, person_id))
    if email != None:
        cursor.execute("""
        UPDATE client 
           SET email=%s 
         WHERE id=%s;
        """, (email, person_id))
    if phone_number != None:
        cursor.execute("""
        UPDATE phone 
           SET phone_number=%s 
         WHERE person_id=%s;
        """, (phone_number, person_id))
    conn.commit()


def delete_phone_number(cursor, person_id: int, phone_number: str):
    '''Функция, позволяющая удалить телефон для существующего клиента
    '''
    cursor.execute("""
    DELETE FROM phone 
          WHERE person_id=%s 
            AND phone_number=%s;
    """, (person_id, phone_number))
    conn.commit()


def delete_client(cursor, person_id: int):
    '''Функция, позволяющая удалить существующего клиента
    '''
    cursor.execute("""
    DELETE FROM phone
          WHERE person_id=%s;
    """, (person_id, ))
    cursor.execute("""
    DELETE FROM client
          WHERE id=%s;
    """, (person_id, ))


def find_client(cursor, first_name=None, last_name=None, email=None, phone_number=None):
    '''Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)
    '''
    if first_name != None:
        cursor.execute("""
        SELECT c.id, first_name, last_name, email, phone_number 
          FROM client AS c
               JOIN phone AS p 
               ON p.person_id = c.id
         WHERE first_name=%s;
        """, (first_name, ))
    if last_name != None:
        cursor.execute("""
        SELECT c.id, first_name, last_name, email, phone_number 
          FROM client AS c
               JOIN phone AS p 
               ON p.person_id = c.id
         WHERE last_name=%s;
        """, (last_name, ))
    if email != None:
        cursor.execute("""
        SELECT c.id, first_name, last_name, email, phone_number 
          FROM client AS c
               JOIN phone AS p 
               ON p.person_id = c.id
         WHERE email=%s;
        """, (email, ))
    if phone_number != None:
        cursor.execute("""
        SELECT c.id, first_name, last_name, email, phone_number 
          FROM client AS c
               JOIN phone AS p 
               ON p.person_id = c.id
         WHERE phone_number=%s;
        """, (phone_number, ))
    print(cursor.fetchall())


def check(cursor):
    '''Функция, делающая полную выборку из БД
    '''
    cursor.execute("""
    SELECT * 
      FROM client;
    """)
    print(cursor.fetchall())
    cursor.execute("""
    SELECT * 
      FROM phone;
    """)
    print(cursor.fetchall())


with psycopg2.connect(database="netology_db", user="postgres", password="SQL_dmsnn56") as conn:
    with conn.cursor() as cur:
        print(create_tables(cur))
        print(add_new_client(cur, first_name='Some', last_name='Buddy', email='somebuddy@mail.com', phone_number='111-11-11'))
        print(add_new_client(cur, first_name='Any', last_name='Buddy', email='anybuddy@mail.com', phone_number='222-22-22'))
        print(add_new_client(cur, first_name='Third', last_name='Guy', email='thirdguy@mail.com'))
        print(add_new_client(cur, first_name='My', last_name='Man', email='myman@mail.com'))
        print(add_phone_number(cur, person_id=3, phone_number='333-33-33'))
        print(add_phone_number(cur, person_id=1, phone_number='444-44-44'))
        print(change_client_data(cur, person_id=1, first_name='New', email='newbuddy@mail.ru'))
        print(delete_phone_number(cur, person_id=1, phone_number='111-11-11'))
        print(delete_client(cur, person_id=4))
        print(find_client(cur, last_name='Buddy'))
        print(find_client(cur, email='thirdguy@mail.com'))
        print(find_client(cur, first_name='Any'))
        print(find_client(cur, phone_number='333-33-33'))
        print(check(cur))
