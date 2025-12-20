# Layer 1: The Base OS
FROM python:3.9-slim

# Layer 2: Set working directory
WORKDIR /app

# Layer 3: Install Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Layer 4: Copy the Code
COPY . .

# Layer 5: Command to run
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
