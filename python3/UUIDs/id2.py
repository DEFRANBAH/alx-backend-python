import uuid

my_id = uuid.uuid4()
print(my_id)

hash1 = uuid.uuid3(uuid.NAMESPACE_DNS, 'example.com')
print(hash1.bytes_le)

hash2 = uuid.uuid5(uuid.NAMESPACE_DNS, 'example.com')
print(hash2.fields)

hash3 = uuid.uuid5(uuid.NAMESPACE_X500, 'example.com')
print(hash3.urn)


