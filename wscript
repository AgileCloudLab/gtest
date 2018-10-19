from waflib.Tools.compiler_cxx import cxx_compiler

APPNAME = 'gtest'
VERSION = '1.0.0'

cxx_compiler['linux'] = ['clang++']

def options(opt) :
    opt.load('compiler_cxx')

def configure(cnf) :
    cnf.load('compiler_cxx')
    cnf.env.append_value('LINKFLAGS',
                         ['-std=c++17', '-Wall', '-Werror', '-Wextra', '-pthread'])

def build(bld):

    bld(
        features='cxx',
        source=['gtest/src/gtest-all.cc'],
        target='gtest',
        includes=['gtest/include', 'gtest'],
        export_includes=['gtest/include']
    )
