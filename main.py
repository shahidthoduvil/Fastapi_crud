
 

from fastapi import FastAPI

app=FastAPI()

@app.get('/',tags=['Root'])
async def root():
    return {'message':'pingpong'}


# creating a crud api using fast api


# Get 
@app.get('/todo/',tags=['Todos'])
async def Get_todo():
    return {'data':todos}

# Post
@app.post('/todo/',tags=['Todos'])
async def add_todo(todo:dict):
    todos.append(todo)
    return {
        'data':'A todo has been added !'
    }
# Put
@app.put('/todo/{id}',tags=['Todos'])
async def update_todo(id:int,body:dict):
    for todo in todos:
        if int((todo['id']))==id:
            todo['Activity']=body['Activity']
            return  {
                'data':f'Todo with id {id} has been updated'
            }
    
    return{
        'data':f'Todo with id{id} is not found'
    }


# Delete

@app.delete('/todo/{id}',tags=['Todos'])
async def Delete_todo(id:int)  -> dict:
    for todo in todos:
        if int((todo['id']))==id:
            todos.remove(todo)
            return {
                'data':'Todo with id {id} is has been updated '
            }
        
    return {
        'data':'Todo  with id {id} wasnt found'
    }



todos=[

    {
    'id':1,
    'Activity':'fast api is python framework for creating apis'
    },

  {
    'id':2,
    'Activity':' high performance, easy to learn, fast to code, ready for production',
    },
]








# import uvicorn


# if __name__ == "__main__":
#     uvicorn.run("app.app:app", port=8000, reload=True)