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
