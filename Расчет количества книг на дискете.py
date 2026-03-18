# ТОО Найдите количество книг, которое можно разместить на дискете
disk_size_mb = 1.44
pages = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4

# Объём одной книги в байтах
book_size_bytes = pages * lines_per_page * chars_per_line * bytes_per_char

# Объём дискеты в байтах (1 Мб = 1024 Кб, 1 Кб = 1024 байта)
disk_size_bytes = disk_size_mb * 1024 * 1024

# Количество целых книг, помещающихся на дискете
num_books = int(disk_size_bytes // book_size_bytes)

print("Количество книг, помещающихся на дискету:", num_books)
