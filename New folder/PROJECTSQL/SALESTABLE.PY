import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',password='Bhavana@459')
cur=mydb.cursor()
S='CREATE TABLE SALES (PRODUCT_ID INT NOT NULL,PRODUCT_NAME VARCHAR(30) NOT NULL,SALES_QUANTITY INT NOT NULL,SALES_DATE DATE NOT NULL,SALES_AMOUNT INT NOT NULL,PROFIT_MARGIN INT NOT NULL)'
