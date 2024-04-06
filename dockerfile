FROM python:3.10
WORKDIR /code
COPY requirements.txt ./requirements.txt
COPY QuestionProcessor.py ./QuestionProcessor.py
RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "QuestionProcessor:app", "--host", "0.0.0.0", "--port", "8000"]