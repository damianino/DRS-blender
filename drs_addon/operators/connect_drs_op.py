import bpy
from ..drs_client.grpc_client import GRPCClient

class DRS_OP_Connect(bpy.types.Operator):
    bl_idname = "drs.connect"
    bl_label = "DRS_OP_Connect"

    ip : bpy.props.StringProperty(name="ip address", default="")
    id : bpy.props.IntProperty(name="user id", default=1)

    def execute(self, context):
        GRPCClient.Connect(self.ip + ":4000", self.id)

        return {'FINISHED'}
