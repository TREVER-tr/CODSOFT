#include <iostream>
#include <vector>
#include <string>
#include <ctime>

using namespace std;

struct Book {
    string title, author, ISBN;
    bool isAvailable;
    time_t dueDate;

    Book(string t, string a, string i) : title(t), author(a), ISBN(i), isAvailable(true), dueDate(0) {}
};

struct Borrower {
    string name;
    vector<Book*> borrowedBooks;

    Borrower(string n) : name(n) {}

    void borrowBook(Book &book) {
        if (book.isAvailable) {
            borrowedBooks.push_back(&book);
            book.isAvailable = false;
            time(&book.dueDate);  // Set due date to current time for simplicity
            cout << "Book borrowed successfully!\n";
        } else {
            cout << "Book is currently unavailable.\n";
        }
    }

    void returnBook(Book &book) {
        for (size_t i = 0; i < borrowedBooks.size(); i++) {
            if (borrowedBooks[i]->ISBN == book.ISBN) {
                book.isAvailable = true;
                borrowedBooks.erase(borrowedBooks.begin() + i);
                cout << "Book returned successfully!\n";
                return;
            }
        }
        cout << "This book was not borrowed by " << name << ".\n";
    }
};

vector<Book> books;        // Library book database
vector<Borrower> borrowers; // Borrower database

void addBook() {
    string title, author, ISBN;
    cout << "Enter book title: "; cin.ignore(); getline(cin, title);
    cout << "Enter author name: "; getline(cin, author);
    cout << "Enter ISBN: "; cin >> ISBN;
    books.emplace_back(title, author, ISBN);
    cout << "Book added successfully!\n";
}

void searchBook() {
    string keyword;
    cout << "Enter title, author, or ISBN to search: ";
    cin.ignore();
    getline(cin, keyword);

    for (auto &book : books) {
        if (book.title == keyword || book.author == keyword || book.ISBN == keyword) {
            cout << "Found: " << book.title << " by " << book.author << " | ISBN: " << book.ISBN << " | Status: " 
                 << (book.isAvailable ? "Available" : "Checked Out") << endl;
            return;
        }
    }
    cout << "No matching book found.\n";
}

void borrowBook() {
    string ISBN, borrowerName;
    cout << "Enter borrower's name: "; cin.ignore(); getline(cin, borrowerName);
    cout << "Enter ISBN of the book to borrow: "; cin >> ISBN;

    Borrower *borrower = nullptr;
    for (auto &b : borrowers) {
        if (b.name == borrowerName) {
            borrower = &b;
            break;
        }
    }

    if (!borrower) {
        borrower = new Borrower(borrowerName);
        borrowers.push_back(*borrower);
    }

    for (auto &book : books) {
        if (book.ISBN == ISBN) {
            borrower->borrowBook(book);
            return;
        }
    }
    cout << "Book not found.\n";
}

void returnBook() {
    string ISBN, borrowerName;
    cout << "Enter borrower's name: "; cin.ignore(); getline(cin, borrowerName);
    cout << "Enter ISBN of the book to return: "; cin >> ISBN;

    for (auto &b : borrowers) {
        if (b.name == borrowerName) {
            for (auto &book : books) {
                if (book.ISBN == ISBN) {
                    b.returnBook(book);
                    return;
                }
            }
        }
    }
    cout << "Borrower or book not found.\n";
}

void calculateFine() {
    double fineRate = 2.0;  // Example fine rate per day
    time_t currentTime;
    time(&currentTime);

    for (auto &borrower : borrowers) {
        for (auto book : borrower.borrowedBooks) {
            double overdueDays = difftime(currentTime, book->dueDate) / (60 * 60 * 24);
            if (overdueDays > 7) { // Example: Fine after 7 days
                cout << "Overdue book: " << book->title << " | Borrower: " << borrower.name
                     << " | Fine: $" << (overdueDays - 7) * fineRate << endl;
            }
        }
    }
}

int main() {
    int choice;
    do {
        cout << "\nLibrary Management System\n";
        cout << "1. Add Book\n2. Search Book\n3. Borrow Book\n4. Return Book\n5. Calculate Fine\n6. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;

        switch (choice) {
            case 1: addBook(); break;
            case 2: searchBook(); break;
            case 3: borrowBook(); break;
            case 4: returnBook(); break;
            case 5: calculateFine(); break;
            case 6: cout << "Exiting...\n"; break;
            default: cout << "Invalid choice, try again!\n";
        }
    } while (choice != 6);

    return 0;
}

