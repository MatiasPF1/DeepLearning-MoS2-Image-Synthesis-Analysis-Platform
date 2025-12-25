# AUTOSTEM Core Files for Application Integration

## Overview
This folder contains all essential files needed to integrate STEM (Scanning Transmission Electron Microscopy) image generation into your Dash-Plotly application. These files implement the multislice method for simulating electron microscopy images from atomic coordinates.

**Source**: TEMSIM package by Earl J. Kirkland (GPL v3)  
**Purpose**: Generate STEM images from XYZ atomic coordinates with user-defined microscope parameters

---

## Contents

### Core AUTOSTEM Program Files (3 files)
```
autostem.cpp          - Main STEM calculation engine (class implementation)
autostem.hpp          - Header file for autostem class
autostemcmd.cpp       - Command-line interface (MODIFY THIS for your app)
```

### Supporting Library Files (13 files)
```
slicelib.cpp/.hpp     - Core multislice functions, scattering factors, parameters
probe.cpp/.hpp        - Electron probe generation with aberrations
cfpix.cpp/.hpp        - Complex image FFT operations (uses FFTW)
floatTIFF.cpp/.hpp    - TIFF file I/O for images and parameters
ransubs.cpp/.hpp      - Random number generators (for thermal vibrations)
rfpix.cpp/.hpp        - Real-valued FFT operations (optimized)
newD.hpp              - Memory allocation templates (header-only)
fftw3.h               - FFTW library header
```

### Example Files
```
graphene.xyz          - Example atomic coordinate file (graphene structure)
LICENSE.txt           - GPL v3 license
```

**Total: 19 files**

---

## What Each File Does

### Main Calculation Engine

**autostem.cpp/hpp**  
- Core STEM simulation class
- Implements multislice algorithm
- Propagates electron probe through specimen
- Calculates detector signals (BF, ADF, HAADF)
- Handles thermal diffuse scattering (TDS)
- Supports multiple detectors simultaneously
- ~2300 lines of physics calculations

**autostemcmd.cpp** ⚠️ **YOU WILL MODIFY THIS**  
- Currently: Interactive command-line interface
- Your task: Replace with parameter-driven interface
- Options:
  1. Add command-line argument parsing
  2. Read from JSON/config file
  3. Create Python-callable wrapper
  4. Compile as shared library

### Core Libraries

**slicelib.cpp/hpp**  
- Atomic scattering factor tables (Z=1 to 103)
- Electron wavelength calculations
- Aberration functions (chi)
- Transmission function calculations
- Projected atomic potentials (vzatom, vzatomLUT)
- Parameter definitions and constants
- ~2600 lines

**probe.cpp/hpp**  
- Generates focused electron probe wavefunctions
- Handles aberrations: Cs3, Cs5, astigmatism, coma, etc.
- Supports multipole aberrations (up to 5th order)
- Calculates probe intensity distributions
- ~600 lines

**cfpix.cpp/hpp**  
- Complex 2D image class with FFT
- Wraps FFTW3 library
- FFT/inverse FFT operations
- Image manipulation and memory management
- Thread-safe operations
- ~400 lines

**floatTIFF.cpp/hpp**  
- Reads/writes 32-bit floating point TIFF files
- Stores calculation parameters in TIFF metadata
- Handles multi-page TIFF (display + data + params)
- Cross-platform (big-endian/little-endian)
- ~1400 lines

**ransubs.cpp/hpp**  
- High-quality random number generator (xorshift*)
- ranflat(): Uniform distribution [0,1]
- rangauss(): Gaussian distribution
- ranPoisson(): Poisson distribution
- Used for thermal vibrations and noise
- ~200 lines

**rfpix.cpp/hpp**  
- Real-valued FFT operations
- Memory-efficient for real images
- Optimized performance
- ~300 lines

**newD.hpp**  
- Template functions for multi-dimensional array allocation
- new2D(), new3D(), delete2D(), delete3D()
- Type-safe memory management
- Header-only library

---

## External Dependencies

