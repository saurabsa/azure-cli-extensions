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

from .sql_migration_task_input import SqlMigrationTaskInput


class MigrateSqlServerSqlDbTaskInput(SqlMigrationTaskInput):
    """Input for the task that migrates on-prem SQL Server databases to Azure SQL
    Database.

    All required parameters must be populated in order to send to Azure.

    :param source_connection_info: Required. Information for connecting to
     source
    :type source_connection_info:
     ~azure.mgmt.datamigration.models.SqlConnectionInfo
    :param target_connection_info: Required. Information for connecting to
     target
    :type target_connection_info:
     ~azure.mgmt.datamigration.models.SqlConnectionInfo
    :param selected_databases: Required. Databases to migrate
    :type selected_databases:
     list[~azure.mgmt.datamigration.models.MigrateSqlServerSqlDbDatabaseInput]
    :param validation_options: Options for enabling various post migration
     validations. Available options,
     1.) Data Integrity Check: Performs a checksum based comparison on source
     and target tables after the migration to ensure the correctness of the
     data.
     2.) Schema Validation: Performs a thorough schema comparison between the
     source and target tables and provides a list of differences between the
     source and target database, 3.) Query Analysis: Executes a set of queries
     picked up automatically either from the Query Plan Cache or Query Store
     and execute them and compares the execution time between the source and
     target database.
    :type validation_options:
     ~azure.mgmt.datamigration.models.MigrationValidationOptions
    """

    _validation = {
        'source_connection_info': {'required': True},
        'target_connection_info': {'required': True},
        'selected_databases': {'required': True},
    }

    _attribute_map = {
        'source_connection_info': {'key': 'sourceConnectionInfo', 'type': 'SqlConnectionInfo'},
        'target_connection_info': {'key': 'targetConnectionInfo', 'type': 'SqlConnectionInfo'},
        'selected_databases': {'key': 'selectedDatabases', 'type': '[MigrateSqlServerSqlDbDatabaseInput]'},
        'validation_options': {'key': 'validationOptions', 'type': 'MigrationValidationOptions'},
    }

    def __init__(self, **kwargs):
        super(MigrateSqlServerSqlDbTaskInput, self).__init__(**kwargs)
        self.selected_databases = kwargs.get('selected_databases', None)
        self.validation_options = kwargs.get('validation_options', None)
