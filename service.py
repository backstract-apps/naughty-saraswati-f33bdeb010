from sqlalchemy.orm import Session, aliased
from database import SessionLocal
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException, status
import models, schemas
import boto3
import jwt
from datetime import datetime
import requests
import math
import random
import asyncio
from pathlib import Path


def convert_to_datetime(date_string):
    if date_string is None:
        return datetime.now()
    if not date_string.strip():
        return datetime.now()
    if "T" in date_string:
        try:
            return datetime.fromisoformat(date_string.replace("Z", "+00:00"))
        except ValueError:
            date_part = date_string.split("T")[0]
            try:
                return datetime.strptime(date_part, "%Y-%m-%d")
            except ValueError:
                return datetime.now()
    else:
        # Try to determine format based on first segment
        parts = date_string.split("-")
        if len(parts[0]) == 4:
            # Likely YYYY-MM-DD format
            try:
                return datetime.strptime(date_string, "%Y-%m-%d")
            except ValueError:
                return datetime.now()

        # Try DD-MM-YYYY format
        try:
            return datetime.strptime(date_string, "%d-%m-%Y")
        except ValueError:
            return datetime.now()

        # Fallback: try YYYY-MM-DD if not already tried
        if len(parts[0]) != 4:
            try:
                return datetime.strptime(date_string, "%Y-%m-%d")
            except ValueError:
                return datetime.now()

        return datetime.now()


async def get_tags(request: Request, db: Session):

    query = db.query(models.Tags)

    tags_all = query.all()
    tags_all = [new_data.to_dict() for new_data in tags_all] if tags_all else tags_all

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"tags_all": tags_all},
    }
    return res


async def get_tags_id(request: Request, db: Session, id: Union[int, float]):

    query = db.query(models.Tags)
    query = query.filter(and_(models.Tags.id == id))

    tags_one = query.first()

    tags_one = (
        (tags_one.to_dict() if hasattr(tags_one, "to_dict") else vars(tags_one))
        if tags_one
        else tags_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"tags_one": tags_one},
    }
    return res


async def get_note_tags(request: Request, db: Session):

    query = db.query(models.NoteTags)

    note_tags_all = query.all()
    note_tags_all = (
        [new_data.to_dict() for new_data in note_tags_all]
        if note_tags_all
        else note_tags_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"note_tags_all": note_tags_all},
    }
    return res


async def get_notebooks(request: Request, db: Session):

    query = db.query(models.Notebooks)

    notebooks_all = query.all()
    notebooks_all = (
        [new_data.to_dict() for new_data in notebooks_all]
        if notebooks_all
        else notebooks_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"notebooks_all": notebooks_all},
    }
    return res


async def delete_note_tags_note_id(
    request: Request, db: Session, note_id: Union[int, float]
):

    query = db.query(models.NoteTags)
    query = query.filter(and_(models.NoteTags.note_id == note_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        note_tags_deleted = record_to_delete.to_dict()
    else:
        note_tags_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"note_tags_deleted": note_tags_deleted},
    }
    return res


async def get_platform_auth_package_mayson_sso_auth_login_google(
    request: Request, db: Session
):

    # define client

    try:
        import httpx

        async def google_login():
            async with httpx.AsyncClient() as client:
                headers = {
                    "Authorization": "Bearer v4.public.eyJlbWFpbF9pZCI6ICJzaGl2YW10ZXN0aW5ncmVsZWFzZUB5b3BtYWlsLmNvbSIsICJ1c2VyX2lkIjogIjEyMGMxZTA1MGQ0OTQ5ZTRiZTdmNzg0MWJmOGNkNTI5IiwgIm9yZ19pZCI6ICJOQSIsICJzdGF0ZSI6ICJzaWdudXAiLCAicm9sZV9uYW1lIjogIk5BIiwgInJvbGVfaWQiOiAiTkEiLCAicGxhbl9pZCI6ICIxMTIiLCAiYWNjb3VudF92ZXJpZmllZCI6ICIxIiwgImFjY291bnRfc3RhdHVzIjogIjAiLCAidXNlcl9uYW1lIjogIjEyMGMxZTA1MGQ0OTQ5ZTRiZTdmNzg0MWJmOGNkNTI5IiwgInNpZ251cF9xdWVzdGlvbiI6IDAsICJ0b2tlbl9saW1pdCI6IG51bGwsICJ0b2tlbl90eXBlIjogImFjY2VzcyIsICJleHAiOiAxNzc0MzU2ODQ3LCAiZXhwaXJ5X3RpbWUiOiAxNzc0MzU2ODQ3fe1BXfbCR9nhC743zq4Tr3crzSlbGuDtRDb7FC-Q1VK1Q4FZf_JdMubzEGgipyUfiH3fb0XMqjFblnwMsAz60wU",
                    "Content-Type": "application/json",
                }

                res = await client.get(
                    "https://api-release.beemerbenzbentley.site/sigma/api/v1/sso/auth/google/login?collection_id=coll_5b470af4607143dfa3320626b0520f2a",
                    headers=headers,
                )

            res.raise_for_status()
            print(res.json())

        await google_login()
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

    res = {
        "status": 200,
        "message": "The request has been successfully processed",
        "data": {"message": "success_response"},
    }
    return res


