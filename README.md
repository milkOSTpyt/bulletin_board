### Deploy project ( docker-compose )
Install docker and docker-compose and next run command:

#### Copy and fill env file:
`cp example.env .env`

#### After update variables:
`docker compose up -d --build`

#### Create superuser:
`docker compose run --rm bulletin_board python manage.py createsuperuser`

### Update project (docker-compose):
For update project you need pull latest changes from git, and run next command:\
`docker compose up -d --build`