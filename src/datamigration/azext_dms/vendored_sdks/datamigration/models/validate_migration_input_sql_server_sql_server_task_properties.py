# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .project_task_properties import ProjectTaskProperties


class ValidateMigrationInputSqlServerSqlServerTaskProperties(ProjectTaskProperties):
    """Properties for task that validates migration input for SQL to SQL on VM
    migrations.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar errors: Array of errors. This is ignored if submitted.
    :vartype errors: list[~azure.mgmt.datamigration.models.ODataError]
    :ivar state: The state of the task. This is ignored if submitted. Possible
     values include: 'Unknown', 'Queued', 'Running', 'Canceled', 'Succeeded',
     'Failed', 'FailedInputValidation', 'Faulted'
    :vartype state: str or ~azure.mgmt.datamigration.models.TaskState
    :ivar commands: Array of command properties.
    :vartype commands:
     list[~azure.mgmt.datamigration.models.CommandProperties]
    :param client_data: Key value pairs of client data to attach meta data
     information to task
    :type client_data: dict[str, str]
    :param task_type: Constant filled by server.
    :type task_type: str
    :param input: Task input
    :type input:
     ~azure.mgmt.datamigration.models.ValidateMigrationInputSqlServerSqlServerTaskInput
    :ivar output: Task output. This is ignored if submitted.
    :vartype output:
     list[~azure.mgmt.datamigration.models.ValidateMigrationInputSqlServerSqlServerTaskOutput]
    """

    _validation = {
        'errors': {'readonly': True},
        'state': {'readonly': True},
        'commands': {'readonly': True},
        'task_type': {'required': True},
        'output': {'readonly': True},
    }

    _attribute_map = {
        'errors': {'key': 'errors', 'type': '[ODataError]'},
        'state': {'key': 'state', 'type': 'str'},
        'commands': {'key': 'commands', 'type': '[CommandProperties]'},
        'client_data': {'key': 'clientData', 'type': '{str}'},
        'task_type': {'key': 'taskType', 'type': 'str'},
        'input': {'key': 'input', 'type': 'ValidateMigrationInputSqlServerSqlServerTaskInput'},
        'output': {'key': 'output', 'type': '[ValidateMigrationInputSqlServerSqlServerTaskOutput]'},
    }

    def __init__(self, client_data=None, input=None):
        super(ValidateMigrationInputSqlServerSqlServerTaskProperties, self).__init__(client_data=client_data)
        self.input = input
        self.output = None
        self.task_type = 'ValidateMigrationInput.SqlServer.SqlServer'
