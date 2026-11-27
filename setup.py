# Explicit metadata so that old setuptools (<61, e.g. Ubuntu 22.04's apt 59.6.0
# used by pip 22.0.2 build isolation) does not fall back to name "UNKNOWN".
# Keep in sync with pyproject.toml.
from setuptools import find_packages, setup

setup(
    name="gluefactory",
    version="0.0",
    packages=find_packages(include=["gluefactory*"]),
    package_data={
        "gluefactory": ["datasets/megadepth_scene_lists/*.txt", "configs/*.yaml"]
    },
    install_requires=[
        "torch>=1.7",
        "torchvision>=0.8",
        "numpy",
        "opencv-python",
        "tqdm",
        "matplotlib",
        "scipy",
        "h5py",
        "omegaconf",
        "tensorboard",
        "kornia",
        "seaborn",
        "joblib",
        "scikit-learn>=1.5",
        "lightglue @ git+https://github.com/EnChargeAI/ThirdParty_lightglue@mybranch",
        "albumentations",
    ],
)
