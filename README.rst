Sliders
-------

Currently only includes one module: flextableparser. To use::

    >>> from sliders import flextableparser
    >>> parser = flextableparser.FlexTableParser(config.json, output_file, static_values)
    >>> parser = flextableparser.FlexTableParser()
    >>> parser.configure(json_file)
    >>> parser.add_static_values(dict)
    >>> parser.parse_file(input_file, output_file_handle)
    >>> output = parser.parse_file(input_file)