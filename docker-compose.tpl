services:
  api:
    build: ./api
    ports:
      - "8000:8000"
    volumes:
      - ./api:/api
    command: bash -c "python manage.py runserver 0.0.0.0:8000"
    environment:
      POSTGRES_USER: $POSTGRES_USER
      POSTGRES_DATABASE: $POSTGRES_DATABASE
      POSTGRES_HOST: $POSTGRES_HOST
      POSTGRES_PASSWORD: $POSTGRES_PASSWORD

  postgres:
    image: postgres
    environment:
      POSTGRES_PASSWORD: $POSTGRES_PASSWORD

  web:
    build: ./frontend
    ports:
      - "3000:3000"
    volumes:
      - ./frontend:/frontend
