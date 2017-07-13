'''
When you want to use Jinja2 outside of a web framework or other existing tool, 
here's a handy quick load function snippet so the template engine can be easily 
used from a script or the REPL.

@ref
    - https://www.pydanny.com/jinja2-quick-load-function.html
'''

from jinja2 import FileSystemLoader, Environment

def render_from_template(directory, template_name, **kwargs):
    loader = FileSystemLoader(directory)
    env = Environment(loader=loader)
    template = env.get_template(template_name)
    return template.render(**kwargs)


if __name__=='__main__':
    data = {
        "date": "June 12, 2014",
        "items": ["oranges", "bananas", "steak", "milk"]
    }
    
    render_from_template(".", "shopping_list.html", **data)