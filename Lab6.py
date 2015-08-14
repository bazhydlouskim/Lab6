# -*- coding: cp1251 -*-
#LAB6 Python starter code
#imports go here
import MySQLdb
import _mysql

#code goes here

buffer = "true"



def oneQuery():
    try:
       
        # Open connection to the database
        db = MySQLdb.connect(host="localhost",user="root",passwd="GdP31_6#03bbm",db="Wiki")
        x = db.cursor()

        x.execute("""SELECT * FROM Category""")
        categories = x.fetchall()
        for category in  categories:
            print category
       
    except MySQLdb.Error as e:
        print "Error %d: %s" % (e.args[0],e.args[1])

    # Close the dababase
    finally:    
            
        if db:    
              db.close()


def twoQuery():
    try:
       
        # Open connection to the database
        db = MySQLdb.connect(host="localhost",user="root",passwd="GdP31_6#03bbm",db="Wiki")
        x = db.cursor()

        x.execute("""SELECT * FROM Articles""")
        articles = x.fetchall()
        for article in  articles:
            print article
       
    except MySQLdb.Error as e:
        print "Error %d: %s" % (e.args[0],e.args[1])

    # Close the dababase
    finally:    
            
        if db:    
              db.close()


def threeQuery():

    # Chooses from entries in categoryName column
    try:

        pattern=raw_input('Enter the pattern you want to search for: ')
        
        # Open connection to the database
        db = MySQLdb.connect(host="localhost",user="root",passwd="GdP31_6#03bbm",db="Wiki")
        x = db.cursor()

        params = '%' + pattern + '%'
        x.execute("""SELECT categoryID, categoryName FROM Category WHERE categoryName like %s;""", params)
        categories = x.fetchall()
        
        print('Pattern found in the following rows: ')
        for category in  categories:
            print category
       
    except MySQLdb.Error as e:
        print "Error %d: %s" % (e.args[0],e.args[1])

    # Close the dababase
    finally:    
            
        if db:    
              db.close()


def fourQuery():
    # Chooses from entries in articleTitle and articleNotes columns

    try:

        pattern=raw_input('Enter the pattern you want to search for: ')
        
        # Open connection to the database
        db = MySQLdb.connect(host="localhost",user="root",passwd="GdP31_6#03bbm",db="Wiki")
        x = db.cursor()

        params = ('%' + pattern + '%', '%' + pattern + '%')
        x.execute("""SELECT * FROM Articles WHERE articleTitle like %s or articleNotes like %s;""", params)
        articles = x.fetchall()
        
        print('Pattern found in the following rows: ')
        for article in  articles:
            print article
       
    except MySQLdb.Error as e:
        print "Error %d: %s" % (e.args[0],e.args[1])

    # Close the dababase
    finally:    
            
        if db:    
              db.close()


def fiveQuery():
    # A query that can potentially warn of any poorly designed categories.

    try:
       
        # Open connection to the database
        db = MySQLdb.connect(host="localhost",user="root",passwd="GdP31_6#03bbm",db="Wiki")
        x = db.cursor()

        x.execute("""SELECT CategoriesCount, AC.CategoryID, CategoryName FROM (SELECT Count(*) AS CategoriesCount,CategoryID FROM Article_Category Group By CategoryID) AS AC 
                        INNER JOIN Category ON Category.CategoryID = AC.CategoryID WHERE CategoriesCount < 2""")
        articleCounts = x.fetchall()
        for articleCount in  articleCounts:
            print articleCount
       
    except MySQLdb.Error as e:
        print "Error %d: %s" % (e.args[0],e.args[1])

    # Close the dababase
    finally:    
            
        if db:    
              db.close()




	
	
while buffer:
	print("""
	0.Exit
	1.See categories
	2.See articles
        3.Search for pattern in categories
	4.Search for pattern in articles
	5.See which categories have only one article
	""")
	buffer=input("what would you like to do? ")
	if buffer == 1:
		oneQuery()
	if buffer == 2:
		twoQuery()
	if buffer == 3:
		threeQuery()
	if buffer == 4:
                fourQuery()
	if buffer == 5:
                fiveQuery()
