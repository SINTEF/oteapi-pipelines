## Mapping startegy configuration

The demo_using_graph_mappings.py file demonstrates the mapping configuration, allowing necessary functions and other relations to be loaded or populated into the triple store of the DLite collection. In this context, the required ontology must be available in the provided triple store under a specific graph_uri. For example, in Fuseki, we upload the .ttl file with the graph URI and then provide a SPARQL endpoint along with the graph URI for the configuration of the mapping. This process retrieves the common parent of the objects listed in the triples and fetches the tree from that parent, ultimately populating the DLite collection.

