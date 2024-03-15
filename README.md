# cat-dog-classification

## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py

### Dataset URL:

[Click here to download data](https://github.com/entbappy/Branching-tutorial/raw/master/cat-dog-data.zip)

### STEPS:

Clone the repository

```shell
https://github.com/entbappy/cnnClassifier
```

### STEP 01- Create a conda environment after opening the repository

```shell
conda create -n cnncls python=3.7 -y
```

```shell
conda activate cnncls
```

### STEP 02- install the requirements

```shell
pip install -r requirements.txt
```

```shell
# Finally run the following command
python app.py
```

Now,

```shell
open up you local host and port
```

```shell
Author: Bhor Santosh
Data Scientist
Email: santoshbhor2001@gmail.com

```

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

```
#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
```

## 3. Create ECR repo to store/save docker image

```
- Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/catdog
```

## 4. Create EC2 machine (Ubuntu)

## 5. Open EC2 and Install docker in EC2 Machine:

```

#optinal

533267118224.dkr.ecr.ap-south-1.amazonaws.com/catdogclassification

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

# 6. Configure EC2 as self-hosted runner:

```
setting>actions>runner>new self hosted runner> choose os> then run command one by one
```

# 7. Setup github secrets:

```
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = simple-app
```