### Required: FFTW3 Library
```bash
# Windows (MSYS2/MinGW):
pacman -S mingw-w64-x86_64-fftw

# Ubuntu/Debian:
sudo apt-get install libfftw3-dev libfftw3-3

# macOS (Homebrew):
brew install fftw

# Or download from: www.fftw.org
```

**Required DLL/SO files:**
- Windows: `libfftw3f-3.dll` (must be in PATH or same directory)
- Linux: `libfftw3f.so` (usually in /usr/lib)
- macOS: `libfftw3f.dylib`

### Optional: OpenMP
For CPU multithreading (significant speedup)
- Compile with `-fopenmp` flag
- Usually included in GCC/Clang

---

## Compilation

### Basic Compilation (CPU-only, Windows MinGW)
```bash
# Compile object files first
g++ -O3 -c slicelib.cpp -o slicelib.o
g++ -O3 -c probe.cpp -o probe.o
g++ -O3 -c cfpix.cpp -o cfpix.o
g++ -O3 -c floatTIFF.cpp -o floatTIFF.o
g++ -O3 -c ransubs.cpp -o ransubs.o
g++ -O3 -c rfpix.cpp -o rfpix.o

# Link autostem executable
g++ -O3 -fopenmp -o autostem.exe autostemcmd.cpp autostem.cpp \
    slicelib.o probe.o cfpix.o floatTIFF.o ransubs.o rfpix.o \
    -lfftw3f -static-libgcc -static-libstdc++
```

### Linux/Ubuntu
```bash
g++ -O3 -fopenmp -o autostem autostemcmd.cpp autostem.cpp \
    slicelib.o probe.o cfpix.o floatTIFF.o ransubs.o rfpix.o \
    -lfftw3f_threads -lfftw3f -lpthread
```

### macOS
```bash
g++ -O3 -Xpreprocessor -fopenmp -o autostem autostemcmd.cpp autostem.cpp \
    slicelib.o probe.o cfpix.o floatTIFF.o ransubs.o rfpix.o \
    -lfftw3f -lomp
```

### Compile as Shared Library (for Python integration)
```bash
# Linux
g++ -O3 -fopenmp -fPIC -shared -o libautostem.so \
    autostem.cpp slicelib.cpp probe.cpp cfpix.cpp \
    floatTIFF.cpp ransubs.cpp rfpix.cpp \
    -lfftw3f_threads -lfftw3f

# Windows (MinGW)
g++ -O3 -fopenmp -shared -o autostem.dll \
    autostem.cpp slicelib.cpp probe.cpp cfpix.cpp \
    floatTIFF.cpp ransubs.cpp rfpix.cpp \
    -lfftw3f -static-libgcc -static-libstdc++
```

---

## XYZ Input File Format

### Format Specification
```
# Comments start with #
# Each line: Z  x  y  z  occupancy  [wobble]

Z     x       y       z       occ    wobble
6   0.000   0.000   0.000   1.0    0.078
6   1.420   0.000   0.000   1.0    0.078
6   2.130   1.230   0.000   1.0    0.078
```

**Columns:**
- **Z**: Atomic number (1=H, 6=C, 14=Si, 79=Au, etc.)
- **x, y, z**: Coordinates in Angstroms
- **occupancy**: Site occupancy (0.0-1.0, usually 1.0)
- **wobble**: RMS thermal displacement in Angstroms (optional)

### Example: graphene.xyz
The included file contains a graphene sheet structure. You can use this to test the installation.

---

## Key Parameters Reference

### Units
- **Lengths**: Angstroms (Å)
- **Angles**: Radians (convert from mrad: × 0.001)
- **Energy**: keV
- **Temperature**: Kelvin

### Parameter Array Indices (from slicelib.hpp)
```cpp
pENERGY   = 16   // Beam energy (keV)
pOAPERT   = 17   // Objective aperture (radians)
pCS       = 18   // Spherical aberration Cs3 (Angstroms)
pDEFOCUS  = 0    // Defocus (Angstroms)
pMINDET   = 31   // Detector inner angle (radians)
pMAXDET   = 32   // Detector outer angle (radians)
pDELTAZ   = 30   // Slice thickness (Angstroms)
pSOURCE   = 122  // Source size (Angstroms)
pNWOBBLE  = 111  // Number of TDS configurations
pTEMPER   = 120  // Temperature (Kelvin)
```

