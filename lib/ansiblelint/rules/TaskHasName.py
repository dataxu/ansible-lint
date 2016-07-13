import ansiblelint.utils
from ansiblelint import AnsibleLintRule

class TaskHasName(AnsibleLintRule):
    id = 'ANSIBLE1004'
    shortdesc = 'Tasks must have name'
    description = 'Tasks must have name'
    tags = ['productivity']


    def matchtask(self, file, task):
        # Only tasks that should not have a name are include or fail
        if not set(task.keys()).isdisjoint(['include','fail']):
            return False

        # Task should have tags
        return not task.has_key('name') 
