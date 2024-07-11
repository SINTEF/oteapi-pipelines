## Step 1: Run the Demos

To run the demo, ensure your virtual environment is activated, then execute:

### Demo1

This demonstrates a simple pipeline excecution. It takes in a Json, dummyentity(metadata) and parses it.

To run the first demo, execute:
`bash
	python demo1.py
	`
This script demonstrates a the basic functionality of the OTEAPI framework.

### Demo2

This demonstrates how two partial pipelines (data documentation pipelines) can be connected to generate the required output. Here it shows how the pipeline translates data between two different json structures with different keys with the help of data documentation.

Similarly, to run the second demo:
`bash
	python demo2.py
	`
### Demo3

This demonstrates how to use the function ontology(FO). In this example the function relations are added as a mapping to the pipeline .. which is not the right way. Eventually we would want to connect to a running triple store.

Similarly, to run the third demo:
`bash
	python demo3.py
	`
### Demo4

This extracts the subset of the data.¨

Similarly, to run the 4th demo:
`bash
	python demo4.py
   `
