import bubbles

URL = "https://raw.github.com/Stiivi/cubes/master/examples/hello_world/data.csv"

p = bubbles.Pipeline()
p.source_object("csv_source", resource=URL, infer_fields=True)
p.aggregate("Category", "Amount (US$, Millions)")
p.pretty_print()

p.run()
