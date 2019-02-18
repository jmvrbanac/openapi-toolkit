OpenAPI Toolkit
===============

OpenAPI Toolkit is currently an experimental project to streamline handling
and workarounds related to using OpenAPI in your applications.

While this project is an a experimental state, it is subject to contract
breakage.

Commandline Usage
-----------------

.. code-block:: shell

    openapi-toolkit resolve --help
    usage: openapi-toolkit resolve [-h] [--preprocessor {mako}]
                                   [--save-path SAVE_PATH]
                                   filename

    Resolve OpenAPI Spec

    positional arguments:
      filename              Path of spec to resolve.

    optional arguments:
      -h, --help            show this help message and exit
      --preprocessor {mako}
                            Enable a preprocessor to use on the specification.
      --save-path SAVE_PATH
                            Path to save resolved content.
