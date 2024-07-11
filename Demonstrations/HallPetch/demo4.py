# Import necessary libraries
import json

from otelib import OTEClient

# Initialize the OTEAPI client pointing to the API's base URL.
# This client will be used to interact with the API services.
client = OTEClient("http://localhost:8080")

# Verify the client's base URL and service endpoints.
print(client)

# Create a data resource from a specified URL containing JSON data.
# The URL, media type, and resource type are defined.
try:
    data_resource = client.create_dataresource(
        downloadUrl="https://raw.githubusercontent.com/SINTEF/oteapi-pipelines/main/input/hallpetch.json",
        mediaType="application/json",
        resourceType="resource/url",
    )
    print(data_resource.strategy_id)
except Exception as e:
    print(f"Error creating data resource: {e}")

# Set up a parser with a specific entity and parser type.
# Additionally, a configuration for the storage path is provided.
try:
    parser = client.create_parser(
        entity="http://onto-ns.com/meta/0.4/HallPetch",
        parserType="json/vnd.dlite-json",
        configuration={"storage_path": "/entities"},
    )
    print(parser.strategy_id)
except Exception as e:
    print(f"Error creating parser: {e}")

# Define mappings between different ontology entities.
# These mappings are RDF triples that establish relationships
# between entities for semantic interoperability.
try:
    dataMappings = [
        (
            "http://onto-ns.com/meta/0.4/HallPetch#theta0",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://hall_petch.info/hp.YeildStrength",
        ),
        (
            "http://onto-ns.com/meta/0.4/HallPetch#k",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://hall_petch.info/hp.Coefficient",
        ),
        (
            "http://onto-ns.com/meta/0.4/HallPetch#d",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://hall_petch.info/hp.GrainSize",
        ),
    ]
    mapping = client.create_mapping(
        mappingType="mappings", triples=dataMappings
    )
    print(mapping.strategy_id)
except Exception as e:
    print(f"Error creating mapping: {e}")

# Define additional mappings for another set of ontology entities.
try:
    dataMappings2 = [
        (
            "http://onto-ns.com/meta/0.4/HallPetch3#theta03",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://hall_petch.info/hp.YeildStrength",
        ),
        (
            "http://onto-ns.com/meta/0.4/HallPetch3#k3",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://hall_petch.info/hp.Coefficient",
        ),
    ]
    mapping2 = client.create_mapping(
        mappingType="mappings", triples=dataMappings2
    )
    print(mapping2.strategy_id)
except Exception as e:
    print(f"Error creating second mapping: {e}")

# Create a function to generate output based on the specified configuration.
try:
    generate = client.create_function(
        functionType="application/vnd.dlite-generate",
        configuration={
            "driver": "json",
            "location": "/output/hp.json",
            "datamodel": "http://onto-ns.com/meta/0.4/HallPetch3",
        },
    )
    print(generate.strategy_id)
except Exception as e:
    print(f"Error creating generate function: {e}")

# Build the data pipeline by chaining together the data resource, parser, mappings, and generate function.
try:
    pipeline = data_resource >> parser >> mapping >> mapping2 >> generate

    # Execute the pipeline and process the data.
    result = pipeline.get().decode("utf-8")

    # Convert the result into a JSON object and then format it for readability.
    json_object = json.loads(result)
    json_formatted = json.dumps(json_object, indent=4)
    print(json_formatted)

    # Inform the user that the data has been processed and output is written.
    print("Data is written out to output/hp.json")
except Exception as e:
    print(f"Error executing pipeline: {e}")
