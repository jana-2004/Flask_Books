from flask import Flask,request,jsonify
from routes.book import books_bp
app=Flask(__name__)
app.register_blueprint(books_bp,url_prefix="/books")


# handler for error
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error":"Resource not found"}),404

if __name__=="__main__":
    app.run(debug=True,port=9090)