import sqlite3 as sql
conn = sql.connect('class_scheedule.db')
c = conn.cursor()
c.execute("""create table room (number text, capacity integer)""")
c.execute("insert into room Values ('PCTB211', 25),"
                                  "('NCTB205', 45),"
                                  "('PCTB213', 35),"
                                  "('PCT211A', 40)")
c.execute("""create table meeting_time (id text, time text)""")
c.execute("insert into meeting_time Values ('MT1', 'D1 10:00 - 12:30'),"
                                          "('MT2', 'D1 14:00 - 16:30'),"
                                          "('MT3', 'D2 10:00 - 12:30'),"
                                          "('MT4', 'D2 14:00 - 16:30'),"
                                          "('MT5', 'D3 10:00 - 12:30'),"
                                          "('MT6', 'D3 14:00 - 16:30')")
c.execute("""create table instructor (number text, name text)""")
c.execute("insert into instructor Values ('I1', 'Dr James Web'),"
                                        "('I2', 'Mr. Mike Brown'),"
                                        "('I3', 'Dr Steve Day'),"
                                        "('I4', 'Mrs Jane Doe'),"
                                        "('I5', 'Dr. Julia Blue')")
c.execute("""create table course_instructor (course_number text, instructor_number text)""")
c.execute("insert into course_instructor Values ('TCT201', 'I1'),"
                                               "('TCT201', 'I2'),"
                                               "('TEE201', 'I1')," 
                                               "('TEE201', 'I2')," 
                                               "('TEE201', 'I3')," 
                                               "('TCT203', 'I1'),"
                                               "('TCT203', 'I2'),"
                                               "('TEE202', 'I3'),"
                                               "('TEE202', 'I4'),"
                                               "('TEE203', 'I4'),"
                                               "('TEC201', 'I1'),"
                                               "('TEC201', 'I3'),"
                                               "('TEC202', 'I2'),"
                                               "('TEC202', 'I4'),"
                                               "('TIT201', 'I5'),"
											   "('TIT202', 'I5'),"
											   "('TCT202','I1'),"
											   "('TCT202','I2')")
c.execute("""create table course (number text, name text, max_numb_of_students)""")
c.execute("insert into course Values ('TCT201', 'AI', 25),"
                                    "('TEE201', 'CT', 35)," 
                                    "('TCT203', 'SE', 25),"
                                    "('TEE202', 'EM', 30),"
                                    "('TEE203', 'NT', 35),"
                                    "('TEC201', 'DLC', 45),"
                                    "('TEC202', 'IM', 45),"
                                    "('TIT201', 'MC',  30),"
                                    "('TIT202', 'MT', 40),"
								    "('TCT202','DBMS', 40)")


c.execute("""create table dept (name text)""")
c.execute("insert into dept Values ('CSE'),"
                                  "('EE'),"
                                  "('ECE'),"
                                  "('IT')")
c.execute("""create table dept_course (name text, course_numb text)""")
c.execute("insert into dept_course Values ('CSE', 'TCT201'),"
                                         "('CSE', 'TCT203'),"
                                         "('EE',   'TEE201'),"
                                         "('EE',   'TEE202'),"
                                         "('EE',   'TEE203'),"
                                         "('ECE',  'TEC201'),"
                                         "('ECE',  'TEC201'),"
                                         "('IT',  'TIT201'),"
                                         "('IT',  'TIT202'),"
                                         "('CSE', 'TCT202')")
conn.commit()
c.close()
conn.close()