### Typical Parameter Values

**Microscope Parameters:**
```
Energy:            80, 100, 200, 300 keV (common values)
Cs3:               0-5 mm → 0-5×10^7 Angstroms
Defocus:           -100 to +100 nm → -1000 to +1000 Angstroms
Aperture:          15-30 mrad → 0.015-0.030 radians
Source size:       0.1-1.0 Angstroms
```

**Detector Configurations:**
```
Bright Field (BF):
  Inner: 0 mrad → 0 rad
  Outer: 10 mrad → 0.010 rad

ADF (Annular Dark Field):
  Inner: 60 mrad → 0.060 rad
  Outer: 200 mrad → 0.200 rad

HAADF (High-Angle ADF):
  Inner: 100 mrad → 0.100 rad
  Outer: 300 mrad → 0.300 rad
```

**Calculation Settings:**
```
Supercell size:    256×256 or 512×512 pixels (power of 2)
Scan resolution:   32×32, 64×64, 128×128 pixels
Slice thickness:   1-3 Angstroms (thinner for accuracy)
TDS configs:       10-30 (more = slower but more accurate)
Temperature:       0-1000 K (300 K = room temp)
```

---

## Integration into Your Dash App

### Step 1: Modify autostemcmd.cpp

**Current structure (interactive):**
```cpp
cout << "Input file:" << endl;
cin >> filename;
cout << "Energy (keV):" << endl;
cin >> keV;
// ... many more prompts
```

**Option A: Add command-line arguments**
```cpp
int main(int argc, char* argv[]) {
    if (argc < 3) {
        cout << "Usage: autostem input.xyz output.tif [params.json]" << endl;
        return 1;
    }
    string input_file = argv[1];
    string output_file = argv[2];
    // Read parameters from JSON or config file
}
```

**Option B: Create wrapper function**
```cpp
// New file: autostem_wrapper.cpp
extern "C" int generate_stem_image(
    const char* xyz_file,
    const char* output_file,
    double keV,
    double cs3_mm,
    // ... all parameters
) {
    // Set up parameters
    // Call autostem class
    // Return status
}
```

### Step 2: Call from Python

**Using subprocess (simplest):**
```python
import subprocess
result = subprocess.run([
    './autostem',
    'input.xyz',
    'output.tif',
    'params.json'
], capture_output=True)
```

**Using ctypes (faster):**
```python
from ctypes import *
lib = CDLL('./libautostem.so')
lib.generate_stem_image.argtypes = [c_char_p, c_char_p, c_double, ...]
status = lib.generate_stem_image(
    b'input.xyz',
    b'output.tif',
    200.0,  # keV
    0.5,    # Cs3
    # ...
)
```

### Step 3: Read Output TIFF

```python
import tifffile
import numpy as np

def read_stem_image(tiff_path):
    with tifffile.TiffFile(tiff_path) as tif:
        display = tif.pages[0].asarray()  # 8-bit display
        data = tif.pages[1].asarray()     # 32-bit float data
    return data
```

### Step 4: Display in Dash

```python
import plotly.graph_objects as go

fig = go.Figure(data=go.Heatmap(
    z=stem_data,
    colorscale='gray',
    reversescale=True
))
```

---

## Testing the Installation

### 1. Test Compilation
```bash
# After compiling, run:
./autostem --version
# or just:
./autostem
```

### 2. Test with Example File
```bash
# Run interactively with graphene.xyz
./autostem

# When prompted:
Input file: graphene.xyz
Output file: test_output.tif
Energy: 200
# ... continue with default values
```

### 3. Verify Output
```python
import tifffile
img = tifffile.imread('test_output.tif')
print(f"Output shape: {img.shape}")
print(f"Data range: {img.min():.2e} to {img.max():.2e}")
```

