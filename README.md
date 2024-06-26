# Setup the OTEAPI Demo Environment

This guide will walk you through the process of setting up a demo
environment for the OTEAPI framework. OTEAPI is designed to enable
FAIR data documentation and the execution of dataflow pipelines.

## Prerequisites

Before starting, ensure you have the following installed on your system:

- Docker and Docker Compose: For running the OTEAPI services and Redis in containers.
- Python 3: For setting up a virtual environment and running demo scripts.

## Step 1: Start the OTEAPI Services and Redis

1.  Open a terminal and navigate to the directory containing the docker-compose.yml file.
2.  Run the following command to start the OTEAPI services and Redis using Docker Compose:

        ```bash
        docker compose up -d
        ```

    This command downloads the necessary Docker images and starts the containers in the background.

## Step 2: Setup Your Local Python Environment

1. Create a Python virtual environment to isolate the demo dependencies:
   ```bash
   python3 -m venv ~/.virtualenvs/otedemo
   ```
2. Activate the virtual environment
   ```bash
   source ~/.virtualenvs/otedemo/bin/activate
   ```
3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

   This step ensures that all necessary Python dependencies are installed in your local environment

## Step 3: Run the Demos

To run the demo, ensure your virtual environment is activated, then execute:

### Demo1

This demonstrates a simple pipeline excecution. It takes in a Json, dummyentity(metadata) and parses it.

To run the first demo, execute:
`bash
	python demo1.py
	`
This script demonstrates a the basic functionality of the OTEAPI framework.

### Demo2

This demonstrates how two partial pipelines (data documentation pipelines) can be connected to generate the required output. Here it shows how the pipeline translates data between two different json structures with different keys with the help of data documentation.

Similarly, to run the second demo:
`bash
	python demo2.py
	`
### Demo3

This demonstrates how to use the function ontology(FO). In this example the function relations are added as a mapping to the pipeline .. which is not the right way. Eventually we would want to connect to a running triple store.

Similarly, to run the third demo:
`bash
	python demo3.py
	`
### Demo4

This extracts the subset of the data.¨

Similarly, to run the third demo:
`bash
	python demo4.py
   `
# Troubleshooting

- **Docker Compose Errors**: Ensure Docker is running on your system. If you encounter permission issues, try running the command with sudo.
- **Python Virtual Environment**: If you have multiple Python versions installed, ensure you're using Python 3 by replacing python3 with the specific version you want to use, e.g., python3.11.
- **Dependency Installation Issues**: Ensure you're in the activated virtual environment before installing dependencies. If you encounter any issues, consider upgrading pip using pip install --upgrade pip and try again.

# Conclusion

You've now successfully set up the environment and run the OTEAPI demo scripts. These demos are designed to illustrate the capabilities and ease of integration offered by the OTEAPI framework. Explore the scripts to better understand how OTEAPI works and how it can be adapted for your data integration needs.
