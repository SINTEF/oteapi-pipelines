## Step 1: Run the Demos

To run the demo, ensure your virtual environment is activated and environment variables is set.
Then execute:

### Demo1

This extracts all the data from the influxdb

To run the demo:
`bash
	python Oceanlab_demo_extract_same.py
	`

### Demo2

This extracts just the salinity from the influxdb

To run the demo:
`bash
	python Oceanlab_demo_get_salinity.py
	`
### Demo3

This extracts the salinity and transforms it to knudsen salinity

To run the demo:
`bash
	python Oceanlab_demo_to_knudsen.py
	`

### Demo4

This extracts the castaway data from a csv file and saves the collection instance to the output folder
To run this demo the custom csv parser plugin must be used with ote-services.
To run the demo:
`bash
	python Oceanlab_demo_csv_castaway.py
	`

### Demo5

This is the demo , same as Demo3, but fetching the relations from KG.

To run the demo:
- Create a graph with uri: http://www.semanticweb.org/ocean_functions/oceanlab/0.0.1
- Populate it with KG_V1.rdf in input folder
- `bash
	python Oceanlab_demo_to_knudsen_KG.py
	`
