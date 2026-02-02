class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0

    def get_server(self):
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server

lb = LoadBalancer(["S1", "S2", "S3"])

for _ in range(6):
    print("➡️ Request sent to", lb.get_server())
  
