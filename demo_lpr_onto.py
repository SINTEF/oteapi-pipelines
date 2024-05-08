# Import necessary libraries
import json
from otelib import OTEClient

try:
    client = OTEClient("http://localhost:8080")
    print("OTEAPI Client Configuration:", client)

    data_resource = client.create_dataresource(
        downloadUrl="https://vipcoat-oip.com/minio/vipcoatbucket/dcat_1218495a-6b5b-425a-89cf-1c3ddb7de512/101022_1mM_2amino4methylthiazole_run1_01_LPR_C01.mpr",
        mediaType="application/mpr",
        resourceType="resource/url",
    )
    print("Data Resource Strategy ID:", data_resource.strategy_id)
except Exception as e:
    print("An error occurred:", e)


try:
    parser = client.create_parser(
        entity="http://onto-ns.com/meta/vipcoat/1.0/LPR_properties",
        parserType="mpr",
        configuration={
            "mpr_config": {
                "Control_voltage": "control/V",
                "Current": "<I>/mA",
                "Electrode_potential": "Ewe/V",
                "Flags": "flags",
                "Time": "time/s",
            },
            "storage_path": "/entities",
        },
    )
    print(parser.strategy_id)
except Exception as e:
    print(f"Error creating parser: {e}")


try:
    mapping = client.create_mapping(
        mappingType="mappings",
        triples=[
            (
                "http://onto-ns.com/meta/vipcoat/1.0/LPR_properties#Flags",
                "http://emmo.info/domain-mappings#mapsTo",
                "http://onto-ns.com/meta/vipcoat/demo/0.2/properties#flags",
            ),
            (
                "http://onto-ns.com/meta/vipcoat/1.0/LPR_properties#Control_voltage",
                "http://emmo.info/domain-mappings#mapsTo",
                "http://onto-ns.com/meta/vipcoat/demo/0.2/properties#controlVoltage",
            ),
            (
                "http://onto-ns.com/meta/vipcoat/1.0/LPR_properties#Time",
                "http://emmo.info/domain-mappings#mapsTo",
                "http://onto-ns.com/meta/vipcoat/demo/0.2/properties#time",
            ),
            (
                "http://onto-ns.com/meta/vipcoat/1.0/LPR_properties#Current",
                "http://emmo.info/domain-mappings#mapsTo",
                "http://onto-ns.com/meta/vipcoat/demo/0.2/properties#current",
            ),
            (
                "http://onto-ns.com/meta/vipcoat/1.0/LPR_properties#Electrode_potential",
                "http://emmo.info/domain-mappings#mapsTo",
                "http://onto-ns.com/meta/vipcoat/demo/0.2/properties#electrodePotential",
            ),
        ],
    )
    print(mapping.strategy_id)
except Exception as e:
    print(f"Error creating second mapping: {e}")


try:
    mapping2 = client.create_mapping(
        mappingType="mappings",
        triples=[
            (
                "http://onto-ns.com/meta/vipcoat/1.0/LPR_properties2#Control_voltage",
                "http://emmo.info/domain-mappings#mapsTo",
                "http://onto-ns.com/meta/vipcoat/demo/0.2/properties#controlVoltage",
            ),
            (
                "http://onto-ns.com/meta/vipcoat/1.0/LPR_properties2#Time",
                "http://emmo.info/domain-mappings#mapsTo",
                "http://onto-ns.com/meta/vipcoat/demo/0.2/properties#time",
            )
        ],
    )
    print(mapping.strategy_id)
except Exception as e:
    print(f"Error creating second mapping: {e}")

try:
    generator = client.create_function(
        functionType="application/vnd.dlite-generate",
        configuration={
            "driver": "json",
            "location": "/output/lpr.json",
            "datamodel": "http://onto-ns.com/meta/vipcoat/1.0/LPR_properties2",

        },
    )
    print(generator.strategy_id)
except Exception as e:
    print(f"Error creating generate function: {e}")


# Build the data pipeline by chaining together the data resource, parser, mappings, and generate function.
try:
    pipeline = data_resource >> parser >> mapping >> mapping2 >> generator

    # Execute the pipeline and process the data.
    result = pipeline.get().decode("utf-8")

    # Convert the result into a JSON object and then format it for readability.
    json_object = json.loads(result)
    json_formatted = json.dumps(json_object, indent=4)
    print(json_formatted)

    # Inform the user that the data has been processed and output is written.
    print("Data is written out to output/lpr.json")
except Exception as e:
    print(f"Error executing pipeline: {e}")
