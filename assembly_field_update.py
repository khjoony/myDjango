"""
      test
"""
import os
import django
from assembly.package.package.assembly_member_list import KrName as amK, ChiName as amC, EnName as amE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myDjango.settings")
django.setup()
from assembly.models import Member

Q_SET = Member.objects.all()
for i in range(0, len(amK.KR_NAMES)):
    print(amK.MEMBER_IDS[i], amK.KR_NAMES[i], amC.CHI_NAMES[i], amE.EN_NAMES[i])
## Update CHI_Names
"""
_ID = 1
for chi_name in amC.CHI_NAMES:
    member_instance = Member.objects.get(id=_ID)
    member_instance.chi_name = chi_name
    member_instance.save()
    _ID += 1
"""

## Update Membership_id
"""
_ID = 1
for member_id in amK.MEMBER_IDS:
    member_instance = Member.objects.get(id=_ID)
    member_instance.membership_id = member_id
    member_instance.save()
    _ID += 1
"""

## Update EN_Names
"""
_ID = 1
for en_name in amE.EN_NAMES:
    member_instance = Member.objects.get(id=_ID)
    member_instance.en_name = en_name
    member_instance.save()
    _ID += 1
"""
