import os

def DirectoryOfThisScript():
  return os.path.dirname( os.path.abspath( __file__ ) )

import sys
sys.path.insert(0, DirectoryOfThisScript())

import ycm_jsondb_config
if "GetCompilationDatabaseFolder" in dir(ycm_jsondb_config):
  compilation_database_folder = ycm_jsondb_config.GetCompilationDatabaseFolder(
      DirectoryOfThisScript())
else:
  compilation_database_folder = DirectoryOfThisScript()

import ycm_jsondb_core
ycm_jsondb_core.Init(compilation_database_folder)

def FlagsForFile( filename, **kwargs ):
  return ycm_jsondb_core.FlagsForFile(filename, DirectoryOfThisScript())

