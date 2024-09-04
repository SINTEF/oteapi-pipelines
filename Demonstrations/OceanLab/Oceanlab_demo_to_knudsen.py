# Import necessary libraries
import json
import os

from dotenv import load_dotenv
from otelib import OTEClient

load_dotenv()

url = os.getenv("URL")
USER = os.getenv("USER_OCEANLAB")
PASSWORD = os.getenv("PASSWORD_OCEANLAB")
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
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#sea_water_practical_salinity",
            "http://emmo.info/domain-mappings#mapsTo",
            "https://w3id.org/function/ontology#input_practical_salinity",
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
        mappingType="mappings", triples=dataMappings_salinity
    )
    print(mapping_salinity.strategy_id)
except Exception as e:
    print(f"Error creating mapping_salinity: {e}")

# function mappings --> but eventually this be extracted from a triplestore
try:
    function_ontology_mappings = [
        (
            "https://w3id.org/function/ontology#convert_to_knudsen",
            "http://www.w3.org/1999/02/22-rdf-syntax-ns#type",
            "https://w3id.org/function/ontology#Function",
        ),
        (
            "https://w3id.org/function/ontology#convert_to_knudsen",
            "https://w3id.org/function/ontology#expects",
            "https://w3id.org/function/ontology#salinity",
        ),
        (
            "https://w3id.org/function/ontology#convert_to_knudsen",
            "https://w3id.org/function/ontology#returns",
            "https://w3id.org/function/ontology#knudsen_salinity",
        ),
        (
            "https://w3id.org/function/ontology#salinity",
            "http://www.w3.org/1999/02/22-rdf-syntax-ns#type",
            "https://w3id.org/function/ontology#Parameter",
        ),
        (
            "https://w3id.org/function/ontology#salinity",
            "http://www.w3.org/2000/01/rdf-schema#label",
            '"v"@en',
        ),
        (
            "https://w3id.org/function/ontology#salinity",
            "http://emmo.info/domain-mappings#mapsTo",
            "https://w3id.org/function/ontology#input_practical_salinity",
        ),
        (
            "https://w3id.org/function/ontology#knudsen_salinity",
            "http://www.w3.org/1999/02/22-rdf-syntax-ns#type",
            "https://w3id.org/function/ontology#Output",
        ),
        (
            "https://w3id.org/function/ontology#knudsen_salinity",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#sea_water_knudsen_salinity",
        ),
        (
            "https://w3id.org/function/ontology#knudsen_salinity",
            "http://emmo.info/domain-mappings#mapsTo",
            "https://w3id.org/function/ontology#returned_knudsen_salinity",
        ),
        (
            "https://w3id.org/function/ontology#convert_to_knudsen",
            "http://emmo.info/oteio#hasPythonFunctionName",  # this cannot be changed as tripper uses this ontology : https://github.com/emmo-repo/domain-oteio
            "to_knudsen",
        ),
        (
            "https://w3id.org/function/ontology#convert_to_knudsen",
            "http://emmo.info/oteio#hasPythonModuleName",  # this cannot be changed as tripper uses this ontology : https://github.com/emmo-repo/domain-oteio
            "mymath.util",
        ),
        (
            "https://w3id.org/function/ontology#convert_to_knudsen",
            "http://emmo.info/oteio#hasPypiPackageName",  # this cannot be changed as tripper uses this ontology : https://github.com/emmo-repo/domain-oteio
            "git+https://github.com/Treesarj/converters",
        ),
    ]
    function_mappings = client.create_mapping(
        mappingType="mappings", triples=function_ontology_mappings
    )
    print(function_mappings.strategy_id)
except Exception as e:
    print(f"Error creating second mapping: {e}")


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
    pipeline = (
        parser >> mapping >> mapping_salinity >> function_mappings >> generate
    )

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
