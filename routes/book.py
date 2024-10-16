from flask import Blueprint,request,jsonify

books_bp=Blueprint("books",__name__)

books=[]   #in memory storage

# Get endpoint to fetch all books item
@books_bp.route("/",methods=["GET"])
def get_books():
    return jsonify(books)


# post endpoint to create a new book item

@books_bp.route("/",methods=["POST"])
def create_books():
    book={
        "id":len(books)+1,
        "title":request.json.get("title"),
        "completed":request.json.get("completed",False)
    }
    books.append(book)
    return jsonify(book),201


# PUT endpoint to update
@books_bp.route("/<int:id>",methods=["PUT"])
def update_book(id):
    book=next((b for b in books if b["id"]==id),None)
    if book is None:
        return jsonify({"error":"Book not found"}),404
    book["title"]=request.json.get("title",book["title"])
    book["completed"]=request.json.get("completed",book["completed"])
    return jsonify(book)

# Get by id
@books_bp.route("/<int:id>",methods=["GET"])
def get_book_only_by_id(id):
    book = next((b for b in books if b["id"] == id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book)

# Delete book item

@books_bp.route("/<int:id>", methods=["DELETE"])
def delete_book(id):
    global books
    book_to_delete = next((b for b in books if b["id"] == id), None)
    if book_to_delete is None:
        return {"message": "Book not found"}, 404
    books = [b for b in books if b["id"] != id]
    return '', 204

# handler for error
@books_bp.errorhandler(404)
def not_found(e):
    return jsonify({"error":"Resource not found"}),404

