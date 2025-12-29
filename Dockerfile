# =========================
# STAGE 1: BUILDER
# =========================

FROM python:3.12-slim AS builder

WORKDIR /app

# Instala dependencias del sistema necesarias (si tienes)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# =========================
# STAGE 2: RUNTIME (LIVIANO)
# =========================

FROM python:3.12-slim

WORKDIR /app

# Copiamos SOLO lo necesario
COPY --from=builder /install /usr/local
COPY app ./app

# Seguridad: no ejecutar como root
RUN useradd -m appuser
USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]