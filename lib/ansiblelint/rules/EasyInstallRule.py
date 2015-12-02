import ansiblelint.utils
from ansiblelint import AnsibleLintRule


class EasyInstallRule(AnsibleLintRule):
    id = 'ANSIBLE1002'
    shortdesc = 'easy_install not recommended tool'
    description = 'easy_install is not a recommended tool for installing ' + \
                  'to production machines. Switch this task to use pip or yum.'
    tags = ['repeatability']

    def matchtask(self, file, task):
        return (task['action']['module'] == 'easy_install')
