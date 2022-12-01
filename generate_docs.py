import ast

with open("statlib.py") as fl:
    src = fl.read()
    lines = src.split("\n")
    root = ast.parse(src)

out: list[str] = []
tldr: list[str] = []

for node in root.body:
    if isinstance(node, ast.FunctionDef):
        out.append("\n---\n")

        func_brief = "`{}({})`".format(
            node.name,
            ", ".join(
                arg.arg
                for i, arg in enumerate(node.args.args)
                if i < len(node.args.args) - len(node.args.defaults)
            ),
        )
        out.append("### " + func_brief)
        tldr.append(" - " + func_brief)

        out.append("**Function signature**")
        out.append("```")
        out.append(lines[node.lineno - 1].strip()[:-1])
        out.append("```")

        doc_comment: ast.Expr = node.body[0]  # type: ignore

        if isinstance(doc_comment.value, ast.Str):
            comment = doc_comment.value.value.strip()
            for line in comment.split("\n"):
                out.append(line.strip())
print("\n".join(tldr))
print("\n".join(out))
