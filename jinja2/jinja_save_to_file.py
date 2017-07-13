'''
How to write the rendered result of a template to a new file.

@ref
     - https://stackoverflow.com/questions/11857530/how-do-i-render-jinja2-output-to-a-file-in-python-instead-of-a-browser
'''

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('test.html')
output_from_parsed_template = template.render(foo='Hello World!')
print output_from_parsed_template

# to save the results
with open("my_new_file.html", "wb") as fh:
    fh.write(output_from_parsed_template)