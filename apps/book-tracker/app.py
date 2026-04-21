from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DB_NAME = "books.db"


def get_connection() -> sqlite3.Connection:
    return sqlite3.connect(DB_NAME)


def init_db() -> None:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            date_read TEXT
        )
        """
    )
    conn.commit()
    conn.close()


init_db()


@app.route("/")
def index():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, title, author, date_read FROM books ORDER BY date_read DESC"
    )
    books = cursor.fetchall()
    conn.close()
    return render_template("index.html", books=books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        date_read = request.form["date_read"] or None

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO books (title, author, date_read) VALUES (?, ?, ?)",
            (title, author, date_read),
        )
        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    return render_template("add.html")


@app.route("/delete/<int:book_id>")
def delete(book_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        date_read = request.form["date_read"] or None

        cursor.execute(
            "UPDATE books SET title = ?, author = ?, date_read = ? WHERE id = ?",
            (title, author, date_read, book_id),
        )
        conn.commit()
        conn.close()
        return redirect(url_for("index"))

    cursor.execute(
        "SELECT id, title, author, date_read FROM books WHERE id = ?", (book_id,)
    )
    book = cursor.fetchone()
    conn.close()
    return render_template("edit.html", book=book)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
