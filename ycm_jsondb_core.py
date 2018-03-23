from __future__ import print_function
from builtins import next
from builtins import zip
from builtins import str
import os
import sys
import fnmatch
import re
import ycm_core
import json
import itertools
import ycm_jsondb_config

flags = []
database = None
compilation_database_folder = None


def Init(compilation_database_folder_):
    debugLog("Init")
    if os.path.exists(compilation_database_folder_):
        debugLog("database_folder OK")
        global compilation_database_folder
        compilation_database_folder = compilation_database_folder_
        global database
        database = ycm_core.CompilationDatabase(compilation_database_folder_)


SOURCE_EXTENSIONS = ['.cpp', '.cxx', '.cc', '.c', '.m', '.mm']


def MakeRelativePathsInFlagsAbsolute(flags, working_directory):
    if not working_directory:
        return list(flags)
    new_flags = []
    make_next_absolute = False
    path_flags = ['-isystem', '-I', '-iquote', '--sysroot=']
    for flag in flags:
        new_flag = flag

        if make_next_absolute:
            make_next_absolute = False
            if not flag.startswith('/'):
                new_flag = os.path.join(working_directory, flag)

        for path_flag in path_flags:
            if flag == path_flag:
                make_next_absolute = True
                break

            if flag.startswith(path_flag):
                path = flag[len(path_flag):]
                new_flag = path_flag + os.path.join(working_directory, path)
                break

        if new_flag:
            new_flags.append(new_flag)
    return new_flags


def IsHeaderFile(filename):
    extension = os.path.splitext(filename)[1]
    return extension in ['.h', '.hxx', '.hpp', '.hh']


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def removeClosingSlash(path):
    if path.endswith('/'):
        path = path[:-1]
    return path


def debugLog(msg):
    print(msg)
    sys.stdout.flush()


def root_path():
    return os.path.abspath(os.sep)


def searchForTranslationUnitWhichIncludesPath(compileCommandsPath, path):
    path = os.path.abspath(path)
    path = removeClosingSlash(path)
    # debugLog("IncludesPath path: " + str(path))
    jsonData = open(compileCommandsPath)
    data = json.load(jsonData)
    found = []
    for translationUnit in data:
        buildDir = translationUnit["directory"]
        switches = translationUnit["command"].split()
        for currentSwitch, nextSwitch in pairwise(switches):
            matchObj = re.match(r'(-I|-isystem)(.*)', currentSwitch)
            includeDir = ""
            isIncFlag = False
            if currentSwitch == "-I" or currentSwitch == "-isystem":
                includeDir = nextSwitch
                isIncFlag = True
            elif matchObj:
                includeDir = matchObj.group(2)
                isIncFlag = True

            if not isIncFlag:
                continue

            includeDir = os.path.join(buildDir, includeDir)
            includeDir = os.path.abspath(includeDir)
            includeDir = removeClosingSlash(includeDir)

            # Check all the parent dirs in path
            pathCopy = path
            distance = 0
            while pathCopy != root_path():
                if includeDir == pathCopy:
                    found.append((distance, str(translationUnit["file"])))

                distance += 1
                pathCopy, tail = os.path.split(pathCopy)

    jsonData.close()
    found.sort()

    if len(found) == 0:
        debugLog("Not Found")
        return None
    else:
        result = found[0][1]
        debugLog("Found best source file: " + result)
        return result


def findFirstSiblingSrc(dirname, findSiblingForThisFile):
    findSiblingForThisFile = os.path.split(findSiblingForThisFile)[1]
    for root, dirnames, filenames in os.walk(dirname):
        for filename in filenames:
            if filename.endswith(tuple(SOURCE_EXTENSIONS)):
                if str(filename) != str(findSiblingForThisFile):
                    compilation_info = database.GetCompilationInfoForFile(
                        str(os.path.join(root, filename)))
                    if compilation_info.compiler_flags_:
                        return os.path.join(root, filename)
    return None


def getFirstEntryOfACompilationDB(compileCommandsPath):
    jsonData = open(compileCommandsPath)
    data = json.load(jsonData)
    # TODO finally
    jsonData.close()
    return str(data[0]["file"])


