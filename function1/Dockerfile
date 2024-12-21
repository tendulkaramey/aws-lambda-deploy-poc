FROM public.ecr.aws/lambda/python:3.11

COPY app/ ${LAMBDA_TASK_ROOT}

RUN pip install --upgrade pip && \
    pip install -r ${LAMBDA_TASK_ROOT}/requirements.txt

CMD ["main.lambda_handler"]
