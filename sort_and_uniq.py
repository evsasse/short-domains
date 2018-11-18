with open('./domains.txt') as file:
  domains = file.readlines()

domains = sorted(set(domains))

print(len(domains))


with open('./domains.txt', '+w') as file:
  for domain in domains:
    file.write(domain)