async def delete_notebooks_id(request: Request, db: Session, id: Union[int, float]):

    query = db.query(models.Notebooks)
    query = query.filter(and_(models.Notebooks.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        notebooks_deleted = record_to_delete.to_dict()
    else:
        notebooks_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"notebooks_deleted": notebooks_deleted},
    }
    return res


async def post_platform_auth_package_mayson_auth_user_login(
    request: Request,
    db: Session,
    raw_data: schemas.PostPlatformAuthPackageMaysonAuthUserLogin,
):
    email: str = raw_data.email
    password: str = raw_data.password

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.email == email))

    oneRecord = query.first()

    oneRecord = (
        (oneRecord.to_dict() if hasattr(oneRecord, "to_dict") else vars(oneRecord))
        if oneRecord
        else oneRecord
    )

    if oneRecord:
        from passlib.hash import md5_crypt

        password_hash = oneRecord["password"]
        password_valid = md5_crypt.verify(password, password_hash)
        if password_valid:
            validated_password = True
        else:
            validated_password = False
    else:
        validated_password = False

    login_status: str = "Login initiated"

    if validated_password:

        login_status = "Login success"

    else:

        raise HTTPException(status_code=401, detail="Bad credentials.")

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.email == email))

    user_record = query.first()

    user_record = (
        (
            user_record.to_dict()
            if hasattr(user_record, "to_dict")
            else vars(user_record)
        )
        if user_record
        else user_record
    )

    import jwt
    from datetime import timezone

    secret_key = """8KPuI_ePISMHwSy8Ri8m-1nc9SrctI10kAChutnCRhI="""
    bs_jwt_payload = {
        "exp": int(datetime.now(timezone.utc).timestamp() + 86400),
        "data": user_record,
    }

    generated_jwt = jwt.encode(bs_jwt_payload, secret_key, algorithm="HS256")

    login_status = "Login successful"

    res = {
        "status": 200,
        "message": "Login successful",
        "data": {"jwt": generated_jwt, "login_status": login_status},
    }
    return res


async def post_platform_auth_package_mayson_auth_user_register(
    request: Request,
    db: Session,
    raw_data: schemas.PostPlatformAuthPackageMaysonAuthUserRegister,
):
    email: str = raw_data.email
    password: str = raw_data.password

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.email == email))

    existing_record = query.first()

    existing_record = (
        (
            existing_record.to_dict()
            if hasattr(existing_record, "to_dict")
            else vars(existing_record)
        )
        if existing_record
        else existing_record
    )

    if existing_record:

        raise HTTPException(status_code=400, detail="User already exists.")
    else:
        pass

    from passlib.hash import md5_crypt

    encrypt_pass = md5_crypt.hash(password)

    record_to_be_added = {"email": email, "password": encrypt_pass}
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    # db.refresh(new_users)
    post_user_record = new_users.to_dict()

    res = {"status": 200, "message": "User registered successfully", "data": {}}
    return res


async def post_tags(
    request: Request,
    db: Session,
    raw_data: schemas.PostTags,
):
    user_id: Union[int, float] = raw_data.user_id
    name: str = raw_data.name
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    record_to_be_added = {
        "name": name,
        "user_id": user_id,
        "created_at_dt": created_at_dt,
    }
    new_tags = models.Tags(**record_to_be_added)
    db.add(new_tags)
    db.commit()
    # db.refresh(new_tags)
    tags_inserted_record = new_tags.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"tags_inserted_record": tags_inserted_record},
    }
    return res


async def put_tags_id(
    request: Request,
    db: Session,
    raw_data: schemas.PutTagsId,
):
    id: Union[int, float] = raw_data.id
    user_id: Union[int, float] = raw_data.user_id
    name: str = raw_data.name
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    query = db.query(models.Tags)
    query = query.filter(and_(models.Tags.id == id))
    tags_edited_record = query.first()

    if tags_edited_record:
        for key, value in {
            "id": id,
            "name": name,
            "user_id": user_id,
            "created_at_dt": created_at_dt,
        }.items():
            setattr(tags_edited_record, key, value)

        db.commit()

        # db.refresh(tags_edited_record)

        tags_edited_record = (
            tags_edited_record.to_dict()
            if hasattr(tags_edited_record, "to_dict")
            else vars(tags_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"tags_edited_record": tags_edited_record},
    }
    return res


