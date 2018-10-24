import psycopg2
import logging
from django.shortcuts import render
from django.http import HttpResponseRedirect
from db_integration.generate_csv import csv_generator
from db_integration.constants import *

logger = logging.getLogger(__name__)

def access_db(request):
    """
    Fetch data from AWS Aurora DB and pass it to csv_generator function.
    :param request:
    :return:
    """
    connection = None

    if request.method == "POST":
        try:
            connection = psycopg2.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
            cursor = connection.cursor()

            cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")

            for table in cursor.fetchall():
                table_name = str(table).strip("() , ''")
                csv_generator(cursor, table_name)
            cursor.close()

        except(Exception, psycopg2.DatabaseError) as error:
            logger.error(error)

        finally:
            if connection is not None:
                connection.close()
        return HttpResponseRedirect('/download/')
    else:
        return render(request, "db-integration.html")