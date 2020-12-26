#include "../simulate.h"
#include "../print.h"

int fmc_init_importance_sampling_mesh(
        int *n,
        particle_state** ps,
        int** ps_indexes,
        int n_total,
        int use_hermite,
        sim_offload_data* sim_offload,
        B_field_data* Bdata,
        real* offload_array,
        offload_package* offload_data,
        int importanceSamplingProbability,
        int importanceSamplingdensity,
        int importanceSamplingFromParticles,
        real t,
        real m,
        real q,
        int rk4_subcycles,
        particle_state* input_ps,
        int input_n_ps
    );
int fmc_init_importance_sampling(
        int *n,
        particle_state** ps,
        int** ps_indexes,
        int n_total,
        int use_hermite,
        sim_offload_data* sim_offload,
        B_field_data* Bdata,
        real* offload_array,
        real t,
        real m,
        real q,
        int rk4_subcycles
    );

int bmc_init_particles(
        int *n,
        particle_state** ps,
        int** ps_indexes,
        int n_per_vertex,
        int use_hermite,
        sim_offload_data* sim_offload,
        B_field_data* Bdata,
        real* offload_array,
        real t,
        real m,
        real q,
        int rk4_subcycles
    );

void buildImportantSamplingHistogram(
    int dist_length,
    real *histogram,
    dist_5D_offload_data* dist5D,
    plasma_data* plasma_data,
    B_field_data* Bdata,
    int importanceSamplingProbability,
    int importanceSamplingdensity,
    int importanceSamplingFromInputParticles,
    real t,
    particle_state* ps,
    int n_ps,
    wall_2d_data* w2d
);

void bmc_init_fo_particle(
        input_particle* p,
        real r, real phi, real z,
        real p_r, real p_phi, real p_z,
        real t,
        real m,
        real q,
        int id
    );
double r2();