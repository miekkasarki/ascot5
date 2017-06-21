#ifndef MCCC_H
#define MCCC_H

#include "../ascot5.h"
#include "../B_field.h"
#include "../plasma_1d.h"
#include "../particle.h"
#include "mccc_wiener.h"

#pragma omp declare target
void mccc_init();

void mccc_update_fo(particle_simd_fo* p, B_field_data* Bdata, plasma_1d_data* pdata, 
		    real* clogab, real* F, real* Dpara, real* Dperp, real* K, real* nu);

void mccc_update_gc(particle_simd_gc* p, B_field_data* Bdata, plasma_1d_data* pdata,
		    real* clogab, real* Dpara, real* DX, real* K, real* nu, real* dQ, real* dDpara);

void mccc_step_fo_fixed(particle_simd_fo* p, B_field_data* Bdata, plasma_1d_data* pdata, real* h, int* err);

void mccc_step_gc_fixed(particle_simd_gc* p, B_field_data* Bdata, plasma_1d_data* pdata, real* h, int* err);

void mccc_step_gc_adaptive(particle_simd_gc* p, B_field_data* Bdata, plasma_1d_data* pdata, real* hin, real* hout, mccc_wienarr** w, real tol, int* err);

void mccc_printerror(int err);

#pragma omp end declare target

#endif
