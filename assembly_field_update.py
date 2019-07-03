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
## print(amK.MEMBER_IDS, amK.KR_NAMES, amC.CHI_NAMES, amE.EN_NAMES)
_ID = 1
for chi_name in amC.CHI_NAMES:
    member_instance = Member.objects.get(id=_ID)
    member_instance.chi_name = chi_name
    member_instance.save()
    _ID += 1
