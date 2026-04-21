from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DB_NAME = "foods.db"


def get_connection() -> sqlite3.Connection:
    return sqlite3.connect(DB_NAME)


def init_db() -> None:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS foods (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            notes TEXT
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
    cursor.execute("SELECT id, name, notes FROM foods ORDER BY id DESC")
    foods = cursor.fetchall()
    conn.close()
    return render_template("index.html", foods=foods)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        notes = request.form["notes"]

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO foods (name, notes) VALUES (?, ?)",
            (name, notes),
        )
        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    return render_template("add.html")


@app.route("/delete/<int:food_id>")
def delete(food_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM foods WHERE id = ?", (food_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


@app.route("/edit/<int:food_id>", methods=["GET", "POST"])
def edit(food_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        name = request.form["name"]
        notes = request.form["notes"]

        cursor.execute(
            "UPDATE foods SET name = ?, notes = ? WHERE id = ?",
            (name, notes, food_id),
        )
        conn.commit()
        conn.close()
        return redirect(url_for("index"))

    cursor.execute("SELECT id, name, notes FROM foods WHERE id = ?", (food_id,))
    food = cursor.fetchone()
    conn.close()
    return render_template("edit.html", food=food)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
