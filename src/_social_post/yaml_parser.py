# same as Mynt, which requires PyYAML
from yaml import load_all, Loader

def read_yaml_from_md(path):
    """Read head yaml content in every markdown (*.md) file.

    Before markdown begins, content for yaml is stored between two "---" lines.

    Examples
    --------
    Here is an example::

        ---
        layout: post
        title: My Title
        author: somebody
        ---

        # Markdown Header
        Some markdown content here.

    If we read this file (example.md), a dict will be return::

        >>> read_yaml_from_md('example.md')
        {'layout': 'post', 'title': 'My Title', 'author': 'somebody'}

    """
    with open(path) as f:
        # "---" is used to separate mutliple YAML entries,
        # so the loader returns a generator
        yaml_gen = load_all(f.read(), Loader=Loader)
        yaml_dict = next(yaml_gen)    # get first entry only
        return yaml_dict


def read_yaml(path):
    """Normal YAML reader, return single yaml record

    Examples
    --------
    Here is an example::

        layout: fb_fan
        title: My Title
        author: somebody

    Read this file (example.yaml) by

        >>> read_yaml('example.yaml')
        {'layout': 'fb_fan', 'title': 'My Title', 'author': 'somebody'}

    """
    with open(path) as f:
        yaml_gen = load_all(f.read(), Loader=Loader)
        yaml_dict = next(yaml_gen)
        return yaml_dict

