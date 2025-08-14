class book:
    def __init__(self,title,author,page_count):
        self.title = title
        self.author = author
        self.page_count = page_count

    def display_info(self):
        return(f"{self.title}, by {self.author}, ({self.page_count} pages)")

book1 = book("Biology Book 4","Amani Paul",450)
print(book1.display_info())