import pygalmesh
import pyvista as pv
print("yeah!")

# box = pv.Box(level=4).triangulate()
# box.plot(show_edges=True)
# pv.save_meshio("box.vtu", box)
pv_mesh = pv.read("elephant.vtu")
pv_mesh.plot(show_edges=True)

print("Now generating the tet mesh...")
mesh = pygalmesh.generate_volume_mesh_from_surface_mesh(
        "elephant.vtu",        
        max_edge_size_at_feature_edges = 0.05,
        min_facet_angle = 25.0,
        max_radius_surface_delaunay_ball = 0.15,
        max_facet_distance = 0.005,
        max_circumradius_edge_ratio = 2.0,
        max_cell_circumradius = 0.040,
        exude_time_limit = 0.0,
        verbose=True,
        feature_angle=33.0,
        perturb=False,
        exude=False,
        reorient=False
    )
print("Successfully generated the tet mesh!")
print("Now writing the tet mesh to a file...")
mesh.write("box_tet.vtu")
print("Now reading the tet mesh into pyvista...")
pv.read("box_tet.vtu").plot(show_edges=True)
print(mesh)