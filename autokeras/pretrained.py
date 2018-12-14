from abc import ABC, abstractmethod
from autokeras.constant import Constant
from autokeras.image.face_detection_pretrained import detect_faces
from autokeras.utils import download_file


class Pretrained(ABC):
    """The base class for all pretrained task.
    Attributes:
        verbose: A boolean value indicating the verbosity mode.
    """

    def __init__(self):
        """Initialize the instance.
        """
        self.model = None

    @abstractmethod
    def load(self):
        """load pretrained model into self.model
        """
        pass

    @abstractmethod
    def predict(self, x_predict):
        """Return predict results for the given image
        Args:
            x_predict: An instance of numpy.ndarray containing the testing data.
        Returns:
            A numpy.ndarray containing the results.
        """
        pass


class FaceDetectionPretrained(Pretrained):

    def __init__(self):
        super(FaceDetectionPretrained, self).__init__()
        self.pnet, self.rnet, self.onet = None, None, None
        for model_link, file_path in zip(Constant.face_detection_pretrained['PRETRAINED_MODEL_LINKS'],
                                         Constant.face_detection_pretrained['FILE_PATHS']):
            download_file(model_link, file_path)
        self.load()

    def load(self, model_path=None):
        self.pnet, self.rnet, self.onet = Constant.face_detection_pretrained['FILE_PATHS']

    def predict(self, img_path, output_file_path=None):
        return detect_faces(self.pnet, self.rnet, self.onet, img_path, output_file_path)
