import numpy as np
import h5py
import ui_B_2D
import analyticBKGpsifun as psifun
import matplotlib.pyplot as plt

def write_hdf5(fn, R0, z0, B_phi0, psi0, psi1, psi_mult, psi_coeff):
    """Write analytical tokamak magnetic field input in hdf5 file.

    Keyword arguments:
    fn        -- path to hdf5 file
    R0        -- axis R coordinate
    z0        -- axis z coordinate
    B_phi0    -- on-axis toroidal magnetic field
    psi0      -- psi at axis
    psi1      -- psi at separatrix
    psi_mult  -- psi multiplier
    psi_coeff -- numpy array of psi coefficients
    """

    # Create bfield group if one does not exists and set 
    # type to B_GS. If one exists, only set type to B_GS.
    f = h5py.File(fn, "a")
    if not "/bfield" in f:
        o = f.create_group('bfield')
        o.attrs["type"] = np.string_("B_GS")
    
    else:
        o = f["bfield"]
        del o.attrs["type"]
        o.attrs["type"] = np.string_("B_GS")
        
    # Remove B_GS field if one is already present
    if  "/bfield/B_GS" in f:
        del f["/bfield/B_GS"]

    f.create_group('bfield/B_GS')
    f.create_dataset('bfield/B_GS/R0', data=R0, dtype='f8')
    f.create_dataset('bfield/B_GS/z0', data=z0, dtype='f8')
    f.create_dataset('bfield/B_GS/B_phi0', data=B_phi0, dtype='f8')
    f.create_dataset('bfield/B_GS/psi0', data=psi0, dtype='f8')
    f.create_dataset('bfield/B_GS/psi1', data=psi1, dtype='f8')
    f.create_dataset('bfield/B_GS/psi_mult', data=psi_mult, dtype='f8')
    f.create_dataset('bfield/B_GS/psi_coeff', data=psi_coeff, dtype='f8')
    f.close()

def write_hdf5_B_2D(fn, R0, z0, B_phi0, psi_mult, psi_coeff, rgrid, zgrid):
    """Write analytical tokamak magnetic field as a 2D field input in hdf5 file.

    Keyword arguments:
    fn        -- path to hdf5 file
    R0        -- axis R coordinate
    z0        -- axis z coordinate
    B_phi0    -- on-axis toroidal magnetic field
    psi_mult  -- psi multiplier
    psi_coeff -- numpy array of psi coefficients
    rgrid     -- [r_min, r_max, n_r] values defining the R grid (m)
    zgrid     -- [z_min, z_max, n_z] values defining the z grid (m)
    """

    n_r = int(rgrid[2])
    n_z = int(zgrid[2])
    rgrid = np.linspace(rgrid[0], rgrid[1], n_r)
    zgrid = np.linspace(zgrid[0], zgrid[1], n_z)
    rlim = np.array([rgrid[0], rgrid[-1]])
    zlim = np.array([zgrid[0], zgrid[-1]])

    zg, Rg = np.meshgrid(zgrid, rgrid);
    Rg = np.transpose(Rg)
    zg = np.transpose(zg)

    psirz = np.zeros((n_z,n_r))

    c = psi_coeff
    psirz = psi_mult*psifun.psi0(Rg/R0,zg/R0,c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8],c[9],c[10],c[11],c[12])

    Br = np.zeros((n_z,n_r))
    Bz = np.zeros((n_z,n_r))
    #Bphi = (2*R0/Rg -1)*B_phi0
    Bphi = (R0/Rg)*B_phi0

    axisRz = np.array([R0, z0])

    axispsi = psi_mult*psifun.psi0(R0/R0,z0/R0,c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8],c[9],c[10],c[11],c[12])

    psivals = np.array([axispsi, 0.0])
    #plt.contour(psirz)
    #plt.show()
    ui_B_2D.write_hdf5(fn, rlim, zlim, psirz, Br, Bphi, Bz, axisRz, psivals)
    
