FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app
COPY telemetry_tool.py test_telemetry_tool.py sample_telemetry.csv ./
RUN python -m unittest -v
ENTRYPOINT ["python", "telemetry_tool.py"]
CMD ["sample_telemetry.csv"]
