from flaskr.views import app
import uvicorn

#Webアプリの起動
if __name__ == '__main__':
    uvicorn.run(app)
