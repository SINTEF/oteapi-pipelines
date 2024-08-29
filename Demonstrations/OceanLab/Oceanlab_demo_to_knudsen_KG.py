# Import necessary libraries
import json
import os

from dotenv import load_dotenv
from otelib import OTEClient

load_dotenv()

url = os.getenv("URL")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")
RETPOLICY = os.getenv("RETPOLICY")

try:
    # Initialize the OTEAPI client with the API's base URL.
    client = OTEClient("http://localhost:8080")

    # Display the client configuration for verification.
    print("OTEAPI Client Configuration:", client)

    parser = client.create_parser(
        entity="http://onto-ns.com/meta/oceanlab/1/ctd_data_munkholmen",
        parserType="influx/vnd.dlite-influx",
        configuration={
            "storage_path": "/entities",
            "url": url,
            "time_range": "-400h",
            "USER": USER,
            "size_limit": 20,
            "PASSWORD": PASSWORD,
            "DATABASE": DATABASE,
            "RETPOLICY": RETPOLICY,
        },
    )
    # Display the ID of the created data resource strategy for tracking.
    print("Parser Strategy ID:", parser.strategy_id)

    # Build the data pipeline by chaining the data resource to the parser.
    pipeline = parser

    # Execute the pipeline to fetch and parse the data, then decode the result from bytes to a string.
    result = pipeline.get().decode("utf-8")

    # Load the string result into a JSON object for further manipulation or analysis.
    json_object = json.loads(result)

    # Pretty-print the JSON object to make it easier to read.
    json_formatted_str = json.dumps(json_object, indent=4)
    print("Formatted JSON Result:\n", json_formatted_str)

except Exception as e:
    print("An error occurred:", e)

try:
    dataMappings = [
        (
            "http://onto-ns.com/meta/oceanlab/1/ctd_data_munkholmen#salinity",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#sea_water_practical_salinity",
        ),
        (
            "http://onto-ns.com/meta/oceanlab/1/ctd_data_munkholmen#pressure",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#sea_water_pressure",
        ),
        (
            "http://onto-ns.com/meta/oceanlab/1/ctd_data_munkholmen#conductivity",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#sea_water_electrical_conductivity",
        ),
        (
            "http://onto-ns.com/meta/oceanlab/1/ctd_data_munkholmen#density",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#sea_water_density",
        ),
        (
            "http://onto-ns.com/meta/oceanlab/1/ctd_data_munkholmen#time",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.wikidata.org/entity/Q186885",
        ),
    ]
    mapping = client.create_mapping(
        mappingType="mappings", triples=dataMappings
    )
    print(mapping.strategy_id)
except Exception as e:
    print(f"Error creating mapping_for_results mapping: {e}")

try:
    dataMappings_salinity = [
        (
            "http://onto-ns.com/meta/oceanlab/1/ctd_salinity_munkholmen#salinity",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#sea_water_knudsen_salinity",
        ),
        (
            "http://onto-ns.com/meta/oceanlab/1/ctd_salinity_munkholmen#time",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.wikidata.org/entity/Q186885",
        ),
    ]
    mapping_salinity = client.create_mapping(
        mappingType="mappings",
        triples=dataMappings_salinity,
        configuration={
            "sparql_endpoint": "http://fuseki:3030/oceanlab/query",
            "graph_uri": "http://www.semanticweb.org/ocean_functions/oceanlab/0.0.1",
            "username": "admin",
            "password": "test",
            # Add username and password if required
        },
    )
    print(mapping_salinity.strategy_id)
except Exception as e:
    print(f"Error creating mapping_salinity: {e}")

# Create a function to generate output based on the specified configuration.
try:
    generate = client.create_function(
        functionType="application/vnd.dlite-generate",
        configuration={
            "driver": "json",
            "location": "/output/hp.json",
            "datamodel": "http://onto-ns.com/meta/oceanlab/1/ctd_salinity_munkholmen",
        },
    )
    print(generate.strategy_id)
except Exception as e:
    print(f"Error creating generate function: {e}")


# Build the data pipeline by chaining together the data resource, parser, mappings, and generate function.
try:
    pipeline = parser >> mapping >> mapping_salinity >> generate

    # Execute the pipeline and process the data.
    result = pipeline.get().decode("utf-8")
    print(result)
    # Convert the result into a JSON object and then format it for readability.
    json_object = json.loads(result)
    json_formatted = json.dumps(json_object, indent=4)
    print(json_formatted)

    # Inform the user that the data has been processed and output is written.
    print("Data is written out to output/hp.json")
except Exception as e:
    print(f"Error executing pipeline: {e}")
