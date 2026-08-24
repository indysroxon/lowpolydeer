bl_info = {
    "name": "Low Poly Deer Tutorial",
    "author": "Indy's Roxon",
    "version": (1, 0, 0),
    "blender": (5, 0, 0),
    "location": "N-Panel > Low Poly Deer",
    "description": "Interactive step-by-step tutorial for low poly character modeling",
    "category": "Tutorials",
}

import bpy
import os
from bpy.types import Panel, Operator, PropertyGroup
from bpy.props import IntProperty, StringProperty

# ============================================================================
# TUTORIAL DATA - All 42 steps with complete information
# ============================================================================

TUTORIAL_STEPS = [
    {
        "title": "Navigation Fundamentals",
        "time": "00:00:00 → 00:00:58",
        "description": "Learn essential Blender viewport navigation controls. Middle mouse button orbits around the pivot point, scroll wheel zooms in/out, and Shift + Middle Mouse Button strafes across the screen.",
        "hotkeys": "Shift + Middle Mouse Button",
        "image_name": "frame_01.jpg"
    },
    {
        "title": "Importing Reference Image",
        "time": "00:00:58 → 00:01:23",
        "description": "Locate your downloaded stag reference artwork and drag-drop it directly into the Blender viewport to spawn a camera-aligned orthographic image plane for initial character setup.",
        "hotkeys": "Click and Drag",
        "image_name": "frame_02.jpg"
    },
    {
        "title": "Resetting Reference Location & Rotation",
        "time": "00:01:23 → 00:01:45",
        "description": "Reset default transformation offsets on the imported reference image by clearing grab position and rotation. Rotate the image 90 degrees around the X-axis so it stands vertically perpendicular to the ground plane.",
        "hotkeys": "Alt + G / Alt + R / R X 90",
        "image_name": "frame_03.jpg"
    },
    {
        "title": "Switching to Front View & Enabling X-Ray",
        "time": "00:01:45 → 00:02:14",
        "description": "Switch the viewport to Orthographic Front View looking directly down the Y-axis. Activate X-Ray view mode to allow full visual visibility of the reference background image through solid viewport meshes.",
        "hotkeys": "Numpad 1 / Alt + Z",
        "image_name": "frame_04.jpg"
    },
    {
        "title": "Adjusting Image Reference Opacity",
        "time": "00:02:14 → 00:02:30",
        "description": "Select the imported reference image plane and navigate to Object Data Properties. Toggle Opacity and lower the value to 0.2 to render grid lines clearly visible behind artwork.",
        "hotkeys": "N/A",
        "image_name": "frame_05.jpg"
    },
    {
        "title": "Centering Front Reference Image",
        "time": "00:02:30 → 00:03:06",
        "description": "Align the stag face precisely over the world origin 3D Cursor using constrained X-axis grabbing. Translate the plane backward along the Y-axis behind the active modeling workspace.",
        "hotkeys": "G X / G Y / Shift + S",
        "image_name": "frame_06.jpg"
    },
    {
        "title": "Duplicating and Rotating Side Reference",
        "time": "00:03:06 → 00:03:45",
        "description": "Switch to Top View, duplicate the front reference image plane, and execute a 90-degree rotation around the Z-axis to quickly construct the orthographic right-side reference plane.",
        "hotkeys": "Numpad 7 / Shift + D / R Z 90",
        "image_name": "frame_07.jpg"
    },
    {
        "title": "Aligning Side Reference View",
        "time": "00:03:45 → 00:04:06",
        "description": "Switch viewport perspective to Right Side View and translate the duplicated reference plane along the Y-axis into position in front of the center cube while preserving exact horizontal height alignment.",
        "hotkeys": "Numpad 3 / G Y",
        "image_name": "frame_08.jpg"
    },
    {
        "title": "Organizing Reference Collections",
        "time": "00:04:06 → 00:04:45",
        "description": "Select both reference image planes in the viewport and assign them into a newly created collection titled 'Ref'. Rename individual image plane objects to 'Front' and 'Side' inside the Outliner for organized file management.",
        "hotkeys": "M",
        "image_name": "frame_09.jpg"
    },
    {
        "title": "Initializing Mesh Cube in Edit Mode",
        "time": "00:04:45 → 00:05:21",
        "description": "Select the default cube object, scale and translate it into position over the stag chest region in Right Side View. Enter Edit Mode with Vertex Selection mode activated to begin manipulating corner points.",
        "hotkeys": "G / S / Tab / 1",
        "image_name": "frame_10.jpg"
    },
    {
        "title": "Box Selecting Base Vertices",
        "time": "00:05:21 → 00:06:10",
        "description": "In Side View with X-Ray mode enabled, use box selection to grab front and rear vertex pairs together. Align the box corners along the top and bottom boundaries of the chest reference artwork outline.",
        "hotkeys": "B / G",
        "image_name": "frame_11.jpg"
    },
    {
        "title": "Extruding Initial Torso Geometry",
        "time": "00:06:10 → 00:06:55",
        "description": "Switch to Face Selection mode, select the rear box face, and extrude geometry outward along the torso contour. Manually tweak individual vertex pair heights to tightly match the reference artwork silhouette.",
        "hotkeys": "3 / E / R / 1",
        "image_name": "frame_12.jpg"
    },
    {
        "title": "Extruding Backwards along Hindquarters",
        "time": "00:06:55 → 00:07:42",
        "description": "Continue extruding face segments sequentially along the back and hindquarters reaching to the base of the tail. Continually switch to Vertex mode to match key anatomical pivot points along the stag reference drawing.",
        "hotkeys": "E / 1 / G",
        "image_name": "frame_13.jpg"
    },
    {
        "title": "Extruding Neck and Head Outline",
        "time": "00:07:42 → 00:08:42",
        "description": "Select front facing polygon surfaces and extrude upward and forward in steps, shaping the neck profile, throat, chin, and snout outline by rotating and translating vertex pairs in Right Side View.",
        "hotkeys": "3 / E / R / 1",
        "image_name": "frame_14.jpg"
    },
    {
        "title": "Adding Mid-Leg Loop Cut",
        "time": "00:08:42 → 00:09:31",
        "description": "Insert a vertical loop cut through the middle of the body block structure aligned with the front leg origin point. Right-click immediately after placement to maintain perfect centered edge alignment across the torso.",
        "hotkeys": "Ctrl + R",
        "image_name": "frame_15.jpg"
    },
    {
        "title": "Inserting Head and Neck Loop Cuts",
        "time": "00:09:31 → 00:10:07",
        "description": "Add extra horizontal loop cuts across the neck and facial regions using loop cut tools to supply sufficient vertex resolution for forming organic curves along the head, jawline, and neck structure.",
        "hotkeys": "Ctrl + R",
        "image_name": "frame_16.jpg"
    },
    {
        "title": "Bisecting the Mesh Down Center",
        "time": "00:10:07 → 00:10:46",
        "description": "Add a central longitudinal loop cut down the complete length of the mesh body. Open the edge loop tool settings to set the offset factor precisely to zero for perfect centerline alignment.",
        "hotkeys": "Ctrl + R",
        "image_name": "frame_17.jpg"
    },
    {
        "title": "Deleting Half the Geometry",
        "time": "00:10:46 → 00:11:03",
        "description": "Switch to Face Select mode in Edit Mode, box select all polygons located on one half of the bisected mesh model, and delete the selected faces to prepare for symmetrical modifier modeling.",
        "hotkeys": "3 / Delete",
        "image_name": "frame_18.jpg"
    },
    {
        "title": "Adding Mirror Modifier with Clipping",
        "time": "00:11:03 → 00:11:51",
        "description": "Navigate to the Modifiers panel, add a Mirror Modifier set along the local X-axis, and enable the Clipping toggle option to securely weld center boundary vertices along the middle symmetry line.",
        "hotkeys": "N/A",
        "image_name": "frame_19.jpg"
    },
    {
        "title": "Adding Longitudinal Body Cut",
        "time": "00:11:51 → 00:12:46",
        "description": "Insert a horizontal loop cut along the outer flank of the half-torso mesh, establishing isolated lower face regions needed to extrude front and hind limbs independently away from the body centerline.",
        "hotkeys": "Ctrl + R",
        "image_name": "frame_20.jpg"
    },
    {
        "title": "Extruding Front Limb Base",
        "time": "00:12:46 → 00:13:22",
        "description": "Select the underside faces located beneath the shoulder section and extrude downward to form the base of the front legs. Scale the extruded face slightly inward to establish correct upper leg thickness.",
        "hotkeys": "3 / E / S",
        "image_name": "frame_21.jpg"
    },
    {
        "title": "Extruding Front Leg to Ground",
        "time": "00:13:22 → 00:14:11",
        "description": "Extrude the front limb downward through joint segments to ground level. Then scale base vertices on the Z-axis by factor zero to flatten the lower hoof flush against the ground plane floor.",
        "hotkeys": "E / S Z 0",
        "image_name": "frame_22.jpg"
    },
    {
        "title": "Extruding Rear Limb Segments",
        "time": "00:14:11 → 00:14:42",
        "description": "Select the rear underside faces and extrude step-by-step downward following side reference artwork to construct the upper hocks, lower legs, ankle joints, and ground-level hooves for the hind legs.",
        "hotkeys": "E / S Y / G",
        "image_name": "frame_23.jpg"
    },
    {
        "title": "Adding Horizontal Body Loop Cut",
        "time": "00:14:42 → 00:15:28",
        "description": "Add a longitudinal loop cut horizontally around the middle of the torso, giving extra edge control needed to push upper and lower body edges into rounded anatomical curves.",
        "hotkeys": "Ctrl + R",
        "image_name": "frame_24.jpg"
    },
    {
        "title": "Adjusting Front Width and Taper",
        "time": "00:15:28 → 00:16:25",
        "description": "In Front View X-Ray mode, translate outer leg and neck faces inward along the X-axis to match reference front width. Take care not to allow off-center vertices to clip onto the center seam.",
        "hotkeys": "Numpad 1 / G X",
        "image_name": "frame_25.jpg"
    },
    {
        "title": "Sliding Edge Loops for Curvature",
        "time": "00:16:25 → 00:17:05",
        "description": "Select horizontal body edge loops with loop select and utilize edge slide tools to shift loop positions, rounding out blocky flat surface geometry into curved contours across the flanks and shoulders.",
        "hotkeys": "Alt + Left Click / G G",
        "image_name": "frame_26.jpg"
    },
    {
        "title": "Rounding Legs and Hindquarters",
        "time": "00:17:05 → 00:18:02",
        "description": "Select corner edge loops running vertically down the legs and slide them inward and outward using edge slide to convert square boxy limb extrusions into rounded, cylinder-like leg structures.",
        "hotkeys": "2 / G G",
        "image_name": "frame_27.jpg"
    },
    {
        "title": "Refining Torso and Underbelly Curves",
        "time": "00:18:02 → 00:18:43",
        "description": "Adjust underbelly vertices upward and push groin edge loops inward toward the center to build realistic transitions where limbs attach to the main torso, eliminating flat underbody geometry.",
        "hotkeys": "G Z / G G",
        "image_name": "frame_28.jpg"
    },
    {
        "title": "Refining Snout, Jaw, and Shoulder",
        "time": "00:18:43 → 00:19:52",
        "description": "Add a vertical loop cut across the head, pull snout vertices inward to create a tapered muzzle, and expand shoulder vertices outward on the X-axis to match front reference proportions.",
        "hotkeys": "Ctrl + R / G X",
        "image_name": "frame_29.jpg"
    },
    {
        "title": "Evening Out Topology Spacing",
        "time": "00:19:52 → 00:20:22",
        "description": "Slide misaligned edge loops across body segments using edge slide to redistribute polygon spacing evenly, creating smooth low-poly surfaces and consistent quad grid distribution across the entire mesh.",
        "hotkeys": "G G",
        "image_name": "frame_30.jpg"
    },
    {
        "title": "Insetting the Eye Polygon",
        "time": "00:20:22 → 00:21:04",
        "description": "Select the facial polygon corresponding to the eye position, inset a smaller face inward, pull it slightly outward on the X-axis, and rotate it forward to form a distinct low-poly eye socket.",
        "hotkeys": "3 / I / R Z",
        "image_name": "frame_31.jpg"
    },
    {
        "title": "Insetting and Extruding Ears",
        "time": "00:21:04 → 00:22:04",
        "description": "Add an extra loop cut near the back of the head, inset a polygon behind the eye socket, extrude it outward twice, and shape vertex locations to form an angled low-poly ear.",
        "hotkeys": "Ctrl + R / I / E",
        "image_name": "frame_32.jpg"
    },
    {
        "title": "Insetting and Extruding Antler Bases",
        "time": "00:22:04 → 00:23:18",
        "description": "Select forehead faces located above the eye sockets, inset new base faces, and extrude upward and outward in short initial segments to begin constructing main antler stems.",
        "hotkeys": "I / E / R",
        "image_name": "frame_33.jpg"
    },
    {
        "title": "Extruding Secondary Antler Tines",
        "time": "00:23:18 → 00:24:12",
        "description": "Select outer side faces on main antler stems, extrude secondary branches outward, and scale down tip faces to quickly build multi-pointed branching antler tines extending from the stag head.",
        "hotkeys": "E / S / R",
        "image_name": "frame_34.jpg"
    },
    {
        "title": "Adding Antler Loop Cuts",
        "time": "00:24:12 → 00:24:56",
        "description": "Insert loop cuts along straight antler sections using the scroll wheel. Then pull and rotate individual loop selections in 3D space to add organic natural curves to the low-poly antlers.",
        "hotkeys": "Ctrl + R / G / R",
        "image_name": "frame_35.jpg"
    },
    {
        "title": "Insetting and Extruding Tail",
        "time": "00:24:56 → 00:25:25",
        "description": "Select the rear face at the base of the spine, inset with boundary mode toggled off to maintain mirror seam symmetry, and extrude backward to construct a low-poly tail.",
        "hotkeys": "3 / I B / E",
        "image_name": "frame_36.jpg"
    },
    {
        "title": "Final Anatomical Proportion Cleanup",
        "time": "00:25:25 → 00:26:01",
        "description": "Disable X-Ray view to inspect solid mesh shading. Slide misaligned vertices with edge slide to smooth planar surfaces and scale up antler selections to match overall reference drawing scale.",
        "hotkeys": "Alt + Z / G G / Numpad Period",
        "image_name": "frame_37.jpg"
    },
    {
        "title": "Assigning Base Light Brown Material",
        "time": "00:26:01 → 00:26:45",
        "description": "Switch to the Shading workspace and hide reference collections. Rename default material to 'Light Brown', set warm orange-brown base color, and increase Roughness to create non-reflective fur appearance.",
        "hotkeys": "N/A",
        "image_name": "frame_38.jpg"
    },
    {
        "title": "Assigning Dark Brown Antler Material",
        "time": "00:26:45 → 00:27:30",
        "description": "Add a secondary material slot in Edit Mode, select all antler polygons using lasso selection, create a 'Dark Brown' material, and click Assign to color the antlers darker than the body.",
        "hotkeys": "Ctrl + Right Click / 3",
        "image_name": "frame_39.jpg"
    },
    {
        "title": "Creating Shiny Black Eye Material",
        "time": "00:27:30 → 00:28:07",
        "description": "Create a third material slot, select eye polygons, add a new material named 'Black' with dark base color and low Roughness, and click Assign to produce glossy shiny eyes.",
        "hotkeys": "3",
        "image_name": "frame_40.jpg"
    },
    {
        "title": "Carving Nose and Mouth with Knife Tool",
        "time": "00:28:07 → 00:29:07",
        "description": "Carve custom facial details on the muzzle using the Knife tool. Dissolve unneeded interior edges, select resulting nose and mouth polygons, and assign the Black material slot to them.",
        "hotkeys": "K / Ctrl + X / 3",
        "image_name": "frame_41.jpg"
    },
    {
        "title": "Reviewing Rendered Low-Poly Stag",
        "time": "00:29:07 → 00:29:27",
        "description": "Switch viewport display to Material Preview mode to inspect and verify multi-material color assignment across body fur, dark antlers, glossy eyes, and carved muzzle details, completing the low-poly stag model.",
        "hotkeys": "Z",
        "image_name": "frame_42.jpg"
    }
]

