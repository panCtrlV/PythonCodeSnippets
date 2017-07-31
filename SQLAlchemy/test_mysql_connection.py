# -*- coding: utf-8 -*-

'''
Quickly test if the connection to a MySQL database is successful. 
Useful when you want to access the MySQL db in your application.

If the following code prints results, then the connection is successful.

@Author: panc
@Date:   2017-07-30 19:20:27
@Last Modified by:   Pan Chao
@Last Modified time: 2017-07-30 20:59:15
'''

from sqlalchemy import create_engine


engine = create_engine('mysql://panc:<my_passowrd>@localhost/rongzhongdb')
connection = engine.connection()
result = connection.execute('select * from data_source')
for row in result:
    print('field_name:', row['field_name'])

connection.close()