---

## Performance Notes

### Computation Time (8-core CPU)
```
32×32 scan, 10 TDS:    ~10 seconds
64×64 scan, 10 TDS:    ~30 seconds
128×128 scan, 30 TDS:  ~10 minutes
256×256 scan, 30 TDS:  ~45 minutes
```

### Optimization Tips
1. **Enable OpenMP**: Compile with `-fopenmp` (already in examples)
2. **Reduce for preview**: Use 32×32 scan, 5 TDS configs
3. **GPU version**: Use autostem_cuda (needs CUDA toolkit)
4. **Efficient slicing**: Use 2-3 Å slices (balance speed/accuracy)

### Memory Requirements
Approximate memory usage:
```
Formula: ~8 × nx × ny × scan_nx × scan_ny bytes

Example:
256×256 supercell, 64×64 scan = ~500 MB
512×512 supercell, 128×128 scan = ~8 GB
```

---

## Troubleshooting

### Compilation Errors

**"fftw3.h not found"**
```bash
# Install FFTW3 development files
# Ubuntu: sudo apt-get install libfftw3-dev
# Or specify path: -I/path/to/fftw/include
```

**"undefined reference to fftwf_*"**
```bash
# Add FFTW library: -lfftw3f
# Check library path: -L/path/to/fftw/lib
```

**"undefined reference to omp_*"**
```bash
# Remove -fopenmp flag or install OpenMP
# Or use: -Xpreprocessor -fopenmp (macOS)
```

### Runtime Errors

**"libfftw3f-3.dll not found" (Windows)**
```bash
# Add FFTW DLL to PATH or copy to executable directory
# Or compile with static linking: -static
```

**"Segmentation fault"**
- Check XYZ file format (correct columns)
- Ensure supercell size is power of 2 (128, 256, 512)
- Reduce scan size if out of memory

**Slow performance**
- Enable OpenMP: check compilation flags
- Reduce TDS configurations
- Use coarser scan (fewer pixels)
- Consider GPU version

---

## Next Steps for Your App

### Immediate Tasks
- [ ] Compile and test autostem standalone
- [ ] Verify output with graphene.xyz example
- [ ] Modify autostemcmd.cpp for batch mode
- [ ] Test Python subprocess integration

### App Integration
- [ ] Create parameter configuration UI in Dash
- [ ] Implement XYZ file upload
- [ ] Add detector type dropdown (BF/ADF/HAADF presets)
- [ ] Create job queue for batch processing
- [ ] Display output images in Plotly

### Optimization
- [ ] Add progress reporting
- [ ] Implement result caching
- [ ] Add preview mode (low resolution)
- [ ] Consider GPU version for production

---

## Additional Resources

### Documentation
- Original TEMSIM package: Search for "Kirkland TEMSIM"
- FFTW documentation: www.fftw.org
- See `../AUTOSTEM_APP_INTEGRATION.md` for detailed integration guide

### References
1. E. Kirkland, "Advanced Computing in Electron Microscopy", 3rd ed., Springer 2020
2. Multislice method: Cowley & Moodie, Acta Cryst. (1957)

### Support Files
- Integration guide: `../AUTOSTEM_APP_INTEGRATION.md`
- More example XYZ files: `../inputdata/` folder
- License: `LICENSE.txt` (GPL v3)

---

## License

Copyright 1998-2024 Earl J. Kirkland

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

See LICENSE.txt for full text.

---

## Contact & Modification Notes

**For your app development:**
- Modify `autostemcmd.cpp` as needed
- Create wrapper functions for Python integration
- Keep core calculation files (autostem.cpp, slicelib.cpp) unchanged
- Document any modifications for future reference

**Version Information:**
- Source: TEMSIM package (2024 version)
- Extracted: December 2025
- Purpose: Integration into Dash-Plotly STEM simulation app

---

**Ready to integrate!** Start by compiling the code, testing with graphene.xyz, then modify autostemcmd.cpp for your application needs.
