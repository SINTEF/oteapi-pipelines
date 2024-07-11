# Import necessary libraries
import json

from otelib import OTEClient

try:
    # Initialize the OTEAPI client with the API's base URL.
    client = OTEClient("http://localhost:8080")

    # Display the client configuration for verification.
    print("OTEAPI Client Configuration:", client)

    # Define a data resource from a public URL containing JSON data.
    data_resource = client.create_dataresource(
        downloadUrl="https://raw.githubusercontent.com/SINTEF/oteapi-pipelines/main/input/hallpetch.json",
        mediaType="application/json",
        resourceType="resource/url",
    )

    # Display the ID of the created data resource strategy for tracking.
    print("Data Resource Strategy ID:", data_resource.strategy_id)

    # Set up a parser for the JSON data.
    parser = client.create_parser(
        entity="http://onto-ns.com/meta/0.4/dummy_entity",
        parserType="parser/json",
    )

    # Display the ID of the created parser strategy for tracking.
    print("Parser Strategy ID:", parser.strategy_id)

    # Build the data pipeline by chaining the data resource to the parser.
    pipeline = data_resource >> parser

    # Execute the pipeline to fetch and parse the data, then decode the result from bytes to a string.
    result = pipeline.get().decode("utf-8")

    # Load the string result into a JSON object for further manipulation or analysis.
    json_object = json.loads(result)

    # Pretty-print the JSON object to make it easier to read.
    json_formatted_str = json.dumps(json_object, indent=4)
    print("Formatted JSON Result:\n", json_formatted_str)

except Exception as e:
    print("An error occurred:", e)
