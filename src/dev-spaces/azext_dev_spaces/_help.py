# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps


helps['aks use-dev-spaces'] = """
    type: command
    short-summary: (PREVIEW) Use Azure Dev Spaces with a managed Kubernetes cluster.
    long-summary: "If needed, a Dev Spaces resource will be created and connected to the target cluster, and Dev Spaces commands will be installed on this machine."
    parameters:
        - name: --name -n
          type: string
          short-summary: Name of the managed cluster.
        - name: --resource-group -g
          type: string
          short-summary: Name of resource group. You can configure the default group. Using `az configure –defaults group=<name>`.
        - name: --space -s
          type: string
          short-summary: Name of the dev space to use.
        - name: --parent-space
          type: string
          short-summary: Name of a parent dev space to inherit from when creating a new dev space. By default, if there is already a single dev space with no parent, the new space inherits from this one.
"""

helps['aks remove-dev-spaces'] = """
    type: command
    short-summary: (PREVIEW) Detach Azure Dev Spaces from a managed Kubernetes cluster.
    parameters:
        - name: --name -n
          type: string
          short-summary: Name of the managed cluster.
        - name: --resource-group -g
          type: string
          short-summary: Name of resource group. You can configure the default group. Using `az configure –defaults group=<name>`.
        - name: --yes -y
          type: bool
          short-summary: Do not prompt for confirmation.
"""
