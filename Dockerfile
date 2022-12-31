FROM python:3.9
# 
WORKDIR /api
# 
COPY /api/requirements.txt /api/requirements.txt
# 
RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt
# 
COPY /api ../api/api

COPY /db ../api/db
# 

EXPOSE 8000

CMD ["uvicorn", "api.main:app"]