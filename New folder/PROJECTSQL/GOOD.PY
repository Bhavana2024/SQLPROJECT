import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',password='Bhavana@459')
cur=mydb.cursor()
G='CREATE TABLE GOODS (PRODUCT_ID INT NOT NULL,PRODUCT_NAME VARCHAR(30) NOT NULL,MANUFACTURED_COMPANY VARCHAR(30) NOT NULL,MANUFACTURED_DATE DATE NOT NULL,AVAILABLE_QUANTITY INT NOT NULL,COST_OF_EACH_ITEM INT NOT NULL)'
cur.execute(G)