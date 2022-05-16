import sqlite3
import pandas as pd

connection = sqlite3.connect("books.db")
output = open("Part1Output.txt", "w")

output.write("Viewing the authors Table's Contents\n\n")
output.write(pd.read_sql("SELECT * FROM authors", connection, index_col=["id"]).to_string())

output.write("\n\nLooking at the titles Table\n\n")
output.write(pd.read_sql("SELECT * FROM titles", connection).to_string())

output.write("\n\nLooking at the first few entries for author_ISBN\n\n")
output.write(pd.read_sql("SELECT * FROM author_ISBN", connection).head().to_string())

output.write("\n\nLooking at first and last names from the authors table\n\n")
output.write(pd.read_sql("SELECT first, last FROM authors", connection).to_string())

output.write("\n\nUsing WHERE to select certain entries\n\n")
output.write(pd.read_sql("SELECT title, edition, copyright FROM titles WHERE copyright > '2016'", connection).to_string())

output.write("\n\nUsing LIKE to select certain entries by pattern matching\n\n")
output.write(pd.read_sql("SELECT id, first, last FROM authors WHERE last LIKE 'D%'", connection, index_col=["id"]).to_string())

output.write("\n\nUsing LIKE, part two\n\n")
output.write(pd.read_sql("SELECT id, first, last FROM authors WHERE first LIKE '_b%'", connection, index_col=["id"]).to_string())

output.write("\n\nUsing ORDER BY to sort the results\n\n")
output.write(pd.read_sql("SELECT title FROM titles ORDER BY title ASC", connection).to_string())

output.write("\n\nSorting by multiple columns\n\n")
output.write(pd.read_sql("SELECT id, first, last FROM authors ORDER BY last, first", connection, index_col=["id"]).to_string())

output.write("\n\nSorting by multiple columns part 2\n\n")
output.write(pd.read_sql("SELECT id, first, last FROM authors ORDER BY last DESC, first ASC", connection, index_col=["id"]).to_string())

output.write("\n\nCombining WHERE and ORDER BY\n\n")
output.write(pd.read_sql("SELECT isbn, title, edition, copyright FROM titles WHERE title LIKE '%How to Program' ORDER BY title", connection).to_string())

output.write("\n\nUsing INNER JOIN to merge data\n\n")
output.write(pd.read_sql("SELECT first, last, isbn FROM authors INNER JOIN author_ISBN ON authors.id = author_ISBN.id ORDER BY last, first", connection).head().to_string())

output.write("\n\nUsing the INSERT INTO statement\n\n")
cursor = connection.cursor()
cursor.execute("INSERT INTO authors (first, last) VALUES ('Sue','Red')")
output.write(pd.read_sql("SELECT id, first, last FROM authors", connection, index_col=["id"]).to_string())

output.write("\n\nUsing the UPDATE statement\n\n")
cursor.execute("UPDATE authors SET last='Black' WHERE last='Red' AND first='Sue'")
output.write(pd.read_sql("SELECT id, first, last FROM authors", connection, index_col=["id"]).to_string())

output.write("\n\nUsing the DELETE FROM statement\n\n")
cursor.execute("DELETE FROM authors WHERE id=6")
output.write(pd.read_sql("SELECT id, first, last FROM authors", connection, index_col=["id"]).to_string())

output.close()
connection.close()