async def delete_tags_id(request: Request, db: Session, id: Union[int, float]):

    query = db.query(models.Tags)
    query = query.filter(and_(models.Tags.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        tags_deleted = record_to_delete.to_dict()
    else:
        tags_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"tags_deleted": tags_deleted},
    }
    return res


async def get_note_tags_note_id(
    request: Request, db: Session, note_id: Union[int, float]
):

    query = db.query(models.NoteTags)
    query = query.filter(and_(models.NoteTags.note_id == note_id))

    note_tags_one = query.first()

    note_tags_one = (
        (
            note_tags_one.to_dict()
            if hasattr(note_tags_one, "to_dict")
            else vars(note_tags_one)
        )
        if note_tags_one
        else note_tags_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"note_tags_one": note_tags_one},
    }
    return res


async def post_note_tags(
    request: Request,
    db: Session,
    raw_data: schemas.PostNoteTags,
):
    note_id: Union[int, float] = raw_data.note_id
    tag_id: Union[int, float] = raw_data.tag_id

    record_to_be_added = {"tag_id": tag_id, "note_id": note_id}
    new_note_tags = models.NoteTags(**record_to_be_added)
    db.add(new_note_tags)
    db.commit()
    # db.refresh(new_note_tags)
    note_tags_inserted_record = new_note_tags.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"note_tags_inserted_record": note_tags_inserted_record},
    }
    return res


async def put_note_tags_note_id(
    request: Request,
    db: Session,
    raw_data: schemas.PutNoteTagsNoteId,
):
    note_id: Union[int, float] = raw_data.note_id
    tag_id: Union[int, float] = raw_data.tag_id

    query = db.query(models.NoteTags)
    query = query.filter(and_(models.NoteTags.note_id == note_id))
    note_tags_edited_record = query.first()

    if note_tags_edited_record:
        for key, value in {"tag_id": tag_id, "note_id": note_id}.items():
            setattr(note_tags_edited_record, key, value)

        db.commit()

        # db.refresh(note_tags_edited_record)

        note_tags_edited_record = (
            note_tags_edited_record.to_dict()
            if hasattr(note_tags_edited_record, "to_dict")
            else vars(note_tags_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"note_tags_edited_record": note_tags_edited_record},
    }
    return res


async def get_notes(request: Request, db: Session):

    query = db.query(models.Notes)

    notes_all = query.all()
    notes_all = (
        [new_data.to_dict() for new_data in notes_all] if notes_all else notes_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"notes_all": notes_all},
    }
    return res


async def get_notes_id(request: Request, db: Session, id: Union[int, float]):

    query = db.query(models.Notes)
    query = query.filter(and_(models.Notes.id == id))

    notes_one = query.first()

    notes_one = (
        (notes_one.to_dict() if hasattr(notes_one, "to_dict") else vars(notes_one))
        if notes_one
        else notes_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"notes_one": notes_one},
    }
    return res


async def post_notes(
    request: Request,
    db: Session,
    raw_data: schemas.PostNotes,
):
    user_id: Union[int, float] = raw_data.user_id
    notebook_id: Union[int, float] = raw_data.notebook_id
    title: str = raw_data.title
    content: str = raw_data.content
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    record_to_be_added = {
        "title": title,
        "content": content,
        "user_id": user_id,
        "notebook_id": notebook_id,
        "created_at_dt": created_at_dt,
    }
    new_notes = models.Notes(**record_to_be_added)
    db.add(new_notes)
    db.commit()
    # db.refresh(new_notes)
    notes_inserted_record = new_notes.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"notes_inserted_record": notes_inserted_record},
    }
    return res


async def put_notes_id(
    request: Request,
    db: Session,
    raw_data: schemas.PutNotesId,
):
    id: Union[int, float] = raw_data.id
    user_id: Union[int, float] = raw_data.user_id
    notebook_id: Union[int, float] = raw_data.notebook_id
    title: str = raw_data.title
    content: str = raw_data.content
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    query = db.query(models.Notes)
    query = query.filter(and_(models.Notes.id == id))
    notes_edited_record = query.first()

    if notes_edited_record:
        for key, value in {
            "id": id,
            "title": title,
            "content": content,
            "user_id": user_id,
            "notebook_id": notebook_id,
            "created_at_dt": created_at_dt,
        }.items():
            setattr(notes_edited_record, key, value)

        db.commit()

        # db.refresh(notes_edited_record)

        notes_edited_record = (
            notes_edited_record.to_dict()
            if hasattr(notes_edited_record, "to_dict")
            else vars(notes_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"notes_edited_record": notes_edited_record},
    }
    return res


