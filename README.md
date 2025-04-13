PYTHONPATH=BackEnd alembic revision --autogenerate -m "description"
PYTHONPATH=BackEnd alembic upgrade head

 PYTHONPATH=BackEnd python BackEnd/app/utils/process_uploads.py