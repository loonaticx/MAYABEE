import zipfile
import os


def zip_files(files_to_zip, zip_filename):
    """
    Compresses given files into a zip archive.

    Args:
        files_to_zip (list): List of file paths to be zipped.
        zip_filename (str): Name of the output zip file.
    """

    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in files_to_zip:
            zipf.write(f"MAYBEE/{file}")


included_files = [
    "README.md",
    "LICENSE",
    "RELEASE",
    "yabee.py",
    "yabee_libs/__init__.py",
    "yabee_libs/egg_writer.py",
    "yabee_libs/texture_processor.py",
    "yabee_libs/utils.py",
    "img/banner.png",
    "img/logo.png",
    "examples/cube.egg",
    "examples/PBSDF.png",
    "examples/tex/Untitled.png"
]
os.chdir("..")
zip_files(included_files, "MAYBEE_v220.zip")
