from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal
from middleware.application_middleware import default_dependency, platform_auth_platform_auth_middleware_group_dependency


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/tags/')
async def get_tags(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.get_tags(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/tags/id/')
async def get_tags_id(request: Request, query: schemas.GetTagsIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.get_tags_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/note_tags/')
async def get_note_tags(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.get_note_tags(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/notebooks/')
async def get_notebooks(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.get_notebooks(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/note_tags/note_id/')
async def delete_note_tags_note_id(request: Request, query: schemas.DeleteNoteTagsNoteIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.delete_note_tags_note_id(request, db, query.note_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/platform_auth_package/mayson/sso/auth/login/google')
async def get_platform_auth_package_mayson_sso_auth_login_google(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.get_platform_auth_package_mayson_sso_auth_login_google(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/notebooks/id/')
async def delete_notebooks_id(request: Request, query: schemas.DeleteNotebooksIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.delete_notebooks_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/platform_auth_package/mayson/auth/user/login')
async def post_platform_auth_package_mayson_auth_user_login(request: Request, raw_data: schemas.PostPlatformAuthPackageMaysonAuthUserLogin, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.post_platform_auth_package_mayson_auth_user_login(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/platform_auth_package/mayson/auth/user/register')
async def post_platform_auth_package_mayson_auth_user_register(request: Request, raw_data: schemas.PostPlatformAuthPackageMaysonAuthUserRegister, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.post_platform_auth_package_mayson_auth_user_register(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/tags/')
async def post_tags(request: Request, raw_data: schemas.PostTags, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.post_tags(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/tags/id/')
async def put_tags_id(request: Request, raw_data: schemas.PutTagsId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.put_tags_id(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/tags/id/')
async def delete_tags_id(request: Request, query: schemas.DeleteTagsIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.delete_tags_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/note_tags/note_id/')
async def get_note_tags_note_id(request: Request, query: schemas.GetNoteTagsNoteIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.get_note_tags_note_id(request, db, query.note_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/note_tags/')
async def post_note_tags(request: Request, raw_data: schemas.PostNoteTags, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.post_note_tags(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/note_tags/note_id/')
async def put_note_tags_note_id(request: Request, raw_data: schemas.PutNoteTagsNoteId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.put_note_tags_note_id(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/notes/')
async def get_notes(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.get_notes(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/notes/id/')
async def get_notes_id(request: Request, query: schemas.GetNotesIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.get_notes_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/notes/')
async def post_notes(request: Request, raw_data: schemas.PostNotes, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.post_notes(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/notes/id/')
async def put_notes_id(request: Request, raw_data: schemas.PutNotesId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.put_notes_id(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/notes/id/')
async def delete_notes_id(request: Request, query: schemas.DeleteNotesIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.delete_notes_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/notebooks/id/')
async def get_notebooks_id(request: Request, query: schemas.GetNotebooksIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.get_notebooks_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/notebooks/')
async def post_notebooks(request: Request, raw_data: schemas.PostNotebooks, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.post_notebooks(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/notebooks/id/')
async def put_notebooks_id(request: Request, raw_data: schemas.PutNotebooksId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.put_notebooks_id(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/')
async def get_users(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.get_users(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/id/')
async def get_users_id(request: Request, query: schemas.GetUsersIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.get_users_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(request: Request, raw_data: schemas.PostUsers, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.post_users(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/id/')
async def put_users_id(request: Request, raw_data: schemas.PutUsersId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.put_users_id(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/id/')
async def delete_users_id(request: Request, query: schemas.DeleteUsersIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.delete_users_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/platform_auth_package/mayson/sso/auth/callback/')
async def get_platform_auth_package_mayson_sso_auth_callback(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.get_platform_auth_package_mayson_sso_auth_callback(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

