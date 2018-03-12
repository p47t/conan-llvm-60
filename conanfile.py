from conans import ConanFile, CMake, tools

class LlvmConan(ConanFile):
    name = "LLVM"
    version = "release_50"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Llvm here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/llvm-mirror/llvm -b %s --depth 1" % self.version)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.install()

    def package(self):
        pass

    def package_info(self):
        pass
