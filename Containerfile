# Python Workshop Container
# Build: podman build -t python-workshop .
# Run:   podman run -p 5000:5000 python-workshop

FROM registry.access.redhat.com/ubi9/python-311:latest

LABEL maintainer="Red Hat Python Workshop"
LABEL description="Interactive Python learning application"

# Set working directory
WORKDIR /app

# Copy requirements first for better layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download TextBlob corpora (needed for NLP features)
RUN python -c "import nltk; nltk.download('punkt'); nltk.download('averaged_perceptron_tagger')"

# Copy application files
COPY app.py .
COPY templates/ templates/
COPY static/ static/

# Expose port
EXPOSE 5000

# Environment variables for Flask
ENV FLASK_HOST=0.0.0.0
ENV FLASK_PORT=5000
ENV FLASK_DEBUG=false

# Run the application
CMD ["python", "app.py"]
