from SPARQLWrapper import SPARQLWrapper, JSON

# Replace this URL with the endpoint of the FoodOn server
foodon_endpoint = "http://example.com/sparql"

# Replace this query with your desired SPARQL query
sparql_query = """
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX foodon: <http://foodon.org/ontology#>

    SELECT ?relatedObject
    WHERE {
        ?egg rdfs:subClassOf* foodon:FOODON_03400018 .
        ?relatedObject rdfs:subClassOf* ?egg .
    }
"""

# Create a SPARQLWrapper instance and set the endpoint URL
sparql = SPARQLWrapper(foodon_endpoint)

# Set the query string
sparql.setQuery(sparql_query)

# Set the return format to JSON
sparql.setReturnFormat(JSON)

# Execute the query and get the results
results = sparql.query().convert()

# Process the results
if "results" in results:
    bindings = results["results"]["bindings"]
    for result in bindings:
        related_object_uri = result["relatedObject"]["value"]
        print(related_object_uri)