# ============================================================================
# HELPER FUNCTIONS - Store progress as binary string (workaround for Blender 5.2)
# ============================================================================

def encode_progress(bool_list):
    """Encode list of 42 booleans as a binary string"""
    binary = ''.join('1' if b else '0' for b in bool_list)
    return binary

def decode_progress(binary_str):
    """Decode binary string back to list of 42 booleans"""
    if not binary_str or len(binary_str) != 42:
        return [False] * 42
    return [c == '1' for c in binary_str]

# ============================================================================
# PROPERTY GROUP FOR PERSISTENT STEP TRACKING
# ============================================================================

class TutorialStepProperties(PropertyGroup):
    """Store completed steps per file"""
    completed_steps_binary: StringProperty(
        name="Completed Steps",
        description="Track which tutorial steps have been completed (binary string)",
        default="000000000000000000000000000000000000000000"
    )
    current_step: IntProperty(
        name="Current Step",
        description="Currently selected step (1-42)",
        min=1,
        max=42,
        default=1
    )
    image_folder_path: StringProperty(
        name="Image Folder Path",
        description="Path to folder containing frame_XX.jpg images",
        subtype='DIR_PATH'
    )

# ============================================================================
# OPERATORS
# ============================================================================

class LPDT_OT_toggle_step(Operator):
    """Toggle step completion status"""
    bl_idname = "lpdt.toggle_step"
    bl_label = "Toggle Step"
    bl_options = {'REGISTER', 'UNDO'}
    
    step_index: IntProperty()
    
    def execute(self, context):
        props = context.scene.lpdt_props
        completed = decode_progress(props.completed_steps_binary)
        completed[self.step_index] = not completed[self.step_index]
        props.completed_steps_binary = encode_progress(completed)
        return {'FINISHED'}

