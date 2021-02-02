deploy:
	- cd client && npm install && npm run build && cd ../
	- docker-compose build
	- docker-compose up -d

migrate:
	- docker-compose exec server make migrate
