#!/bin/bash
set -e  # Exit on errors

# Load configuration
source config.env

# Variables
AWS_REGION="${AWS_REGION}"
FUNCTION_NAME="${FUNCTION_NAME}"
ECR_REPO="${ECR_REPO}"
IMAGE_TAG="latest"
AWS_ACCOUNT_ID="${AWS_ACCOUNT_ID}"
AWS_PROFILE="${AWS_PROFILE}"

# Step 1: Build Docker Image with buildx for x86_64 architecture
echo "🚀 Building Docker image for $FUNCTION_NAME (x86_64 architecture)..."
docker buildx build \
  --platform linux/amd64 \
  --load \
  -t ${ECR_REPO}:${IMAGE_TAG} .

# Step 2: Authenticate Docker to ECR using AWS profile
echo "🔑 Authenticating with AWS ECR..."
aws ecr get-login-password --region ${AWS_REGION} --profile ${AWS_PROFILE} | \
  docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com

# Step 3: Tag and Push Docker Image to ECR
echo "📤 Pushing Docker image to ECR..."
docker tag ${ECR_REPO}:${IMAGE_TAG} ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}
docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}

# Step 4: Update Lambda Function using AWS profile
echo "⚙️  Updating Lambda function $FUNCTION_NAME..."
aws lambda update-function-code \
  --function-name ${FUNCTION_NAME} \
  --image-uri ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG} \
  --profile ${AWS_PROFILE}

echo "✅ Deployment of $FUNCTION_NAME complete!"
