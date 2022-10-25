import os
file1 = '/usr/local/lib/python3.9/site-packages/xadmin-0.6.1-py3.9.egg/xadmin/sites.py'
new_file = []
with open(file1, 'r', encoding='utf-8') as f:
    for one_line in f.readlines():
        if one_line.startswith('from django.utils import six'):
            new_file.append('import six\n')
        elif one_line.startswith('from django.core.urlresolvers import NoReverseMatch, reverse'):
            new_file.append('from django.urls import NoReverseMatch, reverse\n')
        else:
            new_file.append(one_line)
with open(file1, 'w', encoding='utf-8') as f:
    f.writelines(new_file)

file2 = '/usr/local/lib/python3.9/site-packages/xadmin-0.6.1-py3.9.egg/xadmin/models.py'
new_file = []
with open(file2, 'r', encoding='utf-8') as f:
    for one_line in f.readlines():
        if one_line.startswith('from django.core.urlresolvers import NoReverseMatch, reverse'):
            new_file.append('from django.urls import NoReverseMatch, reverse\n')
        elif one_line.startswith('from django.utils.encoding import python_2_unicode_compatible, smart_text'):
            new_file.append('from six import python_2_unicode_compatible\n')
            new_file.append('from django.utils.encoding import smart_text\n')
        else:
            new_file.append(one_line)
with open(file2, 'w', encoding='utf-8') as f:
    f.writelines(new_file)

file3 = '/usr/local/lib/python3.9/site-packages/xadmin-0.6.1-py3.9.egg/xadmin/util.py'
new_file = []
with open(file3, 'r', encoding='utf-8') as f:
    for one_line in f.readlines():
        if one_line.startswith('from django.forms.forms import pretty_name'):
            pass
        elif one_line.startswith('from django.utils import formats, six'):
            new_file.append('from django.utils import formats\n')
            new_file.append('import six\n')
        elif one_line.startswith('from django.core.urlresolvers import reverse'):
            new_file.append('from django.urls import reverse\n')
        elif one_line.find('from django.contrib.staticfiles.templatetags.staticfiles import static') > 0:
            new_file.append('    from django.templatetags.static import static\n')
        else:
            new_file.append(one_line)
with open(file3, 'w', encoding='utf-8') as f:
    f.writelines(new_file)