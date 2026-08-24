# lowpolydeer

Mastering low-poly character modeling in Blender requires a solid foundation in viewport navigation, reference image alignment, and a structured geometry workflow. In this tutorial, you will learn how to transform a basic cube into a stylized 3D stag model from start to finish. We will begin by setting up camera-aligned front and side reference artwork to establish precise anatomical proportions. From there, you will master core box-modeling techniques, utilizing face extrusions, strategically placed loop cuts, and a Mirror Modifier to efficiently construct a symmetrical torso, head, and limbs. As we refine the mesh, you will gain valuable insights into edge sliding, topology spacing, and converting blocky shapes into smooth, organic forms. You will also learn practical detailing methods, including insetting facial geometry, extruding multi-branched antlers, and using the Knife tool to carve precise nose and mouth features. Finally, we will set up multiple material slots to assign distinct surface colors and roughness settings for fur, antlers, and glossy eyes. By the end of this guide, you will possess essential 3D modeling skills and a clean, repeatable workflow that can be applied to any low-poly creature or asset creation project.

---

## 1. Navigation Fundamentals

**Time Range**: `00:00:00,000` → `00:00:58,000`

![Navigation Fundamentals](./lowpolydeer_images/frame_01.jpg)

Learn essential Blender viewport navigation controls within a fresh startup file, utilizing middle mouse button dragging to orbit around the pivot point, scroll wheel to zoom smoothly in and out, and Shift plus middle mouse button to strafe across the screen.

### Key Takeaways

- Hotkey: Shift + Middle Mouse Button

---

## 2. Importing Reference Image

**Time Range**: `00:00:58,000` → `00:01:23,000`

![Importing Reference Image](./lowpolydeer_images/frame_02.jpg)

Locate the downloaded stag reference artwork file on your computer, then drag and drop the image directly into the Blender viewport to instantly spawn a camera-aligned orthographic image plane for initial character modeling setup.

### Key Takeaways

- Hotkey: Click and Drag

---

## 3. Resetting Reference Location & Rotation

**Time Range**: `00:01:23,000` → `00:01:45,000`

![Resetting Reference Location & Rotation](./lowpolydeer_images/frame_03.jpg)

Reset default transformation offsets on the imported reference image by clearing grab position and rotation, then rotate the image ninety degrees around the X-axis so it stands vertically perpendicular to the ground plane.

### Key Takeaways

- Hotkey: Alt + G / Alt + R / R X 90

---

## 4. Switching to Front View & Enabling X-Ray

**Time Range**: `00:01:45,000` → `00:02:14,000`

![Switching to Front View & Enabling X-Ray](./lowpolydeer_images/frame_04.jpg)

Switch the viewport to Orthographic Front View looking directly down the Y-axis, then activate X-Ray view mode to allow full visual visibility of the reference background image artwork through solid viewport meshes.

### Key Takeaways

- Hotkey: Numpad 1 / Alt + Z

---

## 5. Adjusting Image Reference Opacity

**Time Range**: `00:02:14,000` → `00:02:30,000`

![Adjusting Image Reference Opacity](./lowpolydeer_images/frame_05.jpg)

Select the imported reference image plane, navigate to Object Data Properties panel on the right interface, toggle Opacity setting enabled, and lower the value to 0.2 to render grid lines clearly visible behind artwork.

### Key Takeaways

- Hotkey: N/A

---

## 6. Centering Front Reference Image

**Time Range**: `00:02:30,000` → `00:03:06,000`

![Centering Front Reference Image](./lowpolydeer_images/frame_06.jpg)

Align the stag face precisely over the world origin 3D Cursor using constrained X-axis grabbing with Shift key precision, then translate the plane backward along the Y-axis behind the active modeling scene workspace.

### Key Takeaways

- Hotkey: G X / G Y / Shift + S

---

## 7. Duplicating and Rotating Side Reference

**Time Range**: `00:03:06,000` → `00:03:45,000`