class LPDT_OT_set_current_step(Operator):
    """Set the current step to display"""
    bl_idname = "lpdt.set_current_step"
    bl_label = "Set Current Step"
    bl_options = {'REGISTER', 'UNDO'}
    
    step_index: IntProperty()
    
    def execute(self, context):
        props = context.scene.lpdt_props
        props.current_step = self.step_index + 1
        return {'FINISHED'}

class LPDT_OT_reset_progress(Operator):
    """Reset all progress with confirmation"""
    bl_idname = "lpdt.reset_progress"
    bl_label = "Reset All Progress"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        props = context.scene.lpdt_props
        props.completed_steps_binary = "000000000000000000000000000000000000000000"
        props.current_step = 1
        self.report({'INFO'}, "Tutorial progress reset")
        return {'FINISHED'}
    
    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)

class LPDT_OT_set_image_folder(Operator):
    """Set the folder containing tutorial images"""
    bl_idname = "lpdt.set_image_folder"
    bl_label = "Set Image Folder"
    bl_options = {'REGISTER', 'UNDO'}
    
    directory: StringProperty(
        name="Image Folder",
        subtype='DIR_PATH'
    )
    
    def execute(self, context):
        props = context.scene.lpdt_props
        props.image_folder_path = self.directory
        self.report({'INFO'}, f"Image folder set to: {self.directory}")
        return {'FINISHED'}
    
    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

