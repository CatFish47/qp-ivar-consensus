# -----------------------------------------------------------------------------
# Copyright (c) 2020, Qiita development team.
#
# Distributed under the terms of the BSD 3-clause License License.
#
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------

from qiita_client import QiitaPlugin, QiitaCommand
from .qp_ivar_consensus import ivar_consensus
from .utils import plugin_details
from os.path import splitext


THREADS = 15


# Initialize the plugin
plugin = QiitaPlugin(**plugin_details)

# Define the command
# req_params = {'input': ('artifact', ['per_sample_BAM'])}
req_params = {'input': ('artifact', ['per_sample_FASTQ'])}
opt_params = {
    'threads': ['integer', f'{THREADS}']}

# outputs = {'Filtered files': 'per_sample_BAM'}
outputs = {'Filtered files': 'per_sample_FASTQ'}
default_params = {
    'default params': {'threads': THREADS}
}

ivar_consensus_cmd = QiitaCommand(
    'Samtools sorting', "Sorting using samtools",
    ivar_consensus, req_params, opt_params, outputs, default_params)

plugin.register_command(ivar_consensus_cmd)
