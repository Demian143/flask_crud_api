# exporting needed variables
source .env

# if there's no image
docker pull postgres

# if container already exists
docker stop some-postgres
docker rm some-postgres

# run new container
docker run --name some-postgres -p 6666:6666 -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD -d postgres