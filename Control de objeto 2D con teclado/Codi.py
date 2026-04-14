import bpy

class CupheadMover(bpy.types.Operator):
    bl_idname = "object.cuphead_mover"
    bl_label = "Mover Cuphead Modal"

    def modal(self, context, event):
        obj = bpy.data.objects.get("Cuphead")

        if obj is None:
            self.report({'ERROR'}, "No existe un objeto llamado 'Cuphead'")
            return {'CANCELLED'}

        # Salir con ESC o click derecho
        if event.type in {'ESC', 'RIGHTMOUSE'}:
            context.workspace.status_text_set(None)
            self.report({'INFO'}, "Control finalizado.")
            return {'FINISHED'}

        if event.value == 'PRESS':
            if event.type == 'LEFT_ARROW':
                obj.location.x -= 0.5
                context.area.tag_redraw()
                return {'RUNNING_MODAL'}

            elif event.type == 'RIGHT_ARROW':
                obj.location.x += 0.5
                context.area.tag_redraw()
                return {'RUNNING_MODAL'}

            elif event.type == 'UP_ARROW':
                obj.location.z += 0.5
                context.area.tag_redraw()
                return {'RUNNING_MODAL'}

            elif event.type == 'DOWN_ARROW':
                obj.location.z -= 0.5
                context.area.tag_redraw()
                return {'RUNNING_MODAL'}

        return {'PASS_THROUGH'}

    def invoke(self, context, event):
        context.window_manager.modal_handler_add(self)
        context.workspace.status_text_set("Usa las flechas para mover Cuphead | ESC para salir")
        return {'RUNNING_MODAL'}


def register():
    bpy.utils.register_class(CupheadMover)

def unregister():
    bpy.utils.unregister_class(CupheadMover)


if __name__ == "__main__":
    register()
    bpy.ops.object.cuphead_mover('INVOKE_DEFAULT')