![Duplicating and Rotating Side Reference](./lowpolydeer_images/frame_07.jpg)

Switch to Top View, duplicate the front reference image plane, and execute a ninety-degree rotation around the Z-axis to quickly construct the orthographic right-side reference plane for lateral profile tracing.

### Key Takeaways

- Hotkey: Numpad 7 / Shift + D / R Z 90

---

## 8. Aligning Side Reference View

**Time Range**: `00:03:45,000` → `00:04:06,000`

![Aligning Side Reference View](./lowpolydeer_images/frame_08.jpg)

Switch viewport perspective to Right Side View and translate the duplicated reference plane along the Y-axis into position in front of the center cube while preserving exact horizontal height alignment with the front image plane.

### Key Takeaways

- Hotkey: Numpad 3 / G Y

---

## 9. Organizing Reference Collections

**Time Range**: `00:04:06,000` → `00:04:45,000`

![Organizing Reference Collections](./lowpolydeer_images/frame_09.jpg)

Select both reference image planes in the viewport, assign them into a newly created collection titled Ref, and rename individual image plane objects to Front and Side inside the Outliner for organized file management.

### Key Takeaways

- Hotkey: M

---

## 10. Initializing Mesh Cube in Edit Mode

**Time Range**: `00:04:45,000` → `00:05:21,000`

![Initializing Mesh Cube in Edit Mode](./lowpolydeer_images/frame_10.jpg)

Select the default cube object, scale and translate it into position over the stag chest region in Right Side View, then enter Edit Mode with Vertex Selection mode activated to begin manipulating corner points.

### Key Takeaways

- Hotkey: G / S / Tab / 1

---

## 11. Box Selecting Base Vertices

**Time Range**: `00:05:21,000` → `00:06:10,000`

![Box Selecting Base Vertices](./lowpolydeer_images/frame_11.jpg)

In Side View with X-Ray mode enabled, use box selection to grab front and rear vertex pairs together, aligning the box corners along the top and bottom boundaries of the chest reference artwork outline.

### Key Takeaways

- Hotkey: B / G

---

## 12. Extruding Initial Torso Geometry

**Time Range**: `00:06:10,000` → `00:06:55,000`

![Extruding Initial Torso Geometry](./lowpolydeer_images/frame_12.jpg)

Switch to Face Selection mode, select the rear box face, and extrude geometry outward along the torso contour, manually tweaking individual vertex pair heights to tightly match the reference artwork silhouette.

### Key Takeaways

- Hotkey: 3 / E / R / 1

---

## 13. Extruding Backwards along Hindquarters

**Time Range**: `00:06:55,000` → `00:07:42,000`

![Extruding Backwards along Hindquarters](./lowpolydeer_images/frame_13.jpg)

Continue extruding face segments sequentially along the back and hindquarters reaching to the base of the tail, continually switching to Vertex mode to match key anatomical pivot points along the stag reference drawing.

### Key Takeaways

- Hotkey: E / 1 / G

---

## 14. Extruding Neck and Head Outline

**Time Range**: `00:07:42,000` → `00:08:42,000`

![Extruding Neck and Head Outline](./lowpolydeer_images/frame_14.jpg)

Select front facing polygon surfaces and extrude upward and forward in steps, shaping the neck profile, throat, chin, and snout outline by rotating and translating vertex pairs in Right Side View.

### Key Takeaways

- Hotkey: 3 / E / R / 1

---

## 15. Adding Mid-Leg Loop Cut

**Time Range**: `00:08:42,000` → `00:09:31,000`

![Adding Mid-Leg Loop Cut](./lowpolydeer_images/frame_15.jpg)

Insert a vertical loop cut through the middle of the body block structure aligned with the front leg origin point, right-clicking immediately after placement to maintain perfect centered edge alignment across the torso.

### Key Takeaways

- Hotkey: Ctrl + R

---

