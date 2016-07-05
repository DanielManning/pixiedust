# -------------------------------------------------------------------------------
# Copyright IBM Corp. 2016
# 
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -------------------------------------------------------------------------------

from ..display import *
from .test1 import *

class TestsDisplayMeta(DisplayHandlerMeta):
    @addId
    def getMenuInfo(self,entity):
        if entity=="test1":
            return [
                {"categoryId": "Test", "title": "Test1", "icon": "fa-bar-chart", "id": "Test1"}
            ]
        else:
            return []
    def newDisplayHandler(self,handlerId,entity):
        return Test1Display(entity)

registerDisplayHandler(TestsDisplayMeta())