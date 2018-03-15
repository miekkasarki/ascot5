"""
Options IO.
"""
import h5py
import numpy as np

from . ascot5group import creategroup

def write_hdf5(fn, options):
    """
    Write options.

    Unlike most other "write" functions, this one takes dictionary
    as an argument. The dictionary should have exactly the same format
    as given by the "read" function in this module.

    Parameters
    ----------
    fn : str
        Full path to HDF5 file.
    options : dictionary
        Options to be written in dictionary format.
    """

    mastergroup = "options"
    subgroup    = "opt"
    
    # Create a group for this input.
    f = h5py.File(fn, "a")
    path = creategroup(f, mastergroup, subgroup)
    
    # TODO Check that inputs are consistent.

    # Actual data.
    for opt in options:
        f.create_dataset(path + "/" + opt, (options[opt].size,), data=options[opt])
    
    f.close()


def read_hdf5(fn, qid):
    """
    Read options from HDF5 file.

    Parameters
    ----------

    fn : str
        Full path to the HDF5 file.
    qid : str
        qid of the options to be read.

    Returns
    -------

    Dictionary containing options.
    """
    
    path = "options" + "/opt-" + qid

    f = h5py.File(fn,"r")

    out = {}

    # Metadata.
    out["qid"]  = qid
    out["date"] = f[path].attrs["date"]
    out["description"] = f[path].attrs["description"]

    # Actual data.
    for opt in f[path]:
        out[opt] = f[path][opt][:]
        

    f.close()

    return out
