FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git build-essential libldap2-dev libsasl2-dev libssl-dev \
    libpq-dev python3-dev curl && rm -rf /var/lib/apt/lists/*

# Create app dir
WORKDIR /app

# Copy code
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8069

CMD ["./odoo/odoo-bin", "-c", "odoo_docker.conf"]