import sqlite3
import pandas as pd

connection = sqlite3.connect("books.db")
output = open("Part2Output.txt", "w")

output.write("Select all authors' last names from the authors table in descending order.\n\n")
output.write(pd.read_sql("SELECT last FROM authors ORDER BY last DESC", connection).to_string())

output.write("\n\nSelect all book titles from the titles table in ascending order.\n\n")
output.write(pd.read_sql("SELECT title FROM titles ORDER BY title ASC", connection).to_string())

output.write("\n\nUse an INNER JOIN to select all the books for a specific author. Include the title, copyright year, and ISBN. Order the information alphabeticlaly by title.\n\n")
output.write(pd.read_sql("SELECT title, first, last, copyright, titles.isbn FROM titles INNER JOIN author_ISBN ON titles.isbn = author_ISBN.isbn INNER JOIN authors ON authors.id = author_ISBN.id WHERE first = 'Harvey' AND last = 'Deitel' ORDER BY title ASC", connection).to_string())

output.write("\n\nInsert a new author into the authors table.\n\n")
cursor = connection.cursor()
cursor.execute("INSERT INTO authors (first, last) VALUES ('John', 'Doe')")
output.write(pd.read_sql("SELECT * from authors", connection, index_col=["id"]).to_string())

output.write("\n\nInsert a new title for an author.\n\n")
cursor.execute("INSERT INTO titles (isbn, title, edition, copyright) VALUES ('0123456789', 'Sample Book Title', '1', '1970')")
cursor.execute("INSERT INTO author_ISBN (id, isbn) VALUES ('6','0123456789')")
output.write(pd.read_sql("SELECT id, titles.isbn, title, edition, copyright FROM titles INNER JOIN author_ISBN ON titles.isbn = author_ISBN.isbn WHERE id = '6'", connection).to_string())

output.close()
connection.close()
