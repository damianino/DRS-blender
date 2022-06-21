# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "DRS",
    "author" : "alessandro",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 2),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}


import logging
import bpy

from drs_addon.operators.connect_drs_op import DRS_OP_Connect
from .operators.render_section_op import DRS_OT_RenderSection
from .operators.initiate_task_render_op import DRS_OP_InitiateTaskRender
from .operators.enable_logging_op import DRS_OP_EnableLoggingOperator
from .panels.DRS_PT_DRS import DRS_PT_Panel
from .store.store import DRS

from .drs_client.drs_client import *

def register():
    bpy.types.WindowManager.DRS = DRS
    bpy.utils.register_class(DRS_OP_EnableLoggingOperator)
    bpy.utils.register_class(DRS_OT_RenderSection)
    bpy.utils.register_class(DRS_OP_InitiateTaskRender)
    bpy.utils.register_class(DRS_OP_Connect)
    bpy.utils.register_class(DRS_PT_Panel)

    print(__name__)

def unregister():
    bpy.utils.unregister_class(DRS_OP_EnableLoggingOperator)
    bpy.utils.unregister_class(DRS_OP_InitiateTaskRender)
    bpy.utils.unregister_class(DRS_OT_RenderSection)
    bpy.utils.unregister_class(DRS_OP_Connect)
    bpy.utils.unregister_class(DRS_PT_Panel)

    print(__name__)