def GetCompilationInfoForFile(filename):
    debugLog("GetCompilationInfoForFile: filename: " + filename)

    result = database.GetCompilationInfoForFile(filename)
    if result.compiler_flags_:
        return result

    basename = os.path.split(filename)[1]
    dirname = os.path.dirname(filename)

    # The compilation_commands.json file generated by CMake does not have entries
    # for header files. So we do our best by asking the db for flags for a
    # corresponding source file, if any. If one exists, the flags for that file
    # should be good enough.
    compilation_database_file = compilation_database_folder + \
        "/" + "compile_commands.json"

    if IsHeaderFile(filename):
        basename = os.path.splitext(filename)[0]
        for extension in SOURCE_EXTENSIONS:
            replacement_file = basename + extension
            if os.path.exists(replacement_file):
                debugLog(
                    "Matching src file, based on method0: " +
                    replacement_file)
                compilation_info = database.GetCompilationInfoForFile(
                    replacement_file)
                if compilation_info.compiler_flags_:
                    return compilation_info

        # If still not found a candidate translation unit,
        # then try to browse the json db to find one,
        # which uses the directory of our header as an include path (-I,
        # -isystem).
        candidateSrcFile = searchForTranslationUnitWhichIncludesPath(
            compilation_database_file, dirname)
        if candidateSrcFile is not None:
            debugLog(
                "Matching src file, based on searchForTranslationUnitWhichIncludesPath: " +
                candidateSrcFile)
        else:
            candidateSrcFile = findFirstSiblingSrc(dirname, filename)
            if candidateSrcFile is not None:
                debugLog(
                    "Matching src file, based on findFirstSiblingSrc: " +
                    candidateSrcFile)
            else:
                candidateSrcFile = getFirstEntryOfACompilationDB(
                    compilation_database_file)
                if candidateSrcFile is not None:
                    debugLog(
                        "Matching src file, based on getFirstEntryOfACompilationDB: " +
                        candidateSrcFile)

        if (candidateSrcFile is None):
            debugLog("Could not find any matches")
            candidateSrcFile = ""
        return database.GetCompilationInfoForFile(candidateSrcFile)

    # Src file
    result = database.GetCompilationInfoForFile(filename)
    candidateSrcFile = filename
    # TODO this is a bit redundant with the header part
    if not result.compiler_flags_:
        candidateSrcFile = findFirstSiblingSrc(dirname, filename)
        if candidateSrcFile is not None:
            debugLog(
                "Matching src file, based on findFirstSiblingSrc: " +
                candidateSrcFile)
        else:
            candidateSrcFile = getFirstEntryOfACompilationDB(
                compilation_database_file)
            if candidateSrcFile is not None:
                debugLog(
                    "Matching src file, based on getFirstEntryOfACompilationDB: " +
                    candidateSrcFile)

        if (candidateSrcFile is None):
            debugLog("Could not find any matches")
            candidateSrcFile = ""
    else:
        debugLog("Matching src file, found in compilation db")

    return database.GetCompilationInfoForFile(candidateSrcFile)


def FlagsForFile(filename, directory):
    if database:
        # Bear in mind that compilation_info.compiler_flags_ does NOT return a
        # python list, but a "list-like" StringVec object
        compilation_info = GetCompilationInfoForFile(filename)
        if not compilation_info:
            debugLog("not compilation_info")
            return None

        final_flags = MakeRelativePathsInFlagsAbsolute(
            compilation_info.compiler_flags_,
            compilation_info.compiler_working_dir_)

        try:
            final_flags.extend(ycm_jsondb_config.GetAdditionalFlags())
        except ValueError:
            pass

        try:
            ignoredFlags = ycm_jsondb_config.GetIgnoredFlags()
            final_flags = [
                flag for flag in final_flags if flag not in ignoredFlags]
        except ValueError:
            pass

    else:
        debugLog("database NOK")
        relative_to = directory
        final_flags = MakeRelativePathsInFlagsAbsolute(flags, relative_to)

    return {
        'flags': final_flags,
        'do_cache': True
    }
