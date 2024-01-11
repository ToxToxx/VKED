class Book:
    def __init__(self, isbn, title, year):
        self.isbn = isbn
        self.title = title
        self.year = year

def merge_sort(books):
    if len(books) > 1:
        mid = len(books) // 2
        left_half = books[:mid]
        right_half = books[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i].year < right_half[j].year or (left_half[i].year == right_half[j].year and left_half[i].title < right_half[j].title):
                books[k] = left_half[i]
                i += 1
            else:
                books[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            books[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            books[k] = right_half[j]
            j += 1
            k += 1

if __name__ == "__main__":
    n = int(input())
    books = []

    for _ in range(n):
        line = input().split()
        isbn = int(line[0])
        title = " ".join(line[1:-1])[1:-1]
        year = int(line[-1])
        books.append(Book(isbn, title, year))

    merge_sort(books)

    for book in books:
        print(f"{book.isbn} \"{book.title}\" {book.year}")
