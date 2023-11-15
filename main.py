from fastapi import FastAPI

from phot.photo_aapi import photo_router
from user.user_api import user_router
from post.post_api import posts_router

app = FastAPI(docs_url='/')

app.include_router(photo_router)
app.include_router(user_router)
app.include_router(posts_router)

@app.get('/test')
async def test():
    return 'This is test page'