async def delete_notes_id(request: Request, db: Session, id: Union[int, float]):

    query = db.query(models.Notes)
    query = query.filter(and_(models.Notes.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        notes_deleted = record_to_delete.to_dict()
    else:
        notes_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"notes_deleted": notes_deleted},
    }
    return res


async def get_notebooks_id(request: Request, db: Session, id: Union[int, float]):

    query = db.query(models.Notebooks)
    query = query.filter(and_(models.Notebooks.id == id))

    notebooks_one = query.first()

    notebooks_one = (
        (
            notebooks_one.to_dict()
            if hasattr(notebooks_one, "to_dict")
            else vars(notebooks_one)
        )
        if notebooks_one
        else notebooks_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"notebooks_one": notebooks_one},
    }
    return res


async def post_notebooks(
    request: Request,
    db: Session,
    raw_data: schemas.PostNotebooks,
):
    user_id: Union[int, float] = raw_data.user_id
    title: str = raw_data.title
    color_hex: str = raw_data.color_hex
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    record_to_be_added = {
        "title": title,
        "user_id": user_id,
        "color_hex": color_hex,
        "created_at_dt": created_at_dt,
    }
    new_notebooks = models.Notebooks(**record_to_be_added)
    db.add(new_notebooks)
    db.commit()
    # db.refresh(new_notebooks)
    notebooks_inserted_record = new_notebooks.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"notebooks_inserted_record": notebooks_inserted_record},
    }
    return res


async def put_notebooks_id(
    request: Request,
    db: Session,
    raw_data: schemas.PutNotebooksId,
):
    id: Union[int, float] = raw_data.id
    user_id: Union[int, float] = raw_data.user_id
    title: str = raw_data.title
    color_hex: str = raw_data.color_hex
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    query = db.query(models.Notebooks)
    query = query.filter(and_(models.Notebooks.id == id))
    notebooks_edited_record = query.first()

    if notebooks_edited_record:
        for key, value in {
            "id": id,
            "title": title,
            "user_id": user_id,
            "color_hex": color_hex,
            "created_at_dt": created_at_dt,
        }.items():
            setattr(notebooks_edited_record, key, value)

        db.commit()

        # db.refresh(notebooks_edited_record)

        notebooks_edited_record = (
            notebooks_edited_record.to_dict()
            if hasattr(notebooks_edited_record, "to_dict")
            else vars(notebooks_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"notebooks_edited_record": notebooks_edited_record},
    }
    return res


async def get_users(request: Request, db: Session):

    query = db.query(models.Users)

    users_all = query.all()
    users_all = (
        [new_data.to_dict() for new_data in users_all] if users_all else users_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_all": users_all},
    }
    return res


async def get_users_id(request: Request, db: Session, id: Union[int, float]):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    users_one = query.first()

    users_one = (
        (users_one.to_dict() if hasattr(users_one, "to_dict") else vars(users_one))
        if users_one
        else users_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_one": users_one},
    }
    return res


async def post_users(
    request: Request,
    db: Session,
    raw_data: schemas.PostUsers,
):
    email: str = raw_data.email
    password: str = raw_data.password
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    record_to_be_added = {
        "email": email,
        "password": password,
        "created_at_dt": created_at_dt,
    }
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    # db.refresh(new_users)
    users_inserted_record = new_users.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_inserted_record": users_inserted_record},
    }
    return res


async def put_users_id(
    request: Request,
    db: Session,
    raw_data: schemas.PutUsersId,
):
    id: Union[int, float] = raw_data.id
    email: str = raw_data.email
    password: str = raw_data.password
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))
    users_edited_record = query.first()

    if users_edited_record:
        for key, value in {
            "id": id,
            "email": email,
            "password": password,
            "created_at_dt": created_at_dt,
        }.items():
            setattr(users_edited_record, key, value)

        db.commit()

        # db.refresh(users_edited_record)

        users_edited_record = (
            users_edited_record.to_dict()
            if hasattr(users_edited_record, "to_dict")
            else vars(users_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_edited_record": users_edited_record},
    }
    return res


async def delete_users_id(request: Request, db: Session, id: Union[int, float]):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete.to_dict()
    else:
        users_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_deleted": users_deleted},
    }
    return res


async def get_platform_auth_package_mayson_sso_auth_callback(
    request: Request, db: Session
):

    # define client

    try:
        print(f"callback: {request}")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

    res = {
        "status": 200,
        "message": "The request has been successfully processed",
        "data": {"message": "success_response"},
    }
    return res
