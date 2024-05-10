# Give dev user ownership of the workspace
chown -R dev /workspaces/sqlalchemy-concurrency-poc

# Install all Python dependencies
pip install --upgrade --requirement /workspaces/sqlalchemy-concurrency-poc/requirements.txt
