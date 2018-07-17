from conans import ConanFile, tools


class HelloConan(ConanFile):
    name = "hello"
    version = "1.0.0"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "*"

    def package(self):
        self.copy("*")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
