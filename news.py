#! /usr/bin/python2.7

import psycopg2

db = psycopg2.connect("dbname=news")
c = db.cursor()

# returns most popular 3 articles of all time
c.execute('''
  SELECT articles.title, count(log.status) AS num
  FROM articles
  JOIN log ON log.path LIKE concat('%',articles.slug)
  GROUP BY articles.title
  ORDER BY num DESC
  LIMIT 3;''')

top_articles = c.fetchall()

print
print "Here are the most popular 3 articles of all time:"
print
print('1) ' '"' + str(top_articles[0][0]) + '" ' + '- ' +
      str(top_articles[0][1]) + ' views')
print('2) ' '"' + str(top_articles[1][0]) + '" ' + '- ' +
      str(top_articles[1][1]) + ' views')
print('3) ' '"' + str(top_articles[2][0]) + '" ' + '- ' +
      str(top_articles[2][1]) + ' views')
print


# returns list of authors sorted by total page views

c.execute('''
  SELECT authors.name, count(log.id) AS num
  FROM authors
  JOIN articles ON authors.id = articles.author
  JOIN log ON log.path LIKE concat('%',articles.slug)
  GROUP BY authors.name
  ORDER BY num DESC;''')

top_authors = c.fetchall()
print
print "Here are the most popular authors by page views:"
print
# prints all the top authors:
n = 0
while n < len(top_authors):
    print str(top_authors[n][0]) + ' - ' + str(top_authors[n][1]) + ' views'
    n = n + 1

print

# returns which days more than 1% of requests led to errors
# (see README.txt for source code on error_log view)

c.execute('''
  SELECT date, (errors * 100) / requests AS percentage from error_log
  WHERE errors > (requests / 100);''')

bad_days = c.fetchall()
print
print "Here are the days where more than 1 percent of requests led to errors:"
print
n = 0
while n < len(bad_days):
    print str(bad_days[0][0]) + ': ' + str(bad_days[0][1]) + '%' + ' errors'
    n = n + 1
print

db.close()
