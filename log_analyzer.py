import re

log_file = "server.log"
error_count = {}

with open(log_file) as f:
    for line in f:
        match = re.search(r"(ERROR|WARNING)", line)
        if match:
            error_count[match.group()] = error_count.get(match.group(), 0) + 1

print("📊 Log Summary:")
for k, v in error_count.items():
    print(k, v)
