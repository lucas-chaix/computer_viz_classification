from setuptools import setup, find_packages

setup(
   name='silos',
   version='1.0',
   description='Classification and segmentation of silos images',
   packages=find_packages(),
   package_data={'silos':['classification/prediction/models/cnn_nath.hdf5', 'segmentation/prediction/models/segment1.h5']},
   entry_points={
      'console_scripts':['isthereasilo = silos.classification.prediction.silosclassification:main']
   },
   install_requires=['numpy', 'pandas', 'keras', 'tensorflow-cpu', 'pillow', 'click', 'matplotlib']
)

