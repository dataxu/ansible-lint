import ansiblelint.utils
from ansiblelint import AnsibleLintRule
import re


class YumHasVersionRule(AnsibleLintRule):
    id = 'ANSIBLE1003'
    shortdesc = 'Yum installing package without explicit version'
    description = 'When installing packages be explicit with ' + \
                  'version. This helps create a reproducable ' + \
                  'environment and limits the impact from ' + \
                  'unexpected changes to the system'
    tags = ['repeatability']

    _pattern = re.compile(r'.*\-[0-9]+(\.[0-9]+)+')
    _variable_pattern = re.compile(r'.*(\{\{.*\}\}|\*)')

    def matchtask(self, file, task):
        if task['action']['module'] == 'yum':
            name = task['action'].get('name')
            if(name and not self._pattern.match(name) and
               not self._variable_pattern.match(name)):
               message = 'Yum package {0} should be installed with ' +\
                         'explicit version'
               return message.format(name)
