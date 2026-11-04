
from flask import Flask, render_template, Response

app = Flask(__name__)

# Endereço público do site
SITE_URL = "https://medidaweb.onrender.com"


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/sitemap.xml')
def sitemap():
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>{SITE_URL}/</loc>
    </url>
    <url>
        <loc>{SITE_URL}/sobre</loc>
    </url>
</urlset>
"""
    return Response(xml, mimetype='application/xml')


@app.route('/robots.txt')
def robots():
    texto = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
    return Response(texto, mimetype='text/plain')


if __name__ == '__main__':
    app.run(debug=True)
