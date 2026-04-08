from flask import Flask, render_template, request, send_file
import qrcode
import io

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    url = request.form.get("url")
    filename = request.form.get("filename", "qrcode")
    if not filename.endswith(".png"):
        filename += ".png"

    img = qrcode.make(url)
    buf = io.BytesIO()
    img.save(buf)
    buf.seek(0)

    return send_file(buf, mimetype="image/png", as_attachment=True, download_name=filename)

if __name__ == "__main__":
    app.run(debug=True)