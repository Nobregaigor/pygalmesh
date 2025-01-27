#ifndef GENERATE_FROM_OFF_HPP
#define GENERATE_FROM_OFF_HPP

#include <string>
#include <vector>

namespace pygalmesh
{

    void
    generate_from_off(
        const std::string &infile,
        const std::string &outfile,
        const bool lloyd = false,
        const bool odt = false,
        const bool perturb = true,
        const bool exude = true,
        const double max_edge_size_at_feature_edges = 0.0, // std::numeric_limits<double>::max(),
        const double min_facet_angle = 0.0,
        const double max_radius_surface_delaunay_ball = 0.0,
        const double max_facet_distance = 0.0,
        const double max_circumradius_edge_ratio = 0.0,
        const double max_cell_circumradius = 0.0,
        const double exude_time_limit = 0.0,
        const double exude_sliver_bound = 0.0,
        const bool verbose = true,
        const bool reorient = false,
        const int seed = 0,
        const double feature_angle = 0.0 // New parameter for feature detection sensitivity
    );

} // namespace pygalmesh

#endif // GENERATE_FROM_OFF_HPP
