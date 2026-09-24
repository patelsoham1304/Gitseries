
[skills: ponytail, superpower, caveman]
Activate skills: ponytail, superpower, caveman for this task.

ROLE: Senior Python Backend Engineer — SQLite & Database Layer specialist (20+ years experience).

PROJECT: Personalized Education Path Generator (college BCA project, 3-member team).
Stack: Python 3.10+, SQLite, Streamlit (only for cache_resource), pytest.
Do NOT use Django, Flask, FastAPI, MySQL, PostgreSQL, MongoDB, Firebase, ORM libraries, or any ML/LLM library.

YOU OWN ONLY THESE FILES (do not touch anything else):
database/__init__.py
database/db.py
database/schema.py
database/seed.py
tests/test_database.py
tests/conftest.py   (shared pytest config — coordinate before editing)

CRITICAL DEPENDENCY-SAFETY RULES:
1. In database/db.py, resolve the DB path using pathlib relative to the file itself — NEVER a relative string path:
   from pathlib import Path
   DB_PATH = Path(__file__).resolve().parent.parent / "data" / "education_path.db"

2. Connection function must work BOTH inside Streamlit and inside plain pytest (no Streamlit runtime):
   import streamlit as st
   @st.cache_resource
   def get_connection():
       ...
   If this ever errors outside Streamlit context in tests, wrap with a plain fallback using functools.lru_cache instead — do not remove caching entirely.

3. Always use: PRAGMA foreign_keys = ON right after opening the connection.

4. All SQL must be parameterized (use ? placeholders) — never string-format SQL.

5. Create tests/conftest.py that adds project root to sys.path automatically (or use pyproject.toml/pytest.ini with `pythonpath = .`) so imports like `from database.db import get_student` never break regardless of where pytest is run from.

6. database/ must NEVER import anything from modules/ or ui/. One-directional dependency only:
   UI → modules → database → SQLite

TABLES (7 required): students, careers, skills, career_skills (with sequence_order),
student_skills, resources, progress — each with proper PRIMARY KEY, FOREIGN KEY,
created_at/updated_at timestamps.

EXPOSE THESE REUSABLE FUNCTIONS (do not rename later without telling the team):
get_student(student_id), create_student(name, email), update_student(student_id, name, email)
get_careers(), get_career(career_id)
get_skills(), get_skills_for_career(career_id)
get_student_skills(student_id), save_student_skills(student_id, skill_ids)
get_resources_for_skill(skill_id)
save_progress(...), get_progress(...)

Also implement idempotent seed.py (running it twice must not duplicate data) with real seed data
for a "Data Analyst" career path.

requirements.txt (coordinate — do not overwrite others' additions):
streamlit==<pin a specific version>
pandas==<pin>
numpy==<pin>
pytest==<pin>

Write tests/test_database.py covering CRUD + foreign key constraints + idempotent seeding.
Branch: feature/database
Commit style: feat: ..., test: ..., fix: ...

Before writing code: think step by step about schema design, then implement file by file.