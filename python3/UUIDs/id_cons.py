import uuid

dns_uuid = uuid.uuid3(uuid.NAMESPACE_DNS, 'example.com')
print(dns_uuid)

