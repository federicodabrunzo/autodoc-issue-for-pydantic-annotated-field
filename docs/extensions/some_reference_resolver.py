from sphinx.transforms.post_transforms import ReferencesResolver
import typing
from sphinx import addnodes


class SomeReferenceResolver(ReferencesResolver):
    default_priority = 8

    def run(self, **kwargs: typing.Any) -> None:
        print("===============================")
        for node in self.document.findall(addnodes.pending_xref):
            print(node["reftarget"])
        print("===============================")

def setup(app):
    app.add_post_transform(SomeReferenceResolver)
    # Allow extension to be used when building with multiple processes
    return dict(parallel_read_safe=True)