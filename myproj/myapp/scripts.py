import pandas as pd
import mysql.connector


def csv_dump(csv_file_path):
    try:
        df_data = pd.read_csv(csv_file_path, encoding='latin-1', on_bad_lines='skip')
        df_data.fillna(0, inplace=True)

        df_col = df_data.columns.tolist()
        df_col.append('active')
        df_val = df_data.values.tolist()

        col_mapping = {
            "uniq_id": "uniq_id VARCHAR(1000)",
            "crawl_timestamp": "crawl_timestamp VARCHAR(1500)",
            'product_url': "product_url VARCHAR(500)",
            'product_name': "product_name VARCHAR(500)",
            'product_category_tree': "product_category_tree VARCHAR(1000)",
            'pid': "pid VARCHAR(2500)",
            'retail_price': "retail_price VARCHAR(1500)",
            'discounted_price': "discounted_price VARCHAR(500)",
            'image': "image VARCHAR(3000)",
            'is_FK_Advantage_product': "is_FK_Advantage_product VARCHAR(1500)",
            'description': "description BLOB",
            'product_rating': "product_rating VARCHAR(500)",
            'overall_rating': "overall_rating VARCHAR(500)",
            'brand': "brand VARCHAR(500)",
            'product_specifications': "product_specifications BLOB",
            'active': 'active BOOLEAN DEFAULT TRUE NOT NULL'
        }

        val_list = []
        for col in df_col:
            val_list.append(col_mapping[col])

        create_table_query = f"CREATE TABLE IF NOT EXISTS myapp_allproducts ({', '.join([val for val in val_list])})"
        config = {
            "host": "127.0.0.1",
            "database": "flipkart_db",
            "user": "root",
            "password": "Sridevi@95"
        }
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute(create_table_query)

        for df_row in df_val:
            df_row.append(True)

            if len(df_col) == len(df_row):
                placeholders = ', '.join(['%s'] * len(df_col))
                insert_query = f"INSERT INTO myapp_allproducts ({', '.join(df_col)}) VALUES ({placeholders})"
                cursor.execute(insert_query, tuple(df_row))

        connection.commit()
        connection.close()
    except mysql.connector.DatabaseError as e:
        raise Exception(e)


csv_dump('/home/headrun/Downloads/Copy of flipkart - flipkart.csv')
