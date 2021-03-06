# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands import CliCommandType
from azure.cli.core.commands.arm import deployment_validate_table_format, handle_template_based_exception

from ._format import (
    transform_sqlvm_group_output,
    transform_sqlvm_group_list,
    transform_sqlvm_output,
    transform_sqlvm_list,
    transform_aglistener_output,
    transform_aglistener_list
)

from ._util import (
    get_sqlvirtualmachine_availability_group_listeners_operations,
    get_sqlvirtualmachine_sql_virtual_machine_groups_operations,
    get_sqlvirtualmachine_sql_virtual_machines_operations,
)


# pylint: disable=too-many-statements,line-too-long,too-many-locals
def load_command_table(self, _):

    ###############################################
    #            sql virtual machine              #
    ###############################################

    sqlvm_vm_operations = CliCommandType(
        operations_tmpl='azext_sqlvm_preview.vendored_sdks.sqlvirtualmachine.operations.sql_virtual_machines_operations#SqlVirtualMachinesOperations.{}',
        client_factory=get_sqlvirtualmachine_sql_virtual_machines_operations
    )

    with self.command_group('sqlvm',
                            sqlvm_vm_operations,
                            client_factory=get_sqlvirtualmachine_sql_virtual_machines_operations) as g:
        g.generic_update_command('update', custom_func_name='sqlvm_update', transform=transform_sqlvm_output)
        g.command('show', 'get', transform=transform_sqlvm_output)
        g.custom_command('list', 'sqlvm_list', transform=transform_sqlvm_list)
        g.command('delete', 'delete', confirmation=True)
        g.generic_update_command('add-to-group', custom_func_name='add_sqlvm_to_group', transform=transform_sqlvm_output)
        g.generic_update_command('remove-from-group', custom_func_name='remove_sqlvm_from_group', transform=transform_sqlvm_output)
        g.custom_command('create', 'sqlvm_create', transform=transform_sqlvm_output, table_transformer=deployment_validate_table_format, exception_handler=handle_template_based_exception)

    ###############################################
    #      sql virtual machine groups             #
    ###############################################

    sqlvm_group_operations = CliCommandType(
        operations_tmpl='azext_sqlvm_preview.vendored_sdks.sqlvirtualmachine.operations.sql_virtual_machine_groups_operations#SqlVirtualMachineGroupsOperations.{}',
        client_factory=get_sqlvirtualmachine_sql_virtual_machine_groups_operations
    )

    with self.command_group('sqlvm group',
                            sqlvm_group_operations,
                            client_factory=get_sqlvirtualmachine_sql_virtual_machine_groups_operations) as g:
        g.generic_update_command('update', custom_func_name='sqlvm_group_update', transform=transform_sqlvm_group_output)
        g.command('show', 'get', transform=transform_sqlvm_group_output)
        g.custom_command('list', 'sqlvm_group_list', transform=transform_sqlvm_group_list)
        g.command('delete', 'delete', confirmation=True)
        g.custom_command('create', 'sqlvm_group_create', transform=transform_sqlvm_group_output, table_transformer=deployment_validate_table_format, exception_handler=handle_template_based_exception)

    ###############################################
    #      availability group listener            #
    ###############################################

    sqlvm_agl_operations = CliCommandType(
        operations_tmpl='azext_sqlvm_preview.vendored_sdks.sqlvirtualmachine.operations.availability_group_listeners_operations#AvailabilityGroupListenersOperations.{}',
        client_factory=get_sqlvirtualmachine_availability_group_listeners_operations
    )

    with self.command_group('sqlvm aglistener',
                            sqlvm_agl_operations,
                            client_factory=get_sqlvirtualmachine_availability_group_listeners_operations) as g:
        g.generic_update_command('add-sqlvm', custom_func_name='add_sqlvm_to_aglistener', transform=transform_aglistener_output)
        g.generic_update_command('remove-sqlvm', custom_func_name='remove_sqlvm_from_aglistener', transform=transform_aglistener_output)
        g.command('show', 'get', transform=transform_aglistener_output)
        g.command('list', 'list_by_group', transform=transform_aglistener_list)
        g.command('delete', 'delete', confirmation=True)
        g.custom_command('create', 'sqlvm_aglistener_create', transform=transform_aglistener_output, table_transformer=deployment_validate_table_format, exception_handler=handle_template_based_exception)
