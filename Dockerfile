# Grab python base image from aws' public lambda images
FROM public.ecr.aws/lambda/python:3.8

# Install certbot and dns plugin with pip
RUN pip3 install certbot-dns-route53

# Copy lambda function into docker environment
COPY lambda_function.py ./

# Run the lambda function
CMD ["lambda_function.lambda_handler"]
