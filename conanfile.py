from conans import ConanFile, CMake
import glob
import os

class LlvmConan(ConanFile):
    name = "LLVM"
    version = "release_60"
    license = "LLVM Release License"
    url = "https://github.com/p47r1ck7541/llvm-60"
    description = "%s %s" % (name, version)
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/llvm-mirror/llvm -b %s --depth 1 src" % self.version)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.install()

    def package(self):
        # nothing to do here now because we reuse 'cmake install' to package files
        pass

    def package_info(self):
        self.cpp_info.libs = [os.path.basename(a) for a in glob.glob(os.path.join(self.package_folder, "lib", "*.a"))]
        self.cpp_info.cppflags = ["-std=c++11", "-fno-rtti"]
        self.cpp_info.exelinkflags = ["-lcurses", "-lz"]

