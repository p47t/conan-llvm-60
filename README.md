A sample project to demonstrate how to create Conan package for LLVM 5.0.

# Build LLVM into local cache

```
$ conon create . LLVM/release_50
```

# Use LLVM in local cache

Create a file named `conanfile.txt` in your project folder:

```
[requires]
LLVM/release_50@LLVM/release_50

[generators]
cmake
```

Add the following snippet to your `CMakeLists.txt`:

```
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
```

Add `${CONAN_INCLUDE_DIRS}` to your include directories and `${CONAN_LIBS}` to your link libraries.

Create `conanbuildinfo.cmake` assuming using build folder 'build/':

```
$ mkdir build && cd build
$ conan install ..
```
