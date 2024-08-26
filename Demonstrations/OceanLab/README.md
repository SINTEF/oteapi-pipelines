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
