from fastapi import APIRouter

from comments import CommentModel, EditCommentModel

from database.comment_service import add_comment_db, edit_comment_db, delete_comment_db, get_post_comments

coms_router = APIRouter(prefix='/comment', tags=['work with comments'])

@coms_router.post('/add_comment')
async def add_comment(data: CommentModel):
    pass

@coms_router.put('/edit_comment')
async def change_comment(data: EditCommentModel):
    pass

@coms_router.delete('/delete_comment')
async def delete_comment(comment_id: int):
    pass

@coms_router.get('/get_comments')
async def get_comments(post_id: int):
    pass