from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple,Union

import re

class Users(BaseModel):
    email: Optional[str]=None
    password: Optional[str]=None
    created_at_dt: Optional[Any]=None


class ReadUsers(BaseModel):
    email: Optional[str]=None
    password: Optional[str]=None
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True


class Notebooks(BaseModel):
    user_id: Optional[Union[int, float]]=None
    title: Optional[str]=None
    color_hex: Optional[str]=None
    created_at_dt: Optional[Any]=None


class ReadNotebooks(BaseModel):
    user_id: Optional[Union[int, float]]=None
    title: Optional[str]=None
    color_hex: Optional[str]=None
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True


class Notes(BaseModel):
    user_id: Optional[Union[int, float]]=None
    notebook_id: Optional[Union[int, float]]=None
    title: Optional[str]=None
    content: Optional[str]=None
    created_at_dt: Optional[Any]=None


class ReadNotes(BaseModel):
    user_id: Optional[Union[int, float]]=None
    notebook_id: Optional[Union[int, float]]=None
    title: Optional[str]=None
    content: Optional[str]=None
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True


class Tags(BaseModel):
    user_id: Optional[Union[int, float]]=None
    name: Optional[str]=None
    created_at_dt: Optional[Any]=None


class ReadTags(BaseModel):
    user_id: Optional[Union[int, float]]=None
    name: Optional[str]=None
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True


class NoteTags(BaseModel):
    note_id: int
    tag_id: int


class ReadNoteTags(BaseModel):
    note_id: int
    tag_id: int
    class Config:
        from_attributes = True




class PostPlatformAuthPackageMaysonAuthUserLogin(BaseModel):
    email: str = Field(..., max_length=100)
    password: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostPlatformAuthPackageMaysonAuthUserRegister(BaseModel):
    email: str = Field(..., max_length=100)
    password: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostTags(BaseModel):
    user_id: Optional[int]=None
    name: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutTagsId(BaseModel):
    id: int = Field(...)
    user_id: Optional[int]=None
    name: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostNoteTags(BaseModel):
    note_id: int = Field(...)
    tag_id: int = Field(...)

    class Config:
        from_attributes = True



class PutNoteTagsNoteId(BaseModel):
    note_id: int = Field(...)
    tag_id: int = Field(...)

    class Config:
        from_attributes = True



class PostNotes(BaseModel):
    user_id: Optional[int]=None
    notebook_id: Optional[int]=None
    title: Optional[str]=None
    content: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutNotesId(BaseModel):
    id: int = Field(...)
    user_id: Optional[int]=None
    notebook_id: Optional[int]=None
    title: Optional[str]=None
    content: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostNotebooks(BaseModel):
    user_id: Optional[int]=None
    title: Optional[str]=None
    color_hex: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutNotebooksId(BaseModel):
    id: int = Field(...)
    user_id: Optional[int]=None
    title: Optional[str]=None
    color_hex: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostUsers(BaseModel):
    email: Optional[str]=None
    password: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutUsersId(BaseModel):
    id: int = Field(...)
    email: Optional[str]=None
    password: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



# Query Parameter Validation Schemas

class GetTagsIdQueryParams(BaseModel):
    """Query parameter validation for get_tags_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteNoteTagsNoteIdQueryParams(BaseModel):
    """Query parameter validation for delete_note_tags_note_id"""
    note_id: Optional[Union[int, float]] = Field(None)

    class Config:
        populate_by_name = True


class DeleteNotebooksIdQueryParams(BaseModel):
    """Query parameter validation for delete_notebooks_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteTagsIdQueryParams(BaseModel):
    """Query parameter validation for delete_tags_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetNoteTagsNoteIdQueryParams(BaseModel):
    """Query parameter validation for get_note_tags_note_id"""
    note_id: Optional[Union[int, float]] = Field(None)

    class Config:
        populate_by_name = True


class GetNotesIdQueryParams(BaseModel):
    """Query parameter validation for get_notes_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteNotesIdQueryParams(BaseModel):
    """Query parameter validation for delete_notes_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetNotebooksIdQueryParams(BaseModel):
    """Query parameter validation for get_notebooks_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetUsersIdQueryParams(BaseModel):
    """Query parameter validation for get_users_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteUsersIdQueryParams(BaseModel):
    """Query parameter validation for delete_users_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True