# ============================================================================
# UI PANEL
# ============================================================================

class LPDT_PT_tutorial_panel(Panel):
    """Main tutorial panel in N-Panel"""
    bl_label = "Low Poly Deer Tutorial"
    bl_idname = "LPDT_PT_tutorial"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Low Poly Deer'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        props = context.scene.lpdt_props
        completed = decode_progress(props.completed_steps_binary)
        
        # ====== HEADER ======
        box = layout.box()
        box.scale_y = 1.2
        row = box.row(align=True)
        row.label(text="🦌 LOW POLY DEER TUTORIAL", icon='HELP')
        
        # ====== IMAGE FOLDER SETUP ======
        box = layout.box()
        box.label(text="Setup", icon='PREFERENCES')
        
        row = box.row(align=True)
        if props.image_folder_path:
            folder_name = os.path.basename(props.image_folder_path)
            row.label(text=f"📁 {folder_name}", icon='FILE_FOLDER')
        else:
            row.label(text="⚠️  No image folder set", icon='ERROR')
        
        row.operator("lpdt.set_image_folder", text="Browse", icon='FILEBROWSER')
        
        # ====== CURRENT STEP HEADER ======
        box = layout.box()
        step_pct = int((props.current_step / len(TUTORIAL_STEPS)) * 100)
        box.label(text=f"Step {props.current_step}/{len(TUTORIAL_STEPS)} ({step_pct}%)", icon='PLAY')
        
        step = TUTORIAL_STEPS[props.current_step - 1]
        
        # Step title and info
        col = box.column(align=True)
        col.label(text=step['title'], icon='LIBRARY_DATA_DIRECT')
        col.separator()
        
        # Time and hotkeys
        row = col.row(align=True)
        row.label(text=f"⏱  {step['time']}")
        
        col = box.column(align=True)
        col.label(text=f"⌨  {step['hotkeys']}", icon='HAND')
        col.separator()
        
        # Description with word wrap
        col = box.column(align=True)
        col.label(text="Description:", icon='TEXT')
        
        words = step['description'].split()
        line = ""
        for word in words:
            if len(line) + len(word) < 60:
                line += word + " "
            else:
                if line:
                    col.label(text=line)
                line = word + " "
        if line:
            col.label(text=line)
        
        # ====== IMAGE DISPLAY ======
        box = layout.box()
        box.label(text="Reference Image", icon='IMAGE_DATA')
        
        if props.image_folder_path:
            image_path = os.path.join(props.image_folder_path, step['image_name'])
            if os.path.exists(image_path):
                row = box.row()
                row.label(text=f"✓ {step['image_name']}", icon='CHECKMARK')
            else:
                row = box.row()
                row.label(text=f"✗ {step['image_name']} not found", icon='ERROR')
                row.label(text="Check image folder path")
        else:
            row = box.row()
            row.label(text="Set image folder above to preview", icon='INFO')
        
        # ====== NAVIGATION BUTTONS ======
        col = layout.column(align=True)
        row = col.row(align=True)
        
        if props.current_step > 1:
            op = row.operator("lpdt.set_current_step", text="◀ Previous", emboss=True)
            op.step_index = props.current_step - 2
        else:
            row.label(text="")
        
        row.label(text=f"{props.current_step}/{len(TUTORIAL_STEPS)}", icon='SEQ_STRIP_DUPLICATE')
        
        if props.current_step < len(TUTORIAL_STEPS):
            op = row.operator("lpdt.set_current_step", text="Next ▶", emboss=True)
            op.step_index = props.current_step
        else:
            row.label(text="")
        
        # ====== STEP COMPLETION ======
        col = layout.column(align=True)
        is_complete = completed[props.current_step - 1]
        
        icon = 'CHECKBOX_HLT' if is_complete else 'CHECKBOX_DEHLT'
        text = "✓ Completed" if is_complete else "☐ Mark Complete"
        op = col.operator("lpdt.toggle_step", text=text, emboss=True, icon=icon)
        op.step_index = props.current_step - 1
        
        # ====== PROGRESS SUMMARY ======
        box = layout.box()
        completed_count = sum(completed)
        progress_pct = int((completed_count / len(TUTORIAL_STEPS)) * 100)
        
        box.label(text=f"Progress: {completed_count}/{len(TUTORIAL_STEPS)} ({progress_pct}%)", icon='DRIVER')
        
        # Progress bar visualization
        row = box.row()
        row.scale_x = 1.0
        row.scale_y = 0.5
        for i in range(42):
            if completed[i]:
                row.label(text="█", icon='NONE')
            else:
                row.label(text="░", icon='NONE')
        
        # ====== STEP LIST ======
        box = layout.box()
        box.label(text="Step Navigator", icon='SEQ_STRIP_DUPLICATE')
        
        col = box.column(align=True)
        for i, tutorial_step in enumerate(TUTORIAL_STEPS):
            row = col.row(align=True)
            icon = 'CHECKBOX_HLT' if completed[i] else 'BLANK1'
            is_current = (i + 1) == props.current_step
            emboss = not is_current
            
            op = row.operator("lpdt.set_current_step", 
                            text=f"{i+1:2d}. {tutorial_step['title'][:35]}",
                            emboss=emboss,
                            icon=icon,
                            depress=is_current)
            op.step_index = i
        
        # ====== RESET BUTTON ======
        box = layout.box()
        col = box.column(align=True)
        col.operator("lpdt.reset_progress", text="🔄 Reset All Progress", icon='LOOP_BACK')

# ============================================================================
# REGISTRATION
# ============================================================================

classes = (
    TutorialStepProperties,
    LPDT_OT_toggle_step,
    LPDT_OT_set_current_step,
    LPDT_OT_reset_progress,
    LPDT_OT_set_image_folder,
    LPDT_PT_tutorial_panel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    bpy.types.Scene.lpdt_props = bpy.props.PointerProperty(type=TutorialStepProperties)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    
    del bpy.types.Scene.lpdt_props

if __name__ == "__main__":
    register()
