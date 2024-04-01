import pandas as pd
import psycopg2
import os


def csv_dump(csv_file_path):
    """
    read csv data
    """
    try:
        df_data = pd.read_csv(csv_file_path, encoding='latin-1', on_bad_lines='skip')
        df_data.fillna(0, inplace=True)

        df_col = df_data.columns.tolist()
        df_col.append('active')
        df_val = df_data.values.tolist()

        config = {
            "host": "db",
            "database": "test_db",
            "user": "coachpro",
            "password": "Sridevi@95"
        }
        connection = psycopg2.connect(**config)
        cursor = connection.cursor()
        for df_row in df_val:
            df_row.append(True)

            if len(df_col) == len(df_row):
                placeholders = ', '.join(['%s'] * len(df_col))
                insert_query = f"INSERT INTO myapp_allproducts ({', '.join(df_col).lower()}) VALUES ({placeholders})"
                cursor.execute(insert_query, tuple(df_row))

        connection.commit()
        connection.close()
    except psycopg2.DatabaseError as e:
        raise Exception(e)


csv_dump(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'flipkart.csv'))
