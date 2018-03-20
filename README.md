A sample project to demonstrate how to create Conan package for LLVM 6.0.

# Build LLVM into local cache

```
$ conon create . LLVM/release_60
```

See it in action:

[![asciicast](https://asciinema.org/a/9yi010lhV4Bvjk321P8h151aB.png)](https://asciinema.org/a/9yi010lhV4Bvjk321P8h151aB)

# Use LLVM in local cache

Create a file named `conanfile.txt` in your project folder:

```
[requires]
LLVM/release_60@LLVM/release_60

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
