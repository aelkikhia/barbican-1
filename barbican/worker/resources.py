# Copyright (c) 2013 Rackspace, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Queue Resources related objects and functions.
"""
from oslo.config import cfg
from barbican.openstack.common import importutils


CONF = cfg.CONF

def get_worker_api():
    return importutils.import_module(CONF.worker.worker_api)

class WorkerResource(object):
    """Handles Queue related requests"""
    
    def __init__(self, worker_api=None):
        self.api = worker_api or get_worker_api() 

    def receive(self, message):
        self.api.process(message)
    
