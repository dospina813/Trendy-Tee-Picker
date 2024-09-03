from flask import render_template
from flask import current_app as app
import random

def register_routes(app):
    @app.route("/")
    def home_route():
        tshirts = [
            {"image": "https://example.com/tshirt1.jpg", "url": "https://example.com/buy1", "source": "Site 1"},
            {"image": "https://example.com/tshirt2.jpg", "url": "https://example.com/buy2", "source": "Site 2"},
            {"image": "https://example.com/tshirt3.jpg", "url": "https://example.com/buy3", "source": "Site 3"},
            {"image": "https://example.com/tshirt4.jpg", "url": "https://example.com/buy4", "source": "Site 4"},
            {"image": "https://example.com/tshirt5.jpg", "url": "https://example.com/buy5", "source": "Site 5"},
            {"image": "https://example.com/tshirt6.jpg", "url": "https://example.com/buy6", "source": "Site 6"},
            {"image": "https://example.com/tshirt7.jpg", "url": "https://example.com/buy7", "source": "Site 7"},
            {"image": "https://example.com/tshirt8.jpg", "url": "https://example.com/buy8", "source": "Site 8"},
            {"image": "https://example.com/tshirt9.jpg", "url": "https://example.com/buy9", "source": "Site 9"},
            {"image": "https://example.com/tshirt10.jpg", "url": "https://example.com/buy10", "source": "Site 10"}
        ]
        selected_tshirts = random.sample(tshirts, 6)
        return render_template("home.html", tshirts=selected_tshirts)