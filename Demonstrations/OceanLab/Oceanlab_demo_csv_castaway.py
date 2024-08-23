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
        entity="http://onto-ns.com/meta/1/castaway",
        parserType="text/vnd.dlite-castawaycsv",
        configuration={
            "resourceType": "resource/url",
            "downloadUrl": "https://gist.githubusercontent.com/quaat/3c0de76b8cdb373284990d797518ea03/raw/8070696d43b44fa552825a8fefdf7d784a5272be/data.csv",
            "mediaType": "text/csv",
            "storage_path": "/entities",
            "header_keywords_mappings": {
                "Device": "device",
                "File name": "filename",
                "Cast time (UTC)": "cast_time_utc",
                "Cast time (local)": "cast_time_local",
                "Sample type": "sample_type",
                "Cast data": "cast_data",
                "Location source": "location_source",
                "Default lat*": "latitude_default",
                "Default alt*": "altitude_default",
                "Start lat*": "latitude_start",
                "Start lon*": "longitude_start",
                "Start alt*": "altitude_start",
                "Start GPS horizontal error*": "gps_horizontal_error_start",
                "Start GPS vertical error*": "gps_vertical_error_start",
                "Start GPS number of satellites": "gps_number_of_satellites_start",
                "End latitude": "latitude_end",
                "End longitude": "longitude_end",
                "End altitude": "altitude_end",
                "End GPS horizontal error*": "gps_horizontal_error_end",
                "End GPS vertical error*": "gps_vertical_error_end",
                "End GPS number of satellites": "gps_number_of_satellites_end",
                "Cast duration*": "cast_duration",
                "Samples per second": "samples_per_second",
                "Electronics * date": "electronics_calibration_date",
                "Conductivity * date": "conductivity_calibration_date",
                "Temperature * date": "temperature_calibration_date",
                "Pressure * date": "pressure_calibration_date",
                "Pressure *": "pressure",
                "Temperature *": "temperature",
                "Salinity *": "salinity",
                "Depth *": "depth",
            },
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
            "http://onto-ns.com/meta/1/castaway#device",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#device",
        ),
        (
            "http://onto-ns.com/meta/1/castaway#filename",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#filename",
        ),
        (
            "http://onto-ns.com/meta/1/castaway#salinity",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#sea_water_practical_salinity",
        ),
        (
            "http://onto-ns.com/meta/1/castaway#pressure",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#sea_water_pressure",
        ),
        (
            "http://onto-ns.com/meta/1/castaway#temperature",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#temperature",
        ),
        (
            "http://onto-ns.com/meta/1/castaway#depth",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#depth",
        ),
        (
            "http://onto-ns.com/meta/1/castaway#cast_time_utc",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.wikidata.org/entity/Q186885",
        ),
        (
            "http://onto-ns.com/meta/1/castaway#cast_time_local",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.wikidata.org/entity/Q186885",
        ),
        (
            "http://onto-ns.com/meta/1/castaway#sample_type",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#sample_type",
        ),
        (
            "http://onto-ns.com/meta/1/castaway#cast_data",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#cast_data",
        ),
        (
            "http://onto-ns.com/meta/1/castaway#location_source",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#location_source",
        ),
        (
            "http://onto-ns.com/meta/1/castaway#latitude_default",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#latitude_default",
        ),
        (
            "http://onto-ns.com/meta/1/castaway#altitude_default",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#altitude_default",
        ),
        (
            "http://onto-ns.com/meta/1/castaway#latitude_start",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#latitude_start",
        ),
        (
            "http://onto-ns.com/meta/1/castaway#longitude_start",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#longitude_start",
        ),
        (
            "http://onto-ns.com/meta/1/castaway#altitude_start",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#altitude_start",
        ),
        (
            "http://onto-ns.com/meta/1/castaway#gps_horizontal_error_start",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#gps_horizontal_error_start",
        ),
        (
            "http://onto-ns.com/meta/1/castaway#gps_vertical_error_start",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#gps_vertical_error_start",
        ),
        (
            "http://onto-ns.com/meta/1/castaway#gps_number_of_satellites_start",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#gps_number_of_satellites_start",
        ),
        (
            "http://onto-ns.com/meta/1/castaway#latitude_end",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#latitude_end",
        ),
        (
            "http://onto-ns.com/meta/1/castaway#longitude_end",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#longitude_end",
        ),
        (
            "http://onto-ns.com/meta/1/castaway#altitude_end",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#altitude_end",
        ),
        (
            "http://onto-ns.com/meta/1/castaway#gps_horizontal_error_end",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#gps_horizontal_error_end",
        ),
        (
            "http://onto-ns.com/meta/1/castaway#gps_vertical_error_end",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#gps_vertical_error_end",
        ),
        (
            "http://onto-ns.com/meta/1/castaway#gps_number_of_satellites_end",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#gps_number_of_satellites_end",
        ),
        (
            "http://onto-ns.com/meta/1/castaway#cast_duration",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#cast_duration",
        ),
        (
            "http://onto-ns.com/meta/1/castaway#samples_per_second",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#samples_per_second",
        ),
        (
            "http://onto-ns.com/meta/1/castaway#electronics_calibration_date",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#electronics_calibration_date",
        ),
        (
            "http://onto-ns.com/meta/1/castaway#conductivity_calibration_date",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#conductivity_calibration_date",
        ),
        (
            "http://onto-ns.com/meta/1/castaway#temperature_calibration_date",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#temperature_calibration_date",
        ),
        (
            "http://onto-ns.com/meta/1/castaway#pressure_calibration_date",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#pressure_calibration_date",
        ),
    ]
    input_mapping = client.create_mapping(
        mappingType="mappings", triples=dataMappings
    )
    print(input_mapping.strategy_id)
except Exception as e:
    print(f"Error creating mapping_for_results mapping: {e}")

try:
    dataMappings2 = [
        (
            "http://onto-ns.com/meta/1/castawayreturn#salinity",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#sea_water_practical_salinity",
        ),
        (
            "http://onto-ns.com/meta/1/castawayreturn#pressure",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#sea_water_pressure",
        ),
        (
            "http://onto-ns.com/meta/1/castawayreturn#temperature",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#temperature",
        ),
        (
            "http://onto-ns.com/meta/1/castawayreturn#depth",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#depth",
        ),
        (
            "http://onto-ns.com/meta/1/castawayreturn#cast_time_utc",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.wikidata.org/entity/Q186885",
        ),
        (
            "http://onto-ns.com/meta/1/castawayreturn#samples_per_second",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#samples_per_second",
        ),
    ]
    generator_mapping = client.create_mapping(
        mappingType="mappings", triples=dataMappings2
    )
    print(generator_mapping.strategy_id)
except Exception as e:
    print(f"Error creating mapping_salinity: {e}")


# Create a function to generate output based on the specified configuration.
try:
    generate = client.create_function(
        functionType="application/vnd.dlite-generate",
        configuration={
            "driver": "json",
            "location": "/output/hp.json",
            "datamodel": "http://onto-ns.com/meta/1/castawayreturn",
        },
    )
    print(generate.strategy_id)
except Exception as e:
    print(f"Error creating generate function: {e}")


# Build the data pipeline by chaining together the data resource, parser, mappings, and generate function.
try:
    pipeline = parser >> input_mapping >> generator_mapping >> generate

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
