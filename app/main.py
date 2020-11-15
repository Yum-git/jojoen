from flaskr.views import app

#Webアプリの起動
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)