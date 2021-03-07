docker build -t example-container .
docker tag example-container:latest aws_account_id.dkr.ecr.aws_region.amazonaws.com/example-container-repository:latest
docker push aws_account_id.dkr.ecr.aws_region.amazonaws.com/example-container-repository:latest
