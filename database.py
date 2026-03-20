

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(
     "sqlite+libsql:///embedded.db",
     connect_args={
         "sync_url": "libsql://coll-5b470af4607143dfa3320626b0520f2a-mayson.aws-ap-south-1.turso.io",
         "auth_token": "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NzM3NTIwMTIsInAiOnsicm9hIjp7Im5zIjpbIjAxOWNmYmRiLWI1MDEtNzQwMC04OGQwLTBhMTFkYTM3NGNiYyJdfSwicnciOnsibnMiOlsiMDE5Y2ZiZGItYjUwMS03NDAwLTg4ZDAtMGExMWRhMzc0Y2JjIl19fSwicmlkIjoiZWNjNTcxOTctMTMxOC00M2ExLWFiZWItZjI1NDEyMmQ5ZDdkIn0.fiFPOFo8YNUvCZpAakGrKdVynpdKoVqePx8CG6yJtC7-KaUXP01MnkFAIiKDPmXymbCANCCbTHklYYb5krZ_CA",
     },
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)
Base = declarative_base()

