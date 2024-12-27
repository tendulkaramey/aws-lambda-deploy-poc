FROM public.ecr.aws/lambda/python:3.11

RUN yum install -y postgresql-devel gcc python3-devel

COPY database/ ${LAMBDA_TASK_ROOT}/database/
# Copy the function-specific app directory
COPY app/ ${LAMBDA_TASK_ROOT}


RUN pip install --upgrade pip && \
pip install psycopg2-binary && \
    pip install -r ${LAMBDA_TASK_ROOT}/requirements.txt


CMD ["main.lambda_handler"]

