import os

from PySide2 import QtWidgets
import ffmpeg

from libs.plugin_collection import Plugin

SCRIPT_PATH = os.path.dirname(__file__)


class H264Encoder(Plugin):
    """This plugin convert files in H.264"""
    def __init__(self):
        super(H264Encoder, self).__init__()
        self.logger = None

        self.description = 'Convert any file in H.264'
        self.name = 'H.264'
        self.extension = 'mp4'

    def perform_operation(self,
                          logger,
                          input_path,
                          output_path,
                          overwrite_output,
                          *args, **kwargs):
        self.logger = logger
        logger.info('Start conversion H.264')

        status = False
        try:
            self.create_output_path(path=output_path)
            stream = ffmpeg.input(input_path)
            stream = ffmpeg.output(stream, output_path)
            ffmpeg.run(stream, overwrite_output=overwrite_output)
            status = True
        except Exception as error:
            logger.error(error)
            status = False

        return status

    def create_output_path(self, path):
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
