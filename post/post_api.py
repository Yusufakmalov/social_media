from fastapi import APIRouter, UploadFile

from post import PublicPostValidator, EditPostValidator

from database.post_service import add_post_photo_db, edit_post_db, delete_post_db

posts_router = APIRouter(prefix='/user_post', tags=['work with publications'])

@posts_router.post('/public_post')
async def public_post(data: PublicPostValidator):
    pass

@posts_router.put('/change_post')
async def change_post(data: EditPostValidator):
    pass

@posts_router.delete('/delete_post')
async def delete_post(post_id: int):
    pass
@posts_router.get('/get_all_posts')
async def get_all_posts():
    pass

@posts_router.post('/add_photo')
async def add_photo():
    pass

@posts_router.get('/get_exact_post')
async def get_exact_post(post_id: int):
    pass
