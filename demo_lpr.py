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
        entity="https://vipcoat-oip.com/minio/vipcoatbucket/data_models/vipcoat_LPR_properties.json",
        parserType="mpr",
        configuration={
            "mpr_config": {
                "Control_voltage": "control/V",
                "Current": "<I>/mA",
                "Electrode_potential": "Ewe/V",
                "Flags": "flags",
                "Time": "time/s",
            }
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
                "https://vipcoat-oip.com/minio/vipcoatbucket/data_models/vipcoat_LPR_properties.json#Flags",
                "http://emmo.info/domain-mappings#mapsTo",
                "http://onto-ns.com/meta/vipcoat/demo/0.2/properties#flags",
            ),
            (
                "https://vipcoat-oip.com/minio/vipcoatbucket/data_models/vipcoat_LPR_properties.json#Control_voltage",
                "http://emmo.info/domain-mappings#mapsTo",
                "http://onto-ns.com/meta/vipcoat/demo/0.2/properties#controlVoltage",
            ),
            (
                "https://vipcoat-oip.com/minio/vipcoatbucket/data_models/vipcoat_LPR_properties.json#Time",
                "http://emmo.info/domain-mappings#mapsTo",
                "http://onto-ns.com/meta/vipcoat/demo/0.2/properties#time",
            ),
            (
                "https://vipcoat-oip.com/minio/vipcoatbucket/data_models/vipcoat_LPR_properties.json#Current",
                "http://emmo.info/domain-mappings#mapsTo",
                "http://onto-ns.com/meta/vipcoat/demo/0.2/properties#current",
            ),
            (
                "https://vipcoat-oip.com/minio/vipcoatbucket/data_models/vipcoat_LPR_properties.json#Electrode_potential",
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
                "https://vipcoat-oip.com/minio/vipcoatbucket/data_models/vipcoat_LPR_properties2.json#Control_voltage",
                "http://emmo.info/domain-mappings#mapsTo",
                "http://onto-ns.com/meta/vipcoat/demo/0.2/properties#controlVoltage",
            ),
            (
                "https://vipcoat-oip.com/minio/vipcoatbucket/data_models/vipcoat_LPR_properties2.json#Time",
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
            "location": "/output/output.json",
            "datamodel": "https://vipcoat-oip.com/minio/vipcoatbucket/data_models/vipcoat_LPR_properties2.json",

        },
    )
    print(generator.strategy_id)

except Exception as e:
    print(f"Error creating generate function: {e}")


pipeline = data_resource >> parser >> mapping >> mapping2 >> generator


# pipeline = data_resource >> parser
result = pipeline.get().decode("utf-8")

json_object = json.loads(result)

json_formatted = json.dumps(json_object, indent=4)


print(json_formatted)
