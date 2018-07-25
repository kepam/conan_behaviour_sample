from conans import ConanFile, CMake


class RootConan(ConanFile):
    name = "root"
    version = "1.0.0"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Root here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = "src/*"
    #requires = "test/1.0.0@test/test", "hello/1.0.0@test/test"
    requires = "test/1.0.0@test/test", "hello/1.0.1@test/test"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()

