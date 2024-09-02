# OceanLab demonstration

To run the demo, ensure your virtual environment is activated and environment variables is set.
It is recommended to add a `.env` file in the OceanLab folder with the necessary environment variables:

```shell
# .env
USER_OCEANLAB=<user>
PASSWORD_OCEANLAB=<password>
URL=<url>
DATABASE=<database>
RETPOLICY=<retention_policy>
```

## Extra plugin for OTEAPI Services

To run the demo, the custom csv parser plugin must be used with OTEAPI Services.
To install the plugin, add the following line to the `OTEAPI_PLUGIN_PACKAGES` environment variable in the [`compose.yml`](../../compose.yml) file: `|git+https://__token__:${GITHUB_TOKEN}@github.com/SemanticMatter/oteapi-iliad@main`.
It should look like this:

```yaml
services:
  oteapi:
    # ...
    environment:
      OTEAPI_PLUGIN_PACKAGES: 'git+https://github.com/SINTEF/oteapi-dlite-Mod@master|git+https://__token__:${GITHUB_TOKEN}@github.com/SemanticMatter/oteapi-iliad@main'
# ...
```

## Demonstrators

### Demo1

This extracts all the data from the influxdb.

To run the demo:

```bash
python Oceanlab_demo_extract_same.py
```

### Demo2

This extracts just the salinity from the influxdb.

To run the demo:

```bash
python Oceanlab_demo_get_salinity.py
```

### Demo3

This extracts the salinity and transforms it to knudsen salinity.

To run the demo:

```bash
python Oceanlab_demo_to_knudsen.py
```

### Demo4

This extracts the castaway data from a csv file and saves the collection instance to the output folder.
To run this demo, the custom csv parser plugin must be used with ote-services.
To run the demo:

```bash
python Oceanlab_demo_csv_castaway.py
```

### Demo5

This is the demo, same as [Demo3](#demo3), but fetching the relations from a Knowledge Graph (KG).

To run the demo:

- Create a graph with uri: `http://www.semanticweb.org/ocean_functions/oceanlab/0.0.1`
- Populate it with [`KG_V1.rdf`](../../input/KG_V1.rdf) in input folder

Then, run:

```bash
python Oceanlab_demo_to_knudsen_KG.py
```
