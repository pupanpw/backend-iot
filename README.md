# backend-iot

## Project Overview

`Backend-iot` is a backend service for IoT applications using Flask and Docker Compose. This service handles communication and data processing for IoT devices, leveraging a MySQL database for data storage.

## Prerequisites

- Docker
- Docker Compose
- Python 3
- SQL (MySQL)


## Setup

1. **Clone the Repository**

```bash
   git clone https://github.com/pupanpw/backend-iot.git
   cd backend-iot
```
2. **Install Python Dependencies**

Install the required Python packages using pip. This ensures that all necessary libraries for the Flask application are available:

3.  **Create Environment File**
  ```bash
    pip install -r requirements.txt

  ```
   ```Copy the .env.example file to .env and adjust the environment variables as needed ```
```bash
cp .env.example .env
```

```Update the .env file with the following variables:```

```bash 
# Database Configuration
DATABASE_HOST=your_database_host
DATABASE_PORT=your_database_port
DATABASE_USER=your_database_user
DATABASE_PASSWORD=your_database_password
DATABASE_DB=your_database_name

# Flask Configuration
FLASK_URL=your_flask_url

# MQTT Configuration
MQTT_USERNAME=your_mqtt_username
MQTT_PASSWORD=your_mqtt_password
MQTT_TOPIC=your_mqtt_topic
MQTT_BROKER_IP=your_mqtt_broker_ip
MQTT_PORT=1883
```

4. **Build and Run the Application**

  <p>Use Docker Compose to build and run the service </p>

 ```bash 
docker-compose up --build 
```
This command builds the Docker image and starts the flask_app service. The application will be accessible on port 4000.

<h2>Configuration</h2>
<p>The docker-compose.yml file defines the following service:

<ul>
<li>flask_app: A Flask application container </li>
<li>Container Name: service-mqtt</li>
<li>Image: pupan/backend</li>
<li>Ports: Exposes port 4000</li>
<li>Environment Variables: Configured from .env file</li>
<li>Restart Policy: Always restart on failure</li>
</ul>
</p>
