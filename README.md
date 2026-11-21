# UCalgary Python Codebook (CPyC)
CPyC is a Competitive Programming codebook written in Python3 intended for beginner to intermediate competitive programmers.

# Building
To build the codebook you need to use the buildtools submodule which can be installed directly via
```bash
pip install git+https://github.com/TaylorWong159/cpyc_buildtools.git
```
Alternatively, you can checkout out the buildtools submodule and install locally via
```bash
git submodule update --init
```
Then in the `buildtools` directory run
```bash
pip install -e .
```
Then to you should be able to use
```bash
build_cpyc cpyc.json
```
to compile the codebook.

## Building a specific Section or Entry
The `-s`/`--scope` option can be used to build only a section or entry. To build only a specific section run
```bash
build_cpyc -s <section> cpyc.json
```
and to build only a specific entry run
```bash
build_cpyc -s <section>/<entry> cpyc.json
```
In either case the section (and entry) must be configured in the `cpyc.json` file.