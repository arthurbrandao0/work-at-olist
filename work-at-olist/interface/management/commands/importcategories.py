from django.core.management.base import BaseCommand
from datetime import datetime
import os
import csv
import sqlite3
import os.path

import psycopg2

try:
    db = psycopg2.connect("dbname='hetafbkk' user='hetafbkk' host='pellefant.db.elephantsql.com' port='5432' password='_5dXi5IiOxjsh0JPCybqhs5UXKkC5dJ5'")
except Exception as e:
    print(e)
    print("I am unable to connect to the database")



# db = sqlite3.connect("E:\GitHub\work-at-olist-v2\work-at-olist\db.sqlite3")
# db = sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "db.sqlite3")))
cursor = db.cursor()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('marketplace_name', type=str)  # get marketplace name
        parser.add_argument('csv_file_name', type=str)  # get csv file name

    def handle(self, *args, **options):
        marketplace_name = str(options.get('marketplace_name', None)).upper()
        csv_file_name = options.get('csv_file_name', None)
        cursor.execute("""SELECT channel_id FROM interface_channel WHERE name = UPPER('%s')""" % marketplace_name)
        data = cursor.fetchall()

        if len(data) == 0:  # check if marketplace exists in db and create if necessary
            cursor.execute("""INSERT INTO interface_channel (name) VALUES ('%s')""" % marketplace_name)

        cursor.execute("""SELECT channel_id FROM interface_channel WHERE name = UPPER('%s')""" % marketplace_name)  # get marketplace id
        channel_id = cursor.fetchone()[0]
        cursor.execute('''DELETE FROM interface_category WHERE channel_id = %s''' % channel_id)  # delete all marketplace related categories

        with open(str(os.getcwd()) + '\\' + csv_file_name) as f:
            reader = csv.reader(f)
            for row in reader:
                tree_category_name = str(row)  # set full category tree name
                print("----------------------------------------")
                if tree_category_name != "['Category']" and tree_category_name != "[]":  # ignore unwanted rows
                    category_divisor = (tree_category_name.count(" / "))
                    if category_divisor == 0:  # check if is a main category
                        category_name_ = (str(tree_category_name).replace("[", "").replace("]", "").replace("'", ""))
                        print(category_name_ + " has no parent")
                        cursor.execute('''SELECT * FROM interface_category  WHERE name = '%s' AND channel_id = %s''' % (category_name_, channel_id))
                        data = cursor.fetchall()
                        if len(data) == 0:
                            cursor.execute('''INSERT INTO interface_category (name, channel_id) VALUES ('%s', %s)''' % (category_name_, channel_id))

                    else:

                        tree_list = tree_category_name.split(" / ")
                        last_item = None
                        for level_category in tree_list:
                            parent_category_id = ''
                            level_category = level_category.replace("[", "").replace("]", "").replace("'", "")
                            print("\nCategory name: " + level_category)
                            if last_item is not None:
                                print("Parent category name: " + last_item)
                                cursor.execute("""SELECT category_id FROM interface_category WHERE name = '%s'""" % last_item)
                                parent_category_id = cursor.fetchone()[0]
                                print("Parent category id: " + str(parent_category_id))

                            cursor.execute('''SELECT * FROM interface_category  WHERE name = '%s' AND channel_id = %s''' % (level_category, channel_id))
                            data2 = cursor.fetchall()
                            if len(data2) == 0:
                                print("Registering category")
                                cursor.execute("""INSERT INTO interface_category (name, parent_category_id, channel_id) 
                                                VALUES ('%s',%s,%s)""" % (level_category, parent_category_id, channel_id))

                            last_item = level_category

                else:
                    print("Invalid row. Ignoring content")

        db.commit()
        db.close()
