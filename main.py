from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def hello():
    return {'message':'Hello world'}
@app.get('/about')
def about():
    return {'message':'This is educational platform where you can run many more things and make real to your thoughts'}