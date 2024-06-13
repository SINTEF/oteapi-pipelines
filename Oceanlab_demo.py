# Import necessary libraries
import json
from otelib import OTEClient

# Initialize the OTEAPI client pointing to the API's base URL.
# This client will be used to interact with the API services.
client = OTEClient("http://localhost:8080")

# Verify the client's base URL and service endpoints.
print(client)


try:
    dataMappings_density = [
        (
            "http://onto-ns.com/1/ctd_density_munkholmen#density",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#sea_water_density",
        ),
        (
            "http://onto-ns.com/1/ctd_density_munkholmen#time",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#timestamp",
        ),
    ]
    mapping_density = client.create_mapping(
        mappingType="mappings", triples=dataMappings_density
    )
    print(mapping_density.strategy_id)
except Exception as e:
    print(f"Error creating mapping_density: {e}")

try:
    dataMappings_pressure = [
        (
            "http://onto-ns.com/1/ctd_pressure_munkholmen#pressure",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#sea_water_pressure",
        ),
        (
            "http://onto-ns.com/1/ctd_pressure_munkholmen#time",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#timestamp",
        ),
    ]
    mapping_pressure = client.create_mapping(
        mappingType="mappings", triples=dataMappings_pressure
    )
    print(mapping_pressure.strategy_id)
except Exception as e:
    print(f"Error creating mapping_pressure: {e}")

try:
    dataMappings_salinity = [
        (
            "http://onto-ns.com/1/ctd_salinity_munkholmen#salinity",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#sea_water_practical_salinity",
        ),
        (
            "http://onto-ns.com/1/ctd_salinity_munkholmen#time",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#timestamp",
        ),
    ]
    mapping_salinity = client.create_mapping(
        mappingType="mappings", triples=dataMappings_salinity
    )
    print(mapping_salinity.strategy_id)
except Exception as e:
    print(f"Error creating mapping_salinity: {e}")

try:
    dataMappings_temperature = [
        (
            "http://onto-ns.com/1/ctd_temperature_munkholmen#temperature",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#sea_water_temperature",
        ),
        (
            "http://onto-ns.com/1/ctd_temperature_munkholmen#time",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#timestamp",
        ),
    ]
    mapping_temperature = client.create_mapping(
        mappingType="mappings", triples=dataMappings_temperature
    )
    print(mapping_temperature.strategy_id)
except Exception as e:
    print(f"Error creating mapping_temperature: {e}")

try:
    dataMappings_conductivity = [
        (
            "http://onto-ns.com/1/ctd_conductivity_munkholmen#conductivity",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#sea_water_electrical_conductivity",
        ),
        (
            "http://onto-ns.com/1/ctd_conductivity_munkholmen#time",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#timestamp",
        ),
    ]
    mapping_conductivity = client.create_mapping(
        mappingType="mappings", triples=dataMappings_conductivity
    )
    print(mapping_conductivity.strategy_id)
except Exception as e:
    print(f"Error creating mapping_conductivity: {e}")


# Define additional mappings for another set of ontology entities.
try:
    dataMappings_result = [
        (
            "http://onto-ns.com/1/ctd_data_munkholmen#temperature",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#sea_water_temperature",
        ),
        (
            "http://onto-ns.com/1/ctd_data_munkholmen#salinity",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#sea_water_practical_salinity",
        ),
        (
            "http://onto-ns.com/1/ctd_data_munkholmen#pressure",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#sea_water_pressure",
        ),
        (
            "http://onto-ns.com/1/ctd_data_munkholmen#conductivity",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#sea_water_electrical_conductivity",
        ),
        (
            "http://onto-ns.com/1/ctd_data_munkholmen#density",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#sea_water_density",
        ),
        (
            "http://onto-ns.com/1/ctd_data_munkholmen#time",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://www.semanticweb.org/ocean_data/cf_standards/Oceanlab/0.0.1#timestamp",
        ),
    ]
    mapping_for_results = client.create_mapping(
        mappingType="mappings", triples=dataMappings_result
    )
    print(mapping_for_results.strategy_id)
except Exception as e:
    print(f"Error creating mapping_for_results mapping: {e}")
