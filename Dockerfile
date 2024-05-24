FROM python:3.9-slim
WORKDIR ./
COPY report.py/ ./report.py
RUN pip install requests
RUN mkdir /reports
CMD ["python", "report.py"]
