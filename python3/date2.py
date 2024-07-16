from datetime import datetime

maintenant = datetime.now()
print(type(maintenant))
print(maintenant)

from datetime import timedelta

demain = maintenant + timedelta(days=1)
print(demain)


