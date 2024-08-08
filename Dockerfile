FROM python:3.10

# Set the working directory
COPY ./requirements.txt /webbapp/requirements.txt

WORKDIR /webbapp

# Install dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /webbapp
COPY webapp/* /webbapp

ENTRYPOINT [ "uvicorn" ]


CMD [ "--host", "0.0.0.0", "main:app" ]

