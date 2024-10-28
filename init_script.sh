#!/bin/bash

# Make migrations and apply them
alembic revision --autogenerate -m "Initial migration"

alembic upgrade head

# Start the application
python server.py



