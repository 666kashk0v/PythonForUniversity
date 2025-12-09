class Library:
    objects_count = 0 #статическая переменная, которая делит состояние между всеми объектами класса

    #конструктор, которой инициализирует объекты класса library и управляет счетчиком
    def __init__(self, books=None):
            if books is not None:
                self.books = books
            else:
                self.books = {}
            Library.objects_count += 1

    def add_book(self, title, available):
        self.books[title] = available

    def remove_book(self, title):
        if title in self.books: #удалит только существующую книгу
            del self.books[title]
        else:
            print(f"Книга '{title}' не найдена.")

    def find_book(self, title):
        if title in self.books: #если есть в библиотеке то проверяем дальше статус
            if self.books[title] == True:
                print(f"Книга '{title}' есть в библиотеке и доступна.")
            else:
                print(f"Книга '{title}' есть в библиотеке, но недоступна.")
        else: #если книги в библиотеке не оказалось
            print(f"Книга '{title}' не найдена в библиотеке.")

    def show_all_available(self):
        for title, available in self.books.items():
            if available == True: #если доступна, то показываем
                print(f"{title}: Available")


    #статический метод, который работает со статической переменной objects_count
    @classmethod # декоратор, который делает метод статическим
    def get_objects_count(cls):
        return cls.objects_count


lib1 = Library()
lib1.add_book("Высокоуровневость хорошо?", False)
lib1.add_book("Низкий/средний уровень абстракции хорошо?", True)
lib1.add_book("Высокоуровневость хорошо?", False)
lib1.add_book("Низкий/средний уровень абстракции хорошо?", True)
lib1.add_book("Питон нормальный ЯП", False)
lib1.add_book("C# хороший ЯП?", True)
lib1.show_all_available() #проверка есть ли книга
lib1.find_book("C# хороший ЯП?")
lib1.find_book("Питон хороший ЯП!")

lib2 = Library({"Война и мир": True})

lib3 = Library()

print(Library.get_objects_count())  #подсчет кол-ва объектов класса, т.е библиотек

