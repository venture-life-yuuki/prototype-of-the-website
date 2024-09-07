from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# グローバル設定
LANGUAGES = {
    'en': 'English',
    'sv': 'Svenska'
}

# ルートページ
@app.route('/')
def home():
    lang = request.cookies.get('lang', 'en')
    return render_template('index.html', lang=lang, languages=LANGUAGES)

# 言語変更
@app.route('/set_language/<lang>')
def set_language(lang):
    if lang in LANGUAGES:
        resp = redirect(url_for('home'))
        resp.set_cookie('lang', lang)
        return resp
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
