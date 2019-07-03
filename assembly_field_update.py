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
_ID = 0
for chi_name in amC.CHI_NAMES:
    Q_SET[_ID].chi_name = chi_name
    Q_SET[_ID].save()
    _ID += 1
