
# Devops Project 


 This project manages application deployment on Kubernetes using Jenkins pipelines. All applications are deployed to Kubernetes using Helm Charts, while user data is persistently stored in PostgreSQL with daily backups managed by PostgreSQL. Redis is used for data caching. Access to PostgreSQL and Redis is provided externally, ensuring passwords and confidential information are securely managed. Shell scripts are available for PostgreSQL and Redis testing in the CLI environment.
   
## Technologies Used

- Terraform
- Docker
- Docker Compose
- Kubernetes (kind)
- Jenkins
- Redis
- PostgreSQL

## Structre

![image](https://github.com/user-attachments/assets/b3e4c40f-0494-48fe-8899-49a567396289)

![drawio](https://github.com/user-attachments/assets/9d80bb80-c9a8-4056-880b-d94dd45760d1)


## Installation Steps:

Install requirements using scripts
```
cd myapp/scripts
chmod +x *
Run each script with './' one by one
```

Creating kind Cluster with Terraform
```
terraform init
terraform plan
terraform apply 
```

Installation of Redis and PostgreSQL with Docker Compose
```
docker-compose up -d
```

# CI/CD
## Installation and Configuration of Jenkins
### Installation of Jenkins
Jenkins is installed on an Ubuntu server and runs on port 8080. It is started and configured to run automatically on system startup.

### Configuration of Jenkins
Set up the CI/CD process according to project requirements, defining stages such as build, test, and deploy tailored to the project's needs.

### Jenkins CI/CD Process

Jenkins detects changes on GitHub and initiates the CI/CD process. The CI process involves  
### Deployment to Kubernetes
After successfully completing the CI process, the Jenkins CD step applies the necessary Kubernetes manifest files (kubectl apply) to deploy the application to the Kubernetes cluster. This step ensures that the latest version of the application is deployed and running in the Kubernetes environment configured for the project.



