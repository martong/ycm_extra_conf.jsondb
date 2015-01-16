import ycm_jsondb_core
import os

# Set this to the absolute path to the folder (NOT the file!) containing the
# compile_commands.json file to use that instead of 'flags'. See here for
# more details: http://clang.llvm.org/docs/JSONCompilationDatabase.html
compilation_database_folder = 'native-editor/build/osx_x64_debug/make'

def DirectoryOfThisScript():
  return os.path.dirname( os.path.abspath( __file__ ) )

ycm_jsondb_core.Init(compilation_database_folder)

def FlagsForFile( filename, **kwargs ):
  return ycm_jsondb_core.FlagsForFile(filename, DirectoryOfThisScript())

