n ?= 11
f ?= data.csv

export

requirements:                                                                                                                              
	docker exec -it fetch_api sh -c 'cd /app/ && pip install -r requirements.txt'

start:
	docker compose up --build -d --remove-orphans

stop:
	docker compose down

show-logs:
	docker compose logs

down-v:
	docker compose down -v

fetch.api:                                                                                                                              
	docker exec -it fetch_api sh -c 'cd /app/solution__1 && python3 fetch_data.py'

generate.random.data:
	docker exec -it random_data_gen sh -c 'cd /app/solution__2 && python3 random_data_gen.py -n $(n) -f $(f)'

test.generated.data:
	docker exec -it random_data_gen sh -c 'cd /app/solution__2 && python3 tests.py'

format.csv:                                                                                                                              
	docker exec -it fetch_api sh -c 'cd /app/solution__3 && python3 format_csv.py'