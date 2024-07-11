from otelib import OTEClient

client = OTEClient("http://localhost:8080")
try:
    dataMappings = [
        (
            "http://onto-ns.com/meta/0.4/HallPetch#theta0",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://hall_petch.info/hp#YeildStrength",
        ),
        (
            "http://onto-ns.com/meta/0.4/HallPetch#k",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://hall_petch.info/hp#Coefficient",
        ),
        (
            "http://onto-ns.com/meta/0.4/HallPetch#d",
            "http://emmo.info/domain-mappings#mapsTo",
            "http://hall_petch.info/hp#GrainSize",
        ),
    ]
    mapping = client.create_mapping(
        mappingType="mappings",
        triples=dataMappings,
        configuration={
            "sparql_endpoint": "http://fuseki:3030/hp/query",
            "graph_uri": "http://sample.com/meta/0.4/hallpetch",
            # Add username and password if required
        },
    )
    print(mapping.strategy_id)
except Exception as e:
    print(f"Error creating mapping: {e}")