## 16. Inserting Head and Neck Loop Cuts

**Time Range**: `00:09:31,000` → `00:10:07,000`

![Inserting Head and Neck Loop Cuts](./lowpolydeer_images/frame_16.jpg)

Add extra horizontal loop cuts across the neck and facial regions using loop cut tools to supply sufficient vertex resolution for forming organic curves along the head, jawline, and neck structure.

### Key Takeaways

- Hotkey: Ctrl + R

---

## 17. Bisecting the Mesh Down Center

**Time Range**: `00:10:07,000` → `00:10:46,000`

![Bisecting the Mesh Down Center](./lowpolydeer_images/frame_17.jpg)

Add a central longitudinal loop cut down the complete length of the mesh body, opening the edge loop tool settings dialog to set the offset factor precisely to zero for perfect centerline alignment.

### Key Takeaways

- Hotkey: Ctrl + R

---

## 18. Deleting Half the Geometry

**Time Range**: `00:10:46,000` → `00:11:03,000`

![Deleting Half the Geometry](./lowpolydeer_images/frame_18.jpg)

Switch to Face Select mode in Edit Mode, box select all polygons located on one half of the bisected mesh model, and delete the selected faces to prepare for symmetrical modifier modeling.

### Key Takeaways

- Hotkey: 3 / Delete

---

## 19. Adding Mirror Modifier with Clipping

**Time Range**: `00:11:03,000` → `00:11:51,000`

![Adding Mirror Modifier with Clipping](./lowpolydeer_images/frame_19.jpg)

Navigate to the Modifiers panel, add a Mirror Modifier set along the local X-axis, and enable the Clipping toggle option to securely weld center boundary vertices along the middle symmetry line.

### Key Takeaways

- Hotkey: N/A

---

## 20. Adding Longitudinal Body Cut

**Time Range**: `00:11:51,000` → `00:12:46,000`

![Adding Longitudinal Body Cut](./lowpolydeer_images/frame_20.jpg)

Insert a horizontal loop cut along the outer flank of the half-torso mesh, establishing isolated lower face regions needed to extrude front and hind limbs independently away from the body centerline.

### Key Takeaways

- Hotkey: Ctrl + R

---

## 21. Extruding Front Limb Base

**Time Range**: `00:12:46,000` → `00:13:22,000`

![Extruding Front Limb Base](./lowpolydeer_images/frame_21.jpg)

Select the underside faces located beneath the shoulder section and extrude downward to form the base of the front legs, scaling the extruded face slightly inward to establish correct upper leg thickness.

### Key Takeaways

- Hotkey: 3 / E / S

---

## 22. Extruding Front Leg to Ground

**Time Range**: `00:13:22,000` → `00:14:11,000`

![Extruding Front Leg to Ground](./lowpolydeer_images/frame_22.jpg)

Extrude the front limb downward through joint segments to ground level, then scale base vertices on the Z-axis by factor zero to flatten the lower hoof flush against the ground plane floor.

### Key Takeaways

- Hotkey: E / S Z 0

---

## 23. Extruding Rear Limb Segments

**Time Range**: `00:14:11,000` → `00:14:42,000`

![Extruding Rear Limb Segments](./lowpolydeer_images/frame_23.jpg)

Select the rear underside faces and extrude step-by-step downward following side reference artwork to construct the upper hocks, lower legs, ankle joints, and ground-level hooves for the hind legs.

### Key Takeaways

- Hotkey: E / S Y / G

---

## 24. Adding Horizontal Body Loop Cut

**Time Range**: `00:14:42,000` → `00:15:28,000`

![Adding Horizontal Body Loop Cut](./lowpolydeer_images/frame_24.jpg)

Add a longitudinal loop cut horizontally around the middle of the torso, giving extra edge control needed to push upper and lower body edges into rounded anatomical curves.

### Key Takeaways

- Hotkey: Ctrl + R

---

