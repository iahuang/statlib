import ast

with open("statlib.py") as fl:
    src = fl.read()
    lines = src.split("\n")
    root = ast.parse(src)

out: list[str] = []

for node in root.body:
    if isinstance(node, ast.FunctionDef):
        out.append("### `{}({})`".format(node.name, ", ".join(arg.arg for arg in node.args.args)))
        
        out.append("**Function signature**")
        out.append("```")
        out.append(lines[node.lineno-1].strip()[:-1])
        out.append("```")

        doc_comment: ast.Expr = node.body[0]  # type: ignore

        if isinstance(doc_comment.value, ast.Str):
            comment = doc_comment.value.value.strip()
            for line in comment.split("\n"):
                out.append(line.strip())
print("\n".join(out))
