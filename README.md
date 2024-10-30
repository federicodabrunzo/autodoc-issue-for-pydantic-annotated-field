# autodoc-issue-for-pydantic-annotated-field
While I was trying to generate documentation with the `autodoc` extension I came into an issue for certain pydantic models.

It looks like that under certain circumstances autodoc is interpreting the `Annotated` class to come from a different module as we would expect — for this example its `reftarget` is `example.enumerations.Annotated`.

This example project contains the bare minimum to trigger the issue:
- there's an [autoclass directive](docs/index.rst?plain=1#L13) for a pydantic model
- the model has an [annotated field](src/example/models.py#L12) with `BeforeValidator`/`AfterValidator`
- the annotated type is an enumeration
- the enumeration is imported from another module

Sphinx is setup with an [additional extension](docs/extensions/some_reference_resolver.py) that prints the `reftarget` of `pending_xref` nodes — in this way we can show the unexpected behavior.

## Steps to reproduce
Install the requirements:
```
pip install -r requirements.txt
```

Run the build:
```
sphinx-build --fresh-env docs docs/_build
```

The output should contain:
```
===============================
example.enumerations.Annotated
example.enumerations.FruitEnum
pydantic.functional_validators.BeforeValidator
example.models.validate
PydanticUndefined
===============================
```

The `example.enumerations.Annotated` line is unexpected.
