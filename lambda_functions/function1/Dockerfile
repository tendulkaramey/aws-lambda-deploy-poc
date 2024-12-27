FROM public.ecr.aws/lambda/python:3.11

# Copy the database files
COPY database/ /var/task/database/

# Copy the function-specific app directory
COPY app/ ${LAMBDA_TASK_ROOT}


RUN pip install --upgrade pip && \
    pip install -r ${LAMBDA_TASK_ROOT}/requirements.txt

CMD ["main.lambda_handler"]