# Specify our container base image
FROM python:3.9

# Select a directory within our container
WORKDIR /source/

# Copy everything from our project root into our WORK DIRECTORY directory
=======
COPY 6_week_project .

# Install dependencies
#RUN pip install -r requirements.txt

# Give our container internet access
#EXPOSE 80

# Execute this command on start
ENTRYPOINT ["python", "app_v2.py"]