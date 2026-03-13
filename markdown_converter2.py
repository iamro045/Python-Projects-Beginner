def convert(line):
    if line.startswith("# "):
        return "<h1>" + line[2:] + "</h1>"
    elif line.startswith("## "):
        return "<h2>" + line[3:] + "</h2>"
    elif line.startswith("- "):
        return "<li>" + line[2:] + "</li>"
    else:
        return "<p>" + line + "</p>"

with open("input.md") as f:
    lines = f.read().splitlines()

html = [convert(line) for line in lines]

with open("output.html", "w") as f:
    f.write("\n".join(html))
