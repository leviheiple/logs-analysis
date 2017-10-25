INSTRUCTIONS FOR USING THE NEWS.PY PROGRAM:

This program is designed to run on Linux (or a Linux-based virtual machine.) After booting up your favorite virtual machine, follow the instructions below:

1) Download the database from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
2) CD to the folder in your Linux terminal
3) Run 'python news.py'


NOTE: The news.py uses a view called 'error_log'. Below is the SQL code used to create the view:

    CREATE VIEW error_log as
    SELECT date(time) as date, count(*) as requests, 
    sum(case status when '200 OK' then 0 else 1 end) as errors
    FROM log
    GROUP BY date;