## 25. Adjusting Front Width and Taper

**Time Range**: `00:15:28,000` → `00:16:25,000`

![Adjusting Front Width and Taper](./lowpolydeer_images/frame_25.jpg)

In Front View X-Ray mode, translate outer leg and neck faces inward along the X-axis to match reference front width, taking care not to allow off-center vertices to clip onto the center seam.

### Key Takeaways

- Hotkey: Numpad 1 / G X

---

## 26. Sliding Edge Loops for Curvature

**Time Range**: `00:16:25,000` → `00:17:05,000`

![Sliding Edge Loops for Curvature](./lowpolydeer_images/frame_26.jpg)

Select horizontal body edge loops with loop select and utilize edge slide tools to shift loop positions, rounding out blocky flat surface geometry into curved contours across the flanks and shoulders.

### Key Takeaways

- Hotkey: Alt + Left Click / G G

---

## 27. Rounding Legs and Hindquarters

**Time Range**: `00:17:05,000` → `00:18:02,000`

![Rounding Legs and Hindquarters](./lowpolydeer_images/frame_27.jpg)

Select corner edge loops running vertically down the legs and slide them inward and outward using edge slide to convert square boxy limb extrusions into rounded, cylinder-like leg structures.

### Key Takeaways

- Hotkey: 2 / G G

---

## 28. Refining Torso and Underbelly Curves

**Time Range**: `00:18:02,000` → `00:18:43,000`

![Refining Torso and Underbelly Curves](./lowpolydeer_images/frame_28.jpg)

Adjust underbelly vertices upward and push groin edge loops inward toward the center to build realistic transitions where limbs attach to the main torso, eliminating flat underbody geometry.

### Key Takeaways

- Hotkey: G Z / G G

---

## 29. Refining Snout, Jaw, and Shoulder

**Time Range**: `00:18:43,000` → `00:19:52,000`

![Refining Snout, Jaw, and Shoulder](./lowpolydeer_images/frame_29.jpg)

Add a vertical loop cut across the head, pull snout vertices inward to create a tapered muzzle, and expand shoulder vertices outward on the X-axis to match front reference proportions.

### Key Takeaways

- Hotkey: Ctrl + R / G X

---

## 30. Evening Out Topology Spacing

**Time Range**: `00:19:52,000` → `00:20:22,000`

![Evening Out Topology Spacing](./lowpolydeer_images/frame_30.jpg)

Slide misaligned edge loops across body segments using edge slide to redistribute polygon spacing evenly, creating smooth low-poly surfaces and consistent quad grid distribution across the entire mesh.

### Key Takeaways

- Hotkey: G G

---

## 31. Insetting the Eye Polygon

**Time Range**: `00:20:22,000` → `00:21:04,000`

![Insetting the Eye Polygon](./lowpolydeer_images/frame_31.jpg)

Select the facial polygon corresponding to the eye position, inset a smaller face inward, pull it slightly outward on the X-axis, and rotate it forward to form a distinct low-poly eye socket.

### Key Takeaways

- Hotkey: 3 / I / R Z

---

## 32. Insetting and Extruding Ears

**Time Range**: `00:21:04,000` → `00:22:04,000`

![Insetting and Extruding Ears](./lowpolydeer_images/frame_32.jpg)

Add an extra loop cut near the back of the head, inset a polygon behind the eye socket, extrude it outward twice, and shape vertex locations to form an angled low-poly ear.

### Key Takeaways

- Hotkey: Ctrl + R / I / E

---

## 33. Insetting and Extruding Antler Bases

**Time Range**: `00:22:04,000` → `00:23:18,000`

![Insetting and Extruding Antler Bases](./lowpolydeer_images/frame_33.jpg)

Select forehead faces located above the eye sockets, inset new base faces, and extrude upward and outward in short initial segments to begin constructing main antler stems.

### Key Takeaways

- Hotkey: I / E / R

---

## 34. Extruding Secondary Antler Tines

