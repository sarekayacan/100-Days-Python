from flask import Flask, render_template, request

app = Flask(__name__)

# Örnek Blog Verileri
posts = [
    {"id": 1, "title": "Flask'e Giriş", "content": "Flask temelleri", "author": "Alice"},
    {"id": 2, "title": "Routing", "content": "Dinamik route kullanımı", "author": "Bob"},
    {"id": 3, "title": "Jinja2", "content": "Template motoru", "author": "Charlie"},
    {"id": 4, "title": "Blueprint", "content": "Proje yapısı", "author": "David"},
    {"id": 5, "title": "Pagination", "content": "Sayfalama mantığı", "author": "Eve"},
    {"id": 6, "title": "Search", "content": "Arama özelliği", "author": "Frank"},
]

POSTS_PER_PAGE = 3

@app.route("/")
def home():
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * POSTS_PER_PAGE
    end = start + POSTS_PER_PAGE

    paginated_posts = posts[start:end]
    total_pages = (len(posts) + POSTS_PER_PAGE - 1) // POSTS_PER_PAGE

    return render_template(
        "index.html",
        posts=paginated_posts,
        page=page,
        total_pages=total_pages
    )

@app.route("/post/<int:post_id>")
def post_detail(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)
    if not post:
        return "Post bulunamadı", 404
    return render_template("post.html", post=post)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/search")
def search():
    query = request.args.get("q", "")
    results = [p for p in posts if query.lower() in p["title"].lower()]
    return render_template("index.html", posts=results, page=1, total_pages=1)

if __name__ == "__main__":
    app.run(debug=True)
