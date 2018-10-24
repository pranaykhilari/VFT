import csv
from vft import settings

def csv_generator(cursor, table_name):
    """
    Generate CSV file and store it in FILE_PATH folder.
    :param cursor:
    :param table_name:
    :return:
    """
    row_data = []
    FILE_PATH = settings.BASE_DIR + '/CSV/'

    cursor.execute("select * from "+table_name)
    colnames = [desc[0] for desc in cursor.description] #Parse the column name from cursor and store it in colnames.
    row = cursor.fetchone()

    while row is not None:
        row_data.append(row) #Store table data in row_data.
        row = cursor.fetchone()

    with open(FILE_PATH + table_name+".csv", 'w') as file:
        write_csv = csv.writer(file)
        write_csv.writerow(colnames)
        for row in row_data:
            write_csv.writerow(row)
    return