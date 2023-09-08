SELECT * FROM authors
JOIN favorites
ON authors.id = favorites.author_ID
LEFT JOIN books 
ON favorites.book_id = books.id
WHERE authors.id = 1