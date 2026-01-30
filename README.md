[Data Engineering Zoomcamp Docker Terraform Homework](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2026/01-docker-terraform/homework.md)

### Question 1
Run docker with the python:3.13 image. Use an entrypoint bash to interact with the container.

What's the version of pip in the image?

```bash
docker run -it --rm --entrypoint=bash python:3.13
pip --version
```

*25.3*

### Question 2
Given the following docker-compose.yaml, what is the hostname and port that pgadmin should use to connect to the postgres database?

*postgres:5432*

### Question 3
For the trips in November 2025 (lpep_pickup_datetime between '2025-11-01' and '2025-12-01', exclusive of the upper bound), how many trips had a trip_distance of less than or equal to 1 mile?

```sql
SELECT COUNT(*) FROM public.green_trip_data
WHERE 
	lpep_pickup_datetime >= '2025-11-01' 
	AND lpep_pickup_datetime < '2025-12-01'
	AND trip_distance <= 1;
```

*8,007*

### Question 4
Which was the pick up day with the longest trip distance? Only consider trips with trip_distance less than 100 miles (to exclude data errors).

```sql
SELECT lpep_pickup_datetime, trip_distance FROM public.green_trip_data
WHERE trip_distance < 100
ORDER BY trip_distance DESC
LIMIT 1;
```

*2025-11-14*

### Question 5
Which was the pickup zone with the largest total_amount (sum of all trips) on November 18th, 2025?

```sql
SELECT
	zd.zone AS zone_name,
	COUNT(*) AS total_amount 
FROM public.green_trip_data td
JOIN public.zone_data zd
	ON td.pulocationid = zd.locationid
GROUP BY 1
ORDER BY 2 DESC;
```

*East Harlem North*

### Question 6
For the passengers picked up in the zone named "East Harlem North" in November 2025, which was the drop off zone that had the largest tip?

```sql
SELECT
	zd.zone AS zone_name,
	MAX(td.tip_amount) AS max_tip
FROM public.zone_data zd
JOIN public.green_trip_data td
	ON td.pulocationid = zd.locationid
WHERE zd.zone = 'East Harlem North'
GROUP BY 1
```

*Yorkville West*

### Question 7


**