**Time Range**: `00:23:18,000` → `00:24:12,000`

![Extruding Secondary Antler Tines](./lowpolydeer_images/frame_34.jpg)

Select outer side faces on main antler stems, extrude secondary branches outward, and scale down tip faces to quickly build multi-pointed branching antler tines extending from the stag head.

### Key Takeaways

- Hotkey: E / S / R

---

## 35. Adding Antler Loop Cuts

**Time Range**: `00:24:12,000` → `00:24:56,000`

![Adding Antler Loop Cuts](./lowpolydeer_images/frame_35.jpg)

Insert loop cuts along straight antler sections using the scroll wheel, then pull and rotate individual loop selections in 3D space to add organic natural curves to the low-poly antlers.

### Key Takeaways

- Hotkey: Ctrl + R / G / R

---

## 36. Insetting and Extruding Tail

**Time Range**: `00:24:56,000` → `00:25:25,000`

![Insetting and Extruding Tail](./lowpolydeer_images/frame_36.jpg)

Select the rear face at the base of the spine, inset with boundary mode toggled off to maintain mirror seam symmetry, and extrude backward to construct a low-poly tail.

### Key Takeaways

- Hotkey: 3 / I B / E

---

## 37. Final Anatomical Proportion Cleanup

**Time Range**: `00:25:25,000` → `00:26:01,000`

![Final Anatomical Proportion Cleanup](./lowpolydeer_images/frame_37.jpg)

Disable X-Ray view to inspect solid mesh shading, sliding misaligned vertices with edge slide to smooth planar surfaces and scaling up antler selections to match overall reference drawing scale.

### Key Takeaways

- Hotkey: Alt + Z / G G / Numpad Period

---

## 38. Assigning Base Light Brown Material

**Time Range**: `00:26:01,000` → `00:26:45,000`

![Assigning Base Light Brown Material](./lowpolydeer_images/frame_38.jpg)

Switch to the Shading workspace, hide reference collections, rename default material to Light Brown, set warm orange-brown base color, and increase Roughness to create non-reflective fur appearance.

### Key Takeaways

- Hotkey: N/A

---

## 39. Assigning Dark Brown Antler Material

**Time Range**: `00:26:45,000` → `00:27:30,000`

![Assigning Dark Brown Antler Material](./lowpolydeer_images/frame_39.jpg)

Add a secondary material slot in Edit Mode, select all antler polygons using lasso selection, create a Dark Brown material, and click Assign to color the antlers darker than the body.

### Key Takeaways

- Hotkey: Ctrl + Right Click / 3

---

## 40. Creating Shiny Black Eye Material

**Time Range**: `00:27:30,000` → `00:28:07,000`

![Creating Shiny Black Eye Material](./lowpolydeer_images/frame_40.jpg)

Create a third material slot, select eye polygons, add a new material named Black with dark base color and low Roughness, and click Assign to produce glossy shiny eyes.

### Key Takeaways

- Hotkey: 3

---

## 41. Carving Nose and Mouth with Knife Tool

**Time Range**: `00:28:07,000` → `00:29:07,000`

![Carving Nose and Mouth with Knife Tool](./lowpolydeer_images/frame_41.jpg)

Carve custom facial details on the muzzle using the Knife tool, dissolve unneeded interior edges, select resulting nose and mouth polygons, and assign the Black material slot to them.

### Key Takeaways

- Hotkey: K / Ctrl + X / 3

---

## 42. Reviewing Rendered Low-Poly Stag

**Time Range**: `00:29:07,000` → `00:29:27,000`

![Reviewing Rendered Low-Poly Stag](./lowpolydeer_images/frame_42.jpg)

Switch viewport display to Material Preview mode to inspect and verify multi-material color assignment across body fur, dark antlers, glossy eyes, and carved muzzle details, completing the low-poly stag model.

### Key Takeaways

- Hotkey: Z

---

